@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
set "ProgVersion=0.9-beta"
title Dupe Finder ^& Deleter  (c) Psycho-A
color 16

echo ีออออออออออออออออออออออออออออออออธ
echo ณ MOD'S DUPLICATE FILES FINDER   ณ
echo ณ Version: %ProgVersion% (c) Psycho-A ณ
echo ิออออออออออออออออออออออออออออออออพ
echo.

:==============================================================================
:SetBasePaths

pushd "%~dp0"
set "DFHome=%cd%"
set "WhiteListPack=%cd%\service\WhiteList-packs.7z"
set "WhiteListDirs=WhiteList-v1.0-Dirs.lst"
set "WhiteListVpks=WhiteList-v1.0-Vpks.lst"

:SetPrograms
pushd ..\..
set Sfk="%cd%\helpers\sfk.exe"
set Arc="%cd%\helpers\7za.exe"
set Msg="%cd%\helpers\msgbox.exe"
set Sha="%~dp0service\sha1.exe"

set "SourceDir=Vampire"
set "TargetDir=ModDir"
set "TgDirName=ModDir"

:SetConfig
set "ExcludeExts=.ain"
set "ProcWhiteList=Yes"
set "ProcDirTree=No"


:==============================================================================
:DetectPath

if exist "GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
	if /i "%%~a"=="ModDir" (
		set "TargetDir=%%~b"
		set "TgDirName=%%~nb"
	)
))
pushd ..

:CheckAssets
for %%m in (%Sfk% %Msg% %Arc% %Sha%) do (
if not exist "%%~m" (
	%Sfk% echo "[Red]  "Required file not found:
	%Sfk% echo "[Red]  ""%%~m"
	goto Finish
))

:CheckDirs
if not exist "%SourceDir%" (
if /i "%ProcDirTree%"=="Yes" (
	%Sfk% echo "[Red]  "Source dir not found: \"%SourceDir%\"
	%Sfk% echo "[Red]  "Please, specify another one by setting right project in the SDK.
	goto Finish
))
if not exist "%TargetDir%" (
	%Sfk% echo "[Red]  "Target dir not found: \"%TargetDir%\"
	%Sfk% echo "[Red]  "Please, specify another one by setting right project in the SDK.
	goto Finish
)
call :DelTemps

echo   Vampire directory:  "%SourceDir%"
echo   User mod directory: "%TgDirName%"
echo.
echo   This tool allows you to easy detect duplicated content
echo   in your patch or mod comparing to the original (v1.0)
echo   game's one and automatically delete it if you want it.
echo.
echo   Hit any key to start...
pause> nul

cls
echo.
echo   Please, wait...

if /i "%ProcDirTree%"=="No" (
goto ParseWhitelist)

:DumpFileTree
echo.
echo   Processing file tree...
dir /b /s /a-d "%TargetDir%"> "%DFHome%\TargetDir.lst"
%Sfk% replace "%DFHome%\TargetDir.lst" "|%TargetDir%\||" -quiet -yes> nul

:ParseFileTree
for /f "usebackq delims=" %%a in ("%DFHome%\TargetDir.lst") do (
	if exist "%SourceDir%\%%~a" (call :CompareDT "%%~a")
)

:ParseWhitelist
if /i "%ProcWhiteList%"=="No" (
goto CheckIfFound)

%Arc% x "%WhiteListPack%" -o"%DFHome%" -aoa -y "%WhiteListDirs%"> nul
if exist "%DFHome%\%WhiteListDirs%" (
	echo   Processing whitelist for directory tree...
	if /i not "%SourceDir%"=="%TgDirName%" (
		for /f "eol=# usebackq delims=	| tokens=1,2" %%a in ("%DFHome%\%WhiteListDirs%") do (
		if exist "%TargetDir%\%%~a" (call :CompareWL "%%~a" "%%~b"))
		del /f /q /a "%DFHome%\%WhiteListDirs%"> nul
	) else (
		%Sfk% echo "[cyan]    "Source directory equals target directory:
		%Sfk% echo "[cyan]    "[\"%SourceDir%\" = \"%TgDirName%\"]. Scanning denied.
	)
)
%Arc% x "%WhiteListPack%" -o"%DFHome%" -aoa -y "%WhiteListVpks%"> nul
if exist "%DFHome%\%WhiteListVpks%" (
	echo   Processing whitelist for packed content...
	for /f "eol=# usebackq delims=	| tokens=1,2" %%a in ("%DFHome%\%WhiteListVpks%") do (
	if exist "%TargetDir%\%%~a" (call :CompareWL "%%~a" "%%~b"))
	del /f /q /a "%DFHome%\%WhiteListVpks%"> nul
)

:CheckIfFound
if not exist "%DFHome%\ToDelete.lst" (
	echo.
	%Sfk% echo "[Yellow]  "Duplicated files not found in specified dirs.
	goto Finish
)

:AskForDelete
echo.
echo   Scanning complete. You can see the duplicated files above.
echo   Do you want to erase them from the target directory (Y/N)?
echo.

:AskRepeat
set Answer=
set /p "Answer=> "

if /i "%Answer%"=="N" (goto Finish) else (
if /i "%Answer%"=="Y" (goto Delete) else (
goto AskRepeat))

:Delete
cls
echo.
echo   Deleting files...
for /f "usebackq delims=" %%a in ("%DFHome%\ToDelete.lst") do (
	call :DelDupes "%%~a"
)
pushd "%TargetDir%"
call :RemEmptyDirs "%CD%"
popd

:Finish
call :DelTemps
echo.
echo   Hit any key to exit...
pause> nul
pause> nul
exit

:CompareDT
set SSize=& set SSha1=& set TSize=& set TSha1=
for %%s in ("%SourceDir%\%~1") do (set "SSize=%%~zs"
for /f %%c in ('call %Sha% "%%~s"') do (set "SSha1=%%~c"))
for %%s in ("%TargetDir%\%~1") do (set "TSize=%%~zs"
for /f %%c in ('call %Sha% "%%~s"') do (set "TSha1=%%~c"))

if "%SSize%:%SSha1%"=="%TSize%:%TSha1%" (
	for %%x in (%ExcludeExts%) do (
	if /i "%~x1"=="%%~x" (exit /b) )
	%Sfk% echo "[cyan]    "Duplicate: \"%~1\"
	echo "%~1">> "%DFHome%\ToDelete.lst"
)
exit /b

:CompareWL
set TSize=& set TSha1=
for %%s in ("%TargetDir%\%~1") do (set "TSize=%%~zs"
for /f %%c in ('call %Sha% "%%~s"') do (set "TSha1=%%~c"))

if "%TSize%:%TSha1%"=="%~2" (
	for %%x in (%ExcludeExts%) do (
	if /i "%~x1"=="%%~x" (exit /b) )
	%Sfk% echo "[cyan]    "Duplicate: \"%~1\"
	echo "%~1">> "%DFHome%\ToDelete.lst"
)
exit /b

:DelTemps
for %%m in ("%DFHome%\*.lst") do (
del /f /q /a "%%~m"> nul )
exit /b

:DelDupes
del /f /q /a "%TargetDir%\%~1"> nul
%Sfk% echo "[cyan]    Deleted: '%~1'."
exit /b

:RemEmptyDirs2
set Fils=& set Dirs=
for %%m in ("%~1\*") do (set Fils=1)
for /d %%m in ("%~1\*") do (set Dirs=1)
if "%Fils%%Dirs%"=="" (
	%Sfk% echo "[cyan]    Deleted: '%~1'." +filter -rep "|%cd%\||"
	rd /s /q "%~1"> nul
)
exit /b

:RemEmptyDirs
	for /D %%A in ("%~1\*") do (
	 call :RemEmptyDirs "%%~fA")
	rd "%~f1"> nul 2>&1
	if not exist "%~1\" (
	%Sfk% echo "[cyan]    Deleted: '%~1'." +filter -rep "|%cd%\||")
exit /b
