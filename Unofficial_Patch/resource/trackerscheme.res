///////////////////////////////////////////////////////////
// Tracker scheme resource file
//
// sections:
//		Colors			- all the colors used by the scheme
//		BaseSettings	- contains settings for app to use to draw controls
//		Fonts			- list of all the fonts used by app
//		Borders			- description of all the borders
//
// hit ctrl-alt-shift-R in the app to reload this file
//
///////////////////////////////////////////////////////////
Scheme
{
	//////////////////////// COLORS ///////////////////////////
	// color details
	// this is a list of all the colors used by the scheme
	Colors
	{
		// base colors
		"BaseText"		"216 222 211 255"		// used in text windows, lists
		"BrightBaseText" "255 255 255 255"	// brightest text
		"DimBaseText"	"150 159 142 255"		// dim base text
		
		"LabelDimText"	"160 170 149 255"		// slight modification on above, used for info text
												// could be just removed and use DimBaseText?
		
		"ControlText"	"216 222 211 255"		// used in all text controls
		"BrightControlText"	"177 167 98 255"	// use for selected controls
		"DisabledText1"	"117 128 111 255"		// disabled text
		"DisabledText2"	"30 30 30 255"		// overlay color for disabled text (to give that inset look)

		// background colors
//		"ControlBG"		"76 88 68 255"		// background color of controls
//		"ControlDarkBG" "90 106 80 255"		// darker background color; used for background of scrollbars
//		"WindowBG"		"62 70 55 255"		// background color of text edit panes (chat, text entries, etc.)
//		"SelectionBG"	"149 136 49 255"		// background color of any selected text or menu item

		"ControlBG"		"57 47 37 255"		// background color of controls
		"ControlDarkBG" "40 30 21 255"		// darker background color; used for background of scrollbars
		"WindowBG"		"32 32 32 255"		// background color of text edit panes (chat, text entries, etc.)
		"SelectionBG"	"90 24 24 255"		// background color of any selected text or menu item

		// title colors
		"TitleText"		"255 255 255 255"
		"TitleDimText"	"120 132 114 255"
		"TitleBG"		"76 88 68 0"
		"TitleDimBG"	"76 88 68 0"

		// border colors
//		"BorderBright"	"136 145 128 255"		// the lit side of a control
//		"BorderDark"	"45 49 40 255"		// the dark/unlit side of a control
		"BorderBright"	"145 128 128 255"		// the lit side of a control
		"BorderDark"	"40 30 21 255"		// the dark/unlit side of a control
		"BorderSelection"	"0 0 0 255"		// the additional border color for displaying the default/selected button
		
		// Bloody colors
		"BloodNormal" "168 9 9 255"
		"BloodBright" "192 15 15 255"
		"BloodDim" "128 4 4 128"
		
		"DialogBackground" "57 37 27 255"	// vampire load/save/etc dialog background color



		// Vampire Dialog UI:  (Note: Alpha is ignored, as it is overridden in code to "fade in/out")
		"Dlg_FillBkg"		"0 0 0 175"  // Here we care about the alpha!  
//		"Dlg_FillBkg"		"0 0 0 96"  // Here we care about the alpha!  -- Original value

		"Dlg_Base"			"255 255 255 0"
		"Dlg_Persuasion"	"0 120 255 0"
		"Dlg_Seduction"		"255 109 255 0"
		"Dlg_Dominate"		"255 0 0 0"
		"Dlg_Dementation"	"255 0 0 0"
		"Dlg_Intimidate"	"0 255 81 0"
		"Dlg_Autolink"		"255 255 255 0"
		"Dlg_Error"			"255 255 255 0"


		// Vampire Discipline UI:
		"DiscUI_Aqua"		"6 153 102 0"
		"DiscUI_Orange"		"181 130 57 0"
		"DiscUI_Yellow"		"153 197 82 0"
		"DiscUI_Gray"		"181 185 168 0"


		"BrownBorder"		"94 75 49 0"
	}

	///////////////////// BASE SETTINGS ////////////////////////
	//
	// default settings for all panels
	// controls use these to determine their settings
	BaseSettings
	{
		"FgColor"			"ControlText"
		"BgColor"			"ControlBG"
		"LabelBgColor"		"ControlBG"
		"SubPanelBgColor"	"ControlBG"

		"DisabledFgColor1"		"DisabledText1" 
		"DisabledFgColor2"		"DisabledText2"		// set this to the BgColor if you don't want it to draw

		"TitleBarFgColor"			"TitleText"
		"TitleBarDisabledFgColor"	"TitleDimText"
		"TitleBarBgColor"			"TitleBG"
		"TitleBarDisabledBgColor"	"TitleDimBG"

//		"TitleBarIcon"				"resource/icon_steam"
//		"TitleBarDisabledIcon"		"resource/icon_steam_disabled"
		"TitleBarIcon"				"hud/Vamp_Icon1"
		"TitleBarDisabledIcon"			"hud/hud/Vamp_Icon1"

		"TitleButtonFgColor"			"BorderBright"
		"TitleButtonBgColor"			"ControlBG"
		"TitleButtonDisabledFgColor"	"TitleDimText"
		"TitleButtonDisabledBgColor"	"TitleDimBG"

		"TextCursorColor"			"BaseText"		// color of the blinking text cursor in text entries
		"URLTextColor"				"BrightBaseText"		// color that URL's show up in chat window

		Menu
		{
			"FgColor"			"DimBaseText"
			"BgColor"			"ControlBG"
			"ArmedFgColor"		"BrightBaseText"
			"ArmedBgColor"		"SelectionBG"
			"DividerColor"		"BorderDark"

			"TextInset"			"6"
		}

		MenuButton	  // the little arrow on the side of boxes that triggers drop down menus
		{
			"ButtonArrowColor"	"DimBaseText"	// color of arrows
		   	"ButtonBgColor"		"WindowBG"	// bg color of button. same as background color of text edit panes 
			
			"ArmedArrowColor"		"BrightBaseText" // color of arrow when mouse is over button
			"ArmedBgColor"		"DimBaseText"  // bg color of button when mouse is over button
		}

		Slider
		{
			"SliderFgColor"		"ControlBG"		// handle with which the slider is grabbed
			"SliderBgColor"		"ControlDarkBG"		// area behind handle
		}

		ScrollBarSlider
		{
			"BgColor"			"ControlBG"		// this isn't really used

			"ScrollBarSliderFgColor"		"ControlBG"		// handle with which the slider is grabbed
			"ScrollBarSliderBgColor"		"ControlDarkBG"		// area behind handle

			"ButtonFgColor"		"DimBaseText"	// color of arrows
		}


		// text edit windows
		"WindowFgColor"				"BaseText"		// off-white
		"WindowBgColor"				"WindowBG"
		"WindowDisabledFgColor"		"DimBaseText"
		"WindowDisabledBgColor"		"66 80 60 255"		// background of chat conversation

		"SelectionFgColor"			"255 255 255 255"		// fg color of selected text
		"SelectionBgColor"			"SelectionBG"
		"ListSelectionFgColor"		"255 255 255 255"			// 

		"ListBgColor"				"80 65 47 255"	// background of server browser control, etc
		"BuddyListBgColor"			"80 65 47 255"	// background of buddy list pane
		
		// App-specific stuff
		"ChatBgColor"				"WindowBgColor"

		// status selection
		"StatusSelectFgColor"		"BrightBaseText"
		"StatusSelectFgColor2"		"BrightControlText"		// this is the color of the friends status

		// checkboxes
		"CheckButtonBorder1"   		"BorderDark" 		// the left checkbutton border
		"CheckButtonBorder2"   		"BorderBright"		// the right checkbutton border
		"CheckButtonCheck"			"0 0 0 255"				// color of the check itself
		"CheckBgColor"				"158 168 150 255"

		// buttons (default fg/bg colors are used if these are not set)
//		"ButtonArmedFgColor"
//		"ButtonArmedBgColor"
//		"ButtonDepressedFgColor"	"BrightControlText"
//		"ButtonDepressedBgColor"

		// buddy buttons
		BuddyButton
		{
			"FgColor1"		"ControlText"
			"FgColor2"		"117 134 102 255"

			"ArmedFgColor1"	"BrightBaseText"
			"ArmedFgColor2"	"BrightBaseText"
			"ArmedBgColor"	"SelectionBG"
		}

		Chat
		{
			"TextColor"				"BrightControlText"
			"SelfTextColor"			"BaseText"
			"SeperatorTextColor"	"DimBaseText"
		}

		"SectionTextColor"		"BrightControlText"		// text color for IN-GAME, ONLINE, OFFLINE sections of buddy list
		"SectionDividerColor"	"BorderDark"		// color of line that runs under section name in buddy list

		// TF2 HUD
		"HudStatusBgColor"			"0 0 0 64"
		"HudStatusSelectedBgColor"	"0 0 0 192"
	}

	//
	//////////////////////// FONTS /////////////////////////////
	//
	// describes all the fonts
	Fonts
	{
		// fonts are used in order that they are listed
		// fonts listed later in the order will only be used if they fulfill a range not already filled
		// if a font fails to load then the subsequent fonts will replace
		"Default"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultFixed"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultUnderline"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"500"
				"underline" "1"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultSmall"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"13"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultVerySmall"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"12"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"DefaultLarge"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"18"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		// this is the symbol font
		"Marlett"
		{
			"1"
			{
				"name"		"Marlett"
				"tall"		"14"
				"weight"	"0"
				"symbol"	"1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Trebuchet24"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"24"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}


		"Trebuchet20"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"20"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Trebuchet18"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"18"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

// Vampire Fonts
		"PercolatorMedium"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"35"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorSmall"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"26"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Copperplate"
		{
			"1"
			{
				"name"		"Vamp_Small"
				"tall"		"18"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Dominican"
		{
			"1"
			{
				"name"		"Vamp_Plain"
//				"tall"		"19"
				"tall"		"22"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}


// Vampire Localization Fonts
		"Localization_0"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"48"
				"weight"	"1000"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Localization_1"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"14"
				"weight"	"1000"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Localization_2"
		{
			"1"
			{
				"name"		"Vamp_Plain"
				"tall"		"14"
				"weight"	"1000"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Localization_3"
		{
			"1"
			{
				"name"		"Vamp_Plain"
				"tall"		"22"
				"weight"	"1000"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Localization_4"
		{
			"1"
			{
				"name"		"Vamp_Plain"
				"tall"		"44"
				"weight"	"1000"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Localization_5"
		{
			"1"
			{
				"name"		"Vamp_Small"
				"tall"		"16"
				"weight"	"1000"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}



		// [ 640 ]
		"Default_640"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"10"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultFixed_640"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"10"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultUnderline_640"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"10"
				"weight"	"500"
				"underline" "1"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultSmall_640"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"8"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultVerySmall_640"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"7"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"DefaultLarge_640"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"11"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Marlett_640"
		{
			"1"
			{
				"name"		"Marlett"
				"tall"		"8"
				"weight"	"0"
				"symbol"	"1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

//		"Troika_640"
//		{
//			"1"
//			{
//				"name"		"TroikaGames"
//				"tall"		"69"
//				"weight"	"1000"
////				"range"		"0x0000 0x007F"	//	Basic Latin
//				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
//			}
//		}

		"MainMenu_640"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"44"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorMedium_640"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"21"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorSmall_640"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"16"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Copperplate_640"
		{
			"1"
			{
				"name"		"Vamp_Small"
				"tall"		"11"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Dominican_640"
		{
			"1"
			{
//				"name"		"Vamp_Plain"
				"name"		"Vamp_Dialog_Base"
				"tall"		"16"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"ParagraphText_640"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"12"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Trebuchet_640"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"15"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Tahoma_640"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"10"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

			// Used for in-game dialog
		"Dlg_Base_640"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"15"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Malk_640"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"15"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Dementation_640"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"15"	// changed by wesp
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Dominate_640"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"15"	// changed by wesp
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Persuasion_640"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"15"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Seduction_640"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"15"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Intimidate_640"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Intimidate"
				"tall"		"15"	// changed by wesp
				// Changed to fix bug #6803: Intimidation font extends outside dialogue box
//				"name"		"Vamp_Dialog_Base"
//				"tall"		"15"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

			// Used for Ammo UI
		"BenguiatBig_640"
		{
			"1"
			{
				"name"		"Vamp_Ammo"
				"tall"		"19"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"BenguiatSmall_640"
		{
			"1"
			{
				"name"		"Vamp_Ammo"
				"tall"		"15"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"HudFont_640"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"8"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"LCD_640"
		{
			"1"
			{
				"name"		"Vamp_LCD"
				"tall"		"18"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Vamp_Handwriting1_640"
		{
			"1"
			{
				"name"		"Vamp_Handwriting1"
				"tall"		"17"	//"18"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Headline_640"
		{
			"1"
			{
				"name"		"Times New Roman"
				"tall"		"34"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Newsprint_640"
		{
			"1"
			{
				"name"		"Times New Roman"
				"tall"		"11"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		// [ 800 ]
		"Default_800"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"12"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultFixed_800"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"12"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultUnderline_800"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"12"
				"weight"	"500"
				"underline" "1"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultSmall_800"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"10"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultVerySmall_800"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"9"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"DefaultLarge_800"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"14"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Marlett_800"
		{
			"1"
			{
				"name"		"Marlett"
				"tall"		"11"
				"weight"	"0"
				"symbol"	"1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

//		"Troika_800"
//		{
//			"1"
//			{
//				"name"		"TroikaGames"
//				"tall"		"86"
//				"weight"	"1000"
////				"range"		"0x0000 0x007F"	//	Basic Latin
//				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
//			}
//		}

		"MainMenu_800"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"55"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorMedium_800"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"27"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorSmall_800"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"20"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Copperplate_800"
		{
			"1"
			{
				"name"		"Vamp_Small"
				"tall"		"14"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Dominican_800"
		{
			"1"
			{
				"name"		"Vamp_Plain"
				"tall"		"20"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"ParagraphText_800"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"15"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Trebuchet_800"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"18"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Tahoma_800"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"12"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Base_800"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"18"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Malk_800"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"18"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Dementation_800"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"18"	// changed by wesp
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Dominate_800"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"18"	// changed by wesp
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Persuasion_800"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"18"	// changed by wesp
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Seduction_800"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"18"	// changed by wesp
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Intimidate_800"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"18"	// changed by wesp
				// Changed to fix bug #6803: Intimidation font extends outside dialogue box
//				"name"		"Vamp_Dialog_Base"
//				"tall"		"18"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

			// Used for Ammo UI
		"BenguiatBig_800"
		{
			"1"
			{
				"name"		"Vamp_Ammo"
				"tall"		"24"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"BenguiatSmall_800"
		{
			"1"
			{
				"name"		"Vamp_Ammo"
				"tall"		"18"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"HudFont_800"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"9"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"LCD_800"
		{
			"1"
			{
				"name"		"Vamp_LCD"
				"tall"		"23"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Vamp_Handwriting1_800"
		{
			"1"
			{
				"name"		"Vamp_Handwriting1"
				"tall"		"23"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Headline_800"
		{
			"1"
			{
				"name"		"Times New Roman"
				"tall"		"43"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Newsprint_800"
		{
			"1"
			{
				"name"		"Times New Roman"
				"tall"		"14"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		// [ 1024 ]
		"Default_1024"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultFixed_1024"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultUnderline_1024"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"500"
				"underline" "1"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultSmall_1024"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"13"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultVerySmall_1024"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"12"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"DefaultLarge_1024"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"18"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Marlett_1024"
		{
			"1"
			{
				"name"		"Marlett"
				"tall"		"14"
				"weight"	"0"
				"symbol"	"1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

//		"Troika_1024"
//		{
//			"1"
//			{
//				"name"		"TroikaGames"
//				"tall"		"110"
//				"weight"	"1000"
////				"range"		"0x0000 0x007F"	//	Basic Latin
//				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
//			}
//		}

		"MainMenu_1024"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"71"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorMedium_1024"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"35"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorSmall_1024"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"26"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Copperplate_1024"
		{
			"1"
			{
				"name"		"Vamp_Small"
				"tall"		"18"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dominican_1024"
		{
			"1"
			{
				"name"		"Vamp_Plain"
				"tall"		"26"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"ParagraphText_1024"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"20"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Trebuchet_1024"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"24"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Tahoma_1024"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Base_1024"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"24"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Malk_1024"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Malkavian"
				"tall"		"24"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Dementation_1024"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Dementation"
				"tall"		"22"	// changed by wesp
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Dominate_1024"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Domination"
				"tall"		"27"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Persuasion_1024"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Persuasion"
				"tall"		"25"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Seduction_1024"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Seduction"
				"tall"		"33"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Intimidate_1024"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Intimidate"
				"tall"		"20"	//"23"// "15"
				// Changed to fix bug #6803: Intimidation font extends outside dialogue box
//				"name"		"Vamp_Dialog_Base"
//				"tall"		"24"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

			// Used for Ammo UI
		"BenguiatBig_1024"
		{
			"1"
			{
				"name"		"Vamp_Ammo"
				"tall"		"31" //"24"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"BenguiatSmall_1024"
		{
			"1"
			{
				"name"		"Vamp_Ammo"
				"tall"		"24" //"16"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"HudFont_1024"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"12"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"LCD_1024"
		{
			"1"
			{
				"name"		"Vamp_LCD"
				"tall"		"30"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Vamp_Handwriting1_1024"
		{
			"1"
			{
				"name"		"Vamp_Handwriting1"
				"tall"		"30"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Headline_1024"
		{
			"1"
			{
				"name"		"Times New Roman"
				"tall"		"55"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Newsprint_1024"
		{
			"1"
			{
				"name"		"Times New Roman"
				"tall"		"19"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}


		// [ 1280 ]
		"Default_1280"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"20"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultFixed_1280"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"20"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultUnderline_1280"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"20"
				"weight"	"500"
				"underline" "1"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultSmall_1280"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultVerySmall_1280"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"15"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"DefaultLarge_1280"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"22"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Marlett_1280"
		{
			"1"
			{
				"name"		"Marlett"
				"tall"		"17"
				"weight"	"0"
				"symbol"	"1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

//		"Troika_1280"
//		{
//			"1"
//			{
//				"name"		"TroikaGames"
//				"tall"		"137"
//				"weight"	"1000"
////				"range"		"0x0000 0x007F"	//	Basic Latin
//				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
//			}
//		}

		"MainMenu_1280"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"88"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorMedium_1280"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"43"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorSmall_1280"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"32"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Copperplate_1280"
		{
			"1"
			{
				"name"		"Vamp_Small"
				"tall"		"22"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Dominican_1280"
		{
			"1"
			{
				"name"		"Vamp_Plain"
				"tall"		"32"
///"tall"		"26"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"ParagraphText_1280"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"25"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Trebuchet_1280"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"30"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Tahoma_1280"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"20"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Base_1280"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"30"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Malk_1280"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Malkavian"
				"tall"		"30"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Dementation_1280"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Dementation"
				"tall"		"28"	// changed by wesp
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Dominate_1280"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Domination"
				"tall"		"33"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Persuasion_1280"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Persuasion"
				"tall"		"31"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Seduction_1280"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Seduction"
				"tall"		"41"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Intimidate_1280"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Intimidate"
				"tall"		"25"
				// Changed to fix bug #6803: Intimidation font extends outside dialogue box
//				"name"		"Vamp_Dialog_Base"
//				"tall"		"30"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

			// Used for Ammo UI
		"BenguiatBig_1280"
		{
			"1"
			{
				"name"		"Vamp_Ammo"
				"tall"		"38"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"BenguiatSmall_1280"
		{
			"1"
			{
				"name"		"Vamp_Ammo"
				"tall"		"30"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"HudFont_1280"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"15"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"LCD_1280"
		{
			"1"
			{
				"name"		"Vamp_LCD"
				"tall"		"37"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Vamp_Handwriting1_1280"
		{
			"1"
			{
				"name"		"Vamp_Handwriting1"
				"tall"		"37"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Headline_1280"
		{
			"1"
			{
				"name"		"Times New Roman"
				"tall"		"68"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Newsprint_1280"
		{
			"1"
			{
				"name"		"Times New Roman"
				"tall"		"23"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}


		// [ 1600 ]
		"Default_1600"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"25"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultFixed_1600"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"25"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultUnderline_1600"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"25"
				"weight"	"500"
				"underline" "1"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultSmall_1600"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"20"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultVerySmall_1600"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"18"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"DefaultLarge_1600"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"28"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Marlett_1600"
		{
			"1"
			{
				"name"		"Marlett"
				"tall"		"21"
				"weight"	"0"
				"symbol"	"1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

//		"Troika_1600"
//		{
//			"1"
//			{
//				"name"		"TroikaGames"
//				"tall"		"172"
//				"weight"	"1000"
////				"range"		"0x0000 0x007F"	//	Basic Latin
//				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
//			}
//		}

		"MainMenu_1600"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"111"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorMedium_1600"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"54"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorSmall_1600"
		{
			"1"
			{
				"name"		"Vamp_MainFont"
				"tall"		"40"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Copperplate_1600"
		{
			"1"
			{
				"name"		"Vamp_Small"
				"tall"		"28"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Dominican_1600"
		{
			"1"
			{
				"name"		"Vamp_Plain"
				"tall"		"40"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"ParagraphText_1600"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"31"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Trebuchet_1600"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"37"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Tahoma_1600"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"25"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Base_1600"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"37"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Malk_1600"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Malkavian"
				"tall"		"37"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Dementation_1600"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Dementation"
				"tall"		"28"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Dominate_1600"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Domination"
				"tall"		"42"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Persuasion_1600"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Persuasion"
				"tall"		"39"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Seduction_1600"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Seduction"
				"tall"		"51"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Dlg_Intimidate_1600"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Intimidate"
				"tall"		"31"
				// Changed to fix bug #6803: Intimidation font extends outside dialogue box
//				"name"		"Vamp_Dialog_Base"
//				"tall"		"37"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

			// Used for Ammo UI
		"BenguiatBig_1600"
		{
			"1"
			{
				"name"		"Vamp_Ammo"
				"tall"		"48"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"BenguiatSmall_1600"
		{
			"1"
			{
				"name"		"Vamp_Ammo"
				"tall"		"37"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"HudFont_1600"
		{
			"1"
			{
				"name"		"Vamp_Dialog_Base"
				"tall"		"18"
				"weight"	"900"
				"persistent" "1"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"LCD_1600"
		{
			"1"
			{
				"name"		"Vamp_LCD"
				"tall"		"46"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Vamp_Handwriting1_1600"
		{
			"1"
			{
				"name"		"Vamp_Handwriting1"
				"tall"		"46"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Headline_1600"
		{
			"1"
			{
				"name"		"Times New Roman"
				"tall"		"86"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}


		"Newsprint_1600"
		{
			"1"
			{
				"name"		"Times New Roman"
				"tall"		"29"
				"weight"	"900"
//				"range"		"0x0000 0x007F"
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
	}	







	//
	//////////////////// BORDERS //////////////////////////////
	//
	// describes all the border types
	Borders
	{
		BaseBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}
		}
		
		TitleButtonBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"4"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

		TitleButtonDisabledBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BgColor"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BgColor"
					"offset" "1 0"
				}
			}
			Top
			{
				"1"
				{
					"color" "BgColor"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BgColor"
					"offset" "0 0"
				}
			}
		}

		TitleButtonDepressedBorder
		{
			"inset" "1 1 1 1"
			Left
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}
		}

		ScrollBarButtonBorder
		{
			"inset" "2 2 0 0"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

//		ButtonBorder
		OldButtonBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

//		TabBorder
		OldTabBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}
		}

//		TabActiveBorder
		OldTabActiveBorder
		{
			"inset" "0 0 1 0"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "ControlBG"
					"offset" "6 2"
				}
			}
		}


		ToolTipBorder
		{
			"inset" "0 0 1 0"
			Left
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

		// this is the border used for default buttons (the button that gets pressed when you hit enter)
//		ButtonKeyFocusBorder
		OldButtonKeyFocusBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderSelection"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}
			Top
			{
				"1"
				{
					"color" "BorderSelection"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}
			Right
			{
				"1"
				{
					"color" "BorderSelection"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}
			Bottom
			{
				"1"
				{
					"color" "BorderSelection"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

//		ButtonDepressedBorder
		OldButtonDepressedBorder
		{
			"inset" "2 1 1 1"
			Left
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}
		}

		ComboBoxBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}
		}

		MenuBorder
		{
			"inset" "1 1 1 1"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

		CharEditBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BrownBorder"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BrownBorder"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BrownBorder"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BrownBorder"
					"offset" "0 0"
				}
			}
		}
	}
}