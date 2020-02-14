@echo off
@color 61
set ProgVersion=1.6-beta
set WinTitle=TTZ Viewer v%ProgVersion%  (c) Psycho-A

title %WinTitle%
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
pushd "%~dp0"

:Vars
set MsgBox=..\..\helpers\msgbox.exe
set OpenDlg=..\..\helpers\OpenDlg.exe
set TtzDecomp="service\TtzDecomp.exe"
set FileTypes="service\filetypes.bat"
set OpenFile=call "%OpenDlg%" /f
set "TempDir=%WinDir%\Temp\texutils"

:CheckFiles
for %%m in (%MsgBox% %OpenDlg% %TtzDecomp% %FileTypes%) do (
if not exist "%%~m" (
	color 6e
	echo Cant find "%%~m"!
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] TTZView Error: Missing "%cd%\%%~m" file.
	ping>nul "127.0.0.1" -n 2
	exit
))

if "%~x1"=="" (
start /b "" %FileTypes% -ext
) else (set "ShellMode=1")



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

if defined InFile (
	call :ViewScript "%InFile%"
	if "%ShellMode%"=="1" exit
	goto ShowLogo
) else (
	exit
)



:ViewScript
set TTZFix=
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
%TtzDecomp% "%~dpn1.ttz"> nul
if defined TTZFix (
	del /q /a "%~dpn1.ttz"> nul
)

:checkconv
if exist "%~dpn1.vtt" (
	if not exist "%TempDir%\" md "%TempDir%"
	move /y "%~dpn1.vtt" "%TempDir%\%~n1.vtf"> nul
) else (
	start %MsgBox% Error opening file. /c:Error /t:MB_ICONERROR
	exit
)

:view
	VTFEdit.exe "%TempDir%\%~n1.vtf"
	del /f /q "%TempDir%\%~n1.vtf"> nul
exit /b
