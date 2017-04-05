   /*-----------------------------------------------------------.
  /                           Custom                            /
  '-----------------------------------------------------------*/
/*

*/

#define CustomLuma float3(0.2126, 0.7152, 0.0722)

float3 CustomPass(float4 position : SV_Position, float2 texcoord : TEXCOORD0) : SV_Target
{

  float3 colorInput = tex2D(s0, texcoord).rgb; //sample using the s0 sampler at the tex coordinates.
                                          //s0 is an alias for the colorGammaSampler - see sweet.fx for a list of samplers
                                          //texcoord contains the texture coordinates of our current pixel
                                          //.rgb is a component selection for just the red , green and blue channel - a tex2D also returns an alpha channel which we don't need
                                          //or do we? It's your shader - you decide.
                                          
  //just some example code. 
  //float luma = dot(colorInput.rgb,CustomLuma); //Calculate luma
  //float3 chroma = colorInput.rgb - luma; //Calculate chroma
  
  float3 color = 1.0 - colorInput; //invert the luma
  
  //color = color + chroma; //add the chroma back in
  
  color = lerp(color, colorInput, custom_strength); //Adjust the strength of the effect

  return saturate(color); //saturate clamps between 0.0 and 1.0. Used on the output of a instruction it's free (costs no extra performance)
                          //I do it here just as a precaution against any mistakes we might have overlooked.
                          //It should not normally be needed .. but since it's free.. why not?
}