@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title VTex compiler :: SDK mode
if "%~1"=="" (
	vtex.exe
	pause> nul
	exit
)

:DefVars
pushd "%~dp0.."
if not defined ModDir (
set "VProject=%cd%\vampire"
set "ModDir=%cd%\vampire"
set "GameDir=%cd%\vampire")
pushd "%~dp0"

if exist "GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
	if /i "%%~a"=="ModDir" (if exist "%%~b\*" (set "%%~a=%%~b") )
	if /i "%%~a"=="GameDir" (if exist "%%~b\*" (set "%%~a=%%~b") )
))

:ProcTgaPath
set TgaFiles=
set TgaFound=
for %%f in (%*) do (
if /i "%%~xf"==".tga" (
	call :SetTgaFiles "%%~f"
	set "TgaPath=%%~dpf"
	set "TexName=%%~nf"
	set "TgaFound=true"
))
if not defined TgaFound (
	echo -------------------------------------
	echo ERROR! No input TGA images specified.
	echo -------------------------------------
	if "%~1"=="" pause> nul
	exit
)

:ParseCmdline
set CmdLine=
if /i "%~1"=="-shader" set CmdLine=%~1 "%~2"

:StripMatsDir
for /f "delims=" %%a in (
'helpers\sfk.exe echo "%TgaPath%/" +filt -rep "|*materials*\||" -lerep "|/||" -lerep "|\||"'
) do (
	set "TtzPath=%ModDir%\materials\%%~a"
	set "TtzFile=materials\%%~a\%TexName%.tth"
)

:ShowRoundup
echo ------------------
echo Project Dir: "%ModDir%"
echo Target Tth: "%TtzFile%"
echo ------------------
echo. 

:ClearOldFiles
if defined TexNames (
if defined CmdLine (
for %%m in (%TexNames%) do (
if exist "%TtzPath%\%%~m.???" (
del /f /q "%TtzPath%\%%~m.???")
)))> nul

:RunCompiler
call vtex.exe -mkdir -nopause %CmdLine% %TgaFiles%
echo. 

:CheckResult
echo ------------------------------
if not exist "%ModDir%\%TtzFile%" (
	echo An error occurred during compiling!
	echo See VTex log above for details.
) else (
	echo Compiling success.
)
echo ------------------------------

:AppendVmtParams
if /i "%~1"=="-vmtparam" set "VmtParam1=^%~2^ ^%~3^"
if /i "%~2"=="-vmtparam" set "VmtParam2=^%~3^ ^%~4^"
if /i "%~3"=="-vmtparam" set "VmtParam3=^%~4^ ^%~5^"
if /i "%~4"=="-vmtparam" set "VmtParam4=^%~5^ ^%~6^"
if /i "%~5"=="-vmtparam" set "VmtParam5=^%~6^ ^%~7^"
if /i "%~6"=="-vmtparam" set "VmtParam6=^%~7^ ^%~8^"
if /i "%~7"=="-vmtparam" set "VmtParam7=^%~8^ ^%~9^"
if defined TexNames (
for %%m in (%TexNames%) do (
if exist "%TtzPath%\%%~m.vmt" (
	if defined VmtParam1 (helpers\sfk.exe replace "%TtzPath%\%%~m.vmt" -spat "|}|\t%VmtParam1:\=/%\r\n}|" -yes)
	if defined VmtParam2 (helpers\sfk.exe replace "%TtzPath%\%%~m.vmt" -spat "|}|\t%VmtParam2:\=/%\r\n}|" -yes)
	if defined VmtParam3 (helpers\sfk.exe replace "%TtzPath%\%%~m.vmt" -spat "|}|\t%VmtParam3:\=/%\r\n}|" -yes)
	if defined VmtParam4 (helpers\sfk.exe replace "%TtzPath%\%%~m.vmt" -spat "|}|\t%VmtParam4:\=/%\r\n}|" -yes)
	if defined VmtParam5 (helpers\sfk.exe replace "%TtzPath%\%%~m.vmt" -spat "|}|\t%VmtParam5:\=/%\r\n}|" -yes)
	if defined VmtParam6 (helpers\sfk.exe replace "%TtzPath%\%%~m.vmt" -spat "|}|\t%VmtParam6:\=/%\r\n}|" -yes)
	if defined VmtParam7 (helpers\sfk.exe replace "%TtzPath%\%%~m.vmt" -spat "|}|\t%VmtParam7:\=/%\r\n}|" -yes)
	helpers\sfk.exe replace "%TtzPath%\%%~m.vmt" -spat "|^|\q|" -quiet -yes
)))> nul

:ClearChildVmts
if defined TexNames (
for %%m in (%TexNames%) do (
if exist "%TtzPath%\%%~m.vmt" (
	set baseTex=
	for /f "usebackq tokens=1,*" %%a in ("%TtzPath%\%%~m.vmt") do (
		if /i "%%~a"=="$basetexture" call :SetBaseTex "%%~b"
		if /i "%%~a"=="$bumpmap" call :SetBadVmts "%%~b"
		if /i "%%~a"=="$envmapmask" call :SetBadVmts "%%~b"
		if /i "%%~a"=="$selfillumtexture" call :SetBadVmts "%%~b"
	)
)))> nul
if defined BadVmts for %%m in (%BadVmts%) do (
	if exist "%TtzPath%\%%~nm.vmt" del /f /q "%TtzPath%\%%~nm.vmt"
)> nul

:Quit
exit



:: Functions

:SetTgaFiles
if defined TgaFiles (
	set TgaFiles=%TgaFiles% "%~1"
	set TexNames=%TexNames% "%~n1"
) else (
	set TgaFiles="%~1"
	set TexNames="%~n1"
)
exit /b

:SetBaseTex
set "baseTex=%~1"
set "baseTex=%baseTex:/=\%"
exit /b

:SetBadVmts
set "CurrFile=%~1"
set "CurrFile=%CurrFile:/=\%"
if defined baseTex (
if /i "%CurrFile%"=="%baseTex%" (
	rem Don't remove host file...
	exit /b
))
if defined BadVmts (
	set BadVmts=%BadVmts% "%CurrFile%"
) else (
	set BadVmts="%CurrFile%"
)
exit /b