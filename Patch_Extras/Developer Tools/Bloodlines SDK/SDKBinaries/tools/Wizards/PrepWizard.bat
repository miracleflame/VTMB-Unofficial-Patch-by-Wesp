@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title Content Preparation Wizard
color 06
echo Initializing...
pushd "%~dp0"

:app-vars
pushd "..\.."
set "MsgBox=%cd%\service\msgbox.exe"
set "SfkTool=%cd%\service\sfk.exe"
set "Un7zip=%cd%\service\7za.exe"
set "Assets=%cd%\service\ed_assets.7z"
set "GameCfg=%cd%\GameCfg.ini"
popd

:=======================================================================
:CheckFiles

for %%m in (
	"%MsgBox%"
	"%SfkTool%"
	"%Un7zip%"
	"%Assets%"
	"%cd%\service\VExtract.bat"
	"%cd%\service\VExtract0.exe"
	"%cd%\service\VExtract1.exe"
	"%cd%\service\vpkindex.fix"
) do if not exist "%%~m" (
	color 0c
	echo ERROR! No "GameCfg.ini" found. Exiting...
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] PrepWizard error: Missing "%%~m" file.
	exit
)
if not exist "%GameCfg%" (
	color 0c
	echo ERROR! No "GameCfg.ini" found. Exiting...
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] PrepWizard error: Game config "%GameCfg%" not found.
	"%MsgBox%" No "GameCfg.ini" found in SDK binaries directory. Cannot detect valid game paths. /c:ERROR! /t:MB_ICONSTOP
	exit
)


:=======================================================================
:ExtractVPKs

:readgamecfg
set TargetDir=
for /f "usebackq delims== tokens=1,*" %%i in ("%GameCfg%") do (
	if /i "%%~i"=="ModDir" (
	if exist "%%~j\*" (
		set "ModDir=%%~j"
	) else (
		echo ERROR! Incorrect ModDir specified. Exiting...
		"%MsgBox%" No valid game files found at "%%~j\". Please, define the correct "ModDir" path in "GameCfg.ini" using "Change Path to Project Dir" option in the SDK main menu or using Hammer Editor's configuration. /c:ERROR! /t:MB_ICONSTOP
		exit
	))
	if /i "%%~i"=="GameDir" (
		set "TargetDir=%%~j"
		if not exist "%%~j\" md "%%~j"
	)
)

:setvampiredir
set VampireDir=
pushd "%ModDir%\.."
set "VampireDir=%cd%\Vampire"
popd

:checkvpkexist
if not exist "%VampireDir%\pack?*.vpk" (
	if not exist "%VampireDir%\materials\*" (
	if not exist "%VampireDir%\models\*" (
		echo ERROR! No VPK archives and game content found. Exiting...
		"%MsgBox%" No VPK archives and game content found at "%VampireDir%\". Seems like your project is not in game's root that is not allowed. To set the correct location, use "Change Path to Project dir" option in the SDK main menu. /c:ERROR! /t:MB_ICONSTOP
		exit
	))
	echo No VPKs found, game content is already extracted.
	"%MsgBox%" No VPK archives found at "%VampireDir%\". Your game's resources are already extracted, so the SDK tools will access them directly. /c:Note /t:MB_ICONWARNING
	echo Updating GameCfg.ini to access Vampire dir...
	"%SfkTool%" filter "GameCfg.ini" -where "GameDir=" -rep "|GameDir=*|GameDir=%VampireDir%|" -write -yes> nul
	echo - Game config updated.
	set "TargetDir=%VampireDir%"
	goto ExtractEdAssets
)


:checktargetdir
if not defined TargetDir (
	echo ERROR! No GameDir specified. Exiting...
	"%MsgBox%" No "GameDir" specified in "GameCfg.ini" file. This folder is needed to extract the VPK contents into. Please, define the correct "GameDir" path using Hammer Editor's configuration. You can also get the default one by running "Reset SDK Configuration" procedure from the SDK main menu. /c:ERROR! /t:MB_ICONSTOP
	exit
)

:showdirinfo
if /i "%ModDir%"=="%VampireDir%" (
	echo Source Directory [BaseDir]: 
	echo   "%VampireDir%"
) else (
	echo Base Directory [Vampire]: 
	echo   "%VampireDir%"
	echo Project Directory [ModDir]: 
	echo   "%ModDir%"
)
echo Target Directory [Content]: 
echo   "%TargetDir%"
echo.

:getlaunchrules
if /i not "%~1"=="-firstrun" (
	"%MsgBox%" Extracting content from original VPK archives needed for correct SDK-applications work because its current version doesn't support VPK file-system. The extracted resources will go into directory which will be available to the Hammer Editor and other SDK tools.  The original game content and folders won't be touched or modified, nevertheless, your compiled maps will read these resources when you are running them in game.  Extracting may take some time and requires about 2Gb of disk space.  If you don't need tools like the Hammer Editor and don't plan to create own maps, an extraction is not necessary.  Start extracting now? /t:MB_ICONEXCLAMATION,MB_YESNO /c:Note)
if "%ErrorLevel%"=="7" (
	echo Canceled by user. Exiting...
	exit
)

:runvextract
call "service\VExtract.bat" -int


:=======================================================================
:ExtractEdAssets
echo Extracting basic Editor assets...
"%Un7zip%" x "%Assets%" -o"%TargetDir%\" -y -aoa > nul
echo - Editor assets extracted.
echo.


:=======================================================================
:PrepFinish
echo All content transfer operations finished.
echo Exiting Wizard...
if /i not "%~1"=="-firstrun" (
"%MsgBox%" All content transfer operations finished. /c:Information /t:MB_SYSTEMMODAL,MB_ICONINFORMATION)

ping>nul -n 2 "127.0.0.1"
exit
