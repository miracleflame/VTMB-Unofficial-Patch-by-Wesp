@echo off
title Launcher for apps with long path trouble  (c) Psycho-A
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
pushd "%~dp0"

:set_vars
set "AppFile=BSPDetail.exe"
set "Program=%cd%\%AppFile%"
set "Delete="
set "RunKey="

:check_files
if not exist "%Program%" (
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] Program error: App file "%Program%" not found!
	exit
)
if exist "..\..\helpers\sfk.exe" (
	set Sfk="..\..\helpers\sfk.exe") else (
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] %AppFile:.exe=% error: Missing "%cd%\..\..\helpers\sfk.exe" file.
	goto run_program
)

:fix_issue
for /f %%a in ('call %Sfk% strlen "%Program%"') do (
if %%~a GTR 126 (
	if not exist "%Temp%\" md "%Temp%"
	copy /y "%AppFile%" "%Temp%\"> nul
	set "Program=%Temp%\%AppFile%"
	set "Delete=1"
	set "RunKey=/w"
))

:run_program
start %RunKey% "" "%Program%"
if "%Delete%"=="1" (
del /f /q /a "%Program%"> nul)
exit
