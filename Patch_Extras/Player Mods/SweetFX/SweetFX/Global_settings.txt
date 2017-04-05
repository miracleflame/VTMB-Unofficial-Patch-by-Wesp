  /*----------------------.
  | :: Global Settings :: |
  '----------------------*/

#define ReShade_ToggleKey        VK_SCROLL    //Set the key that should toggle the effects On/Off
#define ReShade_DepthToggleKey   VK_MULTIPLY  //Set the key to toggle the depth view On/Off

#define ReShade_Start_Enabled     1   //[0 or 1] Start with the effects enabled or disabled?

#define ReShade_Screenshot_Format 2   //[1 or 2] Sets the screenshot format (1 = bmp, 2 = png) You can take screenshots by pressing PrintScreen

#define ReShade_ShowToggleMessage 1   //[0 or 1] When enabled a message will show when the effects are toggled.

#define SweetFX_Greeting          1   //[0 or 1] Show the SweetFX greeting text on startup.

// -- Statistics --
#define ReShade_ShowStatistics    0   //[0 or 1] Controls the display of the statistics (fps and timecounters). 0 = off, 1 = on

#define ReShade_ShowClock         0   //[0 or 1] Show a clock
#define ReShade_ShowFPS           0   //[0 or 1] Show the FPS




  /*-----------------------.
  | :: Reference layout :: |
  '------------------------/

Keys should be set to a Windows Virtual Keycode in either decimal, hexadecimal or its VK_ alias.
Below is US ANSI keyboard reference for the keycodes in decimal:

US ANSI keyboard (104 keys) keycodes (note that your countrys keyboard layout maybe slightly different) :
.---.  .---.---.---.---. .---.---.---.---. .---.---.---.---.  .---.---.---.
| 27|  |112|113|114|115| |116|117|118|119| |120|121|122|123|  | 44|145| 19|
`---'  `---'---'---'---' `---'---'---'---' `---'---'---'---'  `---'---'---'

.---.---.---.---.---.---.---.---.---.---.---.---.---.------.  .---.---.---.  .---.---.---.---.
|192| 49| 50| 51| 52| 53| 54| 55| 56| 57| 48|189|187|   8  |  | 45| 36| 33|  |144|111|106|109|
:---'---'---'---'---'---'---'---'---'---'---'---'---'------:  :---:---:---:  :---:---:---:---:
|  9 | 81| 87| 69| 82| 84| 89| 85| 73| 79| 80|219|221| 220 |  | 46| 35| 34|  |103|104|105|   |
:----'---'---'---'---'---'---'---'---'---'---'---'---'-----|  `---'---'---'  :---:---:---|107|
|  20 | 65| 83| 68| 70| 71| 72| 74| 75| 76|186|222|   13   |                 |100|101|102|   |
:-----'---'---'---'---'---'---'---'---'---'---'---'--------'      .---.      :---:---:---:---:
|   16  | 90| 88| 67| 86| 66| 78| 77|188|190|191|    16    |      | 38|      | 97| 98| 99|   |
:-------'---'---'---'---'---'---'---'---'---'---'----------'  .---:---|---.  :---'---:---| 13|
| 17 | 91 | 18 |           32          | 18 | 92 | 93 | 17 |  | 37| 40| 39|  |   96  |110|   |
`----'----'----'-----------------------'----'----'----'----'  `---'---'---'  `-------'---'---'

For a complete list of all the keycodes see /SweetFX/Docs/KeyCodes.txt

For more example layouts than just the US ANSI keyboard and more info on keycodes see /SweetFX/Docs/Keyboard.txt

  /*------------------.
  | :: End of file :: |
  '------------------*/