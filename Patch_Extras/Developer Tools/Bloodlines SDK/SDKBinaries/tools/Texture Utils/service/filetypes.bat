@echo off
:if "%~1"=="" exit
if not defined ExportFormat set ExportFormat=tga
pushd "%~dp0.."
echo Registering image formats...

:======== TTH Files =========
REG>nul ADD "HKCU\Software\Classes\.tth" /f /ve                           /d "TTHFile"
REG>nul ADD "HKCU\Software\Classes\TTHFile" /f /ve                        /d "Troika Texture Header"
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell" /f /ve                  /d "View"
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\View" /f /ve             /d "View"
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\View\command" /f /ve     /d "%CD%\TTZView.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\Conv2Vtf" /f /ve         /d "Convert to .vtf..."
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\Conv2Vtf\command" /f /ve /d "%CD%\TexConvert.exe \"%%1\" -tovtf"
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\Expt2Img" /f /ve         /d "Convert to .%ExportFormat%..."
REG>nul ADD "HKCU\Software\Classes\TTHFile\shell\Expt2Img\command" /f /ve /d "%CD%\TexConvert.exe \"%%1\" -toimg"
REG>nul ADD "HKCU\Software\Classes\TTHFile\DefaultIcon" /f /ve            /d "%CD%\TTZView.exe,1"

:======== TTZ Files =========
REG>nul ADD "HKCU\Software\Classes\.ttz" /f /ve                           /d "TTZFile"
REG>nul ADD "HKCU\Software\Classes\TTZFile" /f /ve                        /d "Troika Texture Zipped"
REG>nul ADD "HKCU\Software\Classes\TTZFile\shell" /f /ve                  /d "View"
REG>nul ADD "HKCU\Software\Classes\TTZFile\shell\View" /f /ve             /d "View"
REG>nul ADD "HKCU\Software\Classes\TTZFile\shell\View\command" /f /ve     /d "%CD%\TTZView.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\TTZFile\DefaultIcon" /f /ve            /d "%CD%\TTZView.exe,2"

:======== VTF Files =========
REG>nul ADD "HKCU\Software\Classes\.vtf" /f /ve /t REG_SZ                 /d "VTFFile"
REG>nul ADD "HKCU\Software\Classes\VTFFile" /f /ve                        /d "Valve Texture File"
REG>nul ADD "HKCU\Software\Classes\VTFFile\shell" /f /ve                  /d "View"
REG>nul ADD "HKCU\Software\Classes\VTFFile\shell\View" /f /ve             /d "View"
REG>nul ADD "HKCU\Software\Classes\VTFFile\shell\View\command" /f /ve     /d "%CD%\VTFEdit.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\VTFFile\shell\Conv2Ttz" /f /ve         /d "Convert to .ttz..."
REG>nul ADD "HKCU\Software\Classes\VTFFile\shell\Conv2Ttz\command" /f /ve /d "%CD%\TexConvert.exe \"%%1\" -tottz"
REG>nul ADD "HKCU\Software\Classes\VTFFile\shell\Expt2Img" /f /ve         /d "Convert to .%ExportFormat%..."
REG>nul ADD "HKCU\Software\Classes\VTFFile\shell\Expt2Img\command" /f /ve /d "%CD%\TexConvert.exe \"%%1\" -toimg"
REG>nul ADD "HKCU\Software\Classes\VTFFile\DefaultIcon" /f /ve            /d "%CD%\TexConvert.exe,3"

:======== Image Files =========
for %%m in (tga dds bmp png jpg jpeg jpe gif) do (
REG>nul ADD "HKCU\Software\Classes\SystemFileAssociations\.%%~m\shell\Conv2Ttz" /f /ve         /d "Convert to .ttz..."
REG>nul ADD "HKCU\Software\Classes\SystemFileAssociations\.%%~m\shell\Conv2Ttz\command" /f /ve /d "%CD%\TexConvert.exe \"%%1\" -tottz"
REG>nul ADD "HKCU\Software\Classes\SystemFileAssociations\.%%~m\shell\Conv2Vtf" /f /ve         /d "Convert to .vtf..."
REG>nul ADD "HKCU\Software\Classes\SystemFileAssociations\.%%~m\shell\Conv2Vtf\command" /f /ve /d "%CD%\TexConvert.exe \"%%1\" -tovtf")

popd
exit /b