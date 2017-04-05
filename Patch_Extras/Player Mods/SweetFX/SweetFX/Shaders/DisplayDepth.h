void DisplayDepth(in float4 position : SV_Position, in float2 texcoord : TEXCOORD0, out float3 color : SV_Target)
{
    //Depth buffer access
    float depth = tex2D(depthSampler, texcoord).x;

    // Linearize depth
    //const float z_near = 1.0;   // camera z near
    //const float z_far  = 100.0; // camera z far
    depth = (2.0 * Depth_z_near) / ( -(Depth_z_far - Depth_z_near) * depth + (Depth_z_far + Depth_z_near) );	
  
    color.rgb = float3(depth.xxx);

  }