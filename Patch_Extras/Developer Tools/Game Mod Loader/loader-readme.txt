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
