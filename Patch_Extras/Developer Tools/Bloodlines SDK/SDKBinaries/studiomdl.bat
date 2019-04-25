@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title StudioMDL compiler :: SDK mode
if "%~1"=="" (
	studiomdl.exe
	pause> nul
	exit
)
chcp 850> nul

:DefVars
pushd "%~dp0.."
if not defined ModDir (
set "ModDir=%cd%\vampire")
pushd "%~dp0"

if exist "GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
	if /i "%%~a"=="ModDir" (if exist "%%~b\*" (set "%%~a=%%~b") )
))

:ProcQcPath
for %%m in (%*) do (
if /i "%%~xm"==".qc" (
set "QCFile=%%~m") )

for /f "usebackq eol=/ tokens=1,*" %%a in ("%QCFile%") do (
if /i "%%~a"=="$modelname" if not "%%~b"=="" (
	for %%m in ("%ModDir%\models\%%~b") do (
		if /i "%%~xb"==".mdl" (
			set "MdlFile=models/%%~b!") else (
			set "MdlFile=models/%%~b.mdl!"
		)
		if not exist "%%~dpm" md "%%~dpm"> nul
	)
))

:ParseCmdline
set CmdLine=%*
rem Fix StudioCompiler input...
if /i "%~1"=="-game" set CmdLine=%4 %5 %6 %7 %8 %9 %3
if /i "%~1"=="-cdir" set CmdLine=%4 %5 %6 %7 %8 %9 %3

:ShowRoundup
set "MdlFile=%MdlFile:/=\%"
set "MdlFile=%MdlFile:.mdl!=%"
echo ---------------------
echo Project-Dir: "%ModDir%"
echo Target-MDL: "%MdlFile%.mdl"
echo ---------------------

:ClearOldFiles
if exist "%ModDir%\%MdlFile%.??*" (
del /f /q "%ModDir%\%MdlFile%.??*")> nul

:ShowAlphaWarnings
echo Warning: Collision data is currently not supported!
echo Warning: Animations are currently not supported!
echo Warning: Only less than ~10000 polys models allowed!
echo.
if not exist "service\mdlwarn.ini" goto RunCompiler
service\msgbox.exe Please note: The model compiler currently has no normal processing physics data (collision meshes), and they may cause game to crash! To avoid this, please paste *any* compiled model into your maps only as "prop_dynamic" and collision turned Off ("Collisions: Not Solid" in the Hammer Editor, or "solid" "0" flag when pasting to an existing level using VPKTool), or simply as "prop_static" if you're using the Hammer Editor. To make such a model solid with characters and world, surround it with "func_detail" or "func_brush" brush volumes with "toolsinvisible" texture covered on. For prop_dynamic models you can also parent them to "func_physbox" brushes to give them fake physics (take and move). /c:Custom Models Warning! /t:MB_OK,MB_ICONWARNING
del /f /q "service\mdlwarn.ini"> nul

:RunCompiler
call studiomdl.exe -game "%ModDir%" %CmdLine%
echo. 

:CheckResult
echo ---------------------
if not exist "%ModDir%\%MdlFile%.mdl" (
	echo An error occurred during compiling!
	echo See StudioMDL log above for details.
) else (
	echo Compiling success.
)
echo ---------------------

:Quit
exit