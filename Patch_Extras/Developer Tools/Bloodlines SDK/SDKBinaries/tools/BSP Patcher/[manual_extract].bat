@echo off
setlocal enableextensions
title BSP Zipped Content Extractor  (c) Psycho-A
color 47

if "%~1"=="" (
	echo 様様様様
	echo   Usage: 
	echo 様様様様
	echo.
	echo   [1] Move all batch files into the game's "maps\" dir.
	echo.
	echo   [2] Drag and drop your map .bsp file to this batch.
	echo       This will create dir "%%mapname%%_patch" near .bsp.
	echo       You can extract multiple .bsps for one time.
	echo.
	echo   [3] Edit or add something in this folder as you need.
	echo       For this you may also use "map_fixvmts" script...
	echo.
	echo   [4] Run "map_update" script after that to update map.
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
set "UnZip=%CD%\service\7za.exe"
popd

:CheckFiles
if not exist "%BSPZip%" (
	echo ERROR: File "%BSPZip%" not found!
	pause& exit
)
if not exist "%UnZip%" (
	echo ERROR: File "%UnZip%" not found!
	pause& exit
)

:PerformUnpack
for /d %%m in (%*) do (
	call :UnPackBsp "%%~m"
)
echo.
popd

:Finalize
echo Finished.
if "%~2"=="-int" (
	cls & exit /b
)
pause> nul
exit

:UnPackBsp
	set "MapFile=%~1"
	set "MapName=%~n1"
	echo MAP: "%MapName%.bsp"

	"%BSPZip%" -extract "%MapFile%" "%MapName%.zip"
	if exist "%MapName%.zip" (
		"%UnZip%" x "%MapName%.zip" -o"%MapName%_patch\" -y -aoa > nul
		del /f /q /a "%MapName%.zip" > nul
	) else (
		echo      Couldn't obtain "%MapName%.zip".
	)
	if not exist "%MapName%_patch\" (
		echo      Unable to extract "%MapName%.zip".
	)
exit /b
