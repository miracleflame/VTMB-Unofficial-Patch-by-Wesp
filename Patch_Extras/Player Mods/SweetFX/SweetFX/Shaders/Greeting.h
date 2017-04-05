  /*-----------------------.
  | :: Greeting message :: |
  '-----------------------*/

#pragma message "\
SweetFX 2.0 beta by CeeJay.dk\n\
\n"

#if __RENDERER__ >= 0x14300
  #pragma message "Rendering using OpenGL\n"

#elif __RENDERER__ >= 0x9100 && __RENDERER__ <= 0x09300
  #pragma message "Rendering using D3D9\n"
  
#elif __RENDERER__ == 0xA000 || __RENDERER__ == 0xA100
  #pragma message "Rendering using D3D10\n"
  
#elif __RENDERER__ >= 0xB000 && __RENDERER__ <= 0xB200
  #pragma message "Rendering using D3D11\n"
  
#endif

#pragma message "\n\
Press Printscreen to take screenshots\n"

#if ReShade_ToggleKey == VK_SCROLL
  #pragma message "Press Scrolllock to toggle effects on/off\n"
#else
	#pragma message "Press your custom toggle key (see the Reshade settings) to toggle effects on/off\n"
#endif

//#pragma message "\nReticulating splines.."
//#pragma message "\nInsert Coin"
//#pragma message "\nPress START Player 1"