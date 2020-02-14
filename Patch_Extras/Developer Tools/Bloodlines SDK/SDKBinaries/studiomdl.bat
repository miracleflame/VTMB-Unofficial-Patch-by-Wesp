@echo off
title StudioMDL compiler: SDK mode
rem CMD-wrapper for bugfixes and extra features!
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
chcp 850> nul
if "%~1"=="" (
	"%~dp0studiomdl.exe"
	pause> nul
	exit
)

:DefineVars
set "CwD=%Cd%"
pushd "%~dp0.."
if not defined ModDir (
set "ModDir=%Cd%\Vampire")
set "SdkContent=%Cd%\SDKContent"
pushd "%~dp0"
set MsgBox="helpers\msgbox.exe"
if exist "Tools\Texture Utils\TexConvert.exe" (
set TextureConverter="Tools\Texture Utils\TexConvert.exe"
) else set TextureConverter=
set QCFile=
set ModelName=
set CdMaterials=
set SourceTexturesFound=
set Params=
set CmdLine=%*

:ProcessQcPath
for %%m in (%*) do (
if /i "%%~xm"==".qc" (
	set "QCFile=%%~m"
	set "QCPath=%%~dpm"
	if not exist "%%~m" (
	if exist "%CwD%\%%~nxm" (
	set "QCFile=%CwD%\%%~nxm"
	set "QCPath=%CwD%\"))
))
if not defined QCFile (
	echo Invalid commands: no QC file specified!
	goto Quit
) else if not exist "%QCFile%" (
	echo Wrong QC path specified: "%QCFile%"!
	goto Quit
)

:ProcessModDir
if exist "GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
	if /i "%%~a"=="ModDir" (if exist "%%~b\*" (set "%%~a=%%~b") )
))
if not exist "%ModDir%\" (
rem Try VProject env.path...
if defined VProject (
if exist "%VProject%\" (
	set "ModDir=%VProject%"
)))
if not exist "%ModDir%\" (
	echo Wrong mod directory specified: "%ModDir%"!
	goto Quit
)

:GetMdlFilePath
for /f "usebackq eol=/ tokens=1,*" %%a in ("%QCFile%") do (
if /i "%%~a"=="$modelname" (if not "%%~b"=="" (
	if /i "%%~xb"==".mdl" call :SetFixed ModelName "models/%%~b!"
	if /i not "%%~xb"==".mdl" call :SetFixed ModelName "models/%%~b.mdl!"
)))
if not defined ModelName (
	echo Failed to get target MDL path from QC!
	goto Quit
)

:ParseCmdline
for %%l in (-game -mod -build) do (rem Strip mod lines:
if /i "%~1"=="%%~l" set CmdLine=%3 %4 %5 %6 %7 %8 %9)
for %%c in (%CmdLine%) do (rem Fix input QC file order:
if /i not "%%~xc"==".qc" call :FixCmdLine "%%~c")
if /i "%~1"=="-mod" (rem Optimize SC params if empty...
if not defined Params set Params=-fullcollide)
if defined Params set CmdLine=%Params%
if not defined Params set CmdLine=
if not defined Params set Params=-None-

:ShowSummary
call :SetFixed QCPath "%QCPath%"
set "ModelName=%ModelName:.mdl!=%"
echo ---------------------
if /i "%~1"=="-mod" (
	echo Project: "%ModDir: = %"
	echo Target MDL: "%ModelName: = %.mdl"
	echo Parameters: %Params: = %
) else (
	echo Project Dir: "%ModDir%"
	echo Target MDL: "%ModelName%.mdl"
	echo Parameters: %Params%
)
echo ---------------------

:ShowAlphaWarnings
if /i "%~1"=="-mod" (
	echo WARNING: ANIMATIONS ARE CURRENTLY NOT SUPPORTED!
	echo WARNING: MAXIMUM OF 10000 POLYS PER MODEL ALLOWED!
) else (
	echo WARNING: ANIMATIONS ARE CURRENTLY NOT SUPPORTED!
	echo WARNING: MAXIMUM OF 10000 POLYS PER MODEL ALLOWED!
)
echo.

:PreFixModelIssues
if exist studiomdl-fix.bat (
	echo Scanning model files for possible issues...
	call studiomdl-fix.bat "%QCFile%"
)
echo.       

:RunCompiler
echo Starting StudioMDL compiler...
echo ---------------------
if exist  "%ModDir%\%ModelName%.*" (
del /f /q "%ModDir%\%ModelName%.*"> nul)
for %%m in ("%ModDir%\%ModelName%") do (
if not exist "%%~dpm" (md "%%~dpm") )
call studiomdl.exe -game "%ModDir%" %CmdLine% "%QCFile%"
echo. 

:FixBadCollision
if exist studiomdl-fix.exe (
if exist "%ModDir%\%ModelName%.mdl" (
	echo Fixing model's collision data...
	call studiomdl-fix.exe "%ModDir%\%ModelName%.mdl"
))
echo.

:ReturnOriginalFiles
rem This is required after applying rotation fix
for /r "%QCPath%" %%s in (*.qc *.smd) do (
if exist "%%~dpns@orig%%~xs" (del /f /q "%%~s"
	move /y "%%~dpns@orig%%~xs" "%%~s"> nul 2>&1
))

:CheckResult
echo ---------------------
if exist "%ModDir%\%ModelName%.mdl" (
	echo Compiling model success.) else (
	echo An error occurred during compiling!
	echo See StudioMDL log above for details.
)
echo --------------------- 

:CompileTextures
if defined TextureConverter (
	echo.
	echo Compiling Materials...
	echo ---------------------
	call :GetMaterialPath
) else (
	goto Quit
)
if defined CdMaterials (
	echo Texture Path: "%CdMaterials: =_%\",
	echo "%ModDir: =_%\materials\" 
	echo Starting %TextureConverter%... 
	if /i not "%~1"=="-mod" echo.
	for %%p in (
		"%SdkContent%\materials\%CdMaterials%" "%SdkContent%\materialsrc\%CdMaterials%"
		"%ModDir%\materials\%CdMaterials%" "%ModDir%\materialsrc\%CdMaterials%"
		"%QCPath%\materials\%CdMaterials%" "%QCPath%\materialsrc\%CdMaterials%"
		"%QCPath%\%CdMaterials%" "%QCPath%"
	) do (if exist "%%~p\" (
		for %%x in (tga png bmp dds jpg gif) do (
		for %%f in ("%%~p\*.%%~x") do (
			set SourceTexturesFound=True
			echo Converting texture "%%~nxp/%%~nxf"... 
			if not exist "%ModDir%\materials\%CdMaterials%\" (
			md "%ModDir%\materials\%CdMaterials%"> nul)
			if /i not "%%~f"=="%ModDir%\materials\%CdMaterials%\%%~nxf" (
			copy /y "%%~f" "%ModDir%\materials\%CdMaterials%\"> nul)
			%TextureConverter% "%ModDir%\materials\%CdMaterials%\%%~nxf" -silent
			if not exist "%ModDir%\materials\%CdMaterials%\%%~nf.vmt" echo - Failed to create .vmt!
			if not exist "%ModDir%\materials\%CdMaterials%\%%~nf.tth" echo - Failed to create .tth!
			if /i not "%%~f"=="%ModDir%\materials\%CdMaterials%\%%~nxf" (
			del /f /q "%ModDir%\materials\%CdMaterials%\%%~nxf"> nul)
		))
	))
)
rem Check compiling result...
if defined CdMaterials (
if defined SourceTexturesFound (
	echo.
	echo ---------------------
	if exist "%ModDir%\materials\%CdMaterials%\?*.vmt" (
	if exist "%ModDir%\materials\%CdMaterials%\?*.tth" (
		echo Compiling materials success.) else (
		echo Compiling materials failed.)) else (
		echo Compiling materials failed.
	)
	echo ---------------------
) else (
	if /i "%~1"=="-mod" echo.
	echo No source materials found to be compiled.
)) else (
	if /i "%~1"=="-mod" echo.
	echo Unable to get model materials path from the QC file!
)

:Quit
popd
popd
echo.
if /i "%~x1"==".qc" pause
exit



:FixCmdLine
if not defined Params (
set "Params=%~1") else (
set "Params=%Params% %~1")
exit /b

:GetMaterialPath
for /f "usebackq eol=/ tokens=1,*" %%a in ("%QCFile%") do (
if /i "%%~a"=="$cdmaterials" (if not "%%~b"=="" (
	call :SetFixed CdMaterials "%%~b"
	rem Use only first found path as main!
	exit /b
)))
exit /b

:SetFixed
	set "FixVar=%~2"
:SetFixed_loop
	set "FixVar=%FixVar:/=\%"
	set "FixVar=%FixVar:\\=\%"
	if "%FixVar:~-1%"=="\" set "FixVar=%FixVar:~0,-1%"
	if "%FixVar:~0,1%"=="\" set "FixVar=%FixVar:~1%"
	if "%FixVar:~0,14%"=="models\models\" set "FixVar=%FixVar:~7%"
	if "%FixVar:~-1%"=="\" goto SetFixed_loop
	if "%FixVar:~0,1%"=="\" goto SetFixed_loop
	if not "%FixVar:\\=\%"=="%FixVar%" goto SetFixed_loop
	set "%~1=%FixVar%"
exit /b