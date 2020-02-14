@echo off
title Launcher for DDLullu's command line apps  (c) Psycho-A
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
pushd "%~dp0"

:set_vars
set "AppFile=No_more_LOD.exe"
set "Program=%cd%\%AppFile%"
set "MsgBox=%cd%\Show_message.exe"
set "OpenDlg=..\..\helpers\opendlg.exe"

:check_files
for %%m in ("%Program%" "%MsgBox%" "%OpenDlg%") do (if not exist "%%~m" (
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] Program error: Required file "%%~m" not found!
	exit
))

:show_readme
start /b "" "%MsgBox%" "This tool will disable the LODs of the models in the Bloodlines\r\ncharacter sheet making them less blocky. Just select MDL files\r\nwith .dx80 and .dx7 VTX data in the window and it will be done..." "Bloodlines no more LOD tool  (c) DDLullu" OK

:run_program
set ProgramWorked=
for /f "delims=" %%f in ('%OpenDlg% /f /m "/e=*.mdl *.vtx"') do (
for %%v in ("%%~dpnf.dx80.vtx" "%%~dpnf.dx7_2bone.vtx") do (
if exist "%%~v" (
	call "%Program%" "%%~v"
	set "ProgramWorked=True"
)))

:finalize
taskkill /f /im "Show_message.exe"> nul 2>&1
if defined ProgramWorked (
start /b "" "%MsgBox%" "Operation finished. LODs must be disabled." "Bloodlines no more LOD tool  (c) DDLullu" OK)
exit