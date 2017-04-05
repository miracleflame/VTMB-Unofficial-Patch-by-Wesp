  float3 FXAA(in float4 position : SV_Position, in float2 texcoord : TEXCOORD0) : SV_Target
  {
		float3 color = FxaaPixelShader(texcoord, colorGammaSampler, pixel, float4(0.0f, 0.0f, 0.0f, 0.0f), fxaa_Subpix, fxaa_EdgeThreshold, fxaa_EdgeThresholdMin).rgb;
    
    #ifdef Shared_Piggyback_FXAA
			color.rgb = SharedPass(texcoord, float4(color.rgbb)).rgb;
		#endif
	
	return color;
  }
