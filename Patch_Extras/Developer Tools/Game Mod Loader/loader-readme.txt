---------------
GAME MOD LOADER
---------------
Author: Behar
Support: Psycho-A

Main features:
--------------
1. Native widescreen support for all monitor resolutions with 
   correct aspect ratio and fov.
2. All former dll-related fixes from Wesp's Unofficial Patches 
   (more than 2GB RAM fix, lights fix, view histories & weapon 
   stats fixes, etc.) are included. No need for patched dlls!
3. Source-like mods system (an untouched "vampire" directory 
   with the original game, and separate directories for each 
   mod), that gets rid off the need to have multiple copies of
   Bloodlines installed to play different mods or patches.
4. Support of VPK file system for mods with separate folders
   (VPK Creator from Bloodlines SDK needed to build VPK files).
5. Game console enabled by default (no "-console" needed).
6. Compatible with all existing game and patch versions.

Installation:
-------------
Extract content into the Bloodlines game root directory (where 
vampire.exe is) replacing any existing files. Loader is ready!
[already installed into UP and Collector's Edition game bundle]

Usage with mods:
----------------
1. Rename the mod's "vampire" directory to moddir (can be any 
   desired name but must not contain spaces!).
2. Place this renamed mod dir into the game root directory.
3. Run mod with "vampire.exe -game moddir" (without quotes) 
   as a command-line parameter of game's shortcut or batch 
   file (or launch options in Steam).

For mod makers:
---------------
You may distribute the loader assets directly with your mod, 
so this will allow users to install it on any game version.

The loader returns Python's "sys.moddir" variable as the name 
of the mod's main directory, so if your mod uses "fileutil.py" 
functionality, you need to edit your mod's fileutil.py by 
pasting these strings after "import nt" (first line):

#####################
#  Add Mods support #
#####################

import sys
try: sys.moddir
except AttributeError:
	 sys.moddir = "vampire"
from sys import moddir

Next search all Python scripts (fileutil.py, vamputil.py, etc.) 
for access to "vampire" folder and replace ("vampire/...") with
(moddir + "/...") or (fileutil.moddir + "/..."), depending on 
the script and import type.


--------------------------
linux-loader.sh [mod_name]
--------------------------
Script for running Bloodlines in a Wine / Linux environment.

Place this script into the directory where Vampire.exe resides 
or one of its subdirectories. It needs to be executable and the
prefixes are essential, so don't remove them if you modify it. 
To use it, you can either:

- Click it in the file explorer. This requires the GUI builder 
  Zenity installed.

- From the command line: Open a console and execute the script. 
  Zenity is not required or used.

If there are mods installed, it will show the mods and allow 
the user to select one; if not it will run the original game. 
You can also use a mod name as a command-line argument to 
directly start with this mod.

Created by SCO; changed to work from subdirectories by Wrzlprmft
(readme improved by Wesp5 and Wrzlprmft)


This script from Uradamus runs Bloodlines directly from Steam:
--------------------------------------------------------------
#!/bin/bash

# Change this to match your own prefix.
PREFIX="$HOME/wine"

# This assumes you installed Steam in its default location.
cd "$PREFIX/drive_c/Program Files/Steam"

export WINEARCH=win32
export WINEPREFIX="$PREFIX"

wine Steam.exe -no-dwrite

willbane wrote that adding resolution helps with the main menu:
---------------------------------------------------------------
wine vampire.exe -full -width 1920 -height 1080 -game "$opt" &
