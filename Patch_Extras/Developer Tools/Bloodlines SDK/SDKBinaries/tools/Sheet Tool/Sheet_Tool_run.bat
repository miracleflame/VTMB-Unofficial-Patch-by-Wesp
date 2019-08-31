@echo off
title Launcher for apps with long path trouble  (c) Psycho-A
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
pushd "%~dp0"

:set_vars
set "AppFile=Sheet_Tool.exe"
set "Program=%cd%\%AppFile%"
set "Readme=%cd%\Show_readme.exe"
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
	goto show_readme
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

:show_readme
start /b "" "%Readme%" "This is a tool to set a model animation as the character sheet animation.\r\n\nHow to use: \r\n------------- \r\nDrag the mdl from which to use the animation to the first slot or browse for it. Select PC models only! Try using Brujah or Malkavian female or Tremere male, most other PCs won't transfer nicely (bones and weights problems).\r\n\r\nDrag the target mdl to receive the animation to the second slot or browse for it. It can be a PC or NPC model (for PCs other animations may deform the result so best use NPC). Then click \042Do it\042 or check options first. \r\n\r\nDon't check anything for male to male or female to female models. If you see some deformation you could try using the <bip0 and pelvis only> setting. Or do so for special transfers like e. g. male gangrel to female gangrel mdl. \r\n\r\nFor most of the NPC models it is the ACT_RAGDOLL dying animation that is changed. I dont see any problem with that as vampires get a burning death. \r\n\r\nAnd I know one model that will need a hexedit for the animation to work. Maybe they are more, but most models should work fine using this tool." "Character Sheet Animation Injector  (c) DDLullu" OK

:run_program
start %RunKey% "" "%Program%"
if "%Delete%"=="1" (
del /f /q /a "%Program%"> nul)
exit
