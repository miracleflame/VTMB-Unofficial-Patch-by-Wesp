@echo off
setlocal ENABLEEXTENSIONS
if "%~2"=="" exit

:vars
pushd "%~dp0"
set "JarFile=%cd%\%~2"
set "MsgBox=%cd%\..\..\service\msgbox.exe"
set "ErrorMsg=Java Runtime Environment must be installed on your system to run this program. Would you like to download and install it now?"

:checkfiles
for %%m in ("%JarFile%" "%MsgBox%") do if not exist "%%~m" (
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] Java_Run error: Missing "%%~m" file.
	exit
)

:changeworkdir
if exist "..\..\GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("..\..\GameCfg.ini") do (
	if /i "%%~a"=="ModDir" if exist "%%~b\maps\" (pushd "%%~b\maps\") else (
	if exist "%%~b\" (pushd "%%~b\"))
)) else (if exist "..\..\..\Vampire\maps\" (
	pushd "..\..\..\Vampire\maps\") else (pushd "..\..\..")
)

:checkjava
for %%M in (
	"%SystemRoot%\system32"
	"%SystemRoot%\syswow64"
) do if exist "%%~M\java.exe" (
	start /b "java" "%%~M\java.exe" %1 "%JarFile%" %3 %4 %5 %6 %7 %8 %9
	exit
)
for /D %%M in (
	"%ProgramFiles%\Java\jre*"
	"%ProgramW6432%\Java\jre*"
) do if exist "%%~M\bin\java.exe" (
	start /b "java" "%%~M\bin\java.exe" %1 "%JarFile%" %3 %4 %5 %6 %7 %8 %9
	exit
)

:ifnotfound
start /w "message" "%MsgBox%" %ErrorMsg% /c:Error /t:MB_ICONSTOP,MB_YESNO

if "%ErrorLevel%"=="6" (start "url" "www.java.com/download")
exit
