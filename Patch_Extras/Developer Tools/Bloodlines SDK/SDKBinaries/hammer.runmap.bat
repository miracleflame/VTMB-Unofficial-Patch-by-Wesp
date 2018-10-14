@echo off
setlocal ENABLEEXTENSIONS
set "WinTitle=Hammer RunMap Launcher"
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title %WinTitle%
color 07
pushd "%~dp0"
set "RMCfg=%~n0.ini"
if "%~1"=="" (exit)

:========================================================================
:GlobalUserDefs
:========================================================================

set DeletePRT=1
set DeleteBSP=1
set AllowSuspend=1
set Priority=/normal


:========================================================================
:DefineTasks
:========================================================================

:exec_stage
 if /i "%~1"=="execute" (
 if /i "%~2"=="selected" (
	start %~nx0 -execjob
	exit ))
 if /i "%~1"=="-execjob" (
	goto ExecuteJob)

:prep_stage
 if /i "%~1 %~2"=="set map" (
	echo [Main]
	echo RunTask	=	True
	echo MapName	=	"%~n3"
	echo MapFile	=	"%~3"
	echo VmfPath	=	"%~dp3"
	echo.
	echo [Commands])>"%RMCfg%"

:vbsp_stage
 if /i "%~1 %~n2"=="exec vbsp" (
	echo ExecVbsp	=	True
	echo VbspCmds	=	"%~3 %~4 %~5 %~6 %~7 %~8 %~9"
	if /i "%~3"=="-onlyents" (
	echo OnlyEnts	=	True))>>"%RMCfg%"

:vvis_stage
 if /i "%~1 %~n2"=="exec vvis" (
	echo ExecVvis	=	True
	echo VvisCmds	=	"%~3 %~4 %~5 %~6 %~7 %~8 %~9")>>"%RMCfg%"

:vrad_stage
 if /i "%~1 %~n2"=="exec vrad" (
	echo ExecVrad	=	True
	echo VradCmds	=	"%~3 %~4 %~5 %~6 %~7 %~8 %~9")>>"%RMCfg%"

:copy_stage
 if /i "%~1 %~2 %~3 %~4"=="put compiled bsp to" (
	echo PlaceBsp	=	True
	echo TgBspDir	=	"%~5")>>"%RMCfg%"

:cube_stage
 if /i "%~1 %~2"=="build cubemaps" (
	echo BuildCMs	=	True)>>"%RMCfg%"

:bzip_stage
 if /i "%~1 %~2 %~3"=="include custom content" (
	echo PatchBsp	=	True)>>"%RMCfg%"

:game_stage
 if /i "%~1 %~x2"=="run .exe" (
	echo.
	echo [Engine]
	echo LnchGame	=	True
	echo GExeFull	=	"%~2"
	echo GExePath	=	"%~dp2"
	echo GExeFile	=	"%~nx2"
	echo GExeExtn	=	"%~x2"
	echo AddlCmds	=	"alias wc_create echo Info: Map created with Bloodlines SDK."
	echo GameCmds	=	"%~3 %~4 %~5 %~6 %~7 %~8 %~9")>>"%RMCfg%"

:susp_stage
 if "%AllowSuspend%"=="1" (
 if /i "%~1 %~2"=="turn off" (
	echo.
	echo [TurnOff]
	echo SStandBy	=	True)>>"%RMCfg%"
 )
:finl_stage
 if /i "%~1 %~3"=="pause window" (
	echo.
	echo [Window]
	echo PauseWin	=	True)>>"%RMCfg%"
 rem Close previously open windows
	service\nircmd.exe win close ititle "%WinTitle%"

exit



:========================================================================
:ExecuteJob
:========================================================================

:check_files
for %%f in (
	"vbsp.exe"
	"vvis.exe"
	"vrad.exe"
	"%~n0.ini"
	"%~n0.bat"
	"%~n0.exe"
	"cmdseq.wc"
	"service\sfk.exe"
	"service\nircmd.exe"
) do if not exist "%%~f" (
	color 0c
	echo.
	echo   Error: Missing file: "%%~f". Cannot proceed.
	echo>>"..\sdk_errors.log" [%date% %time%] Hammer error: Missing "%cd%\%%~f" file.
	pause>nul
	goto quit
)

set "MapFile="
set "textcolor=service\sfk.exe color"
for /f "usebackq eol=# tokens=1,* delims=	=" %%a in ("%RMCfg%") do set "%%~a=%%~b"
del /f /q "%RMCfg%"> nul

:prepare
if /i not "%RunTask%"=="True" (
	color 0c
	echo.
	echo   Error: Task will not start, specify map first!
	pause>nul
	goto quit
)
if not defined MapFile (
	color 0c
	echo.
	echo   Error: No map file specified!
	pause>nul
	goto quit
)
if not exist "%MapFile%.vmf" (
	color 0c
	echo.
	echo   Error: Wrong map file specified:
	echo   "%MapFile%.vmf"!
	pause>nul
	goto quit
)

:proc_moddir
if defined ModDir (
if exist "%ModDir%\*" (
for %%m in ("%ModDir%") do (
	set "ModDir=%%~m"
	set "ModName=%%~nm"
)) else (
	color 0c
	echo.
	echo   Error: Invalid ModDir specified!
	pause>nul
	goto quit
)) else (
	color 0c
	echo.
	echo   Internal error: ModDir not defined!
	pause>nul
	goto quit
)

:hide_editor_window
service\nircmd.exe win min stitle "Bloodlines Map Editor"


call :get_starttime
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                             Preparing script                                #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo.
echo GameDir: "%ModDir%".
echo BaseDir: "%GameDir%".
echo MapFile: "%MapFile%.vmf".

(echo ================ Log started [%date%, %time:~0,-3%] =================
 echo.
 echo GameDir: "%ModDir%".
 echo BaseDir: "%GameDir%".
 echo MapFile: "%MapFile%.vmf".
)>"%MapFile%.log"
echo.

echo Script started at %time:~0,-3%.
echo Deleting previous compilation dumps...
if exist "%MapFile%.bsp" (
if /i not "%OnlyEnts%"=="True" (
	del /f /q "%MapFile%.bsp"> nul
	echo>>"%MapFile%.log" Deleted old compilation: "%MapName%.bsp".
)) else (if /i "%OnlyEnts%"=="True" (
	if exist "%TgBspDir%\%MapName%.bsp" (
	copy /y "%TgBspDir%\%MapName%.bsp" "%MapFile%.bsp"> nul)
))
if exist "%MapFile%.prt" (
	del /f /q "%MapFile%.prt"> nul
	echo>>"%MapFile%.log" Deleted old compilation: "%MapName%.prt".
)

::#################################
::#   New BuildCubemaps Scripts   #
::#################################

:cm_checkrun
if /i not "%BuildCMs%"=="True" (goto cm_skiprun)
echo Processing cubemaps building request...
echo.>>"%MapFile%.log"

if /i not "%OnlyEnts%"=="True" (
if /i not "%ExecVrad%"=="True" (
	%textcolor% yellow
	echo - Building cubemaps needs full compiling!
	%textcolor% grey
	goto cm_skiprun
))
if /i not "%LnchGame%"=="True" (
	%textcolor% yellow
	echo - Building cubemaps requires Run Game stage!
	%textcolor% grey
	goto cm_skiprun
)

:cm_checkmapforcm
set "CubemapsFound=0"
set "CBuilderFound=0"
echo - Checking map for cubemaps...
echo>>"%MapFile%.log" Checking map for cubemaps...
for /f "usebackq tokens=1,2" %%a in ("%MapFile%.vmf") do (
	if "%%~a"=="classname" (
	if "%%~b"=="env_cubemap" (
		set "CubemapsFound=1"
	))
	if "%%~a"=="targetname" (
	if "%%~b"=="cubemaps_builder" (
		set "CBuilderFound=1"
	))
)

:cm_chkfound
if "%CubemapsFound%"=="0" (
	echo - Cubemaps not found on this map.
	echo>>"%MapFile%.log" Cubemaps not found on this map.
	goto cm_skiprun
) else (
	echo - Cubemaps will be built on map loaded.
	echo>>"%MapFile%.log" Cubemaps will be built on map loaded.
)

:cm_addentity
if "%CBuilderFound%"=="0" (
echo - Creating build helper script...
echo>>"%MapFile%.log" Adding build helper script...
attrib -R "%MapFile%.vmf"> nul)
if "%CBuilderFound%"=="0" (
	echo entity
	echo {
	echo 	"classname" "logic_auto"
	echo 	"targetname" "cubemaps_builder"
	echo 	connections
	echo 	{
	echo 		"OnMapLoad" ",,,1.5,1,ccmd.wc_create,"
	echo 	}
	echo }
)>> "%MapFile%.vmf"

:cm_addcommand
echo>>"%MapFile%.log" Aliasing executing commands...
if /i "%SStandBy%"=="True" set "AddlCmds=alias wc_create quit"
set AddlCmds=alias wc_create "mat_specular 0; buildcubemaps; restart; mat_specular 1; %AddlCmds%"
echo>>"%MapFile%.log" String = %AddlCmds%

:cm_skiprun
echo.
echo.



:run_vbsp
if /i not "%ExecVbsp%"=="True" (goto run_vvis)
set "VbspCmdsInfo=%VbspCmds%"
if "%VbspCmds%"=="      " set "VbspCmdsInfo=[Default]"
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                        Starting VBSP compilation                            #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo Params: %VbspCmdsInfo%
echo.

(echo.
 echo.
 echo ============ Started VBSP compilation [%date%, %time:~0,-3%] =============
 echo Parameters: %VbspCmdsInfo%
)>>"%MapFile%.log"

start /b /w %Priority% vbsp.exe %VbspCmds% "%MapFile%"
if ErrorLevel 1 (goto if_error)
if not exist "%MapFile%.bsp" (goto if_error)
echo.>>"%MapFile%.log"
echo.
echo.



:run_vvis
if /i not "%ExecVvis%"=="True" (goto run_vrad)
set "VvisCmdsInfo=%VvisCmds%"
if "%VvisCmds%"=="      " set "VvisCmdsInfo=[Default]"
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                        Starting VVIS compilation                            #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo Params: %VvisCmdsInfo%
echo.

(echo.
 echo.
 echo ============ Started VVIS compilation [%date%, %time:~0,-3%] =============
 echo Parameters: %VvisCmdsInfo%
)>>"%MapFile%.log"

start /b /w %Priority% vvis.exe %VvisCmds% "%MapFile%"
if ErrorLevel 1 (goto if_error)
if not exist "%MapFile%.prt" (goto if_error)
echo.>>"%MapFile%.log"
echo.
echo.



:run_vrad
if /i not "%ExecVrad%"=="True" (goto copy_file)
set "VradCmdsInfo=%VradCmds%"
if "%VradCmds%"=="      " set "VradCmdsInfo=[Default]"
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                        Starting VRAD compilation                            #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo Params: %VradCmdsInfo%
echo.

(echo.
 echo.
 echo ============ Started VRAD compilation [%date%, %time:~0,-3%] ============
 echo Parameters: %VradCmdsInfo%
)>>"%MapFile%.log"

start /b /w %Priority% vrad.exe %VradCmds% "%MapFile%"
if ErrorLevel 1 (goto if_error)
echo.>>"%MapFile%.log"
echo.
echo.



:copy_file
if /i not "%PlaceBsp%"=="True" (goto patch_bsp)
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                    Copying BSP file to game directory                       #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo.
echo Source path: "%MapFile%.bsp"
echo Destination: "%TgBspDir%\"
if not exist "%TgBspDir%" (md "%TgBspDir%">nul)

(echo.
 echo.
 echo ============ Managing compiled files [%date%, %time:~0,-3%] =============
 echo.
)>>"%MapFile%.log"

echo.
echo Deleting previous compilation...
echo>>"%MapFile%.log" Deleting previous compilation...
if exist "%TgBspDir%\%MapName%.bsp" (
	del /f /q "%TgBspDir%\%MapName%.bsp"> nul
	echo>>"%MapFile%.log" - Deleted: "%TgBspDir%\%MapName%.bsp".
) else (
	echo>>"%MapFile%.log" - Nothing to delete.
)

echo Placing file to BSP directory...
(echo Placing file to BSP directory...
 echo - Source path: "%MapFile%.bsp"
 echo - Destination: "%TgBspDir%\"
)>>"%MapFile%.log"
if exist "%MapFile%.bsp" (
	copy /y "%MapFile%.bsp" "%TgBspDir%\"> nul
	echo>>"%MapFile%.log" - File succesfully copied.
) else (
	echo Error: File "%MapFile%.bsp" not found.
	echo>>"%MapFile%.log" - Error: File "%MapFile%.bsp" not found.
	echo.
)

echo Deleting compilation dumps...
echo>>"%MapFile%.log" Deleting compilation dumps...
if "%DeletePRT%"=="1" (
if exist "%MapFile%.prt" (
	del /f /q "%MapFile%.prt"> nul
	echo>>"%MapFile%.log" - Deleted: "%MapFile%.prt".
) else (
	echo>>"%MapFile%.log" - No prt file exist.
))
if "%DeleteBSP%"=="1" (
if exist "%MapFile%.bsp" (
	del /f /q "%MapFile%.bsp"> nul
	echo>>"%MapFile%.log" - Deleted: "%MapFile%.bsp".
) else (
	echo>>"%MapFile%.log" - No bsp file exist.
))
echo.
echo.



:patch_bsp
if /i not "%PatchBSP%"=="True" (goto run_game)
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                    Importing patched content into BSP                       #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo.
echo Map File: "%MapName%.bsp"

(echo.
 echo.
 echo =========== Importing patched content [%date%, %time:~0,-3%] ============
 echo.
)>>"%MapFile%.log"

:check_bsp
if not exist "%TgBspDir%\%MapName%.bsp" (
if not exist "%MapFile%.bsp" (
	%textcolor% red
	echo Internal error: "%MapName%.bsp" not found at
	echo "%TgBspDir%\";
	echo "%VmfPath%".
	echo Unable to continue.
	%textcolor% grey
	(echo Internal Error! "%MapName%.bsp" not found in
	 echo "%TgBspDir%\";
	 echo "%VmfPath%".
	)>>"%MapFile%.log"
	goto bspzip_err
) else (set "bspfile=%MapFile%.bsp")
) else (set "bspfile=%TgBspDir%\%MapName%.bsp")
echo>>"%MapFile%.log" Target BSP file: "%bspfile%"

:check_pdata
if not exist "%MapFile%_patch\*" (
if not exist "%TgBspDir%\%MapName%_patch\*" (
	%textcolor% yellow
	echo Patch data not presented for "%MapName%"!
	%textcolor% grey
	echo.
	echo - Create "%%mapname%%_patch" directory near your map's VMF file
	echo - or in game "maps" folder and place your custom content into
	echo - with the similar to game's folder structure and hierarchy.
	echo.
	echo - You may include the custom cubemaps, materials, models etc.
	echo - When the including stage is enabled, it'll be automatically
	echo - packed into the compiled .BSP file using the BspZip tool...
	echo>>"%MapFile%.log" Patching data at "%MapName%_patch\" not found.
	goto bspzip_err
))
echo.

if not exist "bspzip.exe" (
	%textcolor% red
	echo BspZip.exe not found at directory
	echo "%cd%"!
	echo>>"%MapFile%.log" BspZip.exe not found in "%cd%\".
	%textcolor% grey
	goto bspzip_err
) else (set "BspZip=%cd%\bspzip.exe")

set cpfl_num=0
for %%f in (
	"%MapFile%_patch"
	"%TgBspDir%\%MapName%_patch"
) do if exist "%%~f\*" (
	echo>>"%MapFile%.log" Patch directory: "%%~f"
	pushd "%%~f\"
	for /d %%m in (*) do call :bspzip_proc "%%~m"
	popd
)
if not "%cpfl_num%"=="0" echo.
echo %cpfl_num% files included into "%MapName%.bsp".
echo>>"%MapFile%.log" %cpfl_num% files included.

:bspzip_err
echo.
echo.



:run_game
if /i not "%LnchGame%"=="True" (goto show_time)
set "GameCmdsInfo=%GameCmds%"
if "%GameCmds%"=="      " set "GameCmdsInfo=[None]"
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                             Starting Engine                                 #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo.
echo GameDir: "%ModDir%"
echo GameExe: "%GExeFull%"
echo MapFile: "%MapName%.bsp"
echo Params: %GameCmdsInfo%
echo.

(echo.
 echo.
 echo ============= Starting map in game [%date%, %time:~0,-3%] ==============
 echo.
 echo GameDir: "%ModDir%"
 echo GameExe: "%GExeFull%"
 echo MapFile: "%MapName%.bsp"
 echo Params:  %GameCmdsInfo%
)>>"%MapFile%.log"

:check_beh
set RunKey=
if /i "%SStandBy%"=="True" (
	set "RunKey=/wait"
if /i not "%BuildCMs%"=="True" (
	%textcolor% yellow
	echo Running game is not allowed while "turn off machine" specified.
	%textcolor% grey
	goto rungame_err
))

:check_exe
if /i not "%GExeExtn%"==".exe" (
	%textcolor% red
	echo Error: Wrong game EXE file specified!
	%textcolor% grey
	(echo.
	 echo Error: Wrong game EXE file specified!
	)>>"%MapFile%.log"
	goto rungame_err
)

:run_engine
call :killproc "%GExeFile%"
pushd "%GExePath%"
set "PATH=%~dp0;%PATH%"
start %RunKey% "game" "%GExeFile%" -game %ModName% +map "%MapName%" +%AddlCmds% %GameCmds%
popd

:rungame_err
echo.


:show_time
for %%m in ("%ExecVbsp%" "%ExecVvis%" "%ExecVrad%") do (
	if /i "%%~m"=="True" goto show_ok)
goto close_log

:show_ok
echo.>>"%MapFile%.log"
echo.>>"%MapFile%.log"
call :get_elapsedtime
echo.


:close_log
(echo.
 echo.
 echo ================ Log closed [%date%, %time:~0,-3%] =================
)>>"%MapFile%.log"
%textcolor% green
echo Finished.
%textcolor% grey


:turnoff
if /i "%SStandBy%"=="True" (
	%textcolor% cyan
	echo Turning machine to Standby mode...
	ping>nul "127.0.0.1" -n 4
	rundll32.exe powrprof.dll,SetSuspendState
	%textcolor% grey
)


:quit
if exist "%RMCfg%" (
del /a /q "%RMCfg%"> nul)

if /i "%PauseWin%"=="True" (
	pause> nul) else (
	ping>nul "127.0.0.1" -n 2
)
exit



:=======================================================
:bspzip_proc
:recurse_dirs
	for /d %%d in ("%~1\*") do (
	for %%f in ("%%~d\*") do call :bspzip_pack "%%~f"
	call :recurse_dirs "%%~d")
exit /b

:bspzip_pack
	set "cur_file=%~1"
	set /A "cpfl_num=%cpfl_num%+1"
	echo - Adding: "%cur_file:\=/%"
	echo>>"%MapFile%.log" - Adding: "%cur_file:\=/%"
	"%BSPZip%" -addfile "%bspfile%" "%cur_file:\=/%" "%cur_file%" "%bspfile%"
exit /b

:=======================================================
:if_error
	echo.
	%textcolor% yellow
	echo __________________________________________
	echo.
	%textcolor% red
	echo [-] An error occured during compiling your map.
	echo [-] See console log for more details.
	%textcolor% grey
	(echo.
	 echo.
	 echo ================ Log closed [%date%, %time:~0,-3%] =================
	)>>"%MapFile%.log"
	pause > nul
	exit
exit /b

:get_starttime
	for /F "tokens=1-4 delims=:.," %%a in ("%time%") do (
	   set /A "startt=(((%%~a*60)+1%%~b %% 100)*60+1%%~c %% 100)*100+1%%~d %% 100"
	)
exit /b

:get_elapsedtime
	:: get end time:
	for /F "tokens=1-4 delims=:.," %%a in ("%time%") do (
	   set /A "endt=(((%%~a*60)+1%%~b %% 100)*60+1%%~c %% 100)*100+1%%~d %% 100"
	)

	:: get elapsed time:
	set /A "elapsedt=endt-startt"

	:: show elapsed time:
	set /A "hh=elapsedt/(60*60*100), rest=elapsedt%%(60*60*100), mm=rest/(60*100), rest%%=60*100, ss=rest/100, cc=rest%%100"

	:: short variant
	rem if %mm% lss 10 set "mm=0%mm%"
	rem if %ss% lss 10 set "ss=0%ss%"
	rem if %cc% lss 10 set "cc=0%cc%"
	rem set "hh=%hh%:"
	rem set "mm=%mm%:"
	
	:: writing variant
	if "%hh%"=="0" (set "hh=") else (if "%hh%"=="1" (set "hh=1 hour ")   else (set "hh=%hh% hours "))
	if "%mm%"=="0" (set "mm=") else (if "%mm%"=="1" (set "mm=1 minute ") else (set "mm=%mm% minutes "))
	if "%hh%%mm%"=="" (set "ss=%ss%,%cc% seconds") else (if "%ss%"=="1" (set "ss=%ss% second") else (set "ss=%ss% seconds")) 
	
	echo __________________________________________
	echo.
	%textcolor% yellow
	echo Total time: %hh%%mm%%ss%.
	%textcolor% grey
	echo __________________________________________
	echo>>"%MapFile%.log" All operations completed.
	echo>>"%MapFile%.log" Total time: %hh%%mm%%ss%.
exit /b

:killproc
	for /f "tokens=1" %%m in ('tasklist /NH') do (
	if /i "%%~m"=="%~1" (taskkill /f /im "%~1"> nul))
exit /b

:rem_empties
	for /D %%A in ("%~1\*") do (
		call :rem_empties "%%~fA"
	)
	rd "%~f1"> nul 2>&1
exit /b
