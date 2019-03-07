@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
set version=0.8 beta
set Title=Create a New Mod
title %Title%
pushd "%~dp0"
pushd "..\.."

set MsgBox=service\msgbox.exe
set Sfk=service\sfk.exe
set InputBox=service\inputbox.exe
set UnZip=service\7za.exe
set UtfConv="%~dp0service\ansi2utf.exe"
set EchoX=%Sfk% echo

:: Check Assets
for %%m in (msgbox sfk inputbox 7za) do if not exist "service\%%~m.exe" (
	echo ERROR!
	echo>>"..\sdk_errors.log" [%date% %time%] Internal error: Missing "%cd%\service\%%~m.exe" file.
	exit
)

:: Check Config
if not exist "GameCfg.ini" (
	%EchoX% [Red]ERROR!
	echo>>"..\sdk_errors.log" [%date% %time%] SDK Error: Missing "%cd%\GameCfg.ini" file. Full reset needed.
	%MsgBox% Can't find "GameCfg.ini" at SDK binaries. Please, re-launch the SDK now to perform full reset procedure which will generate default game config. /c:Bloodlines SDK :: Error /t:MB_SYSTEMMODAL,MB_ICONERROR
	exit
)

:: Check Game Root
set ModDirPassed=
for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
	if /i "%%~a"=="GameExeDir" set "%%~a=%%~b"
	if /i "%%~a"=="ModDir" set ModDirPassed=1
)
if not exist "%GameExeDir%\Vampire.exe" (
	%EchoX% [Red]ERROR!
	echo>>"..\sdk_errors.log" [%date% %time%] Configuration Error: Invalid "%GameExeDir%". Mod will not created.
	%MsgBox% Invalid game root location specified in GameCfg.ini: "%GameExeDir%". Please, re-define the SDK settings by performing full reset procedure which will generate default game config. /c:Bloodlines SDK :: Error /t:MB_SYSTEMMODAL,MB_ICONERROR
	exit
)
if not defined ModDirPassed (
	%EchoX% [Red]ERROR!
	echo>>"..\sdk_errors.log" [%date% %time%] Configuration Error: No existing "ModDir" presented. Mod will not created.
	%MsgBox% No "ModDir" currently specified in GameCfg.ini file. Please, re-define the SDK settings by performing full reset procedure which will generate default game config. /c:Bloodlines SDK :: Error /t:MB_SYSTEMMODAL,MB_ICONERROR
	exit
)

:SetModDefs
cls
set NewModName=
set NewModDir=

:: Set Name
for /f "delims=" %%a in (
'%InputBox% "Please, enter your mod name:" "%Title%" "My First Mod" /W:300'
) do set "NewModName=%%~a"
if not defined NewModName exit

:: Set Directory
for /f "delims=" %%a in (
'%InputBox% "Enter mod directory (will be created near vampire/):" "%Title%" "%NewModName: =%" /W:300'
) do set "NewModDir=%%~a"
if not defined NewModDir exit
if defined NewModDir set "NewModDir=%NewModDir: =%"
if defined NewModDir set "NewModDir=%NewModDir::=%"
if defined NewModDir set "NewModDir=%NewModDir:?=%"
if defined NewModDir set "NewModDir=%NewModDir:!=%"
if defined NewModDir set "NewModDir=%NewModDir:&=%"
if defined NewModDir set "NewModDir=%NewModDir:-=%"
if defined NewModDir set "NewModDir=%NewModDir:@=%"
if defined NewModDir set "NewModDir=%NewModDir:#=%"
if defined NewModDir set "NewModDir=%NewModDir:/=%"
if defined NewModDir set "NewModDir=%NewModDir:\=%"
if defined NewModDir set "NewModDir=%NewModDir:|=%"
if defined NewModDir set "NewModDir=%NewModDir:^=%"
if defined NewModDir set "NewModDir=%NewModDir:<=%"
if defined NewModDir set "NewModDir=%NewModDir:>=%"
if defined NewModDir set "NewModDir=%NewModDir:,=%"
if defined NewModDir set "NewModDir=%NewModDir:;=%"
if defined NewModDir set "NewModDir=%NewModDir:`=%"
if defined NewModDir set "NewModDir=%NewModDir:'=%"
if defined NewModDir set "NewModDir=%NewModDir:+=%"
if defined NewModDir set "NewModDir=%NewModDir:(=%"
if defined NewModDir set "NewModDir=%NewModDir:)=%"
if defined NewModDir set "NewModDir=%NewModDir:[=%"
if defined NewModDir set "NewModDir=%NewModDir:]=%"
if defined NewModDir set "NewModDir=%NewModDir:{=%"
if defined NewModDir set "NewModDir=%NewModDir:}=%"
if defined NewModDir set "NewModDir=%NewModDir:$=%"
if not defined NewModDir goto SetModDefs
for %%m in (
	Vampire Unofficial_Patch
) do if /i "%NewModDir%"=="%%~m" (
	%MsgBox% You can't create mod in %%~m\! Please, try another folder. /c:Create a New Mod /t:MB_SYSTEMMODAL,MB_ICONWARNING
	goto SetModDefs
)
if exist "%GameExeDir%\%NewModDir%\" (
	%MsgBox% Mod with such directory already exists! Please, try another one. /c:Create a New Mod /t:MB_SYSTEMMODAL,MB_ICONWARNING
	goto SetModDefs
)

:: Create folder and extract stuff
if not exist "%GameExeDir%\%NewModDir%\" md "%GameExeDir%\%NewModDir%\"> nul
%UnZip% x -o"%GameExeDir%\%NewModDir%\" -y -aoa "%~dp0\service\modbase.zip"> nul

:: Import assets from Unofficial patch
if exist "%GameExeDir%\Unofficial_Patch\materials\" (
	%MsgBox% Found Wesp5's Unofficial Patch inside your game directory. Are you wish to copy its assets into your new mod to use them as the content base? It's very recommended action because this will make all fixed or improved stuff from the patch to be available in your mod as well. /c:Create a New Mod /t:MB_SYSTEMMODAL,MB_ICONQUESTION,MB_YESNO
)
if exist "%GameExeDir%\Unofficial_Patch\materials\" (
if "%ErrorLevel%"=="6" (
	start %MsgBox% Copying patch's assets, please wait... /c:Create a New Mod /t:MB_SYSTEMMODAL,MB_ICONINFORMATION
	for %%m in (
		cfg
		dlg\generic
		materials
		models
		particles
		python
		scripts
		sound\character\dlg\generic
		vdata
	) do if exist "%GameExeDir%\Unofficial_Patch\%%~m\" (
		xcopy /s /c /i /r /q /y "%GameExeDir%\Unofficial_Patch\%%~m" "%GameExeDir%\%NewModDir%\%%~m\"> nul
	)
	for /d %%m in ("%GameExeDir%\Unofficial_Patch\sound\*") do if /i not "%%~nxm"=="character" (
		xcopy /s /c /i /r /q /y "%%~m" "%GameExeDir%\%NewModDir%\sound\%%~nxm\"> nul
	)
	for /d %%m in ("%GameExeDir%\Unofficial_Patch\sound\character\*") do if /i not "%%~nxm"=="dlg" (
		xcopy /s /c /i /r /q /y "%%~m" "%GameExeDir%\%NewModDir%\sound\character\%%~nxm\"> nul
	)
	call taskkill /f /im "MsgBox.exe"> nul
))

:: Parse liblist.gam file
%Sfk% filter "%GameExeDir%\%NewModDir%\scripts\liblist.gam" -lswhere "game " -srep "|game *|game \q%NewModName%\q|" -write -yes> nul
%Sfk% filter "%GameExeDir%\%NewModDir%\scripts\liblist.gam" -lswhere "gamedll " -srep "|gamedll *|gamedll \q..\vampire\dlls\vampire.dll\q|" -write -yes> nul

:: Parse gameui_english.txt file
%Sfk% filter "%GameExeDir%\%NewModDir%\resource\gameui_english.txt" -srep "|\qGameUI_Patch\q*|\qGameUI_Patch\q\t\t\t\q%NewModName%\q|" -write -yes -utf> nul
pushd "%GameExeDir%\%NewModDir%\resource\"
%UtfConv% -i gameui_english.txt -o gameui_english.utf
move /y gameui_english.utf gameui_english.txt > nul
popd
%Sfk% replace "%GameExeDir%\%NewModDir%\resource\gameui_english.txt" -bin "|0000||" -quiet -yes> nul

:: Create .bat launcher
set "NewBatName=%NewModName::=%"
set "NewBatName=%NewBatName:?=%"
set "NewBatName=%NewBatName:&=%"
set "NewBatName=%NewBatName:/=%"
set "NewBatName=%NewBatName:\=%"
set "NewBatName=%NewBatName:|=%"
set "NewBatName=%NewBatName:^=%"
set "NewBatName=%NewBatName:<=%"
set "NewBatName=%NewBatName:>=%"
echo @start Vampire.exe -game %NewModDir%> "%GameExeDir%\%NewBatName%.bat"

:: Ask about adding to GameCfg
%MsgBox% You've created mod "%NewModName%" with directory "%NewModDir%". The batch file (*.bat) with mod name near Vampire.exe created to launch it. Walk inside mod's folder to learn about its file system you will work with in the future. /c:Create a New Mod /t:MB_SYSTEMMODAL,MB_ICONINFORMATION
%MsgBox% Do you want to use a new mod as your current SDK project to work on? /c:Create a New Mod /t:MB_SYSTEMMODAL,MB_ICONEXCLAMATION,MB_YESNO
if "%ErrorLevel%"=="6" (
	%Sfk% filter "GameCfg.ini" -where "ModDir*=" -rep "|ModDir*=*|ModDir=%GameExeDir%\%NewModDir%|" -write -yes> nul
	%Sfk% filter "GameCfg.ini" -where "BSPDir*=" -rep "|BSPDir*=*|BSPDir=%GameExeDir%\%NewModDir%\maps|" -write -yes> nul
	set "VProject=%GameExeDir%\%NewModDir%"
	setx VProject "%GameExeDir%\%NewModDir%"> nul
	reg add "HKCU\Software\Tools\PackfileExplorer" /v "LastPath" /d "%GameExeDir%\%NewModDir%" /f> nul
	reg add "HKCU\Environment" /v "VProject" /d "%GameExeDir%\%NewModDir%" /f> nul
	%MsgBox% All operations done. You can now start your works! /c:Create a New Mod /t:MB_SYSTEMMODAL,MB_ICONINFORMATION
)

:: Quit wizard
exit