  /*--------------------.
  | :: Shared passes :: |
  '--------------------*/

//float4 SweetFX_main(float2 tex, float4 FinalColor) //RadeonPro expects main()
float4 SharedPass(float2 tex, float4 FinalColor)
{

/*
  // SweetCRT
  #if (USE_SWEETCRT == 1)
     
    FinalColor = SweetCRTPass(FinalColor,tex);
  #endif
*/
    // Palette
  #if (USE_NOSTALGIA == 1)
    FinalColor = Nostalgia(FinalColor);
  #endif

  // Levels
  #if (USE_LEVELS == 1)
    FinalColor = LevelsPass(FinalColor);
  #endif

  // Technicolor
  #if (USE_TECHNICOLOR == 1)
    FinalColor = TechnicolorPass(FinalColor);
  #endif
  
  // Technicolor2
  #if (USE_TECHNICOLOR2 == 1)
    FinalColor.rgb = Technicolor2(FinalColor.rgb);
  #endif

  // DPX
  #if (USE_DPX == 1)
    FinalColor = DPXPass(FinalColor);
  #endif

  // Monochrome
  #if (USE_MONOCHROME == 1)
    FinalColor = MonochromePass(FinalColor);
  #endif

  // ColorMatrix
  #if (USE_COLORMATRIX == 1)
    FinalColor = ColorMatrixPass(FinalColor);
  #endif

  // Lift Gamma Gain
  #if (USE_LIFTGAMMAGAIN == 1)
    FinalColor = LiftGammaGainPass(FinalColor);
  #endif

  // Tonemap
  #if (USE_TONEMAP == 1)
    FinalColor = TonemapPass(FinalColor);
  #endif

  // Vibrance
  #if (USE_VIBRANCE == 1)
    FinalColor = VibrancePass(FinalColor);
  #endif

  // Curves
  #if (USE_CURVES == 1)
    FinalColor = CurvesPass(FinalColor);
  #endif

  // Sepia
  #if (USE_SEPIA == 1)
    FinalColor = SepiaPass(FinalColor);
  #endif

  // Vignette
  #if (USE_VIGNETTE == 1)
    FinalColor = VignettePass(FinalColor,tex);
  #endif
 
/* //didn't make it into 1.6
  // Daltonize
  #if (USE_DALTONIZE == 1)
    FinalColor = Daltonize(FinalColor);
  #endif
*/

  // FilmGrain
  #if (USE_FILMGRAIN == 1)
    FinalColor = FilmGrainPass(FinalColor,tex);
  #endif
  
  // Dither (should go near the end as it only dithers what went before it)
  #if (USE_DITHER == 1)
    FinalColor = DitherPass(FinalColor,tex);
  #endif

  // Border
  #if (USE_BORDER == 1)
    FinalColor = BorderPass(FinalColor,tex);
  #endif

  // Splitscreen
  #if (USE_SPLITSCREEN == 1)
    FinalColor = SplitscreenPass(FinalColor,tex);
  #endif

/* //didn't make it into 1.6
  #if (USE_PRINT == 1)
    FinalColor = PrintPass(FinalColor,tex);
  #endif
*/  

  // Return FinalColor
  return FinalColor;
}

void SharedWrap(in float4 position : SV_Position, in float2 texcoord : TEXCOORD0, out float3 color : SV_Target)
{
	color = tex2D(colorGammaSampler, texcoord).rgb;

	color = SharedPass(texcoord, color.rgbb).rgb;
}


