@echo off
title WL Dumper for Dupe Finder ^& Deleter  (c) Psycho-A

:SetBaseDir
pushd "%~dp0..\..\..\.."
set "SourceDir=%CD%\Vampire"

:SetPrograms
pushd "%~dp0"
set "Sfk=..\..\..\helpers\sfk.exe"
set "Sha=sha1.exe"
set "WhiteList=%cd%\WhiteList-Vampire.lst"

:CheckDirs
if not exist "%SourceDir%" (
	echo Source dir not found:
	echo "%SourceDir%"
	echo Please, specify another one by editing this BAT file.
	goto Finish
)

echo Generating, please wait...
echo This must take a much time.
echo.

:DumpFileTOC
call :DelTemps
for /f "delims=" %%a in ('dir /b /s /a-d "%SourceDir%\"') do (call :WriteLine "%%~a")
%Sfk% replace "%WhiteList%" "|%SourceDir%\||" -yes -quiet=2
echo Written to:
echo "%WhiteList%".

:Finish
echo Finished.
echo Hit any key to exit...
pause> nul
exit


:WriteLine
set FName=
set FSize=
set FSha1=

set "FName=%~1"
for %%s in ("%~1") do (set "FSize=%%~zs")
for /f %%c in ('call %Sha% "%~1"') do (set "FSha1=%%~c")
echo "%FName%"		%FSize%:%FSha1%>> "%WhiteList%"
exit /b

:DelTemps
for %%m in ("%WhiteList%*") do (
	del /f /q /a "%%~m"> nul )
exit /b