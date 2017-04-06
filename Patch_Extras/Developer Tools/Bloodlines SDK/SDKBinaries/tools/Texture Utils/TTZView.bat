@echo off
set ProgVersion=1.4-beta

setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title TTZ Viewer v%ProgVersion%  (c) Psycho-A
pushd "%~dp0"
color 61

:Vars
set "MsgBox=..\..\service\msgbox.exe"
set "OpenDlg=..\..\service\OpenDlg.exe"
set "FileTypes=service\filetypes.bat"
set "OpenFile=call %OpenDlg% /f"
set "TempDir=%cd%\temp"

:CheckFiles
for %%m in (
"%MsgBox%" "%OpenDlg%" "%FileTypes%"
) do if not exist "%%~m" (
	color 6e
	echo Cant find "%%~m"!
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] TTZView Error: Missing "%cd%\%%~m" file.
	ping>nul "127.0.0.1" -n 2
	exit
)

if "%~x1"=="" (
call "%FileTypes%" -int) else (
set "ShellMode=1")

:ShowLogo
cls
echo ีออออออออออออออออออออออออออออออออธ
echo ณ TTH/TTZ TEXTURE VIEWER         ณ
echo ณ Version: %ProgVersion% (c) Psycho-A ณ
echo ิออออออออออออออออออออออออออออออออพ
echo.

:check
set InFile=
if "%~x1"=="" (
	echo  Tip:
	echo   To quick view TTh or TTz files, double
	echo   click on them in the Windows Explorer.
	echo.
	echo   [Bloodlines SDK should be installed.]
	for /f "delims=" %%f in ('%OpenFile% "/e=*.tth *.ttz"') do (set "InFile=%%~f")
) else (set "InFile=%~1")

if not "%InFile%"=="" (
call :ViewScript "%InFile%"
if "%ShellMode%"=="1" exit
goto ShowLogo
) else (exit)

:ViewScript
if not exist "%~dpn1.tth" (
	start %MsgBox% Missing header "%~n1.tth". Unable to open. /c:Error /t:MB_ICONERROR
	exit
)

if not exist "%~dpn1.ttz" (
	cd.> "%~dpn1.ttz"
	attrib +H "%~dpn1.ttz"
	set TTZFix=1
)

:convert
"service\TtzDecomp.exe" "%~dpn1.ttz"> nul
if "%TTZFix%"=="1" del /q /a "%~dpn1.ttz"> nul

:check2
if not exist "%~dpn1.vtt" (
	start %MsgBox% Error opening file. /c:Error /t:MB_ICONERROR
	exit
) else (
	if not exist "%TempDir%\" md "%TempDir%"
	move /y "%~dpn1.vtt" "%TempDir%\%~n1.vtf"> nul
)

:view
	VTFEdit.exe "%TempDir%\%~n1.vtf"
	rd /s /q "%TempDir%"> nul
exit /b
