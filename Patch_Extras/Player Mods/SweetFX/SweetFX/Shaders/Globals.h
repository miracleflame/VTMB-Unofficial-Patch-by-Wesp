  /*----------------.
  | :: Constants :: |
  '----------------*/

//These values are normally defined by the injector dlls, but not when analyzed by GPU Shaderanalyzer
//I need to ensure they always have a value to be able to compile them whenever I'm not using the injector.
#ifdef SMAA_PIXEL_SIZE
  #ifndef BUFFER_RCP_WIDTH
    #define BUFFER_RCP_WIDTH SMAA_PIXEL_SIZE.x
    #define BUFFER_RCP_HEIGHT SMAA_PIXEL_SIZE.y
    #define BUFFER_WIDTH (1.0 / SMAA_PIXEL_SIZE.x)
    #define BUFFER_HEIGHT (1.0 / SMAA_PIXEL_SIZE.y)
  #endif
#endif

#ifndef BUFFER_RCP_WIDTH
  #define BUFFER_RCP_WIDTH (1.0 / 1680)
  #define BUFFER_RCP_HEIGHT (1.0 / 1050)
  #define BUFFER_WIDTH 1680
  #define BUFFER_HEIGHT 1050
#endif

#define px BUFFER_RCP_WIDTH
#define py BUFFER_RCP_HEIGHT

#define pixel float2(BUFFER_RCP_WIDTH,BUFFER_RCP_HEIGHT)
#define screen_size float2(BUFFER_WIDTH,BUFFER_HEIGHT)

  /*-----------------------.
  | ::     Uniforms     :: |
  '-----------------------*/

uniform float timer < string source = "timer"; >;
uniform float timeleft < string source = "timeleft"; >;
//uniform float2 pingpong < source = "pingpong"; min = -1; max = 2; step = 2; >;
//uniform int framecount < source = "framecount"; >; // Total amount of frames since the game started.

