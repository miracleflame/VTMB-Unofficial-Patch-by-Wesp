@echo off
title Bloodlines Model Viewer Command Line
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
pushd "%~dp0"

:CheckBin
set HLMV="%cd%\hlmv.exe"
for %%m in (hlmv.exe helpers\sfk.exe) do (
if not exist "%%~m" (
	echo>>"..\sdk_errors.log" [%date% %time%] HlmvShell error: Missing "%cd%\%%~m" file.
	exit
))
if /i not "%~x1"==".mdl" (
	echo>>"..\sdk_errors.log" [%date% %time%] HlmvShell error: "%~1" is not MDL file.
	exit
)

:RegFiles
if "%~1"=="" (
	echo Registering file association...
	reg>nul add "HKCU\Software\Classes\.mdl" /f /ve  /t REG_SZ /d "MDLFile"
	reg>nul add "HKCU\Software\Classes\MDLFile" /f /ve  /t REG_SZ /d "Vampire Model File"
	reg>nul add "HKCU\Software\Classes\MDLFile\shell" /f /ve /t REG_SZ /d "View"
	reg>nul add "HKCU\Software\Classes\MDLFile\shell\View\command" /f /ve /t REG_SZ /d "%~dpn0.exe \"%%1\""
	reg>nul add "HKCU\Software\Classes\MDLFile\DefaultIcon" /f /ve /t REG_SZ /d "%~dpn0.exe,0"
	exit
)

:StripPath
for /f "delims=" %%a in ('helpers\sfk.exe echo "%~1" +filter -rep "|\models\??*||"') do (set "ModDir=%%~a")
for /f "delims=" %%a in ('helpers\sfk.exe echo "%~1" +filter -rep "|??*\models\|models\|"') do (set "FilePath=%%~a")
if not exist "%ModDir%\%FilePath%" (
	echo>>"..\sdk_errors.log" [%date% %time%] HlmvShell error: Can't get ModDir for "%~1".
)

:HookVProject
if not defined VProject (call :SearchBaseDir)
if not exist "%VProject%\materials\" (call :SearchBaseDir)
set "GameDir=%VProject%"

:RunProgram
start "" %HLMV% "%~1"
exit

:SearchBaseDir
pushd ..
if exist "SdkContent\VpkContent\materials\" (
	set "VProject=%cd%\SdkContent\VpkContent") else (
	set "VProject=%ModDir%"
)
popd
exit /b