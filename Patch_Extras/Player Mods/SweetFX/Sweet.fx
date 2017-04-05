
  /*---------------------------------------.
  |   .-.                   .  .---..   .  |
  |  (   )                 _|_ |     \ /   |
  |   `-..  .    ._.-.  .-. |  |---   /    |
  |  (   )\  \  / (.-' (.-' |  |     / \   |
  |   `-'  `' `'   `--' `--'`-''    '   '  |
  |              by CeeJay.dk              | 
  '---------------------------------------*/
  /*---------------------------------------.
  | ::     Using ReShade by Crosire     :: | 
  '---------------------------------------*/

  /*-----------------------.
  | ::     Settings     :: |
  '-----------------------*/

#include "SweetFX/Docs/Keycodes.txt" //load keycode aliases for the Reshade key bindings
#include "SweetFX/Global_settings.txt" //load ReShade settings
#include "SweetFX/SweetFX_settings.txt" //load SweetFX settings

#if SMAA_PREDICATION == 1
	#undef USE_DEPTH
	#define USE_DEPTH 1
#endif

  /*-----------------------.
  | :: Greeting message :: |
  '-----------------------*/

#if SweetFX_Greeting == 1
  #include "SweetFX/Shaders/Greeting.h"
#endif

  /*-----------------------.
  | :: ReShade Settings :: |
  '-----------------------*/

#if ReShade_Screenshot_Format != 2
	#pragma reshade screenshot_format bmp //ReShade_Screenshot_Format == 1
#else
	#pragma reshade screenshot_format png //ReShade_Screenshot_Format == 2
#endif

#if ReShade_ShowToggleMessage == 1
	#pragma reshade showtogglemessage
#endif

#if ReShade_ShowClock == 1
  #pragma reshade showclock
#endif

#if ReShade_ShowFPS == 1
  #pragma reshade showfps
#endif

#if ReShade_ShowStatistics == 1
	#pragma reshade showstatistics
#endif

  /*-----------------------.
  | ::      Globals     :: |
  '-----------------------*/

#include "SweetFX/Shaders/Globals.h" //define global contants and uniforms

  /*-----------------------.
  | ::     Textures     :: |
  '-----------------------*/
  
/*
Default values if explicitly not set are:
	Width = 1;
	Height = 1;
	Format = R8G8B8A8;
	MipLevels = 1;
*/

texture colorTex : SV_Target; //Game texture

#if USE_DEPTH == 1
  texture depthTex : SV_Depth;  //Game depth
#endif 

#if USE_TRANSITION == 1
  texture transitionTex < string source = "SweetFX/Textures/" Transition_texture ; >
  {
    Width = Transition_texture_width;
    Height = Transition_texture_height;
  };
#endif 


#if (USE_SMAA == 1 || USE_SMAA_ANTIALIASING == 1)
  texture edgesTex
  {
    Width = BUFFER_WIDTH;
    Height = BUFFER_HEIGHT;
    Format = R8G8B8A8; //R8G8 is also an option  
  };

  texture blendTex
  {
    Width = BUFFER_WIDTH;
    Height = BUFFER_HEIGHT;
    Format = R8G8B8A8;
  };

  texture areaTex < string source = "SweetFX/Textures/SMAA_AreaTex.dds"; >
  {
    Width = 160;
    Height = 560;
    Format = R8G8;
  };
  
  texture searchTex < string source = "SweetFX/Textures/SMAA_SearchTex.dds"; >
  {
    Width = 64;
    Height = 16;
    Format = R8;
  };
#endif 

  /*-----------------------.
  | ::     Samplers     :: |
  '-----------------------*/
/* -- Note that DirectX has a  maximum number of 16 possible samplers -- */


sampler colorGammaSampler
{
	Texture = colorTex;
  AddressU  = Clamp; AddressV = Clamp;
  MipFilter = Linear; MinFilter = Linear; MagFilter = Linear; //Why Mipfilter linear - shouldn't point be fine?
  SRGBTexture = false;
};

sampler BorderSampler
{
	Texture = colorTex;
  AddressU  = Border; AddressV = Border;
  MipFilter = Linear; MinFilter = Linear; MagFilter = Linear; //Why Mipfilter linear - shouldn't point be fine?
  SRGBTexture = false;
};

sampler colorLinearSampler
{
	Texture = colorTex;
	AddressU  = Clamp; AddressV = Clamp;
	MipFilter = Point; MinFilter = Linear; MagFilter = Linear;
	SRGBTexture = true;
};

#if USE_TRANSITION == 1
  sampler transitionSampler
  {
    Texture = transitionTex;
  };
#endif

#if (USE_SMAA == 1 || USE_SMAA_ANTIALIASING == 1)

	sampler edgesSampler
	{
		Texture = edgesTex;
		AddressU = Clamp; AddressV = Clamp;
		MipFilter = Linear; MinFilter = Linear; MagFilter = Linear;
		SRGBTexture = false;
	};

	sampler blendSampler
	{
		Texture = blendTex;
		AddressU = Clamp; AddressV = Clamp;
		MipFilter = Linear; MinFilter = Linear; MagFilter = Linear;
		SRGBTexture = false;
	};

	sampler areaSampler
	{
		Texture = areaTex;
		AddressU = Clamp; AddressV = Clamp; AddressW = Clamp;
		MipFilter = Linear; MinFilter = Linear; MagFilter = Linear;
		SRGBTexture = false;
	};

  sampler searchSampler
  {
    Texture = searchTex;
    AddressU = Clamp; AddressV = Clamp; AddressW = Clamp;
    MipFilter = Point; MinFilter = Point; MagFilter = Point;
    SRGBTexture = false;
  };

#endif

#if USE_DEPTH == 1
  sampler depthSampler
  {
    Texture = depthTex;
    AddressU  = Clamp; AddressV = Clamp;
    MipFilter = Linear; MinFilter = Linear; MagFilter = Linear; //Why Mipfilter linear - shouldn't point be fine?
    // SRGBTexture = true; // The depth buffer is always linear and cannot be set to gamma.
  };
#endif 

#define predicationSampler depthSampler //Use the depth sampler as our predication sampler

  /*----------------------.
  | ::  Vertex Shader  :: |
  '----------------------*/

void FullscreenTriangle(in uint id : SV_VertexID, out float4 position : SV_Position, out float2 texcoord : TEXCOORD0)
{
	// Basic Buffer/Layout-less fullscreen triangle vertex shader - used for several of the passes.
	texcoord.x = (id == 2) ? 2.0 : 0.0;
	texcoord.y = (id == 1) ? 2.0 : 0.0;
	position = float4(texcoord * float2(2.0, -2.0) + float2(-1.0, 1.0), 0.0, 1.0);
}

  /*-----------------------.
  | ::     Effects      :: |
  '-----------------------*/
 
#define s0 colorGammaSampler
#define s1 colorLinearSampler
#define myTex2D tex2D 

#include "SweetFX/Shaders/Main.h"


  /*-----------------------.
  | ::    Techniques    :: |
  '-----------------------*/

technique SweetFX <bool enabled = ReShade_Start_Enabled; int toggle = ReShade_ToggleKey; >
{
#if (USE_ASCII == 1)
	pass //Ascii pass
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = AsciiWrap;
	}
#endif

#if (USE_CARTOON == 1)
	pass //Cartoon pass
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = CartoonWrap;
	}
#endif

#if (USE_LUMASHARPEN == 1)
	pass //LumaSharpen pass
	{
    VertexShader = FullscreenTriangle;
		//VertexShader = LumaSharpenVS;
		PixelShader  = LumaSharpenWrap;
	}
#endif

#if (USE_SMAA == 1 || USE_SMAA_ANTIALIASING == 1)

  // SMAA //
	pass SMAA_EdgeDetection //First SMAA Pass
	{
		VertexShader = SMAAEdgeDetectionVSWrap;

	#if SMAA_EDGE_DETECTION == 1
		PixelShader = SMAALumaEdgeDetectionPSWrap;
	#elif SMAA_EDGE_DETECTION == 3
		PixelShader = SMAADepthEdgeDetectionPSWrap;
	#else
		PixelShader = SMAAColorEdgeDetectionPSWrap; //Probably the best in most cases so I default to this.
	#endif

		// We will be creating the stencil buffer for later usage.
		StencilEnable = true;
		StencilPass = REPLACE;
		StencilRef = 1;
		
		RenderTarget = edgesTex;
	}
	
	pass SMAA_BlendWeightCalculation //Second SMAA Pass
	{
		VertexShader = SMAABlendingWeightCalculationVSWrap;
		PixelShader = SMAABlendingWeightCalculationPSWrap;
        
		// Here we want to process only marked pixels.
		StencilEnable = true;
		StencilPass = KEEP;
		StencilFunc = EQUAL;
		StencilRef = 1;
		
		RenderTarget = blendTex;
	}
	
	pass SMAA_NeighborhoodBlending //Third SMAA Pass
	{
		VertexShader = SMAANeighborhoodBlendingVSWrap;
		PixelShader  = SMAANeighborhoodBlendingPSWrap;
		
	#if SMAA_DEBUG_OUTPUT == 5
		// Use the stencil so we can show it.
		StencilEnable = true;
		StencilPass = KEEP;
		StencilFunc = EQUAL;
		StencilRef = 1;
	#else
		// Process all the pixels.
		StencilEnable = false;
	#endif
	
	#if Shared_Piggyback_SMAA == 1
		SRGBWriteEnable = false;
	#else
		SRGBWriteEnable = true;
	#endif
	}
#endif

#if (USE_EXPLOSION == 1)
	pass //Explosion pass
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = ExplosionWrap;
	}
#endif

#if (USE_FXAA == 1 || USE_FXAA_ANTIALIASING == 1)
  //TODO make a luma pass
	pass FXAA
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = FXAA;
	}
#endif

#if (USE_BLOOM == 1)
	pass //Bloom pass
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = BloomWrap;
	}
#endif

#if (USE_HDR == 1)
	pass //HDR pass
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = HDRWrap;
	}
#endif

#if (USE_CA == 1)
	pass //CA pass
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = ChromaticAberrationWrap;
	}
#endif

#if (USE_ADVANCED_CRT == 1)
	pass //Advanced CRT pass
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = AdvancedCRTWrap;
	}
#endif

#if (USE_PIXELART_CRT == 1)
	pass //Pixel Art CRT pass
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = PixelArtCRTWrap;
		
	#if Shared_Piggyback_PixelArt_CRT == 1
		SRGBWriteEnable = false;
	#else
		SRGBWriteEnable = true; //PixelArtCRT uses linear so we must convert to gamma again
	#endif

	}
#endif

#if (USE_LENS_DISTORTION == 1)
	pass //Lens Distortion pass
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = LensDistortionWrap;
	}
#endif



#if ((USE_SHARED + Shared_Piggyback_No) == 2)
	pass //Shared pass - the effects that don't require a seperate pass are all done in this one.
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = SharedWrap;
	}
#endif


#if (USE_CUSTOM == 1) //There is no way of knowing where the users own shader should go so let us just put it at the end for now
	pass //Custom pass
	{
		VertexShader = FullscreenTriangle;
		PixelShader  = CustomPass;
	}
#endif


}
  /*----------------------------.
  | :: Toogleable techniques :: |
  '----------------------------*/

#if USE_DEPTH == 1
  technique Depth < bool enabled = false; int toggle = ReShade_DepthToggleKey;>
  {
    pass
    {
      VertexShader = FullscreenTriangle;
      PixelShader  = DisplayDepth;
    }
  }
#endif

  /*---------------------------.
  | :: Temporary techniques :: |
  '---------------------------*/

#if USE_TRANSITION == 1
  technique Transition < bool enabled = true; int timeout = Transition_time; > //sets the timeleft value. When it reaches 0 the technique is disabled.
  {
    pass
    {
      VertexShader = FullscreenTriangle;
      PixelShader  = Transition_type;
    }
  }
#endif
