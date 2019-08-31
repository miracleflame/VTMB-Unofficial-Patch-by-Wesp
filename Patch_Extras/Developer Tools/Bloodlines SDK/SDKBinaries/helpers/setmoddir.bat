@echo off
title Set Game Directory
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
pushd "%~dp0\.."

set "MsgBox=helpers\msgbox.exe"
set "Sfk=helpers\sfk.exe"
set "ChooseDir=helpers\setdirdlg.exe /d"

:: Check Assets
for %%m in (setdirdlg msgbox sfk) do (
if not exist "helpers\%%~m.exe" (
	echo>>"..\sdk_errors.log" [%date% %time%] Internal error: Missing "%cd%\helpers\%%~m.exe" file.
	exit
))

:: Check Config
if not exist "GameCfg.ini" (
	echo>>"..\sdk_errors.log" [%date% %time%] Setup Error: Missing "%cd%\GameCfg.ini" file. Full reset needed.
	%MsgBox% Can't find "GameCfg.ini" at SDK binaries. Please, re-launch the SDK now to perform full reset procedure which will generate default game config. /c:Bloodlines SDK :: Error /t:MB_SYSTEMMODAL,MB_ICONERROR
	exit
)

:: Get prev ModDir value
for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
	if /i "%%~a"=="ModDir" (set "ModDirPrev=%%~b")
)

:ChangeModDir
set ProcDirRan=0
set DirIsValid=0
for /f "delims=" %%a in ('%ChooseDir%') do (
if not "%%~a"=="" (call :ProcessModDir "%%~a"))
if "%ProcDirRan%"=="0" (exit)

if "%DirIsValid%"=="0" (
	if "%ErrorLevel%"=="2" (
		if exist "FirstRun.ini" (
		del /a /q "FirstRun.ini")
		exit
	) else (goto ChangeModDir)
)

:Finalize
reg add "HKCU\Software\Tools\PackfileExplorer" /v "LastPath" /d "%ModDir%" /f> nul

if /i "%ModDir%"=="%ModDirPrev%" (
if /i not "%~1"=="-first" (
	%MsgBox% Selected game directory is the same as previous: "%ModDir%". /c:Bloodlines SDK /t:MB_SYSTEMMODAL,MB_ICONWARNING
	exit
))

if /i "%~1"=="-first" (
	%MsgBox% This game directory will be used as your project: "%ModDir%". /c:Bloodlines SDK /t:MB_SYSTEMMODAL,MB_ICONINFORMATION
) else (
	if exist "%ModDir%\pack*.vpk" (
		%MsgBox% Game directory changed to "%ModDir%". Note that selected mod contains VPK archives with some content, so if you want to access it, you also need to run "ReExtract VPK Content" menu option to import this content so that will be available for the SDK tools. /c:Bloodlines SDK /t:MB_SYSTEMMODAL,MB_ICONINFORMATION
	) else (
		%MsgBox% Game directory changed to "%ModDir%". /c:Bloodlines SDK /t:MB_SYSTEMMODAL,MB_ICONINFORMATION
	)
)

exit



::==============================================
:: Functions
::==============================================

:ProcessModDir
	set ProcDirRan=1
	for %%m in ("Vampire\" "Vampire.exe") do (
	if not exist "%~1\..\%%~m" (
		%MsgBox% Can't find "%%~m" near selected game directory. Note that your game or mod must be placed into the main game's root directory! /c:Bloodlines SDK :: Error /t:MB_SYSTEMMODAL,MB_ICONERROR,MB_OKCANCEL
		exit /b
	))
	if not exist "%~1\cfg\*" (
	if not exist "%~1\dlls\*" (
	if not exist "%~1\scripts\liblist.gam" (
	if not exist "%~1\materials\*" (
	if not exist "%~1\models\*" (
	if not exist "%~1\python\*" (
	if not exist "%~1\pack*.vpk" (
		%MsgBox% Game assets not found in selected directory. Please, choose a correct one! /c:Bloodlines SDK :: Error /t:MB_SYSTEMMODAL,MB_ICONERROR,MB_OKCANCEL
		exit /b
	)))))))

	set "ModDir=%~1"
	pushd "%~1\.."
	set "GameRoot=%cd%"
	popd
	
	set DirIsValid=1
	%Sfk% filter "GameCfg.ini" -where "GameExeDir=" -rep "|GameExeDir=*|GameExeDir=%GameRoot%|" -write -yes -quiet=2
	%Sfk% filter "GameCfg.ini" -where "GameExe=" -rep "|GameExe=*|GameExe=%GameRoot%\Vampire.exe|" -write -yes -quiet=2
	%Sfk% filter "GameCfg.ini" -where "BSPDir=" -rep "|BSPDir=*|BSPDir=%ModDir%\maps|" -write -yes -quiet=2
	%Sfk% filter "GameCfg.ini" -where "ModDir=" -rep "|ModDir=*|ModDir=%ModDir%|" -write -yes -quiet=2
exit /b