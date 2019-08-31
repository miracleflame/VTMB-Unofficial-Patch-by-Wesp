@echo off
title Reset SDK Configuration
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
pushd "%~dp0\.."

set "MsgBox=helpers\msgbox.exe"

:checkfiles
for %%m in (helpers\msgbox.exe sdklauncher.bat) do (
if not exist "%%~m" (
	echo>>"..\sdk_errors.log" [%date% %time%] Internal error: Missing "%cd%\%%~m" file.
	exit
))

:ask_user
%MsgBox% Bloodlines SDK will be reset to the initial state and all user configurations (except content) will be deleted. Are you sure you want to continue? /c:Important Info /t:MB_YESNO,MB_ICONWARNING
if "%ErrorLevel%"=="7" exit

:makereset
taskkill /f /im "sdklauncher.exe"> nul
if exist "GameCfg.ini" del /a /q "GameCfg.ini"> nul
call "sdklauncher.bat" -int
exit