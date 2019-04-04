@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title Bloodlines SDK launcher
pushd "%~dp0"

:: Main
for %%m in (
	service\sfk.exe
	service\msgbox.exe
	service\7za.exe
	service\nircmd.exe
	service\ed_assets.7z
	service\cmdseq.init
	setmoddir.exe
	resetconfig.exe
	sdklauncher.exe
	tools\wizards\prepwizard.bat
	tools\wizards\createmod.bat
) do if not exist "%%~m" (
	echo>>"..\sdk_errors.log" [%date% %time%] Internal error: Missing "%cd%\%%~m" file.
	exit
)

:: Variables
set "SDKRoot=%CD%"
set "EchoSp=service\sfk.exe echo"
set "MsgBox=service\msgbox.exe"
set "UnZip=service\7za.exe"
set "NirCmd=service\nircmd.exe"

:checkconfig
if exist "GameCfg.ini" (
	for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
		if /i "%%~a=%%~b"=="NumConfigs=0" (
			service\sfk.exe replace "GameCfg.ini" "|NumConfigs=0|NumConfigs=1|" -yes -quiet=2
			call :hammerfix -single
		)
		for %%p in (GameData0 BSP Vis Light GameDir GameExeDir GameExe) do (
		if /i "%%~a"=="%%~p" (
		if not exist "%%~b" (
			%MsgBox% Some paths of the current configuration are invalid: "%%~b" [%%~a]. SDK will be reset to its defaults. /c:Bloodlines SDK :: Warning /t:MB_SYSTEMMODAL,MB_ICONWARNING
			goto beginautosetup
		)))
	)
	goto checkmoddir
)

:beginautosetup
 start %MsgBox% Automatic setup, please wait... /c:Bloodlines SDK /t:MB_SYSTEMMODAL,MB_ICONINFORMATION

:defvarsforcfg
 pushd ..
 set "GameRoot=%CD%"
 set "ModDir=%CD%\Vampire"
 set "MapSrcDir=%CD%\SDKContent\MapSrc"
 set "GameDir=%CD%\SDKContent\VpkContent"
 popd

:mkdirsifmissing
 if not exist "%MapSrcDir%\" (md "%MapSrcDir%")

:defgamecfg
(%echosp% "[Configs]"
 %echosp% "NumConfigs=1"
 echo.
 %echosp% "[GameConfig0]"
 %echosp% "Name=Vampire: Bloodlines"
 %echosp% "GameData0=Vampire.fgd"
 %echosp% "TextureFormat=5"
 %echosp% "MapFormat=4"
 %echosp% "DefaultTextureScale=0.25"
 %echosp% "DefaultLightmapScale=16"
 %echosp% "GameExe=%GameRoot%\Vampire.exe"
 %echosp% "DefaultSolidEntity=func_detail"
 %echosp% "DefaultPointEntity=info_player_start"
 %echosp% "BSP=vbsp.exe"
 %echosp% "Vis=vvis.exe"
 %echosp% "Light=vrad.exe"
 %echosp% "GameExeDir=%GameRoot%"
 %echosp% "MapDir=%MapSrcDir%"
 %echosp% "BSPDir=%ModDir%\maps"
 %echosp% "ModDir=%ModDir%"
 %echosp% "GameDir=%GameDir%"
 %echosp% "CordonTexture=tools/toolsskybox"
 %echosp% "MaterialExcludeCount=17"
 %echosp% "-MaterialExcludeDir0=console"
 %echosp% "-MaterialExcludeDir1=debug"
 %echosp% "-MaterialExcludeDir2=detail"
 %echosp% "-MaterialExcludeDir3=engine"
 %echosp% "-MaterialExcludeDir4=envmap"
 %echosp% "-MaterialExcludeDir5=fonts"
 %echosp% "-MaterialExcludeDir6=highlights"
 %echosp% "-MaterialExcludeDir7=hlmv"
 %echosp% "-MaterialExcludeDir8=hud"
 %echosp% "-MaterialExcludeDir9=interface"
 %echosp% "-MaterialExcludeDir10=launcher"
 %echosp% "-MaterialExcludeDir11=maps"
 %echosp% "-MaterialExcludeDir12=models"
 %echosp% "-MaterialExcludeDir13=particle"
 %echosp% "-MaterialExcludeDir14=shadertest"
 %echosp% "-MaterialExcludeDir15=vgui"
 %echosp% "-MaterialExcludeDir16=worldcraft"
)> "GameCfg.ini"

:hammerfix
(reg delete "HKCU\Software\Troika\Hammer" /f
 reg add "HKCU\Software\Troika\Hammer\2D Views"   /v "AutoSelect"       /t REG_DWORD /d "1" /f
 reg add "HKCU\Software\Troika\Hammer\2D Views"   /v "Crosshairs"       /t REG_DWORD /d "1" /f
 reg add "HKCU\Software\Troika\Hammer\2D Views"   /v "CenterOnCamera"   /t REG_DWORD /d "1" /f
 reg add "HKCU\Software\Troika\Hammer\2D Views"   /v "Gridhigh64"       /t REG_DWORD /d "0" /f
 reg add "HKCU\Software\Troika\Hammer\2D Views"   /v "Nudge"            /t REG_DWORD /d "1" /f
 reg add "HKCU\Software\Troika\Hammer\2D Views"   /v "OrientPrimitives" /t REG_DWORD /d "1" /f
 reg add "HKCU\Software\Troika\Hammer\3D Views"   /v "AnimateModels"    /t REG_DWORD /d "0" /f
 reg add "HKCU\Software\Troika\Hammer\3D Views"   /v "BackPlane"        /t REG_DWORD /d "3000" /f
 reg add "HKCU\Software\Troika\Hammer\3D Views"   /v "ModelDistance"    /t REG_DWORD /d "1500" /f
 reg add "HKCU\Software\Troika\Hammer\3D Views"   /v "Reverse Y"        /t REG_DWORD /d "0" /f
 reg add "HKCU\Software\Troika\Hammer\Configured" /v "Configured"       /t REG_DWORD /d "2" /f
 reg add "HKCU\Software\Troika\Hammer\General"    /v "Autosave Dir"     /t REG_SZ    /d "%MapSrcDir%\autosaves" /f
 reg add "HKCU\Software\Troika\Hammer\Splitter"   /v "WindowPlacement"  /t REG_SZ    /d "(-1 -1) (-1 -1) (-1 -1 -1 -1) 3" /f
 reg add "HKCU\Software\Troika\Hammer\Splitter"   /v "DrawType0,0"      /t REG_DWORD /d "5" /f
 if /i "%~1"=="-single" exit /b
)> nul

:pfexplorerfix
(reg add "HKCU\Software\Tools\PackfileExplorer" /v "LastPath"     /t REG_SZ    /d "%ModDir%" /f
 reg add "HKCU\Software\Tools\PackfileExplorer" /v "ListViewMode" /t REG_DWORD /d "2" /f
 reg add "HKCU\Software\Tools\PackfileExplorer" /v "WindowLayout" /t REG_DWORD /d "1" /f
)> nul

:studiocompfix
(reg delete "HKCU\Software\CFApps\StudioCompiler" /f
 reg add "HKCU\Software\CFApps\StudioCompiler\StudioCompiler" /v "TabSelect"       /t REG_DWORD /d "0" /f
 reg add "HKCU\Software\CFApps\StudioCompiler\StudioCompiler" /v "Anim SMD Check"  /t REG_DWORD /d "1" /f
 reg add "HKCU\Software\CFApps\StudioCompiler\StudioCompiler" /v "Phy SMD Check"   /t REG_DWORD /d "1" /f
 reg add "HKCU\Software\CFApps\StudioCompiler\StudioCompiler" /v "SDKDirectory"    /t REG_SZ /d "%GameRoot%\SdkBinaries" /f
 reg add "HKCU\Software\CFApps\StudioCompiler\StudioCompiler" /v "GameDirectory"   /t REG_SZ /d "%ModDir%" /f
 reg add "HKCU\Software\CFApps\StudioCompiler\StudioCompiler" /v "Shader"          /t REG_SZ /d "VertexLitGeneric" /f
 reg add "HKCU\Software\CFApps\StudioCompiler\StudioCompiler" /v "Model File"      /t REG_SZ /d "mymodels\model_01.mdl" /f
 reg add "HKCU\Software\CFApps\StudioCompiler\StudioCompiler" /v "Materials Dir"   /t REG_SZ /d "mymodels\model_01" /f
 reg add "HKCU\Software\CFApps\StudioCompiler\StudioCompiler" /v "Envmap Tint"     /t REG_SZ /d "\"[0.5 0.5 0.5]\"" /f
 reg add "HKCU\Software\CFApps\StudioCompiler\MDLDecompiler"  /v "OutputDirectory" /t REG_SZ /d "%GameRoot%\SdkContent\ModelSrc" /f
)> nul

:khedmanualfix
(reg delete "HKCU\Software\kHED" /f
)> nul

:installplugins
 start plugins\fileassocs.exe -internal
 start plugins\texplugins.exe -internal

:setconsolefont
(reg add "HKCU\Console" /v "FaceName" /t REG_SZ /d "Lucida Console" /f
 reg add "HKCU\Console" /v "FontFamily" /t REG_DWORD /d "54" /f
 reg add "HKCU\Console" /v "FontSize" /t REG_DWORD /d "851968" /f
 reg add "HKCU\Console" /v "FontWeight" /t REG_DWORD /d "400" /f
 reg add "HKCU\Console" /v "QuickEdit" /t REG_DWORD /d "1" /f
 reg add "HKCU\Console" /v "ScreenBufferSize" /t REG_DWORD /d "52428880" /f
)> nul

:extractassets
 %UnZip% x "service\ed_assets.7z" -o"%GameDir%\" -y -aoa> nul

:cleartemps
 if exist "*.rf"  del /a /q *.rf> nul
 copy /y "service\cmdseq.init" ".\cmdseq.wc"> nul
 reg delete "HKCU\Software\Troika\hlmv" /f> nul

:fisrstrun
 echo # This file needed to detect SDK first launch and run Wizard.> "FirstRun.ini"
 echo # This file needed to detect StudioMdl first launch and show Alpha-state Warning.> "service\mdlwarn.ini"
 echo # This file needed to detect StudioCompiler first launch and show usage Warning.> "tools\StudioCompiler\ShowWarning.ini"
 taskkill /f /im "msgbox.exe"> nul

:setmoddir
 %MsgBox% This is the first launch of the Bloodlines SDK. Choose the mod directory you're using for your project (usually it's folder near "vampire.exe" in the game root directory). If you plan to work with the original game (which is in "Vampire" folder), just click "Cancel" to keep default config. /t:MB_SYSTEMMODAL,MB_ICONINFORMATION,MB_OKCANCEL /c:Note
 if not "%ErrorLevel%"=="2" "setmoddir.exe" -first

:checkmoddir
 for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
	if /i "%%~a"=="GameDir" (
	if exist "%%~b\*" (
		set "VProject=%%~b"
		setx VProject "%%~b"> nul
		reg add "HKCU\Environment" /v "VProject" /d "%%~b" /f > nul
		set "%%~a=%%~b"
	))
	if /i "%%~a"=="ModDir" (
	if exist "%%~b\*" (
		set "%%~a=%%~b"
	) else (goto badmoddir))
 )
 goto startsdk

:badmoddir
 %MsgBox% The currently specified game directory is invalid. Please, choose the correct game content location (this usually is game's "Vampire" or "Unofficial_Patch" subdirectory). If you don't, not all tools will work! /c:Bloodlines SDK :: Error /t:MB_SYSTEMMODAL,MB_ICONWARNING,MB_OKCANCEL
 if "%ErrorLevel%"=="2" (del /a /q "FirstRun.ini"> nul) else ("setmoddir.exe")

:startsdk
 taskkill /f /im SDKLauncher.exe> nul 2>&1
 start SDKLauncher.exe

:wizard
 if not exist "FirstRun.ini" goto finish
 del /a /q "FirstRun.ini"> nul
 %MsgBox% Since the current version doesn't support content packed into .VPK archives, they need to be unpacked for the correct work of some SDK applications. Extracted resources will go to "SDKContent\VpkContent\" directory which will be available to Hammer Editor and other SDK tools.  The original game content and folders won't be touched or modified, nevertheless, your compiled maps will read these resources when you are running them in game.  Extracting may take some time and requires about 2Gb of disk space.  Note that if you don't need tools like the "Hammer Editor" and don't plan to create own maps, an extraction is not necessary.  Start extracting now? /t:MB_SYSTEMMODAL,MB_ICONEXCLAMATION,MB_YESNO /c:Note
 if not "%ErrorLevel%"=="6" (
 	%MsgBox% You may always do the extraction later using the option "ReExtract VPK content" in the Bloodlines SDK main menu. /t:MB_SYSTEMMODAL,MB_ICONINFORMATION /c:Tip
	goto finish
 )
 start /w tools\wizards\prepwizard.bat -firstrun
 %MsgBox% All preparations are finished. Bloodlines SDK is configured and ready to work. Have fun! ;) /t:MB_SYSTEMMODAL,MB_ICONINFORMATION /c:Note

:finish
 rem Hack for moving SDK findow to front
 for %%l in (1 2 3 4 5 6 7 8) do (
	%NirCmd% wait 100
 	%NirCmd% win settopmost process "sdklauncher.exe" 1
 )
 %NirCmd% win settopmost process "sdklauncher.exe" 0
 rem Clear mod's material*/ lumps if empty...
 for %%m in (materialsrc materials\maps) do (
 	if exist "%ModDir%\%%~m\" call :rememptydirs "%ModDir%\%%~m"
 )
 exit

:rememptydirs
 for /d %%a in ("%~1\*") do (
 	call :rememptydirs "%%~fa"
 )
 rmdir "%~f1"> nul 2>&1
 exit /b