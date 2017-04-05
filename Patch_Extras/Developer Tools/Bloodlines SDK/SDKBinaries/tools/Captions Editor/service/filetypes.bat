@echo off
pushd "%~dp0..\..\..\"
echo Registering file formats...

:======== LIP Files =========
REG ADD "HKCU\Software\Classes\.lip" /f /ve /d "LIPFile"
REG ADD "HKCU\Software\Classes\LIPFile" /f /ve /d "LipSync and Captions data"
REG ADD "HKCU\Software\Classes\LIPFile\shell" /f /ve /d "Localize"
REG ADD "HKCU\Software\Classes\LIPFile\shell\Localize" /f /ve /d "Edit Subtitles"
REG ADD "HKCU\Software\Classes\LIPFile\shell\Localize\command" /f /ve /d "%CD%\tools\Captions Editor\CaptionsEditor.bat \"%%1\""
REG ADD "HKCU\Software\Classes\LIPFile\shell\FacePoser" /f /ve /d "Edit LipSync data"
REG ADD "HKCU\Software\Classes\LIPFile\shell\FacePoser\command" /f /ve /d "%CD%\tools\LipVcd Editor\lipvcd_editor.bat \"%%1\""
REG ADD "HKCU\Software\Classes\LIPFile\shell\Notepad" /f /ve /d "Open with NotePad"
REG ADD "HKCU\Software\Classes\LIPFile\shell\Notepad\command" /f /ve /d "notepad.exe \"%%1\""
REG ADD "HKCU\Software\Classes\LIPFile\DefaultIcon" /f /ve /d "%CD%\plugins\fileicons\doc.ico,0"

:======== VCD Files =========
REG ADD "HKCU\Software\Classes\.vcd" /f /ve  /d "VCDFile"
REG ADD "HKCU\Software\Classes\VCDFile" /f /ve  /d "Choreographic Scene"
REG ADD "HKCU\Software\Classes\VCDFile\shell" /f /ve /d "FacePoser"
REG ADD "HKCU\Software\Classes\VCDFile\shell\FacePoser" /f /ve /d "Edit in FacePoser"
REG ADD "HKCU\Software\Classes\VCDFile\shell\FacePoser\command" /f /ve  /d "%CD%\tools\LipVcd Editor\lipvcd_editor.bat \"%%1\""
REG ADD "HKCU\Software\Classes\VCDFile\shell\Notepad" /f /ve /d "Open with NotePad"
REG ADD "HKCU\Software\Classes\VCDFile\shell\Notepad\command" /f /ve  /d "notepad.exe \"%%1\""
REG ADD "HKCU\Software\Classes\VCDFile\DefaultIcon" /f /ve /d "%CD%\plugins\fileicons\vcd.ico,0"

popd
exit /b
