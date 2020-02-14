@echo off
pushd "%~dp0.."
set "FIPath=%~dp0fileicons"
echo Registering file formats...

:======== Image Files =========
if exist "%CD%\tools\Texture Utils\service\filetypes.bat" (
call "%CD%\tools\Texture Utils\service\filetypes.bat" -int)
rem Clear inactual records from previous sdk versions...
REG>nul DELETE "HKCU\Software\Classes\Wunderboy.ShellExtensions.VTFFile\shell\Convert" /f
REG>nul DELETE "HKCU\Software\Classes\TTHFile\shell\Convert" /f
REG>nul DELETE "HKCU\Software\Classes\TTZFile\shell\Convert" /f

:======== VMT Files =========
REG>nul ADD "HKCU\Software\Classes\.vmt" /f /ve /d "VMTFile"
REG>nul ADD "HKCU\Software\Classes\VMTFile" /f /ve /d "Valve Material file"
REG>nul ADD "HKCU\Software\Classes\VMTFile\shell" /f /ve /d "Notepad"
REG>nul ADD "HKCU\Software\Classes\VMTFile\shell\Notepad" /f /ve /d "Edit with NotePad"
REG>nul ADD "HKCU\Software\Classes\VMTFile\shell\Notepad\command" /f /ve /d "notepad.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\VMTFile\DefaultIcon" /f /ve /d "%FIPath%\vmt.ico,0"

:======== VMF Files =========
REG>nul ADD "HKCU\Software\Classes\.vmf" /f /ve /d "VMFFile"
REG>nul ADD "HKCU\Software\Classes\VMFFile" /f /ve /d "Valve Map file"
REG>nul ADD "HKCU\Software\Classes\VMFFile\shell" /f /ve /d "Notepad"
REG>nul ADD "HKCU\Software\Classes\VMFFile\shell\Notepad" /f /ve /d "View with NotePad"
REG>nul ADD "HKCU\Software\Classes\VMFFile\shell\Notepad\command" /f /ve /d "notepad.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\VMFFile\DefaultIcon" /f /ve /d "%FIPath%\vmf.ico,0"

:======== VPK Files =========
REG>nul ADD "HKCU\Software\Classes\.vpk" /f /ve /d "VPKFile"
REG>nul ADD "HKCU\Software\Classes\VPKFile" /f /ve /d "Vampire Pack file"
REG>nul ADD "HKCU\Software\Classes\VPKFile\shell" /f /ve /d "Open"
REG>nul ADD "HKCU\Software\Classes\VPKFile\shell\VPKTool\command" /f /ve /d "%CD%\tools\VPKTool\VPKTool.exe V \"%%1\""
REG>nul ADD "HKCU\Software\Classes\VPKFile\shell\Open\command" /f /ve /d "%CD%\tools\Crowbar\Launcher.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\VPKFile\DefaultIcon" /f /ve /d "%FIPath%\pak.ico,0"

:======== MDL Files =========
REG>nul ADD "HKCU\Software\Classes\.mdl" /f /ve /d "MDLFile"
REG>nul ADD "HKCU\Software\Classes\MDLFile" /f /ve /d "3D Model file"
REG>nul ADD "HKCU\Software\Classes\MDLFile\shell" /f /ve /d "View"
REG>nul ADD "HKCU\Software\Classes\MDLFile\shell\View" /f /ve /d "View Model"
REG>nul ADD "HKCU\Software\Classes\MDLFile\shell\View\command" /f /ve /d "%CD%\hlmv.shell.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\MDLFile\shell\TexInfo" /f /ve /d "Texture Information"
REG>nul ADD "HKCU\Software\Classes\MDLFile\shell\TexInfo\command" /f /ve /d "%CD%\tools\Texture Utils\MDLTexInfo.bat \"%%1\""
REG>nul ADD "HKCU\Software\Classes\MDLFile\DefaultIcon" /f /ve /d "%CD%\hlmv.shell.exe,0"

:======== CFG Files =========
REG>nul ADD "HKCU\Software\Classes\.cfg" /f /ve /d "inifile"

:======== DLG Files =========
REG>nul ADD "HKCU\Software\Classes\.dlg" /f /ve /d "DLGFile"
REG>nul ADD "HKCU\Software\Classes\DLGFile" /f /ve /d "Dialogue data"
REG>nul ADD "HKCU\Software\Classes\DLGFile\shell" /f /ve /d "Notepad"
REG>nul ADD "HKCU\Software\Classes\DLGFile\shell\Notepad" /f /ve /d "Open with NotePad"
REG>nul ADD "HKCU\Software\Classes\DLGFile\shell\Notepad\command" /f /ve /d "notepad.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\DLGFile\DefaultIcon" /f /ve /d "%FIPath%\doc.ico,0"

:======== LIP Files =========
REG>nul ADD "HKCU\Software\Classes\.lip" /f /ve /d "LIPFile"
REG>nul ADD "HKCU\Software\Classes\LIPFile" /f /ve /d "LipSync and Captions data"
REG>nul ADD "HKCU\Software\Classes\LIPFile\shell" /f /ve /d "Localize"
REG>nul ADD "HKCU\Software\Classes\LIPFile\shell\Localize" /f /ve /d "Edit Subtitles"
REG>nul ADD "HKCU\Software\Classes\LIPFile\shell\Localize\command" /f /ve /d "%CD%\tools\Captions Editor\CaptionsEditor.bat \"%%1\""
REG>nul ADD "HKCU\Software\Classes\LIPFile\shell\FacePoser" /f /ve /d "Edit LipSync data"
REG>nul ADD "HKCU\Software\Classes\LIPFile\shell\FacePoser\command" /f /ve /d "%CD%\tools\LipVcd Editor\lipvcd_editor.bat \"%%1\""
REG>nul ADD "HKCU\Software\Classes\LIPFile\shell\Notepad" /f /ve /d "Open with NotePad"
REG>nul ADD "HKCU\Software\Classes\LIPFile\shell\Notepad\command" /f /ve /d "notepad.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\LIPFile\DefaultIcon" /f /ve /d "%FIPath%\doc.ico,0"

:======== VCD Files =========
REG>nul ADD "HKCU\Software\Classes\.vcd" /f /ve /d "VCDFile"
REG>nul ADD "HKCU\Software\Classes\VCDFile" /f /ve /d "Choreographic Scene"
REG>nul ADD "HKCU\Software\Classes\VCDFile\shell" /f /ve /d "FacePoser"
REG>nul ADD "HKCU\Software\Classes\VCDFile\shell\FacePoser" /f /ve /d "Edit in FacePoser"
REG>nul ADD "HKCU\Software\Classes\VCDFile\shell\FacePoser\command" /f /ve /d "%CD%\tools\LipVcd Editor\lipvcd_editor.bat \"%%1\""
REG>nul ADD "HKCU\Software\Classes\VCDFile\shell\Notepad" /f /ve /d "Open with NotePad"
REG>nul ADD "HKCU\Software\Classes\VCDFile\shell\Notepad\command" /f /ve /d "notepad.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\VCDFile\DefaultIcon" /f /ve /d "%FIPath%\vcd.ico,0"

:======== PY Files =========
REG>nul ADD "HKCU\Software\Classes\.py" /f /ve /d "PYFile"
REG>nul ADD "HKCU\Software\Classes\PYFile" /f /ve /d "Python Script"
REG>nul ADD "HKCU\Software\Classes\PYFile\shell" /f /ve /d "Notepad"
REG>nul ADD "HKCU\Software\Classes\PYFile\shell\Notepad" /f /ve /d "Edit with NotePad"
REG>nul ADD "HKCU\Software\Classes\PYFile\shell\Notepad\command" /f /ve /d "notepad.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\PYFile\DefaultIcon" /f /ve /d "%FIPath%\py.ico,0"

:======== QC Files =========
REG>nul ADD "HKCU\Software\Classes\.qc" /f /ve /d "QCFile"
REG>nul ADD "HKCU\Software\Classes\QCFile" /f /ve /d "Model Compile parameters"
REG>nul ADD "HKCU\Software\Classes\QCFile\shell" /f /ve /d "Notepad"
REG>nul ADD "HKCU\Software\Classes\QCFile\shell\Notepad" /f /ve /d "Edit with NotePad"
REG>nul ADD "HKCU\Software\Classes\QCFile\shell\Notepad\command" /f /ve /d "notepad.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\QCFile\shell\Compile" /f /ve /d "Compile to MDL..."
REG>nul ADD "HKCU\Software\Classes\QCFile\shell\Compile\command" /f /ve /d "%CD%\studiomdl.bat \"%%1\""
REG>nul ADD "HKCU\Software\Classes\QCFile\DefaultIcon" /f /ve /d "shell32.dll,69"

:======== SMD Files =========
REG>nul ADD "HKCU\Software\Classes\.smd" /f /ve /d "txtfile"

:======== RAD Files =========
REG>nul ADD "HKCU\Software\Classes\.rad" /f /ve /d "VRADFile"
REG>nul ADD "HKCU\Software\Classes\VRADFile" /f /ve /d "World Lighting parameters"
REG>nul ADD "HKCU\Software\Classes\VRADFile\shell" /f /ve /d "Notepad"
REG>nul ADD "HKCU\Software\Classes\VRADFile\shell\Notepad" /f /ve /d "Edit with NotePad"
REG>nul ADD "HKCU\Software\Classes\VRADFile\shell\Notepad\command" /f /ve /d "notepad.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\VRADFile\DefaultIcon" /f /ve /d "shell32.dll,69"

:======== VBSP Files =========
REG>nul ADD "HKCU\Software\Classes\.vbsp" /f /ve /d "VBSPFile"
REG>nul ADD "HKCU\Software\Classes\VBSPFile" /f /ve /d "World Detail parameters"
REG>nul ADD "HKCU\Software\Classes\VBSPFile\shell" /f /ve /d "Notepad"
REG>nul ADD "HKCU\Software\Classes\VBSPFile\shell\Notepad" /f /ve /d "Edit with NotePad"
REG>nul ADD "HKCU\Software\Classes\VBSPFile\shell\Notepad\command" /f /ve /d "notepad.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\VBSPFile\DefaultIcon" /f /ve /d "shell32.dll,69"

:======== FGD Files =========
REG>nul ADD "HKCU\Software\Classes\.fgd" /f /ve /d "FGDFile"
REG>nul ADD "HKCU\Software\Classes\FGDFile" /f /ve /d "Game Definition file"
REG>nul ADD "HKCU\Software\Classes\FGDFile\shell" /f /ve /d "Notepad"
REG>nul ADD "HKCU\Software\Classes\FGDFile\shell\Notepad" /f /ve /d "Edit with NotePad"
REG>nul ADD "HKCU\Software\Classes\FGDFile\shell\Notepad\command" /f /ve /d "notepad.exe \"%%1\""
REG>nul ADD "HKCU\Software\Classes\FGDFile\DefaultIcon" /f /ve /d "shell32.dll,69"

if "%~1"=="" ping>nul "127.0.0.1" -n 3
exit /b