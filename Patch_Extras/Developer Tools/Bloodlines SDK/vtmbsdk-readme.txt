--------------------
Bloodlines SDK v1.66+
--------------------

This is an unofficial software developer's kit (SDK) for Vampire - The Masquerade: 
Bloodlines, the greatest game of all time developed by Troika Games in 2004. 
Unfortunately, the company quickly went bust, and the official toolkits haven't been released, 
thus leaving modmakers with nothing. As recently some tech-info of the game became available, 
a team of enthusiasts decided to revive the modmakers movement by developing this devkit.

--------------------

Installation:

1) The "SDKBinaries", "SDKContent" dirs and "Bloodlines SDK.exe" file desireable 
should be placed inside the directory where the main "Vampire.exe" file is.
Since version 0.9 you may place SDK assets into the any location on your disk.
If you run the SDK for the first time, it will be configured automatically. 
2) After this, you can choose game directory and unpack your game's content 
(to be visible in the SDK tools), this procedure is automatic too. 
3) Now the SDK is ready. Just run "Bloodlines SDK.exe" to start your works.

> If you have problems with game configuration and editor display settings, 
run the "Reset SDK Configuration" procedure from the main menu.
> You also may override the standard game subdirectory path (for mods, for example):
use "Change Path to Project Dir" option from the SDK main menu.

--------------------

At this moment the project is not fully completed, but already 
it can be used to do the following (with some limitations): 

* Create, edit and compile original or your own maps.
* Create, view and compile game models (animations are still not supported).
* Decompile game maps and models for editing.
* View, manage, extract and create game archives (.vpk files).
* View and convert game textures between tth/ttz, vtf, tga and other formats.
* Create and edit game dialogues, subtitles and lip-sync data (.lip files).
* Partially create or edit cinematics and gesture scripts (.vcd files).
* Manage entity data in existing BSP files (paste, delete and change properties).
* Create your own Source/HL2-like mods with separate folders and unique content.
* Validate and clean misc game resources.

--------------------

This SDK includes various third-party tools, in particular:

* Source SDK GUI (developed by Valve, customized by Psycho-A)
* PackFile Explorer v3.9 (developed by Dave Gaunt)
* MDL 2 SMD Beta (developed by Daedalus, http://forum.bloodlinesresurgence.com)
* BSPSource v1.2.1 (VMEx modification, developed by Barracuda, http://ata4.info/bspsrc/about.html)
* VPKTool v3.9a (Quick and dirty Bloodlines Tools, developed by Turvy)
* VTMBedit Tool (developed by David Arneson [xatmos])
* Bloodlines Dialogue Editor (developed by Raptor for Paradise#77, http://go.to/paradise77)
* EntSpy v0.8 (developed by Rof, http://bagthorpe.org/bob/cofrdrbob/entspy.html)
* BSPEdit v1.09 (developed by Robert Morley, http://www.rob.patcroteau.com)
* BSPDetail v1.00 (developed by DDLullu, http://forums.planetvampire.com/index.php?action=profile;u=3672)
* kHED v1.1.5, low-poly model editor (developed by JDPhU, http://khed.glsl.ru)
* VExtract (developed by Daedalus for Bloodlines Revival project, http://bloodlinesresurgence.com)
* VPK Creator (developed by Psycho-A)
* Texture Converter and its Windows shell extenstions (developed by Psycho-A)
* TTZ Viewer (developed by Psycho-A & Fire64)
* Mods' Dupe Finder (custom script, written by Psycho-A)
* Hammer Run Map Launcher (custom compile dialog, written by Psycho-A)
* StudioMDL Compiler GUI (developed by InterWave Studios)
* Photoshop and Paint.NET texture plugins (the crew of authors)
* LipSync/VCD Editor (Valve's FacePoser modification, extended by Psycho-A)
* Create a New Mod Wizard (custom script, written by Psycho-A)

--------------------

Additional tools (for advanced users):

* vview.exe - map viewer (opengl)
* glview.exe - map visleafs viewer (opengl)
* bspzip.exe - program for un/packing files inside the map

--------------------

The following tools required Java Runtime Environment (http://java.com/download) 
to be installed on your system:

* Model Decompiler
* BSPSource Decompiler
* BSPInfo Tool [disabled for now]
* EntSpy BSP Tool
* PakRat Tool [disabled for now]

--------------------

Usage notes:

[Generic]
* Don't forget to read the last ChangeLogs and check SDK's home page for updates in order
  to keep abreast of the latest changes and new features! Updates may be frequent :).
* Extracted game content (from .vpk) goes to "SdkContent\VpkContent" sub-directory.
  To edit some asset from here (material, model, etc), you need to copy it to your project's 
  folder first with saving original folder structure. Next, make your editions at this place,
  otherwise, your changes won't be applied for other people who'll get your work.
* If the map crashes on/after loading in Hammer, then on launching editor wait until appearing
  the "Messages" window with showing the project paths! This means editor assers loaded fully.
* To create new mod 'from scratch', use "Create a New Mod" option in the Main menu. This will
  create appropriate launcher and mod folder with basic subdirs inside that have descriptions.
* The Administrator rights may be required for installing texture plugins or work some tools.

[Lighting]
* Since version 1.2 we may compile orignal Troika's lighting with hard falloffs after defined
  maximum distances. Using new "Cut-Off Distance" and "Cut-Off Smoothing Factor" params in
  entities, you may achieve interesting results, but besides it may result hard unrealistic 
  lighting. Use these parameters with care! If you don't know how to use them correctly - 
  better leave them with their default settings that suggest Editor on new entity creation.
  Moreover, careless using cut-off distances may lead sharp dropping lights on PCs and NPCs!
* If the model looks too dark at the light area, make it prop_static, create "info_lighting" 
  entity with some name at the point where the ambient lighting is best, and refer to it in
  the model's "Lighting Origin" parameter. This will override mdl's troubled lighting coords.

[Texturing]
* No more need VPKTool and creating DDS for getting game's tth/ttz's since the advanced tool,
  "Texture Converter", included to the SDK. It supports tth,ttz,vtf,tga,dds,bmp,jpg or gifs
  conversion in both directions (convert/de-convert) in single or batch mode as well.
* Since version 1.4 you able to convert game's texture formats into vtf or tga directly from
  Windows Explorer context menu. Also, you may create tth and ttz using the same options for
  all popular image formats (see above). Just follow "Convert to ..." right-click options.
* If your source image files are at one of "materials/" or "materialsrc/" subfolders, then
  required .vmt file will be auto-generated after converting together with tth and ttz files.
  Note if the texture is mask (has postfixes like _normal, _ref..), .vmt won't be generated.
* Since version 1.51, if source image put into one of "materials/" or "materialsrc/" subdirs
  and if you use "Texture Converter" or it's context menu items, the best compression format
  for VTF and TTZ will be adjusted depending on various content type subfolders (for example,
  DXT compression for world's generic textures and no compression for HUD or Skyboxes). Also,
  depending on content, the optimal default parameters will be written into generated .vmts.
* Since version 1.4 the SDK has Paint.NET and Adobe Photoshop integration plugins for VTF
  textures (Valve Texture Format, the decompiled version of game's TTH/TTZs). Also these 
  plugins allow you to create Normal maps, work with alpha-masks and tiling texture images.

[Mapping/Compiling]
* If you need to change the process priority for map compilers, walk inside SDKBinaries/ dir
  and search "hammer.runmap.bat" file. Edit it with Notepad changing "set Priority=" string.
  The priority values are: /low, /belownormal, /normal, /abovenormal, /high, /realtime.
* Since version 1.15 you may able to set various map compiling settings for each individually.
  We used "worldspawn" entity class to write certain params which're readable by compilers.
  For managing them, goto "Map -> Map Properties" in the Hammer menu and look bottom several 
  strings. Now there are four parameters presented which allow you to tweak map lighting or
  overall compiling time (each parameter have descriptions so no reason to describe it here).
* Tool texture "toolsinvisible" slows VVIS full compiling, use "toolsclip" when possible.
* Tool texture "noviz" isn't supported by the SDK, create func_details in its volume instead.
* Func_detail entities may add junk planes, in that case turn them back to world.
* Func_details do not seal the world, use normal brushes to do that (including skyboxes).
* Always turn all detail brush objects which aren't the main world geometry to func_details.
* Always use "nodraw" tool textures for surfaces that the player can't see (optimization).
* Always check for entities outside the world, because they will cause leaks on compiling.
* For a valid map transition, landmark names on both maps must be the same.
* For a valid map transition, landmark angles only matter if flag 1 is set.

[Scoring/Authoring]
* Since version 1.6 you can edit or create the closecaption and lip-syncing files (.lip) and
  choreographic NPC gestures needed for dialogs and cinematic scenes (.vcd files). The direct
  loading models and animations isn't supported yet, but you have full access to edit their
  parameters. Use "Lip/VCD Editor" utility for this, and follow instructions in its messages.
  The rules are almost the same as for the original HL2's FacePoser (excluding details), so 
  the tutorials and infos on Valve's "Developer Wiki" will be useful for learning as well.
* Since version 1.62 you can quickly edit or localize subtitles (captions) inside .lip files 
  directly through the new Windows context menu item or File Open dialog in the SDK menu.


--------------------

Usage limitations:

* The SDK requires unpacking for the game content for now
  (maybe support for VPKs will be added later...)

<Advanced info>
* No correct animation support in multi-bone models - it means that we can't handle the 
  animations in the Editor when creating maps.
* No full-featured model compiler and decompiler - only Type 0 models with no animations 
  can be compiled (basic prop models).
* Not finalized FGD file (Hammer entity data) - there are still a lot of imprecisions and 
  lack of info on some entity parameters.

--------------------

Project Developers:

* Psycho-A (Programming and all subsequent works).
* Behar (Rare, but very useful help).
* Fire64 (Programming, project CEO) [no support anymore].

--------------------

Official project pages:

* Planet-Vampire Community: 
  https://planetvampire.com/modules/files/index.php?id=31
  https://forums.planetvampire.com/index.php?topic=5797.0
* V-Bloodlines/CS-Mapping/VK (Russian Communities):
  http://forum.v-bloodlines.info/topic8100.html [x]
  http://cs-mapping.com.ua/forum/showthread.php?t=37053
  http://vk.com/vtm_bloodlines [game public]

--------------------

For Programmers:

Help Wanted!!!
If you are interested in further project developing and ready
to do something youeself, please, read notes below.

= Bloodlines SDK 1.x =
= Programmer's notes =


[Preparation]

To make able to manage SDK applications, please download the latest version of source code.
This can be found here: http://yadi.sk/d/vs3nqIRxEHd8N After, unpack it inside SDK root directory.

Next, to compile something, you need to install (in specified order):

a) Visual C++ 6.0 Professional
b) VC++ 6.0 Service Pack 5 
c) VC++ 6.0 Processor Pack 5

You can find it here: http://yadi.sk/d/PvzgpPAhEHbvp
If you confused with software incompatiblity warnings on Windows 7 or later OS - just ignore them.

There are ready Batch files presented to quickly build certain applications/commons set.

Note: Since SDK version 1.52, the "portable" version of Visual Studio (with SP5+PP5) is available.
That means you don't need legacy installing as said before - instead you just unpack "vc_studio" folder
near the code's "src_main" folder, so the compiling with batch scripts will be workable immediately.
You can download it together with Code at the same link (legacy VS installers are no longer required).


[Open Issues and Goals]

There are some issues in the project, which we're still not able to solve fully, and there are many unrealized goals.

01) Model animations and almost all NPC models are very buggy since no accurate decoding algorythm was written.
    Solution [Temp]: Disabled for Hammer for using initial poses, partially works in Model Viewer. Reversing needed.

02) No an adequate StudioModel compiler, moreover, the source code to the existing one was missing (just default Valve's left).
    Solution [Temp]: Not found, code/format reversing needed. For now, only single-boned models supported (props).

03) No VPK archives support for filesystem_stdio-related apps (Hammer, HLMV, all map compilers), so we are forced to extract game resources manually. The format structure description (for those who may interest this) can be found in "vpk_notes.txt" file of source code assets.
    Solution [Temp]: All content unpacks into SdkContent\Vampire\ dir via external batch tool.

04) BSP compilers can't compile the water brushes (water is not drawing in game).
    Solution [Temp]: Not found for now, possibly shader-level problem. Use placeholder textures...

05) Something in BSP structures interrupts to use precipitation particles (like rain) - they just stucks like on collisions.
    Solution [Temp]: Scale env_particle density to >10 or use func_particle volumes, but it's more resource-cost.

06) VRAD compiler have serious drawback - we can't get adequate shadows from prop_static complex non-convex models, because convex hull or collision mesh uses for projecting lightmaps.
    Solution [Temp]: Disable shadow casting for model and make separated func_detail shadow brush construction inside the model using tools/tools_shadow material.

07) Sometimes the random Hammer crashes occurs on loading or navigating Troika's maps. This may be related to not completely reversed MDL format or editor unstablity.
    Solution [Temp]: Waiting for loading all assets to editor (appearing "Messages" window) and loading map only after, may reduce the chance of such crashes for now.

08) Other of that I could not remember currently...


[Specific]

These files in original build should NOT be rebuilt since have NEWER versions than presented in code:
- studiomdl.exe  -- vtmb model compiler, the code was missing!

Be careful! ...or just try to restore the missing features :)


[Managing the Code]

I don't use GitHub or SVN for some understandable reasons, so, consider that I'm also working on 
code and sometimes update it (web-link is permanent). So, If you make some changes, PLEASE, mark 
them in existing changelog and //comment inside working files with specifying your name or nickname. 
For the feedback, backup your code using "backup.bat" script and send me via PM on the sites I 
specified in the SDK readme file. You may also email me: psycho-a@rambler.ru, psycho-a@yandex.com.


-- Psycho-A



--------------------
Version History:
--------------------

Global changes for the last year:

* SDK have been unbinded from main Vampire game directory and now supports custom mods and may be placed to any disc location.
* Added new "Texture Converter" utility with shell extensions for quickly batch converting between tth/ttz/vtf and other image formats.
* Added new "Create a New Mod" function into the main menu to be able to create new mods from scratch and connect them to SDK.
* Added tool (based on HL2 FacePoser + wrapper) to create and edit LipSync data, Captions and VCDs for voiceovers and gestures.
* Solved models displaying issues in Hammer and Model Viewer, decoded troubled formats and got rid of model decompression procedure.
* Restored ablility to build normal cubemaps after map compiling. This procedure is automatic.
* Increased BSP map format limits to be able to build large areas with dense entity and texture data.
* Improved Hammer interface elements and compiling dialogs, added new features, fixed crashings, paths limitation and other bugs.
* Mostly rewritten map compilers source code that fixed old bugs, improved lighting and added most of features from later Source Engines.
* Restored original Troika's lighting algorythms, now all recompiled game maps will look as they originally were.
* Fixed computing average lighting by VRad compiler in world's dark and unlit areas (fixes models blacking or whitening).
* Restored detail prop structure, now we may compile detailized surfaces (trash or grass on the ground, etc) normally.
* Improved entity control and descriptions for Editor, added per-one-map compiling settings and advanced controls for lights.
* Simplified and improved Content Preparation Wizard and VPK Creator (tool for building own VPK archives for mods).
* Solved Hammer's problem not-staring compiling after choosing any model or sound in entity's settings.
* Made env_cubemap reflections displayed on brush surfaces, and bumpmaps not overbright textures in 3D-view more.
* Improved Model Viewer rendering settings and default view.
* Improved and updated SDK interface, instructions, file system, some tools and other aspects.

--------------------

1.66 (25.03.2017):
- Generic: Fixed working some tools and scripts on Windows 10 and non-admin user accounts.
- Hammer/Shell: Fixed miss of current project/game configuraion in some cases.
- Hammer/FGD: Fixed description for NPCs "Allow_Alert_Lookaround" parameter.
- Hammer/FGD: Fixed description and data type for "TakeDamage" output command.
- Captions Editor: Added ability to fully disable subtitles and speaker inside .lip files.
- Captions Editor: Fixed appending new captions and speaker-name if source data is empty.
- A few other various minor fixes.

1.65 (21.02.2017):
- LipSync Editor: Fixed working on some machines and added console window with process log.
- LipSync Editor: Fixed Editor window not-showing and improved "Enter Speaker name" dialog.
- LipSync Editor: Fixed opening .lip files if they're not inside of sound/ folder.
- LipSync Editor: Prevented opening Phoneme Editor if none of .lip/.wav pair imported.
- LipSync Editor: Fixed detecting phrase's end-time in case of buggy word's phonemes.
- Hammer/FGD: Fixed description and default value on "Floats Frequency" of NPC entities.
- A few other various minor fixes.

1.64 (01.02.2017):
- Map Compilers [cr]: Increased MAX_MAP_BRUSHES to 32768 to be able to compile huge maps.
- Map Compilers [cr]: Increased MAX_MAP_BRUSHSIDES to 256000 to be able to compile huge maps.
- Map Compilers [cr]: Increased MAX_MAP_TEXINFO to 32768 to be able to compile huge maps.
- LipSync Editor: Fixed crashing file parser during saving .lip files with long phoneme data.
- Updated source code repository.

1.63 (30.01.2017):
- LipSync Editor: Fixed saving .lip files with more than 200 chars subtitles.
- Captions Editor: Fixed and improved text reading algorythms and speed-up overall work.
- Captions Editor: Fixed interface, aligning height of text box and file saving issues.
- "Edit Subtitles" is now default double-click action for .lip files (opens Captions Editor).
- Fixed first seconds flickering the SDK menu window on some systems.

1.62 (25.01.2017):
- LipSync Editor: Shortened file importing time by making script optimizations.
- LipSync Editor: Fixed issues on importing .wav and .mp3 files from VCD links.
- LipSync Editor: Added support for opening .lip and .vcd files from Windows context menu.
- Added simple tool "Captions Editor" to quick edit or localize subtitles inside .lip files.
  -- Tool works from the SDK menu (File Open dialog) and Windows context menu item.

1.61 (20.01.2017):
- LipSync Editor: Shortened program closing time by making some script optimizations.
- LipSync Editor: Importing VCDs now imports all sound files that referred inside of them.
- LipSync Editor: Fixed force changing LIP files not being edited in Phoneme Editor.
- Hammer/FGD: Added a full list of NPC soundgroups to all NPC entities for easy choosing.
- New GUI interface for "Create a New Mod" wizard; also added description for mod's main folder.
- Fixed minimizing and backgrounding the SDK main menu window in some cases.
- Corrected SDK messages when selecting mods with- and without .vpk archives inside.
- Some minor interface/shell fixes, also little improved usage notes in SDK readme.

1.6+ (18.01.2017):
- Added tool to edit LipSync data and Captions for voice files (based on HL2 FacePoser + wrapper), features:
  -- Create new .lip files for existing .wav or .mp3 file with voice.
  -- Automatically generate phonemes and subtitles depending on phrase text;
  -- Edit words, phonemes and subtitiles for already existing .lip files.
- LipSync Editor (see above) renamed to "Lip/VCD Editor" and extended to create and edit VCD files as well.
  -- Now users can edit existing or create new .vcd files to manage NPC gestures and dialog lines.
  -- Fixed some bugs found by users in the tool work and reorganized importing editing files.
- Made normal naming to clan-specific replies in "Dialogue Editor" being "Unknown" before.
- Small SDK file system reorgranization (do not install over older versions!).
- Improved SDK readme and added usage details for new tools.
- Info: This version will be included into Wesp's Unofficial Patch v9.7 final.

1.53 (10.01.2017):
- Hammer/Compiling: Added auto-closing old compile process windows on starting new compiling.
- Hammer/Compiling: Added ability to set custom priority for compilers (set Priority= command inside "SDKBinaries/hammer.runmap.bat").
- Added new "Create a New Mod" function into the main menu to be able to create new mods from scratch and connect them to SDK.
- Added new usage instructions into the SDK readme file.
- Source code: Added "portable" Visual Studio 6 to ease code compiling and strip legacy installation and configuring.
- Source code: Added in-place support for portable VS6 and updated code repository.

1.52 (30.12.2016):
- VRad compiler [cr]: Finally corrected computing average light for dark areas and removed -avglight crutch.
- Hammer/Compiling: Added auto-minimizing editor window on begin compiling (lower CPU usage, faster compiling).
- Source code: Reorganized some files and updated code repository.
- Corrected SDK usage notes in the readme file.

1.51 (14.12.2016):
- Texture Converter: Added ability to change output .vtf format (use TexConvert.bat's 'OutputFormat' param).
- Texture Converter: Added auto-detecting output .vtf/.ttz format and .vmt params by input file's subfolders.
- Texture Converter: Added Template manifests for world, cables, decals, effects, interface, models and skyboxes.
- Added new info on Texturing (see above) and some more usage notes from UP's readme to wider users' knowledges.
- Source code: Made little reorganization of sourcecode file system.
- Info: This version will be included into Wesp's Unofficial Patch v9.7.

1.5 (05-08.2016):
- Model Viewer [cr]: Fixed crashings on launching under Windows XP and Windows 8/10 machines.
- VRad compiler [cr]: Changed computing minumum light for models, now models less stands out from world.
- VRad compiler [cr]: Param "-avglight" now uses 1..255 values where 1 is darkest level, 255 is lightest.
- Hammer/FGD: Added info about needing set "Origin" to "0 0 0" in func_brush'es in pair with func_areportalwindow.
- Corrected Hammer's splash-screen logo and fixed some typos in SDK interface and messages.
- Added some generic usage notes from Unofficial Patch's readme to wider some users knowledges.
- Source code: Updated code repository.

1.45+ (21-26.04.2016):
- Hammer/FGD: Fixed "Moving direction" and "Parent entity" params not-working for trigger_hurt/_push.
- Hammer/FGD: Added full templates list to "NPC Stat Template" to quickly find required one.
- Hammer/FGD: Added "Origin" property to parentable brush entities (like triggers) to determine parenting point.
- Hammer/Compilers: Added "Final" and "Ultra-Fast" compiling modes to Run Map wizard, and renamed others.
- Hammer/Compilers: Added displaying initial time of compiling job into console progress window.
- Compilers/Assets: Fixed some tool textures (tools/rain etc.) to be transparent and shorten compiling/BSP size.
- Texture Converter: Added auto-generating .vmt files for tth's if they are in materials/ or materialsrc/ dirs.
- Texture Converter: Added info about usage and Windows shell extensions to SDK readme's notes.
- A couple other minor fixes; this version also included into the Unofficial Patch by Wesp5.

1.44 (3-5.04.2016):
- Hammer [cr]: Corrected entity picker button position in Outputs section.
- Hammer/FGD: Removed some bad entities that broken or disabled in the game engine.
- Hammer/FGD: Fixed swap errors in parameters layout for npc_maker_* entities.
- Hammer/Compilers [cr]: Added "Collision Shadows" option to map's properties to be able to override shadow models for prop_statics.
- Model Viewer [cr]: Another improvement for default view position of models.
- Source code: Updated code repository.

1.43 (15.03.2016):
- Model Viewer [cr]: Fixed centering and scaling default view for models.
- Hammer/FGD: Added render fields for prop_doorknob entity to control model color.
- Added new materials to lights.rad to self-illumintate on compiling.
- Added info about how to prevent crashing loading maps in Hammer to SDK readme.
- Source code: Updated code repository.

1.42 (17.02.2016):
- Hammer,HLMV [cr]: Fixed random crashes when loading maps or models.
- Hammer/FGD: Better skin selection dialog.
- Source code: Updated code repository.

1.4 (16-30.01.2016):
- Hammer [cr]: Made env_cubemap reflections displayed on brush surfaces in 3D-view.
- Hammer [cr]: Re-fixed overbrighting of bump-mapped materials in 3D-view (it's native mode now).
- Hammer/Assets: Fixed broken default cubemap texture and changed to better reflective one.
- Texture Converter: Added "Convert to TGA" item in Windows context menu for TTh/TTz and VTF files.
- Texture Converter: Added "Convert to TTz/Vtf" Windows context menu items for popular image formats.
- Added VTF texture format, Height-to-Normal and Aplha-mask plugins for Paint.NET image editor.
- Added VTF & DDS format, Tiler tool, NVidia's Normal-Map-filter & scripts for Adobe Photoshop.
- Added auto-installing the above plugins on first SDK launch or reset, when appropriate apps found.
- Note: some system configurations will require administrator rights for success plugins installation!
- Plugins installers separated from general SDK install script to avoid crashes and speedup configure.
- Some file system reorganizations - please, make a full SDK reset after installing new version!
- Other minor changes and also readme file actualization.
- Source code: Updated code repository.

1.33 (18.11.2015):
- Hammer/Shaders: Fixed overbrighting of bump-mapped materials in 3D-view.
- Hammer/FGD: Turned "Cut-off Smoothing factor" to null value to prevent lighting changes on originally decompiled maps.
- Corrected message about needing re-extracting VPKs after changing SDK project folder.
- Other small fixes.

1.32 (18.09.2015):
- Hammer/FGD: Fixed bug that put "../E.mdl" into the 'Dialog File' of "npc_VVampire" NPC class.
- Hammer/FGD: Removed force assigning "Young_Thug" soundgroup for "npc_VHumanCombatant" NPC class.
- VPK Extractor: Fixed VExtract crashings when we're using custom VPKs or missing some standard ones.
- Texture Converter: Fixed critical issue that dissallowed to use TTZ converter an any cases.
- Texture Converter: VTF version now automatically sets to the game's default when converting to TTZ.
- Model Viewer: Fixed Windows 10 OS compatiblity issue.

1.31-beta (10.07.2015):
- Hammer/FGD: Fixed default state (color cubes) rendering for some prop_* models that had 'parent' entity specified.
- VPK Creator: Added ability to make merged VPK with all specified folders.
- VPK Creator: Improved texts and made more clear readme file about main aspects of usage and vpk features.
- Texture Converter: Source VTF files now auto-deleted when converted to TTZ since they no longer needed (you may always convert them back).

1.3 (21.06.2015):
- Hammer [cr]: Fixed most of sprite using/rendering issues:
  -- Fixed translucency through surfaces when 'Glow' render mode was selected;
  -- Fixed not appending ".vmt" extension needed for correct parsing by engine;
  -- Fixed texture browsing dialog: now it goes to "sprites/" by default.
- Hammer [cr]: Fixed issue not-starting compiling if we select any model/sound from entity setting before.
- Hammer [cr]: Increased accuracy for scaling surface textures using Face Edit Sheet, from 2 decimals to 3.
- Hammer [cr]: Added VtMB-specific content types (dlg,particles,signs, etc) into search paths on entity editing for easier access.
- Hammer [cr]: Made combined field types in entity editing dialog: now we may browse files and also choose default suggestions.
- Hammer/FGD: Fixed issue incorrect in-game rendering of func_areaportalwindow/func_brush pair after compiling.
- Hammer/FGD: Completely rewritten all entity classes and made a lot of optimizations and improvemens to simplify works:
  -- Removed bunches of unused and hindering parameters;
  -- Made intelligent sorting all properties by categories;
  -- Filled many 'untested' and 'unknown' parameters with their actual meanings;
  -- Optimized content choosing: now you may use default suggestions (mostly used in game) and also browse files for All VtMB-specific content types;
  -- Added lines between each Parent and Target entities for quick visual finding their connections.
- Updated Source Code repository.

1.15-1.2+ (09.06.2015):
- Map Compilers [cr]: Fully rewritten VVIS and VRAD to fix elder bugs and get better lighting, optimizations and faster compiling time.
- Map Compilers [cr]: Restored 'dprp' gamelump structure, now detailized surfaces like grass/trash will work. Also, disabled writting some unused VBSP lumps.
- VRad Compiler [cr]: Added most of features from later Source Engines like Fine supersampling (add "-final" cmd-line), 0/50-percent falloff distances for lights, etc.
- Map Compilers [cr]: Finaly written valid code to build closest-to-original Troika's maps lighting.
- Map Compilers: Added some new self-illuminated textures to lights.vrad.
- FGD/VRad Compiler: Since original Troika's lighing gives hard lighting falloffs on surfaces if Distance specified, added parameter "Cut-Off Smoothing Factor" to adjust transitions smoothing from sharp to very soft.
- FGD/VRad Compiler: Removed former "Disable Extras / Disable Cutoff" from compiling options since don't need anymore, and added "Smoothing Scale" to override overall map's lighting transitions (see above).
  >> Note: Use "Map Properties" dialog in Hammer or "-lightsmooth <normal>" vrad.exe command line to control. Default it's turned off and not mainly needed to be touched.
- FGD/Hammer/Compilers: Added ability to use individual VVIS & VRAD compiling settings for each map, which may help to solve various per-map lighting/compiling issues or make some tweaks.
  >> Note: To use this feature, goto Hammer's "Map -> Map Properties..." menu and look into bottom several parameters. Description of each one is attached.
     -- "Lighting: Smoothing Scale / Brightness Scale" are equivalents of -lightsmooth and -lightscale cmdline-params of VRad.exe (see above);
     -- "Compiling: Force Fast" is equivalent of "-fast" parameter of VVIS.exe (helps some heavy maps which refuses to compile normally).
- Hammer/FGD: Updated and corrected some more object's entries and improved light entities controls and descriptions.
- Hammer/FGD: Removed some unused properties from prop_* model classes.
- Added global changes and improved usage notes in the SDK Readme file (please, re-read it!), and other minor fixes.
- Updated Source Code repository.

1.12 (28.05.2015):
- VBsp Compiler [cr]: Fixed issue patching already patched materials when working with cubemaps.
- VRad Compiler [cr]: Fixed self-illum textures respecting if they have a cubemap included.
- VRad Compiler [cr]: Disabled loading static props physics collision model (better for shadow calculations).
  >> Note: To turn respecting collision models back, specify "-usephymodels" cmd-line to VRad.exe.
- VRad Compiler [cr]: Improved help/usage info, now useful parameters sorted and have descriptions.
- VRad Compiler [cr]: Unlocked advanced options for more flexible control.
- VRad Compiler [cr]: Unlocked ability to scale light brightness on the map. 
  >> Note: Use "-scale <float>" cmd-line to VRad.exe to control. Value << 1.0 is darker, >> 1.0 is brighter.
- VRad Compiler [cr]: Restored VtMB's extra light features that allows to use "light" entity as light_spot.
  >> Note: To quickly disable spotlight features, add "-nolightextras" cmd-line to VRad.exe on compiling.
- VRad Compiler [cr]: Default average-light multiplier changed to "0.1" as it's better for maps with rarefied lighting.
- Map Compilers/Other: Added new textures to "lights.rad" good to be compiled on map as self-illuminated.
- Other minor fixes/updates, improved the Readme file and added SDK usage notes about some work aspects.
- Updated Source Code repository.

1.1 (20.05.2015):
- VRad Compiler [cr]: Finally fixed model full-brighting issue at the dark/shadowed areas.
  >> Note: to override defaults, use "-avglight <float>" cmd-line to VRad.exe (0.0625 is default/darker, 1.0 is full/lighter).
- Hammer [cr]: Removed limitation of using 127 craracters paths, now SDK may use up to 512 char paths!
- Hammer [cr]: Fixed loading model's .VTX data if not placed near .MDL but found at one of FileSystem places.
- Hammer [cr]: Added "Show Selected Brush Number" menu option for brushes debugging purposes.
- Hammer/FGD: Updated some entity's entries which previously were unknown (also thanks to Malkav).
- Hammer/FGD: Improved "light_environment", "func_particle/env_particle" and "point_camera" entities control.
- Hammer/Compiling: Added ability to turn off (standby) the machine for large map long compilations.
- Hammer/Compiling: Another improvement for Creating Cubemaps stage - now it depends on compile settigns.
- VBsp Compiler [cr]: Fixed creating default materials for cubemap (strips in-game console error).
- VBsp Compiler [cr]: Fixed recognizing tools "novis" and "visonly" mateials, now they use Hint behaviors.
- VVis Compiler [cr]: Fixed (partially) system/compiler's freezing issues on long compilations.
- VRad Compiler [cr]: "Extra" operations are enabled by default, no need to add -extra key. Use -noextra to disable.
- Actualized readme file and other minor fixes/improvements.
- Updated Source Code repository.

1.0 (03.05.2015):
- Common [cr]: Finally obtained valid structures for models with vertex types 1 & 2 [thanks to Behar].
- Common [cr]: Added generic decoder of type 1 & 2 models with access for all sdk tools [thanks Behar].
- Common [cr]: Updated Hammer, ModelViewer & Map Compilers to support type 1 & 2 models [thanks Behar].
  >> NOTE: You don't need more to do models decompression and import mod resources to SdkContent dir!
- Common [cr]: Improved default project paths assigning for tools if some SDK settings are incorrect.
- Hammer: Merged Build Cubemaps with Run Game stages after compiling map (faster, solves areaportal issue).
- Model Viewer [cr]: Fixed rendering large complex models (NPC etc.), improved background.
- Model Viewer [cr]: Fixed loading model's .VTX and .PHY data if not placed near .MDL but found at one of FileSystem places.
- Removed "MDL Decompressor" tool and "Refresh SDK Content" option since they are useless now.
- Added simple Sound Browser tool for quick access to any game sounds in Project's filesystem tree.
- Rewrited Content Preparation Wizard: disabled copying mod content, improved extraction rules.
  >> NOTE: Extracted VPK content now go to dir "SDKContent\VpkContent", not "SDKContent\Vampire"!
- Improved Texture Converter to generate TTH/TTZ's compatible with PackFile Explorer.
- Reworked apps file system: changed search paths priorities and improved searching algorythms.
- Made minor reorganization of SDKBinaries dir. DON'T install this SDK version OVER the older ones!
- Source Code: Merged with branch "src_mdlexp", made little cleaning, updated Repository.
- Corrected Readme file, actualized bugs and goals list an other.
- Other minor fixes, changes and improvements.

0.93+ (17-26.04.2015):
- Hammer [cr]: Fixed generating bounding boxes for models (now models selection is normal).
- Hammer [cr]: Fixed Z-axis rotation for non-static models, now their orientations are correct.
- Hammer [cr]: Fixed multi-boned models pose calculation (now NPCs rendered correctly).
  >> Important: you need to (re)extract VPK content (if exist), and after, when you run Model Decompressor, check "Type 2 and type 1 to type 0 ONLY" option!
- Hammer [cr]: Added "Go to Coordinates" option into "Map" menu to quick go to certain position.
- Hammer [cr]: Integrated launching advanced compile mode, no more "@" or "execute" in SDK binaries dir.
- Hammer [cr]: Added search paths info (GameDir/ModDir) into the starting message window.
- Hammer [cr]: Fixed bounding boxes axis rotation issue for models.
- Hammer [cr]: Improved some interface elements like object properties, visgroups etc.
- Hammer [cr]: Added support for models with number of bones up to 1024 (all game's).
- Hammer: Updated splash screen logo (added "Bloodlines version" string, edited copyrights) and removed manifest.
- Hammer: Updated default settings, added other unused material paths for exclusion.
- VBsp Compiler [cr]: Re-fixed compiling "tools_shadow" materials (previously they were create empty spaces).
- VBsp Compiler [cr]: Rewrited algorythm of managing cubemaps - now you don't need to attach each brush face manually.
- VBsp Compiler [cr]: Turned cubemap textures search to use full materialsystem.
- VBsp Compiler [cr]: Fixed compiling "toolsnpcopaque" materials (previously they were return "bad surface" error).
- VBsp Compiler [cr]: Fixed error "Mod_LoadTexInfo: texdata < 0" caused by incorrect FindTexInfo() calls.
- MaterialSystem [cr]: Improved reading uncompressed textures, fully disabled VTF searching (faster).
- MDL Decompressor: Made startup warning to tell user to enable appropriate checkbox (see above).
- Texture Converter: Fixed critical error not calling parser on get vtf chunk stage (broke tths).
- Prepatation Wizard: Fixed not-waiting until Model Decompressor finished it's work.
- VPK Creator: Improved separating & packing localized resources rules.
- Made a little file reorganization and optimization in SDK file system.
  >> Please, remove SDKBinaries dir before installing this version!
- Source code: Registered Fire64 (prev. developer) works, make backups of untouched files versions.
- Source code: Updated code repository.

0.92 (08.04.2015):
- Improved (again) algorythm of multiple game paths processing for all apps and tools.
- Common [cr]: Fixed paths detection and mounting procedure if not all game paths found in GameCfg.ini.
- Map Compilers [cr]: Increased BSP limits for entity and texture data, it means that large maps will be compiled nice.
- Hammer [cr]: added shadowing on 3D textured polygons view to get brush objects more discernible and volumetric.
- MaterialSystem [cr]: Fixed reading uncompressed TTH textures (without .ttz chunk) for Hammer & all other tools.
- MaterialSystem [cr]: Corrected writing cubemap's headers, now SDK tools generate correct TTH files.
- Texture Converter: Improved TTZ converter to consider texture's MipMaps and Thumbnail data. Now it writes valid TTHs.
- Texture Converter: Added support for compiling uncompressed TTH textures, see :UserDefs inside it's BAT file.
- VTex Utility [cr]: Added support for TTHs (instead of VTFs) and fixed dir managing issues. Now it can be used for game purposes as an easy texture converter.
- VTex Utility: Added batches to SdkContent/MaterialSrc/ dir to quickly import all created textures into the game (use "convert_all.bat" to compile all TGAs inside).
- VTex Library [cr]: Added ability to run "buildcubemaps" command directly in game without engine or map restarting.
- VBsp Compiler [cr]: Fixed compiling "tools_shadow" materials - now it works correctly and not solid to objects.
- Launch Game procedure from SDK menu is separated from Preparation Wizard and gained improved error control.
- Made cleaning SDKBinaries folder from orphaned unused libraries.
- Made general cleaning source code from unconnected game-related stuff.
- Updated SDK source code repository, merged with extended BSP branch.
- Other minor fixes and improvements, also updated readme file notes.

0.91 (02.04.2015):
- Fixed problem that not allowed to call change game dir dialog correctly.
- Fully denied SDK installation for paths that MORE than 127 characters (Hammer doesn't work).
- Included material & model source examples to SDKContent folder (for better shaking down).
- Hammer [cr]: Improved interface elements (texture selection, undo/redo, entity menu, unused elements).
- Hammer [cr]: Now it generates paths from GameCfg as vars that readable by compilers without any tweaks.
- Hammer [sc]: Optimized cubemaps building procedure: now it'll run only if cubemaps exist on the map.
- ModelCompiler: Fixed issue not creating default model path, improved output.
- ModelCompiler: Unbinded from Vampire directory, now it supports SDK project dir.
- ModelCompiler: Added auto-importing compiled models to SDK content dir.
- Map Compilers [cr]: Added support for multiple folders from GameCfg.ini (models, textures etc will be read from native mod's dir).
- Map Compilers [cr]: Restored original ability to direct write TTH textures on building cubemaps (no external scripts more needed).
- Map Compilers [cr]: Fixed function for reading models and scripts from both gamedir and basedir(sdk) folders.
- Model Viewer: Improved viewing models in Explorer by double-click, now content paths detects correctly.
- Added "Open SDK Content folder" option to the main menu for quick access to your works or game resources.
- Minor file-level changes (don't use this version over older ones!).
- Updated SDK source code and it's repository.

0.9 (26.03.2015):
- SDK is fully unbinded from needing to place itself into the game root dir.
- Hammer: Changed default settings to more comfortable (adatped texture viewer, enabled nudging objects and auto-selection in 2D..);
- Hammer: Fixed Entity creation in 2D views by right-click context menu (previuosly didn't work).
- Hammer: Added new experimental ability to build correct cubemaps after map compiling. 
  >> Don't forget to attach "Brush Faces" of surfaces in entity's properties, or cubemaps won't be visible (engine limitation)!
- Hammer: Into the compile batch added new feature that allows you to include any content like custom materials, scripts, etc. into BSP.
- Hammer: In output system fixed "Param override" and "Python" commands not disabling when selecting new entity or empty output.
- Added option "Refresh SDK Content" to the main menu to quickly import all new changes from mod to SDKContent folder.
- Added more steady error control on all SDK managing procedures & tools. See "sdk_errors.log" to learn what error occurs.
- Added shell extension to view game's .MDL files from the Windows Explorer by double click.
- Fixed assigning file types procedure to be worked correctly for normal users (non admins) of OS.
- Fixed problem with tools that can't use paths with more than 127 symbols, also added warning when SDK install path is closer to this number.
- Fixed all batch scripts to work on paths with "&", "()" and other sp.symbols.
- Dupe Finder: Disabled check for "Vampire" dir since we using whitelists; allowed scanning for VPK contents if dirs are equals.
- VPK Creator: fixed pack naming problem when more than 8 vpks exist in dir.
- Reworked Content Preparation Wizard: improved copying method, merged extraction and copying stages, disabled extracting of .lip and .vcd files.
- Heavy and unstable "VConfig" dialog for changing game dir changed to simple Win32 dialog.
- Resorted SDKBinaries assets & tools: now all SDK service tools and data placed into the "service" subdir.
- Removed ModelDecomp tool since it doesn't work normally. Use a standard "MDL2SMD" decompiler.
- In SDKContent dir created missing default dirs with info-files for Materials and Models.
- Updated Readme file: added installation notes and added solutions info to Programmer's part.
- Updated source code repository (see changelog.txt inside to view what was made for now).
- Minor bugfixes and improvements.

0.85 (05.03.2015):
- Reworked all SDK modules to be able to work with separate mod directories.
- Added new "Texture Converter" utility that fast converts any images to TTh+TTz or VTFs (no more painfull manipulations in VPKTool! :)).
- Added new "Mods Dupe Finder" tool to easy detect and remove mod's content duplicated from original game.
- Completely rewrited "VPK Creator": added multi-dir support, unbinded from engine, made dozens of improvements.
- Improved "TTZView" tool: now it has GUI, supports uncompressed TTH textures and doen't create temp files near TTHs.
- BSPSource decompiler turned back to 1.2.1 version because of areaportal errors on newer versions.
- Decreased 3D models draw distance in Hammer Editor to reduce crashes and slow work.
- Changed SDK main menu order to get more effective tools using.
- Created new category "TEXTURING" in the SDK menu in which moved "VTFEdt", "TTZ Viewer" and "TTZ Converter" tools.
- SDK's programs assets now exctracts into SDKContent\ after the first start, each reset or VPK extraction (this avoids overwrittings from original game).
- Removed duplicated editor assets from "Vampire" directory since they're not used more (see above).
- Separated "VTFEdit" utility from TTZView and placed into SDK menu as independent application.
- Added "Install.bat" file to quick install/copy assets the SDK to game root dir in Wesp5's Unofficial patch.
- PakRat tool was removed from SDK main menu since it doesn't work correctly with the Bloodlines BSP format.
- Merged Programmer's notes and readme into the single file, removed "SRC" folder from the SDK root.
- Fixed minor bugs and defects.

0.82:
- Common [cr]: Fixed patches being hardcoded before: VProject detection, Registry paths, Compile process window etc.
- Hammer [cr]: Finaly added full Python scripts support in "Outputs" section (read+write) - no more need to manually edit entity data!
- Hammer [cr]: Removed "Normal" compiile mode as an unnecessary and buggy, and removed an obsolete process window.
- Hammer [cr], HLMV: Actualized all text data, removed all HL' crap and added actual Web-links to game's and mapping communities.
- Hammer, FGD file: Restored some unused in-game item classes that may be used in some advanced directions.
- FGD file: Fixed some entity inconsistencies and defects, and added some new parameters.
- Fixed setting-up 'ModDir' path as VProject path, and changed 'Game Directory' to Game's subdirecoty in some text mentions.
- Removed some unused content from the SDK binaries folder and decreased the target SDK distributive size.
- [cr] Updated VView.exe utility - increased window size, turned back control by hotkeys, etc.
- [cr] Restored GLView.exe tool to view portal files (.prt) of compiling maps.
- Restored ZLib.dll library that was missing in TTZViewer tool.
- Added SDK's source code target directory and programmer's notes document inside (includes code download links and user's guide).
- Updated readme: added links to official project pages and moved programmer's info to separate note in the source code subfolder.
- Corrected some SDK user interface issues, re-sorted maim menu programs and renamed title to "Bloodlines SDK".
- Fixed typo caused error on VPKs extraction in previous build.
- Other minor fixes and tweaks.

0.81:
- Optimized for Wesp5's Unofficial Patch including no more false warnings of Anti-viruses programs ;).
- Added kHED v1.1.5 low-poly model editor to create your own models (.vtf textures and .smd meshes are supported).
- Added ability to run the SDK from another (not Vampire's root) directories and added interface to specify the custom game paths.
- Improved wrong configuration detection on launching: now it causes a warning message and the full settings reset.
- Re-sorted tools on the SDK main menu to be the more convenient and removed still unused "Face Poser" program link.
- Removed models' broken animation enabled in Hammer 3D-View by default.
- Moved MDLDecompressor tool to "SDKBinaries" dir because it doesn't support dirs with tree depth more than 8 levels.
- Fixed "Launch Game" function in the main menu to be able to run the game from custom-defined paths.
- Updated "VPK Creator" tool to be able to work with games from custom-defined paths.
- Restored missing PakRat tool's JAR file in "Java-Based" dir.
- Minor interface fixes and tweaks.

0.8:
- Fixed multiple dirs support: now you can have two (extracted/original) game versions connected to SDK.
- Renamed "VampireSDK" folder to "SDKBinaries", and your maps and extracted content go to "SDKContent" folder.
- Renamed "Vampire SDK.exe" launcher to "BloodlinesSDK.exe" to be match new naming and avoid confusing with Redemption.
- Added MDLDecompressor to fix Type 1/2 models (and NPCs) after extraction, so they may be correctly loaded in Hammer.
- Added automatized Wizard (runs when you start SDK first) that allows to extract game's VPK and then run MDLDecompressor to fix models.
- Solved problem with 'spaces' in paths: The legacy compile commands/dialog were replaced with advanced custom one (in "Expert" mode).
- Fixed VProject's path detection in all SDK apps (now only GameCfg.ini settings considered) - no more errors on compiling maps.
- Added "BSPDetail" v1.0 utility (it places/edits detail props in maps) for SDK GUI access (Hammer can do that too :)).
- Updated "BSPSource" to version 1.3.13 with adding graphical "BSPInfo" tool to view various map features and configuration.
- Added modified version of "VTFEdit" tool for quick viewing of VTF and TTH textures, converting TTH to VTF and editing VTFs.
- Fixed all "editor" models (playerstart, nodes, etc.) to be correctly displayed as point entities in Hammer Editor.
- Added Launch Game, Extract VPKs, Decompress Models and Full SDK State Reset procedures accessable from the main menu.
- Optimized SDK launcher and service tools codes for better compatiblity with Windows 7 and filepaths with special symbols.
- Added auto-patching for apps' registry path and VProject on first SDK launch [for the future version SRC-compile(R)s].
- Fixed (partially) Hammer crash after compiling map when map was opened via Open Windows dialog (see "Known bugs" note).
- Default compile mode in Hammer turned to "Expert", so, more options are available now, and no more errors with Spaces on paths.
- Packfile Explorer now always uses GameDir (your game folder) as the default root directory.
- Added Explorer associations with main game/engine file types like TTH/VMT/VMF etc. TTH-s are now viewable by doubleckick.
- Improved SDK main menu interface: Since we have many tools, they are sorted by categories.
- Fixed "Planet-Vampire" and "Bloodlines Resurgence" links and removed "Team Camarilla" link (does not use this SDK).
- Updated the SDK readme.txt file; added information for future coders.

0.79.2:
- [cr] Removed black background in Model Viewer.
- [cr] Removed error message on loading models with vertex type 2.
- [cr] In VBSP service VMT commands were added that allow to use specific game tooltextures.

0.79:
- Reworked and improved SDK main menu (uncompatible with older versions - delete "VampireSDK\bin" folder before installation.
- [cr] Updated model compiler - fixed sizes and collision/hitboxes compilation (limitations: just 1 bone and 1 frame per model allowed).
- Added StudioMDL Compiler GUI for easy compiling of your models.
- Added VTMBedit Tool for managing and validating the misc game resources.
- Added VPK Creator utility for packing your content into .vpk game archives.
- Added EntSpy BSP editor for managing entity data on the maps.
- Added BSPEdit tool to edit specific entities like static props.
- Adapted to be included into Wesp5's Unofficial Patch.
- Added misc game-related community links.
- Added detailed readme file (the file you read now).
- Fixed some errors in FGD file.

0.78:
- Added Source SDK menu for easy access to all SDK utilities.
- Added complete FGD file for access to all game entities.
- Replaced VampEd with newer and better PackFile Explorer 3.9.
- Added "MDL 2 SMD" model decompiler by CodenameV & Daedalus.
- Replaced "VMEx" with new advanced "BSPSource" map decompiler.
- Fixed conflicts between Vampire Hammer and new Valve's ones (need to run "AutoConfig.bat" to reconfigure).
- [cr] Added Studiomodel compiler for compiling custom models (doesn't work properly - use $scale 250 to get the correct model dimensions).
- [cr] Fixed freezing in Hammer on rendering some models.
- [cr] Fixed cubemap's building on map compiling ('buildcubemaps' not available yet).
- [cr] Fixed hardware rendering of model skins in HLMV (now one can load almost all of the npc models).
- [cr] Added support for models with bone count of more than 128.
- [cr] Added full support for models having vertex format type 2.
- [cr] Added skeletal animation initial support (works crooked for now).

0.7:
- [cr] Fixed construction of the skeleton of models with few bones.
- [cr] Fixed distortion vertices due to improper tension on the mesh skeleton.
- [cr] Fixed crash of high polygon models and models with flex animations.
- [cr] Model can be rotated in HLMV on all 3 axes now.
- [cr] Model in the Editor now has static angles and does not change the position on moving the camera.
- Added beta FGD file with the VTMB entities.
- Added BAT file to automatically configure the editor.

0.57:
- [cr] In HLMV added partial support for models with a few bones (only for prop models, so far).
- [cr] Added model displaying to the Vampire Map Editor.
- Fixed function of copying maps.

0.55:
- [cr] Fixed generation of collision physics.
- [cr] Added generation of shadows for static models.
- [cr] Fixed handling of dynamic and physical models.
- [cr] Added program to view prop models.

0.5:
- First public release.

<0.5:
- VampBSP tools betas (no Editor introduced).

* [cr] - source code-related changes.