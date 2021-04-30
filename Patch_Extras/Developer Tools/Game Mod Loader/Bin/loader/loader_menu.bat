@echo off
title Bloodlines Mods launcher  (c) Psycho-A
setlocal EnableExtensions
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
color 47
pushd "%~dp0"
set ModDir=
set IsCP866=

:: Parse command line
if /i "%~1"=="-game" (
if not "%~2"=="" (
	set "ModDir=%~nx2"
	goto launch_game
))

:: Localize screen messages
for /f %%s in ('chcp ^| find /c "866"') do (set "IsCP866=%%~s")
if "%IsCP866%"=="1" (call :MakeRussian) else (call :MakeEnglish)

:: Scan game's mods entries
echo Scanning game directories...
echo – %ModName.Vampire%   [Vampire]> "%~n0.ini"
rem scan the rest of subdirs
for /d %%m in (..\..\*) do (
if /i not "%%~nxm"=="Vampire" (
	call :ParseModDir "%%~m"
))
rem add sdk toolkit if found
if exist "..\..\Bloodlines SDK.exe" (
echo – %ModName.BloodlinesSDK%   [Bloodlines SDK]>> "%~n0.ini")

:: Start launcher with obtained mod list
for %%s in ("%~n0.ini") do (
if /i %%~zs GTR 48 (for /f "delims=[] tokens=2" %%g in (
'%~n0.exe "%~n0.ini" "%WSelect.Title%" $item "%WSelect.Header%" /menu /fs^=15 /bg^=#413526 /hc^=#B1A762 /fc^=#D8DED3 /ontop'
) do (set "ModDir=%%~g") ) else (set "ModDir=Vampire") )

:launch_game
if not defined ModDir (exit)
echo Selected mod dir: "%ModDir%"

:: Fix various game issues
echo Fixing system libs conflicts...
for %%r in ("%windir%" "%windir%\system32" "%windir%\syswow64") do (
for %%f in ("engine.dll" "binkw32.dll" "mss32.dll" "mss32a.dll" "zlib1.dll") do (
	if exist "%%~r\%%~f" (move /y "%%~r\%%~f" "%%~r\%%~f.bak"> nul)
))
echo Fixing language issues...
for %%p in (1251 1252) do (if exist "c_%%p.nls" (
if not exist "%windir%\system32\c_%%p.nls" (
	copy /y "c_%%p.nls" "%windir%\system32\"> nul
)))
pushd "..\..\"
if exist "%ModDir%\fonts\fontinst.exe" (
	echo Installing mod-specific fonts...
	call "%ModDir%\fonts\fontinst.exe"> nul
)

:: Run game with given options
echo Starting game with selected mod...
set "VProject=%Cd%\%ModDir%"
set "__COMPAT_LAYER=DisableThemes"
if exist *.log del /f /q *.log > nul
if /i "%ModDir%"=="Bloodlines SDK" (
start "" "Bloodlines SDK.exe" & exit)
if /i "%~1"=="-game" set "ModDir=Vampire"
if /i "%ModDir%"=="Vampire"     start /high Vampire.exe %*
if /i not "%ModDir%"=="Vampire" start /high Vampire.exe -game %ModDir% %*
exit


:: Service functions
:MakeEnglish
chcp 1250> nul
	set "WSelect.Title=Vampire: The Masquerade - Bloodlines Mod Launcher"
	set "WSelect.Header=Choose game or mod to run:"
	set "ModName.Vampire=Vanilla Game"
	set "ModName.Russian_Fans=Russian Fan's Translation v1.2"
	set "ModName.Russian_Pirate=Russian Pirate's Translation v1.2"
	set "ModName.Unofficial_Patch=Unofficial Patch"
	set "ModName.BloodlinesSDK=Modding Tools"
exit /b

:MakeRussian
chcp 1251> nul
	set "WSelect.Title=Vampire: Bloodlines – Запуск модов"
	set "WSelect.Header=Выберите версию или мод для запуска:"
	set "ModName.Vampire=Оригинальная игра без патчей"
	set "ModName.Russian_Fans=Фанатская русификация для v1.2"
	set "ModName.Russian_Pirate=Пиратская русификация для v1.2"
	set "ModName.Unofficial_Patch=Неофициальный патч"
	set "ModName.BloodlinesSDK=Инструменты для моддинга"
exit /b

:ParseModDir
	rem Check for main assets...
	if not exist "%~1\cfg\*" (
	if not exist "%~1\dlls\*" (
	if not exist "%~1\materials\" (
	if not exist "%~1\models\" (
	if not exist "%~1\python\" (
	if not exist "%~1\scripts\liblist.gam" (
	if not exist "%~1\pack???.vpk" (
		rem Not a mod, skip it
		exit /b
	)))))))

	rem Here goes aliasing names for dirs and filling modlist menu...
	if /i "%~nx1"=="Antitribu"            (set "ModName=Antitribu Mod") else (
	if /i "%~nx1"=="Antitribu_Mod"        (set "ModName=Antitribu Mod") else (
	if /i "%~nx1"=="Bloodlines_Prelude_I" (set "ModName=Bloodlines Prelude I") else (
	if /i "%~nx1"=="Bloodlines_Prelude_II" (set "ModName=Bloodlines Prelude II") else (
	if /i "%~nx1"=="Bloodlines_Prelude_III" (set "ModName=Bloodlines Prelude III") else (
	if /i "%~nx1"=="CE"                   (set "ModName=Camarilla Edition") else (
	if /i "%~nx1"=="CEfinal"              (set "ModName=Camarilla Edition, Final") else (
	if /i "%~nx1"=="Companion_Mod"        (set "ModName=Companion Mod") else (
	if /i "%~nx1"=="CQM"                  (set "ModName=Clan Quest Mod") else (
	if /i "%~nx1"=="Russian_Fans"         (set "ModName=%ModName.Russian_Fans%") else (
	if /i "%~nx1"=="Russian_Pirate"       (set "ModName=%ModName.Russian_Pirate%") else (
	if /i "%~nx1"=="TFN"                  (set "ModName=The Final Nights") else (
	if /i "%~nx1"=="True_Patch"           (set "ModName=True Patch") else (
	if /i "%~nx1"=="TPG"                  (set "ModName=True Patch GOLD") else (
	if /i "%~nx1"=="Unofficial_Patch"     (set "ModName=%ModName.Unofficial_Patch%") else (
	if /i "%~nx1"=="War_Games"            (set "ModName=War Games") else (
		rem If nothing found, use folder name as mod name
		set "ModName=%~nx1"
	))))))))))))))))

	rem Make name cmd-friendly...
	set "ModName=%ModName:_= %"
	set "ModName=%ModName:\=/%"
	set "ModName=%ModName:|=/%"
	set "ModName=%ModName:&=+%"
	set "ModName=%ModName:>=-%"
	set "ModName=%ModName:<=-%"
	set "ModName=%ModName:[=(%"
	set "ModName=%ModName:]=)%"

	rem Fill the modlist for main menu...
	echo – %ModName%   [%~nx1]>> "%~n0.ini"

	set ModName=
exit /b