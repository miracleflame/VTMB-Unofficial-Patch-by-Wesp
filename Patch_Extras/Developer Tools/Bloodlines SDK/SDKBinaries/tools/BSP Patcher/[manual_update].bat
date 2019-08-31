@echo off
setlocal enableextensions
title BSP Zipped Content Updater  (c) Psycho-A
color 27

if "%~1"=="" (
	echo 様様様様
	echo   Usage: 
	echo 様様様様
	echo.
	echo   [1] Move all batch files into the game's "maps\" dir.
	echo.
	echo   [2] Create dir named "%%mapname%%_patch" with assets to be included.
	echo       If you used "map_extract" script before, it will auto-generated.
	echo.
	echo   [3] After that you may edit or add something inside this folder.
	echo       Folders structure inside it must follow game's folder structure.
	echo.
	echo   [4] Drag and drop your map .bsp file to this batch to update a map.
	echo.
	echo.
	echo 様様様様様様様様様様様様様様様様様様様様様様様様様様様様
	echo   Bloodlines SDK must be installed to perform something!
	echo 様様様様様様様様様様様様様様様様様様様様様様様様様様様様
	pause> nul
	exit
)

:SetAppFiles
pushd "%~dp0"
pushd "..\..\SDKBinaries\"
set "BSPZip=%CD%\bspzip.exe"
set "Sfk=%CD%\helpers\sfk.exe"
popd

:SetMapFile
set "MapFile=%~1"
set "MapName=%~n1"

:CheckFiles
if not exist "%BSPZip%" (
	echo ERROR: File "%BSPZip%" not found!
	pause& exit
)
if not exist "%MapName%_patch\*" (
	echo ERROR: Assets "%MapName%_patch\" not found!
	pause& exit
)

:Prepare
pushd "%MapName%_patch\"
echo MAP: "%MapName%"

:MakeBackup
if not exist "%MapFile%.bak" (
copy /y "%MapFile%" "%MapFile%.bak"> nul)

:PackFiles
for /d %%m in (*) do (
	call :RecurseDirs "%%~m"
)
echo.
popd

:UpdateGraph
if exist "graphs\%MapName%.ain" (
	"%Sfk%" touch "graphs\%MapName%.ain"
)


:Finalize
echo Finished.
if "%~2"=="-int" (
	cls & exit /b
)
pause> nul
exit

:RecurseDirs
for /d %%d in ("%~1\*") do (
	for %%f in ("%%~d\*") do (call :PackToBsp "%%~f")
	call :RecurseDirs "%%~d"
)
exit /b

:PackToBsp
	set "CurFile=%~1"
	echo      Adding: "%CurFile:\=/%"
	"%BSPZip%" -addfile "%MapFile%" "%CurFile:\=/%" "%CurFile%" "%MapFile%"
exit /b
