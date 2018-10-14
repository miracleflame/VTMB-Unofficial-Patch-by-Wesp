@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title Launcher for apps with long path trouble  (c) Psycho-A
pushd "%~dp0"

:set_vars
set "AppFile=Sheet_Tool.exe"
set "Program=%cd%\%AppFile%"
set "Readme=%cd%\Readme.exe"
set "Delete="
set "RunKey="

:check_files
if not exist "%Program%" (
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] Program error: App file "%Program%" not found!
	exit
)
if exist "..\..\service\sfk.exe" (
	set sfk="..\..\service\sfk.exe") else (
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] %AppFile:.exe=% error: Missing "%cd%\..\..\service\sfk.exe" file.
	goto run_program
)

:fix_issue
for /f %%a in ('call %sfk% strlen "%Program%"') do if %%~a GTR 126 (
	copy /y "%Program%" "%~d0\"> nul
	set "Program=%~d0\%AppFile%"
	set "Delete=1"
	set "RunKey=/w"
)

:show_readme
start /b "" "%Readme%" "This is a tool to set a model animation as the character sheet animation.\n\nHow to use: \n------------- \nDrag the mdl from which to use the animation to the first slot or browse for \nit. Select PC models only! Try using Brujah or Malkavian female or Tremere \nmale, most other PCs won't transfer nicely (bones and weights problems).\n\nDrag the target mdl to receive the animation to the second slot or browse \nfor it. It can be a PC or NPC model (for PCs other animations may deform \nthe result so best use NPC). Then click \"Do it\" or check options first. \n\nDon't check anything for male to male or female to female models. If you see \nsome deformation you could try using the <bip0 and pelvis only> setting. \nOr do so for special transfers like e. g. male gangrel to female gangrel mdl. \n\nFor most of the NPC models it is the ACT_RAGDOLL dying animation that is \nchanged. I dont see any problem with that as vampires get a burning death. \n\nAnd I know one model that will need a hexedit for the animation to work. \nMaybe they are more, but most models should work fine using this tool." "Character Sheet Animation Injector  (c) DDLullu" OK

:run_program
start %RunKey% "" "%Program%"
if "%Delete%"=="1" (
del /f /q /a "%Program%"> nul)
exit
