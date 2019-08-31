@echo off
setlocal enableextensions
title BSP Zipped Vmts Fixer  (c) Psycho-A
color 17

if "%~1"=="" (
	echo 様様様様
	echo   Usage: 
	echo 様様様様
	echo.
	echo   [1] Move all batch files into the game's "maps\" dir.
	echo.
	echo   [2] Make sure the .bsp content is already extracted.
	echo.
	echo   [3] Drag and drop your map .bsp file to this batch.
	echo.
	echo   [4] Run "map_update" after that to update .bsp file.
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
set Sfk="%CD%\helpers\sfk.exe"
popd

:CheckFiles
if not exist "%Sfk%" (
	echo ERROR: File "%Sfk%" not found!
	pause& exit
)

:PerformUnpack
for /d %%m in (%*) do (
	call :FixVmts "%%~m"
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

:FixVmts
	set "MapFile=%~1"
	set "MapName=%~n1"
	echo MAP: "%MapName%.bsp"

	if not exist "%MapName%_patch\" (
		echo      Unable to find "%MapName%_patch\".
		echo      Map is probably not extracted yet.
		exit /b
	)
	if not exist "%MapName%_patch\materials\maps\%MapName%" (
		echo      Unable to find "%MapName%_patch\materials\maps\%MapName%\".
		echo      Nothing to fix.
		exit /b
	)

	pushd "%MapName%_patch\materials\maps\%MapName%\"
	for /r %%v in (*.vmt) do (
		set OringVmtName=
		set EnvMapFile=

		call :GetEnvMap "%%~v"
		call :FixVmtPath "%%~v"
		call :WriteNewVmt "%%~v"
	)

	popd
exit /b



:GetEnvMap
	rem Read .vmt file to get cubemap value...
	for /f "usebackq tokens=1,*" %%a in ("%~1") do (
		if "%%~b"=="" (
		if /i "%%~a"=="patch" (
			rem Exclude already patched...
			set EnvMapFile=
			exit /b
		))
		if not "%%~b"=="" (
		if /i "%%~a"=="$envmap" (
			set "EnvMapFile=%%~b"
		))
	)
exit /b

:FixVmtPath
	if not defined EnvMapFile exit /b
	set "VmtName=%~1"
	for %%m in ("c?*_?*_?*.tth") do (
		set "CubeName=%%~nm"
		call :FixPathFunc
	)
exit /b

:FixPathFunc
	set "CubeName=%CubeName:~1%"
	rem Get valid vmt name to append in patch...
	for /f "delims=" %%a in (
	'call %Sfk% echo -lit "%VmtName%" +filt -rep "|%Cd%\||" -lerep "|_%CubeName%.vmt||" -lerep "|.vmt||"'
	) do (
		set "VmtName=%%~a.vmt"
		set "OringVmtName=%%~a"
	)
exit /b

:WriteNewVmt
	if not defined OringVmtName exit /b
	if not defined EnvMapFile exit /b
	rem Write new vmt with inserted $envmap data...
	echo      Fixing %OringVmtName%...
	(echo "patch"
	 echo {
	 echo 	"include"		"%OringVmtName:\=/%"
	 echo 	"replace"
	 echo 	{
	 echo 		"$envmap"		"%EnvMapFile:\=/%"
	 echo 	}
	 echo }
	)> "%~1"
exit /b