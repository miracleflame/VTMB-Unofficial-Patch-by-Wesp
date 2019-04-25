=begin
Valve SketchUp Source Tools Configuration
Copyright (C) 2008-2009 Valve Software Corporation

This file stores configuration data and preferences for Valve Source exporters,
such as vmf_export.rb and smd_export.rb. The settings stored here are re-loaded
every time a Valve plugin is run. This allows you to change how the plugins work
here without having to restart SketchUp.
=end



# ==========
# VMF Export
# ==========

$v_vmf_prompt_save_dialog = "always"
           # always  = (default) Always prompt user with a Save As dialog. Will pre-fill with skp filename or, if selected, prefixed component name
           #           1: If 1 component selected with prefix, i.e. 'VMF_overpass.skp', will use name overpass.vmf in prompt
           #           2: else, if filename is prefixed, i.e. 'MDL_floorlamp.skp', will use that in prompt
           #           3: else, just use the actual filename/component name in prompt
           # never   = Never prompt for filename. Will do as above, but will not prompt. (for advanced users.)
           # context = Will look for context:  If selected single object is prefix named
           #           or file is prefix named, will not prompt. Will prompt in all other cases


$v_vmf_export_boundingbox = false
           # Export 6 bounding box brushes around model. Default=false
           # Note: future versions may have three options instead of true/false:
           # 0 = never output.
           # 1 = always output
           # 2 = only output if no prefix named 'BND_xxx' brushes and/or layers are present


$v_vmf_consoleoutput = false
           #Output more detailed spew to the Ruby Console. Use only to debug, as this will
           #slow down the export due to console spamming on large files. Default=false


$v_vmf_debugoutput = false
           #Output debug information as comments to the output file. Default: false


$v_vmf_defaultmaterial = "dev/graygrid" #The default material.
$v_vmf_defaultmaterial_width= 128.0 #in units
$v_vmf_defaultmaterial_height= 128.0
$v_vmf_defaultmaterial_pixelwidth= 512 #in pixels
$v_vmf_defaultmaterial_pixelheight= 512


$v_vmf_uv_mapping = 2
           #Preferred mode for calculating UVW axis for each solid face. The exporter can
           #detect non-orthogonal mappings and switch between "safe" and "advanced" as
           #needed to prevent lighting errors in the game engine.

           # 0 = Ignore UV calc, skip output. The resulting vmf will load, but won't \
           #     compile. This is for advanced users who want to completely UV by themselves.

           # 1 = Fallback behaviour: Use face normal to create world space projection
           #     This is simple and fast, but the mapping doesn't doesn't look like the
           #     SU model. It's also the safest, as non-ortho projections or missing
           #     uv info will break the lighting pass.

           # 2 = Maintains xform, scale, and UV displacement. (Default)
           #     Slower, but corresponds better with SU model. Will detect cases of non-
           #     Othogonal UV axes that might cause the lighting pass to fail, and will
           #     use mode 1 for those brush surfaces.


$v_vmf_skew_tolerance = 0.01
           #The tolerance in angle degrees within which a skewed UV is allowed on solids.
           #Larger angles will cause the exporter to fall back to mode 0 UV algorithm. default=0.01

$v_vmf_erroralert = true
           #Output error information to a pesky alert dialog.
           #For conditions which will result in bad vmfs

$v_vmf_warnalert = true
           #Output warning information to a pesky alert dialog.
           #For conditions which will result in bad vmfs, but were recoverable

$v_vmf_defaultskyboxname= "urbannightstormhdr"
           #The default skybox texture.
           #$v_vmf_defaultskyboxname= "sky_day01_05"            #Portal, Half Life 2
           #$v_vmf_defaultskyboxname= "sky_tf2_04"              #Team Fortress 2 default
           #$v_vmf_defaultskyboxname= "urbannightstormhdr"      #Left 4 Dead
           # the materials/skybox folder of mosdt source games will have other options


# ==========
# SMD Export
# ==========

$v_smd_prompt_save_dialog = "always"
           #See above for description. Default = "always"

$v_smd_alert_on_auto_overwrite = true
           #alert if auto-named file will overwrite an existing file. This does
           # not apply to the save dialog.

$v_smd_local_space = false
           #Export in local space coordinates (only if a single, 'MDL_' prefix-named component is selected)

$v_smd_warning_tricount = 1000
           #Warn if triangle count exceeds this number. A negative number disables the warning.

$v_smd_up_axis = "z"
           #Preferred axis to use as 'up' direction. can be "z" or "y"

$v_smd_alert_on_success = true
           #inform succesful completion with an alert dialog

$v_smd_verbose_spew = false
           #Output detailed console info useful for debugging. Default = "false"

$v_smd_comment_header_to_file = false
           #add comments to the smd header. Default = "false"

$v_smd_comment_spew_to_file = false
           #add exporter console output to the smd header. Default = "false"

$v_smd_run_qc = false
           #run studiomdl on the associated .qc (if that .qc exists.) ( For advanced users, default = "false" )

$v_smd_default_material = "greygrid"
           #default material

$v_smd_default_material_width = 128.0
$v_smd_default_material_height = 128.0
           #size in inches

# =======
# Folders
# =======

# If you specify game engine paths here, the plugins can perform automated compiling of
# game assets. For more info visit: http://developer.valvesoftware.com/wiki/Game_Directory
# Note: Exporter plugins will not create these folders for you if they don't already exist.
# Note: If you use quoatation marks, the file path needs double slashes. If you use %q<>, you
#       Can copy and paste paths from explorer.


$v_basepath = %q<C:\Program Files\Valve\Steam\SteamApps\common\alien swarm infested>

           # BASE. The base engine folder is where the game executable is. This
           # executable is usually called hl2.exe or left4dead.exe.


$v_modname = "swarm"

           # GAME/MOD NAME. The name of the game or mod you are creating content
           # for. This typically corresponds to a folder name under your base engine folder.


$v_gamepath = $v_basepath + "\\" + $v_modname  #specifying the game dir relative to the base path above
#$v_gamepath = "c:\\Program Files\\Valve\\Steam\\SteamApps\\common\\left 4 dead\\left4dead\\" #specifying the game dir directly

           # GAME DIRECTORY: Each Source game or mod has a file called
           # 'gameinfo.txt' in this folder. This is the root folder for files used directly
           # by the game engine. These include compiled files, such as .mdl (model) and .bsp,
           # (game level) as well as uncompiled files such as .vmt (material) and .wav (sound).
           # By convention, the game directory is the base engine path+the game/mod name.
           # (i.e. "%q<c:\Program Files\Valve\Steam\SteamApps\common\left 4 dead\left4dead>")


$v_toolspath = $v_basepath+"\\bin"  #relative to base path
#$v_toolspath = %q<c:\Program Files\Valve\Steam\SteamApps\username\sourcesdk\bin\orangebox\bin> #Using OB tools

           # TOOLS: Location of sdk/authoring tool .exe files. i.e. studiomdl.exe, vtex.exe, vbsp.exe,
           # vrad.exe, and vvis.exe. These may be used by the plugins to automatically compile
           # .smd or .vmf files that you create.


$v_contentpath = %q<c:\Program Files\Valve\Steam\SteamApps\common\alien swarm infested\mycontent>

           # Content Folder. This is where original source files, those that are
           # to be compiled into game files, are kept. These include .vmf for game
           # levels, .smd for models, .tga for images, and .qc files that control
           # how a model is compiled.
           # (i.e. "c:\Program Files\Valve\Steam\SteamApps\common\left 4 dead\content")


$v_maps_src = $v_contentpath+"\\mapsrc"

            # Maps output folder. This is where automatically created .vmf files are saved.


$v_models_src = $v_contentpath+"\\modelsrc"

            # Models output folder.


$v_models_compiler = "studiomdl.exe"
$v_models_compiler_options = "-game \""+$v_gamepath+"\" -nop4"


# end of config file
