@echo off
setlocal ENABLEEXTENSIONS

:=======================================================================
:checklaunch
if "%~1"=="" exit
if not exist "%VampireDir%\*" (
	color 0c
	echo VExtract: Incorrect call, no valid VampireDir.
	exit)
if not exist "%TargetDir%\*" (
	color 0c
	echo VExtract: Incorrect call, no valid TargetDir.
	exit)
if not exist "service\VExtract?.exe" (
	color 0c
	echo VExtract: Incorrect call, no VExtract.exe found.
	exit)


:=======================================================================
:prepare
echo Preparing...
start "" "%MsgBox%" Content will be extracted into directory "%TargetDir%". First, the basic content (textures, models and sounds) will be extracted. See console window for current progress. Don't close it! /c:Note /t:MB_ICONASTERISK
if exist "%AppData%\vpkindex.ls?" del /a /q "%AppData%\vpkindex.ls?"> nul

:setsrcdirs
set SrcPaths="%VampireDir%"
if exist "%ModDir%\pack???.vpk" (
if /i not "%ModDir%"=="%VampireDir%" (
	set SrcPaths="%VampireDir%" "%ModDir%"
))


:=======================================================================
:excontent
echo Extracting basic content:
call :Extract "Textures" "0 1" "materials" "vmt tth ttz"
call :Extract "Models"   "0"   "models"    "mdl dx80.vtx phy"
call :Extract "Sounds"   "0 1" "sound"     "wav mp3"

echo Basic content extracted.
echo.

call :CheckMsgBox
"%MsgBox%" Basic resources extracted. Do you also want to extract the script assets?  Note they are not needed for level design, just may be useful for learning if you wish to add or customize quests, game mechanics or interfaces.  Since Python scripts and MP3 audio are already extracted, they will be left in the original directory. You can always access it. /c:Information /t:MB_SYSTEMMODAL,MB_ICONQUESTION,MB_YESNO
if not "%ErrorLevel%"=="6" goto finalize


:=======================================================================
:exscripts
echo Extracting scripts content:
call :Extract "Dialogues"     "1"   "dlg"           "dlg"
call :Extract "Particles"     "0"   "particles"     "tga txt"
call :Extract "Sound Scripts" "0"   "sound/schemes" "txt"
rem call :Extract "-"             "1"   "sound"         "lip vcd"
call :Extract "VData Scripts" "1"   "vdata"         "txt"

echo Additional content extracted.
echo.


:=======================================================================
:finalize
if exist "%AppData%\vpkindex.ls?" (
del /a /q "%AppData%\vpkindex.ls?"> nul)

exit /b




:=======================================================================
:Functions

:CheckMsgBox
	for /f "tokens=1" %%m in ('tasklist /NH') do (
	if /i "%%~m"=="msgbox.exe" (taskkill /f /im "msgbox.exe"> nul))
exit /b

:Extract
	if not "%~1"=="-" (
	echo - Extracting %~1...)
	for %%p in (%SrcPaths%) do (
	for %%t in (%~2) do (
	for %%e in (%~4) do (
		if not exist "%%~p\pack%%~t??.vpk" (exit /b)
		service\vextract%%~t.exe -d "%%~p" -i -q> nul
		if exist "%AppData%\vpkindex.ls%%~t" (
			copy /b "%AppData%\vpkindex.ls%%~t" + "service\vpkindex.fix" "%AppData%\vpkindex.ls%%~t"> nul)
		service\vextract%%~t.exe "%~3/*.%%~e" -d "%%~p" -o "%TargetDir%" -q> nul
	)))
exit /b

:CopyLoose
	echo - Copying %~1...
	if exist "%ModDir%\%~2\*" (
		"%SfkTool%" copy "%ModDir%\%~2" "%TargetDir%\%~2" -mirror -file %~3 -yes> nul
	) else (
		echo   No "%~2" dir presented in your game version.
	)
exit /b
