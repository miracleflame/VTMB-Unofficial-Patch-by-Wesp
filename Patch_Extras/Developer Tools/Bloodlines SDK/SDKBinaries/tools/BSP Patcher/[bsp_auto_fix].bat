@echo off
setlocal enableextensions
title BSP Zipped Batch Vmt Fixer  (c) Psycho-A
color 8f

if "%~1"=="" (
	echo 様様様様
	echo   Usage: 
	echo 様様様様
	echo.
	echo   [1] Move all batch files into the game's "maps\" dir.
	echo.
	echo   [2] Drag and drop your map's .bsp file to this batch.
	echo.
	echo   [3] Wait until all update procedures will be finish.
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
set BSPZip="%CD%\bspzip.exe"
set UnZip="%CD%\service\7za.exe"
set Sfk="%CD%\service\sfk.exe"
popd

:CheckFiles
for %%m in (%BSPZip% %UnZip% %Sfk%) do (
	if not exist "%%~m" (
		echo ERROR: File "%%~m" not found!
		echo Please install Bloodlines SDK to suggested location!
		echo.
		pause& exit
	)
)
for %%m in (
	manual_extract
	manual_fixvmts
	manual_update
) do (
	if not exist "[%%~m].bat" (
		echo ERROR: File "%%~m.bat" not found!
		echo Please install Bloodlines SDK to suggested location!
		echo.
		pause& exit
	)
)

:SetMapFile
set "MapFile=%~1"
set "MapName=%~n1"



:RunScripts
call "[manual_extract].bat" "%~1" -int
call "[manual_fixvmts].bat" "%~1" -int
call "[manual_update].bat"  "%~1" -int

:ClearUnzipped
if exist "%MapName%_patch\" (
	rd /s /q "%MapName%_patch"
)

:Finish
color 8f
title BSP Zipped Batch Vmt Fixer  (c) Psycho-A
echo.
echo    Finished.
ping>nul 127.0.0.1 -n 3
exit