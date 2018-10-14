//High Pass Sharpening & Contrast Enhancement
//Version 1.1
/* This shader uses the gaussian blur passes from Boulotaur2024's gaussian blur/ bloom, unsharpmask shader which are based
   on the implementation in the article "Efficient Gaussian blur with linear sampling"
   http://rastergrid.com/blog/2010/09/efficient-gaussian-blur-with-linear-sampling/ .
   The blend modes are based on algorithms found at http://www.dunnbypaul.net/blends/ , 
   http://www.deepskycolors.com/archive/2010/04/21/formulas-for-Photoshop-blending-modes.html ,
   http://www.simplefilter.de/en/basics/mixmods.html and http://en.wikipedia.org/wiki/Blend_modes . 
   For more info go to http://reshade.me/forum/shader-presentation/529-high-pass-sharpening */ 
#include "SweetFX/Clarity_settings.txt" //load Gaussian Blur settings

#define MainSampler frameSampler
#define VertexShader_G Triangle
texture frameTex2D : COLOR;
sampler2D frameSampler { Texture = frameTex2D; MinFilter = Linear; MagFilter = Linear; MipFilter = Linear; AddressU = Clamp; SRGBTexture = FALSE;};

#define CoefLuma_HP float3(0.2126, 0.7152, 0.0722)
#define hpPX_SIZE (float2(1.0f/BUFFER_WIDTH, 1.0f/BUFFER_HEIGHT))

#if USE_HighPassSharpening == 0
	#undef ViewSharpMask 
#endif

#if USE_HighPassContrastEnhancement == 1

#if CETextureFormat == 1
#define CETexFormat RGBA16F
#elif CETextureFormat == 2 
#define CETexFormat RGBA32F
#else
#define CETexFormat RGBA8
#endif

#if CETexScale == 1 
#define CEscale 0.5 
#elif CETexScale == 2 
#define CEscale 0.25 
#else 
#define CEscale 1
#endif

#define cePX_SIZE (hpPX_SIZE*CE_MaskWidth)

texture ceBlurTex2Dping{ Width = BUFFER_WIDTH*CEscale; Height = BUFFER_HEIGHT*CEscale; Format = CETexFormat; };
texture ceBlurTex2Dpong{ Width = BUFFER_WIDTH*CEscale; Height = BUFFER_HEIGHT*CEscale; Format = CETexFormat; };

sampler2D ceBlurSamplerPing { Texture = ceBlurTex2Dping; MinFilter = Linear; MagFilter = Linear; MipFilter = Linear; AddressU = Clamp; SRGBTexture = FALSE;};
sampler2D ceBlurSamplerPong { Texture = ceBlurTex2Dpong; MinFilter = Linear; MagFilter = Linear; MipFilter = Linear; AddressU = Clamp; SRGBTexture = FALSE;};
#endif

void Triangle(in uint id : SV_VertexID, out float4 position : SV_Position, out float2 texcoord : TEXCOORD0)
{
	// Basic Buffer/Layout-less fullscreen triangle vertex shader - used for several of the passes.
	texcoord.x = (id == 2) ? 2.0 : 0.0;
	texcoord.y = (id == 1) ? 2.0 : 0.0;
	position = float4(texcoord * float2(2.0, -2.0) + float2(-1.0, 1.0), 0.0, 1.0);
}

float4 OriginalPixel(in float4 pos : SV_Position, in float2 texcoord : TEXCOORD) : COLOR
{
	float4 color = tex2D(MainSampler, texcoord);
	return saturate(color);
}

#if USE_HighPassSharpening == 1

float4 SharpBlurFinal(in float4 pos : SV_Position, in float2 texcoord : TEXCOORD) : COLOR
{
	#define PX_SIZE (hpPX_SIZE/SharpMaskPrecision)
	float4 color = tex2D(MainSampler, texcoord);
	
	#if SharpMaskQuality == 2
	
		color += tex2D(MainSampler, texcoord + float2(0.0, 3*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord - float2(0.0, 3*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord + float2( 3*PX_SIZE.x, 0.0))*0.04167;
		color += tex2D(MainSampler, texcoord - float2( 3*PX_SIZE.x, 0.0))*0.04167;
	
		color += tex2D(MainSampler, texcoord + float2( 3*PX_SIZE.x, PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord - float2( 3*PX_SIZE.x, PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord + float2( -3*PX_SIZE.x, PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord + float2( 3*PX_SIZE.x, -PX_SIZE.y))*0.04167;
		
		color += tex2D(MainSampler, texcoord + float2( 3*PX_SIZE.x, 2*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord - float2( 3*PX_SIZE.x, 2*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord + float2( -3*PX_SIZE.x, 2*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord + float2( 3*PX_SIZE.x, -2*PX_SIZE.y))*0.04167;		
		
		color += tex2D(MainSampler, texcoord + float2( PX_SIZE.x, 3*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord - float2( PX_SIZE.x, 3*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord + float2( -PX_SIZE.x, 3*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord + float2( PX_SIZE.x, -3*PX_SIZE.y))*0.04167;

		color += tex2D(MainSampler, texcoord + float2( 2*PX_SIZE.x, 3*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord - float2( 2*PX_SIZE.x, 3*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord + float2( -2*PX_SIZE.x, 3*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord + float2( 2*PX_SIZE.x, -3*PX_SIZE.y))*0.04167;
		
		color += tex2D(MainSampler, texcoord + float2( 3*PX_SIZE.x, 3*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord - float2( 3*PX_SIZE.x, 3*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord + float2( -3*PX_SIZE.x, 3*PX_SIZE.y))*0.04167;
		color += tex2D(MainSampler, texcoord + float2( 3*PX_SIZE.x, -3*PX_SIZE.y))*0.04167;
		
		color *= 0.5; 
	#endif
	
	#if SharpMaskQuality >= 1
	
		color += tex2D(MainSampler, texcoord + float2(0.0, 2*PX_SIZE.y))*0.0625;
		color += tex2D(MainSampler, texcoord - float2(0.0, 2*PX_SIZE.y))*0.0625;
		color += tex2D(MainSampler, texcoord + float2( 2*PX_SIZE.x, 0.0))*0.0625;
		color += tex2D(MainSampler, texcoord - float2( 2*PX_SIZE.x, 0.0))*0.0625;
	
		color += tex2D(MainSampler, texcoord + float2( 2*PX_SIZE.x, PX_SIZE.y))*0.0625;
		color += tex2D(MainSampler, texcoord - float2( 2*PX_SIZE.x, PX_SIZE.y))*0.0625;
		color += tex2D(MainSampler, texcoord + float2( -2*PX_SIZE.x, PX_SIZE.y))*0.0625;
		color += tex2D(MainSampler, texcoord + float2( 2*PX_SIZE.x, -PX_SIZE.y))*0.0625;
		
		color += tex2D(MainSampler, texcoord + float2( PX_SIZE.x, 2*PX_SIZE.y))*0.0625;
		color += tex2D(MainSampler, texcoord - float2( PX_SIZE.x, 2*PX_SIZE.y))*0.0625;
		color += tex2D(MainSampler, texcoord + float2( -PX_SIZE.x, 2*PX_SIZE.y))*0.0625;
		color += tex2D(MainSampler, texcoord + float2( PX_SIZE.x, -2*PX_SIZE.y))*0.0625;
		
		color += tex2D(MainSampler, texcoord + float2( 2*PX_SIZE.x, 2*PX_SIZE.y))*0.0625;
		color += tex2D(MainSampler, texcoord - float2( 2*PX_SIZE.x, 2*PX_SIZE.y))*0.0625;
		color += tex2D(MainSampler, texcoord + float2( -2*PX_SIZE.x, 2*PX_SIZE.y))*0.0625;
		color += tex2D(MainSampler, texcoord + float2( 2*PX_SIZE.x, -2*PX_SIZE.y))*0.0625;
		
		color *= 0.5; 
	#endif 
	
		color += tex2D(MainSampler, texcoord + float2(0.0, PX_SIZE.y))*0.125;
		color += tex2D(MainSampler, texcoord - float2(0.0, PX_SIZE.y))*0.125;
		color += tex2D(MainSampler, texcoord + float2( PX_SIZE.x, 0.0))*0.125;
		color += tex2D(MainSampler, texcoord - float2( PX_SIZE.x, 0.0))*0.125;
		color += tex2D(MainSampler, texcoord + float2( PX_SIZE.x, PX_SIZE.y))*0.125;
		color += tex2D(MainSampler, texcoord - float2( PX_SIZE.x, PX_SIZE.y))*0.125;
		color += tex2D(MainSampler, texcoord + float2( -PX_SIZE.x, PX_SIZE.y))*0.125;
		color += tex2D(MainSampler, texcoord + float2( PX_SIZE.x, -PX_SIZE.y))*0.125;
		color *= 0.5;
	
	
	float4 orig = tex2D(MainSampler, texcoord); //Original Image
	float3 luma = dot(orig.rgb,CoefLuma_HP);
	float3 chroma = orig.rgb - luma;
	
			float3 sharp = 1 - dot(color.rgb,CoefLuma_HP);
			sharp = (luma + sharp)*0.5;
		
		#if AdjustHaloStrength == 1
			float3 curve = (2*(sharp - 0.5)*(sharp+0.5))+0.5;
			float3 sharpMin = saturate(lerp(sharp,curve,DarkHaloStrength));
			sharpMin = min(sharp,sharpMin);
			float3 sharpMax = saturate(lerp(sharp,curve,LightHaloStrength));
			sharpMax = max(sharp,sharpMax);
			sharp = 0.5*(sharpMin+sharpMax);
		#elif CurveMask == 1
			float3 curve = (2*(sharp - 0.5)*(sharp+0.5))+0.5;
			sharp = saturate(lerp(sharp,curve,CurveStrength));
		#elif CurveMask == 2
			float3 curve = (2*(sharp - 0.5)*(sharp+0.5))+0.5;
			curve = saturate(lerp(sharp,curve,CurveStrength));
			sharp = min(sharp,curve);
		#elif CurveMask == 3
			float3 curve = (2*(sharp - 0.5)*(sharp+0.5))+0.5;
			curve = saturate(lerp(sharp,curve,CurveStrength));
			sharp = max(sharp,curve);
		#endif
			
			sharp = clamp(sharp,ClampDarkHalos,ClampLightHalos);
			
			#if ViewSharpMask == 1
				orig.rgb = sharp;
				luma = sharp;
			#elif BlendMode == 3
				//Multiply
				sharp = 2 * luma * sharp;
			#elif BlendMode == 6
				//Screen
				sharp = 1.0 - (2*(1.0-luma)*(1.0-sharp));
			#elif BlendMode == 2
				//overlay
				sharp = lerp(2*luma*sharp, 1.0 - 2*(1.0-luma)*(1.0-sharp), step(0.5,luma));
			#elif BlendMode == 4
				//Hardlight
				sharp = lerp(2*luma*sharp, 1.0 - 2*(1.0-luma)*(1.0-sharp), step(0.5,sharp));
			#elif BlendMode == 1 
				//softlight
				sharp = lerp(2*luma*color.rgb + luma*luma*(1.0-2*color.rgb), 2*luma*(1.0-sharp)+pow(luma,0.5)*(2*sharp-1.0), smoothstep(0.0,0.49,sharp.rgb));
			#elif BlendMode == 5
				//vivid light
				sharp = lerp(1-(1-luma)/(2*sharp), luma/(2*(1-sharp)), step(0.5,sharp));
			#endif
		
		/*Blend sharpmask with original*/
		#if SharpMask == 2 
			sharp = lerp(luma, sharp, HPSharpStrength);
			float3 midmask = lerp(1.0,-0.0,luma);
			float3 midmask2 = lerp(-0.0,1.0, luma);
			midmask = saturate(lerp(midmask,midmask2,luma));
			#if ViewMidtoneMask == 1 
			sharp = float3(1.0,0.0,0.0);
			luma = float3(0.0,0.0,1.0);
			#endif
			orig.rgb = lerp(sharp,luma,smoothstep(MidMaskDark,MidMaskLight,midmask));
		#else 
			orig.rgb = lerp(luma, sharp, HPSharpStrength);
		#endif
		
		#if ViewSharpMask == 1 || ViewMidtoneMask == 1
		#else
			orig.rgb += chroma;
		#endif
		
		//orig.rgb = color.rgb;
	return saturate(orig);
}
#endif

#if USE_HighPassContrastEnhancement == 1
float4 CEFinal(in float4 pos : SV_Position, in float2 texcoord : TEXCOORD) : COLOR
{
	
	float sampleOffsets[5] = { 0.0, 1.4347826, 3.3478260, 5.2608695, 7.1739130 };
	float sampleWeights[5] = { 0.16818994, 0.27276957, 0.11690125, 0.024067905, 0.0021112196 };
		
		float4 color = tex2D(ceBlurSamplerPing, texcoord) * sampleWeights[0];
		
		[loop]
		for(int j = 1; j < 5; ++j) {
			color += tex2D(ceBlurSamplerPing, texcoord + float2(0.0, sampleOffsets[j] * cePX_SIZE.y)) * sampleWeights[j];
			color += tex2D(ceBlurSamplerPing, texcoord - float2(0.0, sampleOffsets[j] * cePX_SIZE.y)) * sampleWeights[j];
		}
		
	float4 orig = tex2D(MainSampler, texcoord); //Original Image
	float3 luma = dot(orig.rgb,CoefLuma_HP);
	float3 chroma = orig.rgb - luma;
		
		//Contrast Mask
			float3 sharp = 1 - dot(color.rgb,CoefLuma_HP);
			sharp = (luma+sharp)*0.5;
		#if AdjustHaloStrengthCE == 1
			float3 curve = (2*(sharp - 0.5)*(sharp+0.5))+0.5;
			float3 sharpMin = saturate(lerp(sharp,curve,DarkHaloStrengthCE));
			sharpMin = min(sharp,sharpMin);
			float3 sharpMax = saturate(lerp(sharp,curve,LightHaloStrengthCE));
			sharpMax = max(sharp,sharpMax);
			sharp = 0.5*(sharpMin+sharpMax);		
		#elif CurveCE_Mask == 1
			float3 curve = (2*(sharp - 0.5)*(sharp+0.5))+0.5;
			sharp = saturate(lerp(sharp,curve,CurveCE_Strength));
		#elif CurveCE_Mask == 2
			float3 curve = (2*(sharp - 0.5)*(sharp+0.5))+0.5;
			curve = saturate(lerp(sharp,curve,CurveCE_Strength));
			sharp = min(sharp,curve);
		#elif CurveCE_Mask == 3
			float3 curve = (2*(sharp - 0.5)*(sharp+0.5))+0.5;
			curve = saturate(lerp(sharp,curve,CurveCE_Strength));
			sharp = max(sharp,curve);
		#endif
		
		sharp = clamp(sharp,ClampDarkHalosCE,ClampLightHalosCE);
		
		#if ViewCE_Mask == 1
				orig.rgb = sharp;
				luma = sharp;
			#elif CE_BlendMode == 3
				//Multiply
				sharp = 2 * luma * sharp;
			#elif CE_BlendMode == 6
				//soft light #2
				sharp = lerp(luma*(sharp+0.5),1-(1-luma)*(1-(sharp-0.5)),step(0.5,sharp));
			#elif CE_BlendMode == 2
				//overlay
				sharp = lerp(2*luma*sharp, 1.0 - 2*(1.0-luma)*(1.0-sharp), step(0.49,luma));
			#elif CE_BlendMode == 4
				//Hardlight
				sharp = lerp(2*luma*sharp.rgb, 1.0 - 2*(1.0-luma)*(1.0-sharp), step(0.49,sharp));
			#elif CE_BlendMode == 1 
				//softlight
				sharp = lerp(2*luma*sharp.rgb + luma*luma*(1.0-2*sharp.rgb), 2*luma*(1.0-sharp)+pow(luma,0.5)*(2*sharp-1.0), step(0.49,sharp.rgb));
			#elif CE_BlendMode == 5
				//vivid light
				sharp = lerp(2*luma*sharp, luma/(2*(1-sharp)), step(0.5,sharp));
			#elif CE_BlendMode == 7
				//soft light #3
				sharp = lerp((2*sharp-1)*(luma-pow(luma,2))+luma, ((2*sharp-1)*(pow(luma,0.5)-luma))+luma, step(0.49,sharp));
			#endif
			
			#if CE_Mask == 2 
					sharp = lerp(luma, sharp, CE_Strength);
					float3 midmask = lerp(1.0,0.0,dot(color.rgb,CoefLuma_HP));
					float3 midmask2 = lerp(0.0,1.0,dot(color.rgb,CoefLuma_HP));
					midmask = saturate(lerp(midmask,midmask2,luma));
					#if ViewMidtoneMaskCE == 1 
						sharp = float3(1.0,0.0,0.0);
						luma = float3(0.0,0.0,1.0);
					#endif
					orig.rgb = lerp(sharp,luma,smoothstep(MidMaskDarkCE,MidMaskLightCE,midmask));
			#else
				orig.rgb = lerp(luma, sharp, CE_Strength);
			#endif
			
			#if ViewCE_Mask == 1 || ViewMidtoneMaskCE == 1
			#else 
				orig.rgb += chroma;	
			#endif 
	//orig.rgb = color.rgb;
	return saturate(orig);
}	

float4 CEBlurX1(in float4 pos : SV_Position, in float2 texcoord : TEXCOORD) : COLOR
{
  
	float sampleOffsets[5] = { 0.0, 1.4347826, 3.3478260, 5.2608695, 7.1739130 };
	float sampleWeights[5] = { 0.16818994, 0.27276957, 0.11690125, 0.024067905, 0.0021112196 };

	float4 color = tex2D(ceBlurSamplerPong, texcoord) * sampleWeights[0];
	[loop]
	for(int i = 1; i < 5; ++i) {
		color += tex2D(ceBlurSamplerPong, texcoord + float2(sampleOffsets[i] * hpPX_SIZE.x, 0.0)) * sampleWeights[i];
		color += tex2D(ceBlurSamplerPong, texcoord - float2(sampleOffsets[i] * hpPX_SIZE.x, 0.0)) * sampleWeights[i]; 
	}
	
	return color;
}


float4 CEBlurY1(in float4 pos : SV_Position, in float2 texcoord : TEXCOORD) : COLOR
{
  
	float sampleOffsets[5] = { 0.0, 1.4347826, 3.3478260, 5.2608695, 7.1739130 };
	float sampleWeights[5] = { 0.16818994, 0.27276957, 0.11690125, 0.024067905, 0.0021112196 };

	float4 color = tex2D(ceBlurSamplerPing, texcoord) * sampleWeights[0];
	[loop]
	for(int j = 1; j < 5; ++j) {
		color += tex2D(ceBlurSamplerPing, texcoord + float2(0.0, sampleOffsets[j] * hpPX_SIZE.y)) * sampleWeights[j];
		color += tex2D(ceBlurSamplerPing, texcoord - float2(0.0, sampleOffsets[j] * hpPX_SIZE.y)) * sampleWeights[j];
	}

	return color;
}

float4 CEBlurX2(in float4 pos : SV_Position, in float2 texcoord : TEXCOORD) : COLOR
{
  
	float sampleOffsets[5] = { 0.0, 1.4347826, 3.3478260, 5.2608695, 7.1739130 };
	float sampleWeights[5] = { 0.16818994, 0.27276957, 0.11690125, 0.024067905, 0.0021112196 };

	float4 color = tex2D(ceBlurSamplerPong, texcoord) * sampleWeights[0];
	[loop]
	for(int i = 1; i < 5; ++i) {
		color += tex2D(ceBlurSamplerPong, texcoord + float2(sampleOffsets[i] * cePX_SIZE.x * 0.5, 0.0)) * sampleWeights[i];
		color += tex2D(ceBlurSamplerPong, texcoord - float2(sampleOffsets[i] * cePX_SIZE.x * 0.5, 0.0)) * sampleWeights[i]; 
	}
	
	return color;
}


float4 CEBlurY2(in float4 pos : SV_Position, in float2 texcoord : TEXCOORD) : COLOR
{
  
	float sampleOffsets[5] = { 0.0, 1.4347826, 3.3478260, 5.2608695, 7.1739130 };
	float sampleWeights[5] = { 0.16818994, 0.27276957, 0.11690125, 0.024067905, 0.0021112196 };

	float4 color = tex2D(ceBlurSamplerPing, texcoord) * sampleWeights[0];
	[loop]
	for(int j = 1; j < 5; ++j) {
		color += tex2D(ceBlurSamplerPing, texcoord + float2(0.0, sampleOffsets[j] * cePX_SIZE.y * 0.5)) * sampleWeights[j];
		color += tex2D(ceBlurSamplerPing, texcoord - float2(0.0, sampleOffsets[j] * cePX_SIZE.y * 0.5)) * sampleWeights[j];
	}

	return color;
}

float4 CEBlurX(in float4 pos : SV_Position, in float2 texcoord : TEXCOORD) : COLOR
{
  
	float sampleOffsets[5] = { 0.0, 1.4347826, 3.3478260, 5.2608695, 7.1739130 };
	float sampleWeights[5] = { 0.16818994, 0.27276957, 0.11690125, 0.024067905, 0.0021112196 };

	float4 color = tex2D(ceBlurSamplerPong, texcoord) * sampleWeights[0];
	[loop]
	for(int i = 1; i < 5; ++i) {
		color += tex2D(ceBlurSamplerPong, texcoord + float2(sampleOffsets[i] * cePX_SIZE.x, 0.0)) * sampleWeights[i];
		color += tex2D(ceBlurSamplerPong, texcoord - float2(sampleOffsets[i] * cePX_SIZE.x, 0.0)) * sampleWeights[i]; 
	}
	
	return color;
}


float4 CEBlurY(in float4 pos : SV_Position, in float2 texcoord : TEXCOORD) : COLOR
{
  
	float sampleOffsets[5] = { 0.0, 1.4347826, 3.3478260, 5.2608695, 7.1739130 };
	float sampleWeights[5] = { 0.16818994, 0.27276957, 0.11690125, 0.024067905, 0.0021112196 };

	float4 color = tex2D(ceBlurSamplerPing, texcoord) * sampleWeights[0];
	[loop]
	for(int j = 1; j < 5; ++j) {
		color += tex2D(ceBlurSamplerPing, texcoord + float2(0.0, sampleOffsets[j] * cePX_SIZE.y)) * sampleWeights[j];
		color += tex2D(ceBlurSamplerPing, texcoord - float2(0.0, sampleOffsets[j] * cePX_SIZE.y)) * sampleWeights[j];
	}

	return color;
}
#endif
 
technique Sharp_Tech <bool enabled = true; int toggle = ReShade_ToggleKey; >
{

#if USE_HighPassContrastEnhancement == 1 && ViewSharpMask != 1

	pass G 
	{
		
		VertexShader = VertexShader_G;
		PixelShader = OriginalPixel;
		RenderTarget = ceBlurTex2Dpong;
		
	}

	pass H1
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurX1;
		RenderTarget = ceBlurTex2Dping;
	}

	pass V1
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurY1;
		RenderTarget = ceBlurTex2Dpong;
	}
	
	pass H1
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurX2;
		RenderTarget = ceBlurTex2Dping;
	}

	pass V1
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurY2;
		RenderTarget = ceBlurTex2Dpong;
	}
	
		pass H1
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurX;
		RenderTarget = ceBlurTex2Dping;
	}
#if CE_MaskQuality >= 1
	pass V1
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurY;
		RenderTarget = ceBlurTex2Dpong;
	}
	
	pass H2
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurX;
		RenderTarget = ceBlurTex2Dping;
	}
#endif	
#if CE_MaskQuality >= 2
	pass V2
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurY;
		RenderTarget = ceBlurTex2Dpong;
	}
	
	pass H3
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurX;
		RenderTarget = ceBlurTex2Dping;
	}
#endif	
#if CE_MaskQuality >= 3	
	pass V3
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurY;
		RenderTarget = ceBlurTex2Dpong;
	}
		
	pass H4
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurX;
		RenderTarget = ceBlurTex2Dping;
	}
#endif	
#if CE_MaskQuality >= 4	
	pass V4
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurY;
		RenderTarget = ceBlurTex2Dpong;
	}	
	
	pass H5
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurX;
		RenderTarget = ceBlurTex2Dping;
	}
#endif	
#if CE_MaskQuality == 5	
	pass V5
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurY;
		RenderTarget = ceBlurTex2Dpong;
	}
	
	pass H6
	{
		VertexShader = VertexShader_G;
		PixelShader = CEBlurX;
		RenderTarget = ceBlurTex2Dping;
	}
#endif	
	pass ContEnhance
	{
		VertexShader = VertexShader_G;
		PixelShader = CEFinal;
	}
#endif

#if USE_HighPassSharpening == 1
	pass VFinal
	{
		VertexShader = VertexShader_G;
		PixelShader = SharpBlurFinal;
	}
#endif
}
