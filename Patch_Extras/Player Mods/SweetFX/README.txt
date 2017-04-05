                    ____      ____  _               _
                   |  _ \ ___/ ___|| |__   __ _  __| | ___
                   | |_) / _ \___ \| '_ \ / _` |/ _` |/ _ \
                   |  _ '  __/___) | | | | (_| | (_| |  __/
                   |_| \_\___|____/|_| |_|\__,_|\__,_|\___|
                                  by Crosire


                      .-.                   .  .---..   .
                     (   )                 _|_ |     \ /
                      `-..  .    ._.-.  .-. |  |---   /
                     (   )\  \  / (.-' (.-' |  |     / \
                      `-'  `' `'   `--' `--'`-''    '   '
                                 by CeeJay.dk


==============================================================================
       Please take the time to read this whole readme ... Thank you! =)
==============================================================================

Contents:
---------

1. About
2. Requirements
3. Installation
   3.1 Setup Tool
   3.2 Manually
4. Additional Credits

==============================================================================

About:
------

ReShade  is an  advanced post-processing injector.  It features  its very  own
effect  language, based  on  HLSL, which  not  only  makes  API  and  platform
independent  shaders  possible, but  also introduces  a wide  range  of useful
features designed especially for post-processing effect development.
In contrast  to all the existing injectors ReShade was written to be completly
generic:  it itself does not come with  any effects, it's a toolset for shader
developers to realize  their very own  imagination. Define  and use  your  own
textures right in the shader code, request custom timers etc., retrieve access
to every  game's color  and depthbuffer (which  ReShade is  able to  genericly
identify and hook across  games without any extra configuration), no matter if
it renders with Direct3D8 (which is wrapped to Direct3D9 to allow using higher
shadermodels), Direct3D9, Direct3D10, Direct3D11 or OpenGL (and in  both 32bit
and 64bit). A highly advanced dynamic hooking system is reponsible for keeping
track of the APIs. And  because ReShade as mentioned comes with its own shader
transpiler, shaders written once work in all five.

==============================================================================

Requirements:
-------------

ReShade requires a computer with Windows Vista or higher.
If you want to use it with OpenGL games, your video card needs to have support
for at least OpenGL 4.3.
It is recommended to update your graphics card drivers to latest version.

The only software requirement is the DirectX end-user runtime from June 2010:
- https://www.microsoft.com/download/details.aspx?id=8109


Installation:
-------------

Setup Tool:
~~~~~~~~~~~

Run the provided "ReShade Setup" tool,  press "Select Game" and browse to your
targeted game's  executable file. The setup then tries to detect which API the
game  uses for rendering and uses that knowledge to  continue the installation
progress.  If  auto-detection  failed, choose  the correct  API from  the list
yourself.  Setup  then  copies and  renames  ReShade  +  SweetFX to  the  game
directory and finally  provides you  with the  option  to start the game right
away. That's it!

Next time your  run the game, you should  see the ReShade  greeting popping up
and a SweetFX welcome message displayed in your game.

If that is not the case, try to do a manual installation.
Note  that  the setup tool is  just  provided for  convenience  and in no way
required to get ReShade fully working. A manual installation will do the same
good.

Manually:
~~~~~~~~~

Figure  out  if  the  game  executable  is  32bit or  64bit  and  copy  either
ReShade32.dll or ReShade64.dll into the parent directory of that executable:

Figure out which  API the game uses for rendering, or any of the following DLL
names the game loads and rename the DLL you just copied to that:
- Direct3D8 => d3d8.dll
- Direct3D9[Ex] => d3d9.dll
- Direct3D10+ => dxgi.dll
- OpenGL => opengl32.dll (for 64bit too)

Done!

If it still does not work, make sure the DLL is loaded at all (a log file with
the DLL name is created). Repeat the  process with another name from the list.
Sometimes the  game loads its DLLs from a different  directory (a "bin" folder
for instance), so try to install ReShade to that one instead.

In case you experience  crashes on startup, make sure no third-party overlays,
game  boosters, screen  recording, screen  streaming or  similar  software  is
running.

If that all fails, please report  back with a detailed description of what you
tried so far.

==============================================================================

Additional Credits:
-------------------

Special thanks to Christian Jensen (CeeJay.dk).
He  was  a   very  great  help  in every  possible  way, did  a lot of testing
(especially  regarding the shading language)  and is always  a nice person  to
talk to.

Thank you to all the closed beta testers as well. You were awesome, notably:
- CeeJay.dk
- Marty McFly
- Matsilagi
- Martigen
- K-putt

Libraries used:
- Frexx CPP by Daniel Stenberg (https://github.com/bagder/fcpp)
- GL3W by Slavomir Kaslev (https://github.com/skaslev/gl3w)
- MinHook by Tsuda Kageyu (https://github.com/RaMMicHaeL/minhook)
- NanoVG by Mikko Mononen (https://github.com/crosire/nanovg)
- STB by Sean Barrett (https://github.com/nothings/stb)

==============================================================================