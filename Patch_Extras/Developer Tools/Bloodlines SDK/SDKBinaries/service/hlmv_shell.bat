@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title Bloodlines Model Viewer Command Line
pushd "%~dp0.."

:Check
set "HLMV=%cd%\hlmv.exe"
for %%m in ("hlmv.exe" "service\sfk.exe") do if not exist "%%~m" (
	echo>>"..\sdk_errors.log" [%date% %time%] HlmvShell error: Missing "%cd%\%%~m" file.
	exit
)

:RegFiles
if "%~1"=="" (
	echo Registering file association...
	REG ADD "HKCU\Software\Classes\.mdl" /f /ve  /t REG_SZ /d "MDLFile"
	REG ADD "HKCU\Software\Classes\MDLFile" /f /ve  /t REG_SZ /d "Vampire Model File"
	REG ADD "HKCU\Software\Classes\MDLFile\shell" /f /ve /t REG_SZ /d "View"
	REG ADD "HKCU\Software\Classes\MDLFile\shell\View\command" /f /ve /t REG_SZ /d "%cd%\service\hlmv_shell.exe \"%%1\""
	REG ADD "HKCU\Software\Classes\MDLFile\DefaultIcon" /f /ve /t REG_SZ /d "%cd%\service\hlmv_shell.exe,0"
	exit
)

:StripPath
for /f "delims=" %%a in ('service\sfk.exe echo "%~1" +filter -rep "|??*\models\|models\|"') do (set "FilePath=%%~a")
for /f "delims=" %%a in ('service\sfk.exe echo "%~1" +filter -rep "|\models\??*||"') do (set "ModDir=%%~a")
if not exist "%ModDir%\%FilePath%" (
echo>>"..\sdk_errors.log" [%date% %time%] HlmvShell error: Can't parse: "%ModDir%\%FilePath%".
exit)

:HookVProject
set "GameDir=%VProject%"
if not defined VProject (
	call :SearchBaseDir)
if not exist "%VProject%\materials\" (
	call :SearchBaseDir)

:RunProgram
pushd "%ModDir%"
start "" "%HLMV%" "%FilePath%"
exit

:SearchBaseDir
pushd ..
if exist "SdkContent\VpkContent\materials\" (
	set "VProject=%cd%\SdkContent\VpkContent"
	set "GameDir=%cd%\SdkContent\VpkContent"
	exit /b)
set "VProject=%ModDir%"
set "GameDir=%ModDir%"
exit /b
