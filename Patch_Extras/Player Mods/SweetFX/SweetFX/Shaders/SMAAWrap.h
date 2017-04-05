	////////////////////////////
	// Vertex shader wrappers //
	////////////////////////////
	
	void SMAAEdgeDetectionVSWrap( in uint id : SV_VertexID,
																out float4 position : SV_Position,
																out float2 texcoord : TEXCOORD0,
																out float4 offset0 : TEXCOORD1,
																out float4 offset1 : TEXCOORD2,
																out float4 offset2 : TEXCOORD3 )
	{
		float4 offset[3];
		FullscreenTriangle(id, position, texcoord);
		SMAAEdgeDetectionVS(texcoord, offset);
		
		// Get around OpenGL not accepting array input/outputs
		offset0 = offset[0], offset1 = offset[1], offset2 = offset[2];
	}
	
	void SMAABlendingWeightCalculationVSWrap( in uint id : SV_VertexID,
																						out float4 position : SV_Position,
																						out float2 texcoord : TEXCOORD0,
																						out float2 pixcoord : TEXCOORD1,
																						out float4 offset0 : TEXCOORD2,
																						out float4 offset1 : TEXCOORD3,
																						out float4 offset2 : TEXCOORD4 )
	{
		float4 offset[3];
		FullscreenTriangle(id, position, texcoord);
		SMAABlendingWeightCalculationVS(texcoord, pixcoord, offset);
		
		// Get around OpenGL not accepting array input/outputs
		offset0 = offset[0], offset1 = offset[1], offset2 = offset[2];
	}

	void SMAANeighborhoodBlendingVSWrap(in uint id : SV_VertexID,
																			out float4 position : SV_Position,
																			out float2 texcoord : TEXCOORD0,
																			out float4 offset : TEXCOORD1)
	{
		FullscreenTriangle(id, position, texcoord);
		SMAANeighborhoodBlendingVS(texcoord, offset);
	}

	///////////////////////////
	// Pixel shader wrappers //
	///////////////////////////
	
	#ifndef __RESHADE__//GPU_SHADERANALYZER //GPU Shaderanalyzer requires that DX9-style pixel shaders output a float4
	  #define OUTPUT_FLOAT float4
    #define OUTPUT_COMPONENT rrrr
    #define OUTPUT_FLOAT2 float4
    #define OUTPUT_COMPONENT2 rgrg
    #define OUTPUT_FLOAT3 float4
    #define OUTPUT_COMPONENT3 rgbr
  #else
    #define OUTPUT_FLOAT float
    #define OUTPUT_COMPONENT r
    #define OUTPUT_FLOAT2 float2
    #define OUTPUT_COMPONENT2 rg
    #define OUTPUT_FLOAT3 float3
    #define OUTPUT_COMPONENT3 rgb
  #endif

#if SMAA_EDGE_DETECTION == 1
	OUTPUT_FLOAT2 SMAALumaEdgeDetectionPSWrap(	float4 position : SV_Position,
																			float2 texcoord : TEXCOORD0,
																			float4 offset0 : TEXCOORD1,
																			float4 offset1 : TEXCOORD2,
																			float4 offset2 : TEXCOORD3) : SV_Target
	{
	
		float4 offset[3] = { offset0, offset1, offset2 };

		return SMAALumaEdgeDetectionPS(
																		texcoord,
																		offset,
																		colorGammaSampler
																		
																		#if SMAA_PREDICATION == 1
																		,predicationSampler
																		#endif
																	).OUTPUT_COMPONENT2;
	}
#elif SMAA_EDGE_DETECTION == 3
	OUTPUT_FLOAT2 SMAADepthEdgeDetectionPSWrap(float4 position : SV_Position,
																			float2 texcoord : TEXCOORD0,
																			float4 offset0 : TEXCOORD1,
																			float4 offset1 : TEXCOORD2,
																			float4 offset2 : TEXCOORD3) : SV_Target
	{
		float4 offset[3] = { offset0, offset1, offset2 };
		return SMAADepthEdgeDetectionPS(texcoord, offset, depthSampler).OUTPUT_COMPONENT2;
	}


#else //SMAA_EDGE_DETECTION == 2	
	OUTPUT_FLOAT2 SMAAColorEdgeDetectionPSWrap(float4 position : SV_Position,
																			float2 texcoord : TEXCOORD0,
																			float4 offset0 : TEXCOORD1,
																			float4 offset1 : TEXCOORD2,
																			float4 offset2 : TEXCOORD3) : SV_Target
	{
		float4 offset[3] = { offset0, offset1, offset2 };
		return SMAAColorEdgeDetectionPS(
																		texcoord,
																		offset,
																		colorGammaSampler
																		
																		#if SMAA_PREDICATION == 1
																		 ,predicationSampler
																		#endif
																	 ).OUTPUT_COMPONENT2;
	}
#endif


	float4 SMAABlendingWeightCalculationPSWrap(	float4 position : SV_Position,
																							float2 texcoord : TEXCOORD0,
																							float2 pixcoord : TEXCOORD1,
																							float4 offset0 : TEXCOORD2,
																							float4 offset1 : TEXCOORD3,
																							float4 offset2 : TEXCOORD4) : SV_Target
	{
		float4 offset[3] = { offset0, offset1, offset2 };
		return SMAABlendingWeightCalculationPS(texcoord, pixcoord, offset, edgesSampler, areaSampler, searchSampler, 0.0);
	}

	OUTPUT_FLOAT3 SMAANeighborhoodBlendingPSWrap(float4 position : SV_Position,
																				float2 texcoord : TEXCOORD0,
																				float4 offset : TEXCOORD1) : SV_Target
	{
    #if SMAA_DEBUG_OUTPUT == 1
      return tex2D(edgesSampler, texcoord); // Show edgesTex
    #elif SMAA_DEBUG_OUTPUT == 2
      return tex2D(blendSampler, texcoord); // Show blendTex
    #elif SMAA_DEBUG_OUTPUT == 3
      return tex2D(areaSampler, texcoord); // Show areaTex
    #elif SMAA_DEBUG_OUTPUT == 4
      return tex2D(searchSampler, texcoord); // Show searchTex
    #elif SMAA_DEBUG_OUTPUT == 5
      return float3(1.0, 0.0, 0.0); // Show the stencil in red.
    #else
			
			float3 color = SMAANeighborhoodBlendingPS(texcoord, offset, colorLinearSampler, blendSampler).rgb;
			
			#ifdef Shared_Piggyback_SMAA
				color.rgb = (color.rgb <= 0.0031308) ? saturate(abs(color.rgb) * 12.92) : 1.055 * saturate(pow(abs(color.rgb), 1.0/2.4 )) - 0.055; // Linear to SRGB
			
				color.rgb = SharedPass(texcoord, float4(color.rgbb)).rgb;
			#endif
			
			return color.OUTPUT_COMPONENT3;
			
    #endif
	}

