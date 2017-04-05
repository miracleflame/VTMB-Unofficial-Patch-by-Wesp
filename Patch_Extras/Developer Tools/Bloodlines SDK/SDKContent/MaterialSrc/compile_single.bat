@echo off
title VTex Batch Script
setlocal ENABLEEXTENSIONS
pushd "%~dp0"

if "%~1"=="" (
	echo Usage: 
	echo  1. Ensure this batch placed into "materialsrc\" dir.
	echo  2. Create dir inside as you want to see in "materials" 
	echo     dir and place some source .tga textures inside.
	echo  3. Drag and drop your tgas to this batch and you'll 
	echo     get TTHs at "materials\your_path\" output.
	echo  Tip: You may also compile 6-faces cubemaps textures.
	echo.
	echo Bloodlines SDK must be installed to perform something!
	pause> nul
	exit
)

:Main
set SdkDir=
call :FindSdkDir
set VTex="%SdkDir%\vtex.exe"
set Sfk="%SdkDir%\service\sfk.exe"
set Error=call :IfError

:CheckPaths
if not defined SdkDir (
%Error% Problem finding out SDK assets directory.)
for %%m in (%VTex% %Sfk%) do if not exist %%m (
%Error% Can't find %%m.)

:FindModDir
if exist "%SdkDir%\GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("%SdkDir%\GameCfg.ini") do (
	if /i "%%~a"=="ModDir" if exist "%%~b\" (set "VProject=%%~b")
))

:RunScript
if not exist "%VProject%\materials\" (md "%VProject%\materials")
echo Project Dir: 
echo "%VProject%"
echo.

for %%m in (%*) do (
for /f "delims=" %%x in ('call %Sfk% echo -lit "%%~m" +filter -rep "|*\materialsrc\||" -lerep "|\%%~nxm||"'
) do (
	echo running vtex for "%%~x\%%~nm.tga"...
	%VTex% -quiet -nopause -shader "LightmappedGeneric" "%%~m"

	rem Check if TTH created, then check vmts...
	if exist "%VProject%\materials\%%~x\%%~nm.tth" (
		echo   success: "materials\%%~x\%%~nm.tth".
	) else (
		echo   error creating "%VProject%\materials\%%~x\%%~nm.tth".
	)
	rem Check if VMT created, then exit...
	if exist "%VProject%\materials\%%~x\%%~nm.vmt" (
		echo   success: "materials\%%~x\%%~nm.vmt".
	) else (
		echo   error creating "%VProject%\materials\%%~x\%%~nm.vmt".
	)
	echo.
))

pause> nul
exit

:FindSdkDir
pushd ..
if exist "SDKBinaries\vtex.exe" (
	set "SdkDir=%cd%\SDKBinaries"
	set "VProject=%cd%\Vampire"
) else (
	if /i not "%cd%"=="%~d0\" (
		goto FindSdkDir
	)
)
exit /b

:IfError
	cls
	color 0c
	echo ERROR!
	echo %*
	pause> nul
	pause> nul
exit
