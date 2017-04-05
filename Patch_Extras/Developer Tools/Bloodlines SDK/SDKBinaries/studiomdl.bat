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

:DefVars
pushd "%~dp0.."
if not defined ModDir (
set "ModDir=%cd%\vampire")
pushd "%~dp0"

if exist "GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
	if /i "%%~a"=="ModDir" (if exist "%%~b\*" (set "%%~a=%%~b"))
))

:ProcQcPath
for %%m in (%*) do (
if /i "%%~xm"==".qc" (
set "QCFile=%%~m"))

for /f "usebackq eol=/ tokens=1,*" %%a in ("%QCFile%") do (
	if /i "%%~a"=="$modelname" if not "%%~b"=="" (
		for %%m in ("%ModDir%\models\%%~b") do (
			set "MdlFile=models/%%~b"
			if not exist "%%~dpm" md "%%~dpm"> nul
		)
	)
)

:ShowRoundup
set "MdlFile=%MdlFile:/=\%"
echo ---------------------
echo Project Dir: "%ModDir%"
echo Target MDL: "%MdlFile%"
echo ---------------------

:RunCompiler
call studiomdl.exe -game "%ModDir%" %*
echo.

:CheckResult
echo ---------------------
if not exist "%ModDir%\%MdlFile%" (
	echo An error occurred during compiling!
	echo See StudioMDL log above for details.
) else (
	echo Compiling success.
)
echo ---------------------

:Quit
exit
