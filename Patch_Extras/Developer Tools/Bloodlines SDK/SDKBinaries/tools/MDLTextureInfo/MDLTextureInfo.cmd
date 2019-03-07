:: written by: psycho-a
:: program version: 1.0
:: build date: 19.02.19

@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
set "ProgVersion=1.0"
title MDL Texture Info v%ProgVersion%  (c) Psycho-A
color 06
pushd "%~dp0"


:========================================================================================================
:: PREPARE
:========================================================================================================

set Sfk="%cd%\sfk193.exe"
set "ModDir=%~2"
set "InputMDL=%~1"

if not exist %Sfk% (
	color 0c
	cls
	echo.
	echo     ERROR: %Sfk% not found.
	echo.
	echo     Cannot proceed.
	echo.
	pause>nul
	exit
)



:========================================================================================================
:: SHOW USAGE NOTES
:========================================================================================================

if "%~1"=="" (
	rem Add context menu to registry...
	echo. 
	%Sfk% echo "  [green]Usage: [yellow]%~nx0 [cyan]\"path\file.mdl\""
	%Sfk% echo "  Or Drag and Drop MDL file to this batch..."
	echo.
	(REG ADD "HKCU\Software\Classes\.mdl" /f /ve /d "MDLFile"
	 REG ADD "HKCU\Software\Classes\MDLFile" /f /ve /d "3D Model file"
	 REG ADD "HKCU\Software\Classes\MDLFile\shell\TexInfo" /f /ve /d "Texture Information"
	 REG ADD "HKCU\Software\Classes\MDLFile\shell\TexInfo\command" /f /ve /d "%~0 \"%%1\""
	)> nul
	pause> nul
	exit
)

if not exist "%InputMDL%" exit /b
if not defined ModDir (
for /f "delims=" %%a in ('call %Sfk% echo "%~dp1|" +filt -rep "|\models\*||" -lerep "=\|=="') do (
	set "ModDir=%%~a"
))
if not exist "%ModDir%\materials\" set ModDir=



:========================================================================================================
:: READ MDL DATA
:========================================================================================================

%Sfk% echo [yellow]Reading MDL texture data...

rem read numtextures offset
for /f %%a in ('call %Sfk% hexdump -pure -offlen 292 2 -nofile "%InputMDL%"') do (
for /f %%b in ('call %Sfk% num "0x%%~a" -small -show decle') do set "NumTextures=%%~b" )

rem read texnames bank offset
for /f %%a in ('call %Sfk% hexdump -pure -offlen 296 4 -nofile "%InputMDL%"') do (
for /f %%b in ('call %Sfk% num "0x%%~a" -show decle') do set "TexNamesOffset=%%~b" )

rem read numtpaths offset
for /f %%a in ('call %Sfk% hexdump -pure -offlen 300 2 -nofile "%InputMDL%"') do (
for /f %%b in ('call %Sfk% num "0x%%~a" -small -show decle') do set "NumPaths=%%~b" )

rem read textpaths bank offset
for /f %%a in ('call %Sfk% hexdump -pure -offlen 304 4 -nofile "%InputMDL%"') do (
for /f %%b in ('call %Sfk% num "0x%%~a" -show decle') do set "TexPathsOffset=%%~b" )

%Sfk% echo "[cyan]> Textures paths: %NumPaths%"
%Sfk% echo "[cyan]> Textures count: %NumTextures%"
rem   echo "[blue]> Texpath offset: %TexPathsOffset%"
rem   echo "[blue]> Texname offset: %TexNamesOffset%"

rem read texpath positions
set "CurrStep=1"
set "CurrOffset=%TexPathsOffset%"
call :ReadTexPathOffset "%InputMDL%"

rem read texname positions
set "CurrStep=1"
set "CurrOffset=%TexNamesOffset%"
call :ReadTexNameOffset "%InputMDL%"



:========================================================================================================
:: CHECK IF TEXTURES EXIST
:========================================================================================================

set MissingTextures=
if defined ModDir (
if defined TexNameBank (
if defined TexPathBank (
	echo.
	%Sfk% echo [yellow]Checking textures in mod...
	for %%f in (%TexNameBank%) do (
		call :CheckFileExist "%%~f"
	)
)))
if defined ModDir (
if defined TexNameBank (
if defined TexPathBank (
if not defined MissingTextures (
	%Sfk% echo [blue]- everything is okay.
))))


:: FINISH
echo.
if /i not "%~3"=="-nopause" (
	pause
)
exit



:==============================================================================
:ReadTexPathOffset
	for /f %%a in ('call %Sfk% hexdump -pure -offlen %CurrOffset% 4 -nofile "%~1"') do (
	for /f %%b in ('call %Sfk% num "0x%%~a" -show decle') do set /a "TexPathPosition=%%~b")
	rem Texture path position: %TexPathPosition%

	rem Show texture name at position...
	call :ReadOffsetName "%~1" "%TexPathPosition%" "TexturePath"
	%Sfk% echo [green]- Path: "%TexturePath%"

	rem Collect texture paths...
	if not defined TexPathBank (
		set "TexPathBank=%TexturePath%"
	) else set "TexPathBank=%TexPathBank% %TexturePath%"

	set /a "CurrStep=%CurrStep%+1"
	set /a "CurrOffset=%CurrOffset%+4"
	if %CurrStep% LEQ %NumPaths% call :ReadTexPathOffset "%~1"
exit /b

:ReadTexNameOffset
	for /f %%a in ('call %Sfk% hexdump -pure -offlen %CurrOffset% 2 -nofile "%~1"') do (
	for /f %%b in ('call %Sfk% num "0x%%~a" -small -show decle') do set /a "TexNamePosition=%CurrOffset%+%%~b")
	rem Texture name position: %TexNamePosition%

	rem Show texture name at position...
	call :ReadOffsetName "%~1" "%TexNamePosition%" "TextureName"
	echo - Texture: "%TextureName%.vmt"

	rem Collect texture names...
	if not defined TexNameBank (
		set "TexNameBank=%TextureName%"
	) else set "TexNameBank=%TexNameBank% %TextureName%"

	set /a "CurrStep=%CurrStep%+1"
	set /a "CurrOffset=%CurrOffset%+20"
	if %CurrStep% LEQ %NumTextures% call :ReadTexNameOffset "%~1"
exit /b

:ReadOffsetName
	%Sfk% partcopy "%~1" -allfrom %~2 "%~dpn0.tmp" -yes -quiet=2
	%Sfk% replace "%~dpn0.tmp" -binary "=00=0a=" -yes -quiet=2
	for /f "delims=" %%a in ('call %Sfk% filter "%~dpn0.tmp" -rep "=/=\=" -lerep "=\=="') do (
		set "%~3=%%~a"
		del /f /q "%~dpn0.tmp"
		exit /b
	)
exit /b

:==============================================================================
:CheckFileExist
	set TexIsExist=
	for %%p in (%TexPathBank%) do (
		if exist "%ModDir%\materials\%%~p\%~1.vmt" (
			set TexIsExist=1
			call :ReadVmtInsides "%ModDir%\materials\%%~p\%~1.vmt"
		)
	)
	if not defined TexIsExist (
		%Sfk% echo [red]- Missing: \"%~1.vmt\"
		set MissingTextures=True
	)
exit /b

:ReadVmtInsides
	copy /y "%~1" "%~dpn0.tmp"> nul
	%Sfk% filter "%~dpn0.tmp" -+/ -+\ -srep =\q*//*=\q= -rep =//*== -rep =/=\= -write -quiet=2 -yes
	for /f "useback tokens=1,2" %%a in ("%~dpn0.tmp") do (
		if not "%%~b"=="" (
		if not exist "%ModDir%\materials\%%~b.tth" (
			%Sfk% echo [red]- Missing: \"%%~b.tth\"
			set MissingTextures=True
		))
	)
	del /f /q "%~dpn0.tmp"
exit /b
