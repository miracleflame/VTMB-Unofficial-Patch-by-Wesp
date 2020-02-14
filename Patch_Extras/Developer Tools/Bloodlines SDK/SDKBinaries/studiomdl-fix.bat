@echo off
rem StudioMDL rotation and animation issues fixer
rem Written by Psycho-A at [14:26 02.02.2020]
setlocal EnableExtensions
if "%~1"=="" exit /b
if not defined QCFile exit /b
if not defined ModelName exit /b
if not exist %MsgBox% exit /b

:Vars
set CollisionModel=
set IsVtmbDecompiled=
set ModelIsStaticProp=
set StaticPropIsSet=
set HasOriginOverride=


:ScanFiles
rem Check if model is VtmB's (don't rotate others!):
if not "%ModelName:models\scenery\=%"=="%ModelName%" set IsVtmbDecompiled=True
if not "%ModelName:models\items\=%"=="%ModelName%" set IsVtmbDecompiled=True
rem Analyze QC file...
for /f "usebackq eol=/ tokens=1,*" %%a in ("%QCFile%") do (
	rem Static phy-model gets 90-deg rotated on decompiling:
	if /i "%%~a"=="$collisionmodel" (if not "%%~b"=="" (
		if exist "%QCPath%\%%~b" call :SetFixed CollisionModel "%QCPath%\%%~b"
		if exist "%QCPath%\%%~b.smd" call :SetFixed CollisionModel "%QCPath%\%%~b.smd"
	))
	rem Find if Origin rotation fix needed:
	if /i "%%~a"=="$origin" (if not "%%~b"=="" (
	for /f "tokens=1-4" %%i in ("%%~b") do (
		if "%%~l"=="-90" (set HasOriginOverride=True)
	)))
	rem Check if need to correct StaticProp definition:
	if /i "%%~a"=="$staticprop" (set StaticPropIsSet=True)
)
rem Check if model is originally static:
rem Only static models needs fixing rotation
for /r "%QCPath%" %%s in (*.smd) do (
for /f "usebackq eol=/ tokens=1-4" %%a in ("%%~s") do (
	if "%%~a"=="0" (if "%%~d"=="" (
	if /i "%%~b"=="static_prop" (
		rem Only Vtmb models have this bone
		set IsVtmbDecompiled=True
		set ModelIsStaticProp=True
	)))
))


:CheckCriterias
rem Skip missing criterias:
if defined StaticPropIsSet (
	rem For Static props...
	if defined ModelIsStaticProp (
	if defined IsVtmbDecompiled (
	if defined HasOriginOverride (
		goto Quit_skip
	))) else (
		rem Non-Static props...
		goto Quit_skip
	)
)


:Summary
if defined IsVtmbDecompiled  (echo - Decompiled from VtmB game: Yes ) else (echo - Decompiled from VtmB game: No  )
if defined CollisionModel    (echo - Model contain physics SMD: Yes ) else (echo - Model contain physics SMD: No  )
if defined ModelIsStaticProp (echo - Model used as static_prop: Yes ) else (echo - Model used as static_prop: No  )
if defined StaticPropIsSet   (echo - Flag "StaticProp" defined: Yes ) else (echo - Flag "StaticProp" defined: No  )
if defined HasOriginOverride (echo - Model has origin override: Yes ) else (echo - Model has origin override: No  )


:RequestUser
if defined ModelIsStaticProp (
	rem Fixes for static_props:
	%MsgBox% It looks like the model is decompiled from Vampire: Bloodlines, so the resulting model in your project may have 90-degree rotation issue on Z-axis of the reference, physics or sequence meshes. The program may try to fix this issue if you click "Yes". The source QC and SMD files won't be modified, so you can always revert this fix just by recompiling. Do it? /c:StudioMDL warning /t:MB_ICONQUESTION,MB_YESNO,MB_SYSTEMMODAL
) else (
	rem Fixes for dynamic props:
	%MsgBox% It looks like the model is designed as a dynamic object, which is not allowed for StudioMDL compiler at this moment, and it may cause the game to crash or render bugs. The program can fix it by compiling the model as a static prop if you click "Yes". The source QC file won't be modified, so you can always revert this fix just by recompiling. Do it? /c:StudioMDL warning /t:MB_ICONQUESTION,MB_YESNO,MB_SYSTEMMODAL
)
if "%ErrorLevel%"=="7" (goto Quit) else echo.


:RotatePhyMesh
set LastKey=
if defined ModelIsStaticProp (
if defined CollisionModel (
for %%x in ("%CollisionModel%") do (
	echo Rotating collision mesh... 
	copy /y "%%~x" "%%~dpnx@orig.smd"> nul
	type nul> "%%~x"
	for /f "usebackq tokens=1-9,*" %%a in ("%%~dpnx@orig.smd") do (
		set "Key1=%%~a"
		set "Key2=%%~b"
		set "Key3=%%~c"
		set "Key4=%%~d"
		set "Key5=%%~e"
		set "Key6=%%~f"
		set "Key7=%%~g"
		set "Key8=%%~h"
		set "Key9=%%~i"
		set "KeyL=%%~j"
		call :RotateSMD "%%~x"
	)
	rem Check resulting work by file sizes...
	for %%s in ("%%~dpnx@orig.smd") do (
		if "%%~zs"=="%%~zx" echo - Operation failed.
	)
)))


:FixQCParams
if defined StaticPropIsSet (
if defined HasOriginOverride (
	rem No fixing QC needed.
	goto Quit
))
for %%x in ("%QCFile%") do (
	echo Fixing values in QC file... 
	copy /y "%%~x" "%%~dpnx@orig.qc"> nul
	type nul> "%%~x"
	if defined ModelIsStaticProp (
	if not defined HasOriginOverride (
		rem Origin value must be first to fix all issues
		echo - Adding $Origin override... 
		echo>>"%%~x" $Origin 0 0 0 -90
	))
	if not defined StaticPropIsSet (
		rem Add flag to avoid potential axis conflicts on static_prop's
		rem Also fixes crash and bone placement if model had animations
		echo - Adding $StaticProp flag... 
		echo>>"%%~x" $StaticProp
	)
	copy /b "%%~x" + "%%~dpnx@orig.qc" "%%~x"> nul
	rem Check resulting work by file sizes...
	for %%s in ("%%~dpnx@orig.qc") do (
		if "%%~zs"=="%%~zx" echo - Operation failed.
	)
)


:Quit
exit /b

:Quit_skip
echo No required conditions found for fixing.
exit /b


:RotateSMD
set SMDString=
if defined LastKey (
	if /i "%LastKey%"=="nodes" (
	if defined Key3 (
		rem Fix bone names with spaces...
		if defined Key3 set SMDString=%Key1% "%Key2%" %Key3%
		if defined Key4 set SMDString=%Key1% "%Key2% %Key3%" %Key4%
		if defined Key5 set SMDString=%Key1% "%Key2% %Key3% %Key4%" %Key5%
		if defined Key6 set SMDString=%Key1% "%Key2% %Key3% %Key4% %Key5%" %Key6%
	))
	if /i "%LastKey%"=="triangles" (
	if defined Key9 (
		rem Reverse X and Y coords/norms to rotate mesh
		call :ProcessPolyString
	))
)
if not defined SMDString (
	rem Rest of unprocessed strings...
	if defined Key1 set "SMDString=%Key1%"
	if defined Key2 set "SMDString=%Key1% %Key2%"
	if defined Key3 set "SMDString=%Key1% %Key2% %Key3%"
	if defined Key4 set "SMDString=%Key1% %Key2% %Key3% %Key4%"
	if defined Key5 set "SMDString=%Key1% %Key2% %Key3% %Key4% %Key5%"
	if defined Key6 set "SMDString=%Key1% %Key2% %Key3% %Key4% %Key5% %Key6%"
	if defined Key7 set "SMDString=%Key1% %Key2% %Key3% %Key4% %Key5% %Key6% %Key7%"
	if defined Key8 set "SMDString=%Key1% %Key2% %Key3% %Key4% %Key5% %Key6% %Key7% %Key8%"
	if defined Key9 set "SMDString=%Key1% %Key2% %Key3% %Key4% %Key5% %Key6% %Key7% %Key8% %Key9%"
	if defined KeyL set "SMDString=%Key1% %Key2% %Key3% %Key4% %Key5% %Key6% %Key7% %Key8% %Key9% %KeyL%"
)
rem Remember last block name to use:
if not defined Key2 (
for %%k in (header nodes skeleton triangles vertexanimation) do (
	if /i "%Key1%"=="%%~k" set "LastKey=%Key1%"
))
rem Write new SMD file:
echo>>"%~1" %SMDString%
exit /b

:ProcessPolyString
	rem Use negative values of X coord and normal
	if "%Key2:~0,1%"=="-" (set "Key2=%Key2:~1%") else (set "Key2=-%Key2%")
	if "%Key5:~0,1%"=="-" (set "Key5=%Key5:~1%") else (set "Key5=-%Key5%")
	rem Swap X and Y to make -90-degrees rotation
	set "SMDString=%Key1% %Key3% %Key2% %Key4% %Key6% %Key5% %Key7% %Key8% %Key9% %KeyL%"
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