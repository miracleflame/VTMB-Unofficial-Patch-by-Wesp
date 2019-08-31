@echo off
pushd "%~dp0.."

:paint.net-plugins
 set PlgInstSuccess=0
 echo Installing PaintDotNet plugins...
 echo Querying registry path for 32-bit installation mode...
 for /f "tokens=1,2,*" %%i in ('call "%windir%\system32\reg.exe" query "HKLM\SOFTWARE\Paint.NET"') do (
 	if /i "%%~i"=="TARGETDIR" call :InstallPNPlugs "%%~k")
 echo Querying registry path for 64-bit installation mode...
 for /f "tokens=1,2,*" %%i in ('call "%windir%\sysnative\reg.exe" query "HKLM\SOFTWARE\Paint.NET"') do (
 	if /i "%%~i"=="TARGETDIR" call :InstallPNPlugs "%%~k")
 echo Checking "Program Files" installation paths...
 for %%p in ("%ProgramFiles%" "%ProgramFiles(x86)%" "%ProgramW6432%") do (
 	for /d %%s in ("%%~p\Paint*NET*") do (call :InstallPNPlugs "%%~s"))
 if "%PlgInstSuccess%"=="1" (echo ...Success!) else (echo ...Failed!)
 echo.

:photoshop-plugins
 set PlgInstSuccess=0
 echo Installing Photoshop plugins...
 echo Querying registry path for 32-bit installation mode...
 for /f "tokens=1,2,*" %%i in ('call "%windir%\system32\reg.exe" query "HKLM\SOFTWARE\Adobe\Photoshop" /s') do (
 	if /i "%%~i"=="ApplicationPath" call :InstallPSPlugs "%%~k")
 echo Querying registry path for 64-bit installation mode...
 for /f "tokens=1,2,*" %%i in ('call "%windir%\sysnative\reg.exe" query "HKLM\SOFTWARE\Adobe\Photoshop" /s') do (
 	if /i "%%~i"=="ApplicationPath" call :InstallPSPlugs "%%~k")
 if %PlgInstSuccess%==1 (echo ...Success!) else (echo ...Failed!)
 echo.

:plugins-finish
if "%~1"=="" ping>nul "127.0.0.1" -n 3
exit /b


:InstallPNPlugs
	if exist "plugins\texturing\paintdotnet.7z" if exist "%~1\Paint*Net?*" (
	helpers\7za.exe x "plugins\texturing\paintdotnet.7z" -o"%~1\" -y -aoa> nul
	if exist "%~1\FileTypes\VtfFileType.dll" set PlgInstSuccess=1)
exit /b

:InstallPSPlugs
	if exist "plugins\texturing\photoshop.7z" if exist "%~1\Photoshop.exe" (
	helpers\7za.exe x "plugins\texturing\photoshop.7z" -o"%~1\" -y -aoa> nul
	if exist "%~1\Plug-Ins\File Formats\VTF.8bi" set PlgInstSuccess=1)
exit /b