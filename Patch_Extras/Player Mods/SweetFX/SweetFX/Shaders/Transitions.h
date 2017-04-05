  /*------------------.
  | :: Transitions :: |
  '------------------*/
/*
These effects run when SweetFX is initialized and disable themselves when a counter (timeleft) reaches 0
*/




// MMMmnnn Juicy :)
void FadeIn(in float4 position : SV_Position, in float2 texcoord : TEXCOORD0, out float4 color : SV_Target)
{
	color = tex2D(colorGammaSampler, texcoord);
	color.rgb *= -timeleft * (1.0 / 8000.0) + 1.0;
}

void FadeOut(in float4 position : SV_Position, in float2 texcoord : TEXCOORD0, out float4 color : SV_Target)
{
	color = tex2D(colorGammaSampler, texcoord);
	color.rgb *= timeleft * (1.0 / 8000.0) - 1.0;
}

void CurtainOpen(in float4 position : SV_Position, in float2 texcoord : TEXCOORD0, out float4 color : SV_Target)
{
		const float curtain_time = 3500.0; //Time it takes for the curtain to slide away. (timeleft - curtain_time) will be the time before it starts to slide away.

		float coord = abs(texcoord.x - 0.5);
		float factor = saturate(1.0 - timeleft / curtain_time);

		if (coord < factor || timer > 10000.0)
			color = tex2D(colorGammaSampler, texcoord);
		else
			color = tex2D(transitionSampler, texcoord + float2(texcoord.x < 0.5 ? factor : -factor, 0));
}

void CurtainClose(in float4 position : SV_Position, in float2 texcoord : TEXCOORD0, out float4 color : SV_Target)
{
  float coord = abs(texcoord.x - 0.5);
  float factor = (timeleft / 8000.0);
  if (coord < factor)
	  color = tex2D(colorGammaSampler, texcoord);
  else
	  color = tex2D(transitionSampler, texcoord + float2(texcoord.x < 0.5 ? factor : -factor, 0));
}

void ImageFadeOut(in float4 position : SV_Position, in float2 texcoord : TEXCOORD0, out float3 color : SV_Target)
{
	float3 image = tex2D(transitionSampler, texcoord).rgb;
	color = tex2D(colorGammaSampler, texcoord).rgb;
	color = lerp(color,image, saturate(timeleft * (1.0 / 1000.0)));
}