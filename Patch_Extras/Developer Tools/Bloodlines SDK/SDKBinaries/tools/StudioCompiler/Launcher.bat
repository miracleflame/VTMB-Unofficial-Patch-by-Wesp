@echo off
title StudioCompiler :: SDK mode
setlocal EnableExtensions
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"

set "SMCHome=%~dp0"
set "SMCRegPath=HKCU\Software\CFApps\StudioCompiler"

pushd "%~dp0\..\..\.."
if not exist "SDKContent\ModelSrc\" md "SDKContent\ModelSrc"
if not exist "SDKContent\MaterialSrc\" md "SDKContent\MaterialSrc"
if not defined ModDir  set "ModDir=%CD%\Vampire"
if not defined GameDir set "GameDir=%CD%\SDKContent\VpkContent"

if exist "SDKBinaries\GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("SDKBinaries\GameCfg.ini") do (
	if /i "%%~a"=="ModDir" (if exist "%%~b\*" (set "%%~a=%%~b") )
	if /i "%%~a"=="GameDir" (if exist "%%~b\*" (set "%%~a=%%~b") )
))
set "VProject=%GameDir%"

:fix_regpaths
reg add "%SMCRegPath%\StudioCompiler" /v "TabSelect"       /t REG_DWORD /d "0" /f
reg add "%SMCRegPath%\StudioCompiler" /v "SDKDirectory"    /t REG_SZ /d "%CD%\SdkBinaries" /f
reg add "%SMCRegPath%\StudioCompiler" /v "GameDirectory"   /t REG_SZ /d "%ModDir%" /f
reg add "%SMCRegPath%\StudioCompiler" /v "Shader"          /t REG_SZ /d "VertexLitGeneric" /f

:copy_reqfiles
for %%m in ("%SMCHome%\CopyFiles\*") do (
if not exist "SDKBinaries\%%~nxm" (
	copy /y "%%~m" "SDKBinaries\%%~nxm"> nul
))

:run_program
start "smc" "%SMCHome%\StudioCompiler.exe"
exit
