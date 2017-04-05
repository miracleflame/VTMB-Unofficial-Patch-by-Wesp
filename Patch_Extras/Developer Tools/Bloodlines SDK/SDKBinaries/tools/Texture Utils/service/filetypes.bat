@echo off
:if "%~1"=="" exit
if not defined ExportFormat set ExportFormat=tga
pushd "%~dp0.."

echo Registering image formats...
:======== VTF Files =========
REG>nul ADD "HKCU\Software\Classes\.vtf" /f /ve  /t REG_SZ /d "Wunderboy.ShellExtensions.VTFFile"
REG>nul ADD "HKCU\Software\Classes\Wunderboy.ShellExtensions.VTFFile" /f /ve  /t REG_SZ /d "Valve Texture File"
REG>nul ADD "HKCU\Software\Classes\Wunderboy.ShellExtensions.VTFFile\shell" /f /ve                  /t REG_SZ /d "View"
REG>nul ADD "HKCU\Software\Classes\Wunderboy.ShellExtensions.VTFFile\shell\View" /f /ve             /t REG_SZ /d "View"
REG>nul ADD "HKCU\Software\Classes\Wunderboy.ShellExtensions.VTFFile\shell\View\command" /f /ve     /t REG_SZ /d "%CD%\VTFEdit.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\Wunderboy.ShellExtensions.VTFFile\shell\Conv2Ttz" /f /ve         /t REG_SZ /d "Convert to .ttz..."
REG>nul ADD "HKCU\Software\Classes\Wunderboy.ShellExtensions.VTFFile\shell\Conv2Ttz\command" /f /ve /t REG_SZ /d "%CD%\TexConvert.exe \"%%1\" -tottz"
REG>nul ADD "HKCU\Software\Classes\Wunderboy.ShellExtensions.VTFFile\shell\Expt2Img" /f /ve         /t REG_SZ /d "Convert to .%ExportFormat%..."
REG>nul ADD "HKCU\Software\Classes\Wunderboy.ShellExtensions.VTFFile\shell\Expt2Img\command" /f /ve /t REG_SZ /d "%CD%\TexConvert.exe \"%%1\" -toimg"
REG>nul ADD "HKCU\Software\Classes\Wunderboy.ShellExtensions.VTFFile\DefaultIcon" /f /ve /t REG_SZ /d "%CD%\TexConvert.exe,3"
:======== TTH Files =========
REG>nul ADD "HKCU\Software\Classes\.tth" /f /ve /t REG_SZ /d "TTHFile"
REG>nul ADD "HKCU\Software\Classes\TTHFile" /f /ve /t REG_SZ /d "Troika Texture Header"
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell" /f /ve                  /t REG_SZ /d "View"
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\View" /f /ve             /t REG_SZ /d "View"
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\View\command" /f /ve     /t REG_SZ /d "%CD%\TTZView.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\Conv2Vtf" /f /ve         /t REG_SZ /d "Convert to .vtf..."
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\Conv2Vtf\command" /f /ve /t REG_SZ /d "%CD%\TexConvert.exe \"%%1\" -tovtf"
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\Expt2Img" /f /ve         /t REG_SZ /d "Convert to .%ExportFormat%..."
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\Expt2Img\command" /f /ve /t REG_SZ /d "%CD%\TexConvert.exe \"%%1\" -toimg"
REG>nul ADD "HKCU\Software\Classes\TTHFile\DefaultIcon" /f /ve /t REG_SZ /d "%CD%\TTZView.exe,1"
:======== TTZ Files =========
REG>nul ADD "HKCU\Software\Classes\.ttz" /f /ve /t REG_SZ /d "TTZFile"
REG>nul ADD "HKCU\Software\Classes\TTZFile" /f /ve /t REG_SZ /d "Troika Texture Zipped"
REG>nul ADD "HKCU\Software\Classes\TTZFile\shell" /f /ve                  /t REG_SZ /d "View"
REG>nul ADD "HKCU\Software\Classes\TTZFile\shell\View" /f /ve             /t REG_SZ /d "View"
REG>nul ADD "HKCU\Software\Classes\TTZFile\shell\View\command" /f /ve     /t REG_SZ /d "%CD%\TTZView.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\TTZFile\shell\Conv2Vtf" /f /ve         /t REG_SZ /d "Convert to .vtf..."
REG>nul ADD "HKCU\Software\Classes\TTZFile\shell\Conv2Vtf\command" /f /ve /t REG_SZ /d "%CD%\TexConvert.exe \"%%1\" -tovtf"
REG>nul ADD "HKCU\Software\Classes\TTZFile\shell\Expt2Img" /f /ve         /t REG_SZ /d "Convert to .%ExportFormat%..."
REG>nul ADD "HKCU\Software\Classes\TTZFile\shell\Expt2Img\command" /f /ve /t REG_SZ /d "%CD%\TexConvert.exe \"%%1\" -toimg"
REG>nul ADD "HKCU\Software\Classes\TTZFile\DefaultIcon" /f /ve /t REG_SZ /d "%CD%\TTZView.exe,2"

:======== Image Files =========
for %%m in (tga dds bmp png jpg gif) do (call :ProcessImgFmts "%%~m")

popd
exit /b

:ProcessImgFmts
set RegKeyName=
for /f "tokens=1,2,3,4" %%a in ('reg query "HKCR\.%~1" /ve') do (
	if /i "%%~b"=="REG_SZ" (set "RegKeyName=%%~c") else (
	if /i "%%~c"=="REG_SZ" (set "RegKeyName=%%~d"))
)
for /f "tokens=1,2,3,4" %%a in ('reg query "HKCU\Software\Classes\.%~1" /ve') do (
	if /i "%%~b"=="REG_SZ" (set "RegKeyName=%%~c") else (
	if /i "%%~c"=="REG_SZ" (set "RegKeyName=%%~d"))
)
if not defined RegKeyName set "RegKeyName=%~1file"

REG>nul ADD "HKCU\Software\Classes\.%~1" /f /ve /t REG_SZ /d "%RegKeyName%"
REG>nul ADD "HKCU\Software\Classes\%RegKeyName%\shell\Conv2Ttz" /f /ve         /t REG_SZ /d "Convert to .ttz..."
REG>nul ADD "HKCU\Software\Classes\%RegKeyName%\shell\Conv2Ttz\command" /f /ve /t REG_SZ /d "%CD%\TexConvert.exe \"%%1\" -tottz"
REG>nul ADD "HKCU\Software\Classes\%RegKeyName%\shell\Conv2Vtf" /f /ve         /t REG_SZ /d "Convert to .vtf..."
REG>nul ADD "HKCU\Software\Classes\%RegKeyName%\shell\Conv2Vtf\command" /f /ve /t REG_SZ /d "%CD%\TexConvert.exe \"%%1\" -tovtf"
exit /b
