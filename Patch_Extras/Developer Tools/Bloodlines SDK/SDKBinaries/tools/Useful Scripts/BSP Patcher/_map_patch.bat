@echo off
title BSP Patcher/Zipper  (c) Psycho-A

if "%~1"=="" (
	echo Usage: 
	echo  1. Move this batch into the game's "maps\" dir.
	echo  2. Create dir named "%%mapname%%_patch" with assets to be included.
	echo  3. Drag and drop your map .bsp file to this batch.
	echo.
	echo Bloodlines SDK must be installed to perform something!
	pause> nul
	exit
)

:SetAppFile
pushd "%~dp0"
pushd "..\..\SDKBinaries\"
set "BSPZip=%CD%\bspzip.exe"
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
for /d %%m in (*) do call :RecurseDirs "%%~m"
echo.
popd

:Finalize
echo Finished.
pause> nul
exit

:RecurseDirs
for /d %%d in ("%~1\*") do (
	for %%f in ("%%~d\*") do call :PackToBsp "%%~f"
	call :RecurseDirs "%%~d"
)
exit /b

:PackToBsp
	set "CurFile=%~1"
	echo   Adding: "%CurFile:\=/%"
	"%BSPZip%" -addfile "%MapFile%" "%CurFile:\=/%" "%CurFile%" "%MapFile%"
exit /b
