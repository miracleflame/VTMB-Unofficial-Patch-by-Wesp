:: written by: psycho-a
:: program version: 2.7
:: build date: 03.03.17

@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
set "ProgVersion=2.7"
title Bloodlines VPK Creator v%ProgVersion%  (c) Psycho-A
color 06
pushd "%~dp0"

:==============================================================================
:Readme
:==============================================================================

cls
echo    ีอออออออออออออออออออออออออออธ
echo    ณ V-BLOODLINES VPK CREATOR  ณ
echo    ณ Version: %ProgVersion% (c) Psycho-A ณ
echo    ิอออออออออออออออออออออออออออพ
echo.
echo     This tool allows you to create your own VPK archives
echo     from specific directories or entire games and mods.
echo.
echo     Press any key to enter the program menu...

pause > nul




:========================================================================================================
:Prepare
:========================================================================================================

:Vars
set "VCHome=%CD%"
set "VCConfig=%VCHome%\Config.ini"
set "SfkTool=%VCHome%\..\..\service\sfk.exe"
set "VBuilder=%VCHome%\service\vpkbuilder.exe"
set "PackDirsList=%VCHome%\pack_dirs.txt"

set Wait=call :WaitFunc
set ViewReadme=start "" "%VCHome%\Readme.txt"

set MergingMode=1

:==============================================================================
:DetectPaths

pushd ..\..
if exist "GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
	if /i "%%~a"=="ModDir" (
		set "ModDirFull=%%~b"
		set "ModDir=%%~nb"
	)
	if /i "%%~a"=="GameExeDir" (pushd "%%~b")
)) else (
	pushd ..
	set "ModDirFull=%CD%\..\Vampire"
	set "ModDir=Vampire"
)

:==============================================================================
:CheckFiles

for %%M in (
	"%VCConfig%"
	"%SfkTool%"
	"%VBuilder%"
	"%ModDirFull%"
	"%VCHome%\Readme.txt"
	"%VCHome%\service\KillApps.exe"
	"%VCHome%\service\Empty.vpk"
) do (
	if not exist "%%~M" (
		color 0c
		cls
		echo.
		echo     ERROR: "%%~M" not found.
		echo.
		echo     Cannot proceed.
		echo.
		%Wait% 5
		exit
	)
)

pushd "%ModDir%"









:========================================================================================================
:StartMenu
:========================================================================================================
if exist "%PackDirsList%" (
del /f /q "%PackDirsList%"> nul)

cls
color 06
echo    ีอออออออออออออออออออออออออออธ
echo    ณ V-BLOODLINES VPK CREATOR  ณ
echo    ิอออออออออออออออออออออออออออพ
echo     Current game: ["%ModDir%"]
echo.
echo     What action you want to do?
echo.
echo     1. Pack specific folders;
echo     2. Pack all game content;
echo     3. Pack localized resources;
echo     4. Build dir tree (vpk header);
echo     5. View the readme file;
echo     6. Quit the program.
echo.

set "Choice="
set /p "Choice=>   Your choice: "

if "%Choice%"=="1" (goto PackSingle)
if "%Choice%"=="2" (goto PackAll)
if "%Choice%"=="3" (goto PackLocals)
if "%Choice%"=="4" (goto PackDrTree)
if "%Choice%"=="5" (%ViewReadme%)
if "%Choice%"=="6" (exit)
goto StartMenu












:========================================================================================================
:PackSingle
:========================================================================================================

cls
color 06
echo.
echo     Enter the directory name you want to be packed.
echo     Subfolders inside of this will be packed too.
echo.
echo     You can define up to 12 directories simultaneously.
echo     To finish, just leave field empty and press "Enter".
echo.

for %%m in (
01 02 03 04 05 06 07 08 09 10 11 12
) do (set "DirToPack%%~m=")

set /p "DirToPack01=>   Directory 01: "
if "%DirToPack01%"=="" (goto PackSingle)
set /p "DirToPack02=>   Directory 02: "
if "%DirToPack02%"=="" (goto PackSingleStart)
set /p "DirToPack03=>   Directory 03: "
if "%DirToPack03%"=="" (goto PackSingleStart)
set /p "DirToPack04=>   Directory 04: "
if "%DirToPack04%"=="" (goto PackSingleStart)
set /p "DirToPack05=>   Directory 05: "
if "%DirToPack05%"=="" (goto PackSingleStart)
set /p "DirToPack06=>   Directory 06: "
if "%DirToPack06%"=="" (goto PackSingleStart)
set /p "DirToPack07=>   Directory 07: "
if "%DirToPack07%"=="" (goto PackSingleStart)
set /p "DirToPack08=>   Directory 08: "
if "%DirToPack08%"=="" (goto PackSingleStart)
set /p "DirToPack09=>   Directory 09: "
if "%DirToPack09%"=="" (goto PackSingleStart)
set /p "DirToPack10=>   Directory 10: "
if "%DirToPack10%"=="" (goto PackSingleStart)
set /p "DirToPack11=>   Directory 11: "
if "%DirToPack11%"=="" (goto PackSingleStart)
set /p "DirToPack12=>   Directory 12: "
if "%DirToPack12%"=="" (goto PackSingleStart)


:=======================================
:PackSingleStart

(echo=%DirToPack01%
 echo=%DirToPack02%
 echo=%DirToPack03%
 echo=%DirToPack04%
 echo=%DirToPack05%
 echo=%DirToPack06%
 echo=%DirToPack07%
 echo=%DirToPack08%
 echo=%DirToPack09%
 echo=%DirToPack10%
 echo=%DirToPack11%
 echo=%DirToPack12%
)> "%PackDirsList%"

:=======================================
:ValidateDirs
set InvalidsFound=0
for /f "usebackq delims=" %%f in ("%PackDirsList%") do (call :VDFunc "%%~f")
if "%InvalidsFound%"=="1" (goto PackSingle)
goto PackSingleSetMode

:VDFunc
	if not exist "%CD%\%~1\*" (
		cls
		color 0c
		echo.
		echo     Error! Folder "%~1" not found at "%ModDir%" game directory!
		set InvalidsFound=1
		%Wait% 3
		exit /b
	)
	set DirIsValid=0
	for /f "usebackq eol=# delims=	= tokens=1,2" %%a in ("%VCConfig%") do (
		if /i "%%~a"=="Dir" (if /i "%%~b"=="%~1" (set "DirIsValid=1") )
	)
	if "%DirIsValid%"=="0" (
		cls
		color 0e
		echo.
		echo     Error! Directory "%~1" cannot be packed since it
		echo     not contains data that is valid for VPK file system.
		set InvalidsFound=1
		%Wait% 3
		exit /b
	)
exit /b

:=======================================
:PackSingleSetMode
cls
color 06
echo.
echo     Select desired mode in which the folders will be packed:
echo.
echo     1. Intelligently separate packs depending on folders' content.
echo     2. Use single vpk for all specified folders (if size is small).
echo.
set MergingMode=
set /p "MergingMode=>   Your choice: "

if not "%MergingMode%"=="1" (
if not "%MergingMode%"=="2" (
goto PackSingleSetMode))

:=======================================
:PackSingleBegin

color 03
call :StartBuilder
call :FinalFileOperations

:=======================================
:PackSingleFinalize
cls
color 02
echo.
echo     Packs with selected folders were successfully
echo     created and placed into "%ModDir%" folder as
echo     %FinalPackNames%.
echo     Delete unpacked versions of these directories?
echo.
echo     1 - Yes; 2 - No (keep them and back to menu).
echo.
set "Choice="
set /p "Choice=>   Your choice: "

if "%Choice%"=="1" (
	call :DelUnpackedVersions
	echo.
	echo     All selected directories deleted.
	echo.
	%Wait% 4
	goto StartMenu
)
if "%Choice%"=="2" (goto StartMenu)
goto PackSingleFinalize














:========================================================================================================
:PackAll
:========================================================================================================

cls
color 06
echo.
echo     Warning: before doing this action make sure that ALL of
echo     your game resources are unpacked. Otherwise, the packed 
echo     version of the game will not be playable. To only pack
echo     some game content, please use point "1" of main menu.
echo.
echo     Type '1' to start or '2' to return...
echo.
set "Choice="
set /p "Choice=>   Your choice: "

if "%Choice%"=="1" (goto PackAllBegin)
if "%Choice%"=="2" (goto StartMenu)
goto PackAll

:=======================================
:PackAllBegin

color 03
call :BuildVpkIndex
type nul>"%PackDirsList%"
for /f "usebackq eol=# delims=	= tokens=1,2" %%a in ("%VCConfig%") do (
if /i "%%~a"=="Dir" (if exist "%CD%\%%~b\*" (echo %%~b>> "%PackDirsList%")) )

call :StartBuilder +proclocales
call :FinalFileOperations

:=======================================
:PackAllFinalize
cls
echo.
echo     All the game resources have been packed.
echo     Some resource types were not packed, so they were
echo     kept as they are. See "%ModDir%" dir for details.
echo.
echo     Delete unpacked versions of directories?
echo     They will no longer be used by the game.
echo.
echo     1 - Yes; 2 - No (back to main menu).
echo.
set "Choice="
set /p "Choice=>   Your choice: "

if "%Choice%"=="1" (
	call :DelUnpackedVersions
	echo.
	echo     All directories were deleted. 
	echo     Your unpacked game was converted into a packed one.
	echo.
	%Wait% 5
	goto StartMenu
)
if "%Choice%"=="2" (goto StartMenu)
goto PackAllFinalize













:========================================================================================================
:PackLocals
:========================================================================================================

cls
color 06
echo.
echo     This procedure will pack only the resources
echo     that are suitable for language translation.
echo.
echo     These are dialogue and subtitles data, menu
echo     and HUD interfaces, fonts and some textures.
echo.
echo     Type '1' to start or '2' to return...
echo.
set "Choice="
set /p "Choice=>   Your choice: "

if "%Choice%"=="1" (goto PackLocalsBegin)
if "%Choice%"=="2" (goto StartMenu)
goto PackLocals

:=======================================
:PackLocalsBegin

cls
color 03
echo.
echo     Running building programs...
echo     Please wait until the process ends.
echo.
for /f "usebackq eol=# delims=	= tokens=1,2,3,4" %%l in ("%VCConfig%") do (
	if /i "%%~l"=="Loc" if exist "%CD%\%%~m\*" (
		echo     Preparing "%%~m" content...
		call :ProcLocalized "%%~m" "" -nodelete
	)
)
if exist "%CD%\_pack_loc\*" (
	echo     Packing localized resources...
	"%VBuilder%" "zzz_localized.vpk" "_pack_loc"> nul
	rd /s /q "_pack_loc"> nul
)

call :FinalFileOperations

:=======================================
:PackLocalsFinalize
cls
color 02
echo.
echo     Existing localized resources were succesfully packed
echo     and placed into '%ModDir%\' as %FinalPackNames% file.
echo.
echo     You may delete the unpacked version of these resources
echo     since they no longer will be used in game. Do it now?
echo.
echo     1 - Yes; 2 - No (back to main menu).
echo.
set "Choice="
set /p "Choice=>   Your choice: "

if "%Choice%"=="1" (
	call :DelUnpackedVersions -locals
	echo.
	echo     All unpacked localized resources deleted. 
	echo.
	%Wait% 5
	goto StartMenu
)
if "%Choice%"=="2" (goto StartMenu)
goto PackLocalsFinalize

%Wait% 5
goto StartMenu













:========================================================================================================
:PackDrTree
:========================================================================================================

cls
color 06
echo.
echo     Index building is necessary in case the game directories were
echo     packaged separately (as in point "1" of menu). This creates 
echo     an additional directory index that is required for the correct
echo     work of some types of resources.
echo.
echo     Remember that ALL the game's directories should have it's 
echo     unpacked versions, otherwise VPK header will not be full.
echo.
echo     Type '1' to start or '2' to return...
echo.
set "Choice="
set /p "Choice=>   Your choice: "

if "%Choice%"=="1" (goto PackIndexBegin)
if "%Choice%"=="2" (goto StartMenu)
goto PackDrTree

:=======================================
:PackIndexBegin

color 03
call :BuildVpkIndex
call :FinalFileOperations

:=======================================
cls
color 02
echo.
echo     Directory index was built successfully.
echo     Total number of directories: %DirNum%.
echo.
echo     Placed into '%ModDir%\' as %FinalPackNames%.

%Wait% 5
goto StartMenu










:========================================================================================================
:FunctionCalls
:========================================================================================================

:=======================================
:StartBuilder
	cls
	echo.
	echo     Starting VPK Builder...
	echo     Please wait until the process ends.
	echo.
	for /f "usebackq delims=|" %%f in ("%PackDirsList%") do (
		for /f "usebackq eol=# delims=	= tokens=1,2,3,4" %%w in ("%VCConfig%") do (
			if /i "%%~w"=="Dir" if /i "%%~x"=="%%~f" (
				echo     Preparing "%%~f" files...
				if not "%%~z"=="" (
					if /i "%%~y"=="Sep" (
					if "%MergingMode%"=="1" (
						"%SfkTool%" copy "%%~f" "_pack_sep\%%~f" -file %%~z -yes> nul
						if /i "%~1"=="+proclocales" (call :ProcLocalized "%%~f" "_pack_sep\")
						echo     Packing "%%~f" content...
						"%VBuilder%" "zzz_pak-%%~f.vpk" "_pack_sep"> nul
						rd /s /q "_pack_sep"> nul
					) else (
						"%SfkTool%" copy "%%~f" "_pack_com\%%~f" -file %%~z -yes> nul
					))
					if /i "%%~y"=="Com" (
						"%SfkTool%" copy "%%~f" "_pack_com\%%~f" -file %%~z -yes> nul
						if /i "%~1"=="+proclocales" (call :ProcLocalized "%%~f" "_pack_com\")
					)
				)
			)
		)
	)
	if exist "%CD%\_pack_com\*" (
		echo     Packing other/merged content...
		"%VBuilder%" "zzz_pak-vbmergeds.vpk" "_pack_com"> nul
		rd /s /q "_pack_com"> nul
	)
	if /i "%~1"=="+proclocales" (
	if exist "%CD%\_pack_loc\*" (
		echo     Packing localized resources...
		"%VBuilder%" "zzz_localized.vpk" "_pack_loc"> nul
		rd /s /q "_pack_loc"> nul
	))

exit /b

:=======================================
:ProcLocalized
for /f "usebackq eol=# delims=	= tokens=1,2,3,4" %%l in ("%VCConfig%") do (
	if /i "%%~l"=="Loc" if /i "%%~m"=="%~1" if exist "%~2%%~m\%%~n\" (
		"%SfkTool%" copy "%~2%%~m\%%~n" "_pack_loc\%%~m\%%~n" -file %%~o -yes> nul
		if /i not "%~3"=="-nodelete" (
		"%SfkTool%" del -withdirs "%~2%%~m\%%~n" %%~o -yes> nul)
	)
)
exit /b

:=======================================
:BuildVpkIndex
	cls
	echo.
	echo     Building VPK index, please wait...
	echo     Preparing...
	pushd "%VCHome%"

	dir /b /s /a:d "%ModDirFull%\"> "dirlst.lst"
	"%SfkTool%" replace "dirlst.lst" "|%ModDirFull%\||" -quiet -yes> nul
	"%SfkTool%" replace "dirlst.lst" "|\|/|" -quiet -yes> nul

	set DirNum=0
	copy /y "service\Empty.vpk" "%ModDirFull%\zzz_vpk-index.vpk"> nul
	for /f "usebackq delims=" %%m in ("dirlst.lst") do (
		cls
		echo.
		echo     Building VPK index, please wait...
		echo     Processing: "%%~m"
		"%SfkTool%" linelen "%%~m" +hex -digits=2 +filter -form "$col1+000000" +hextobin "cchunk.bin" -quiet
		"%SfkTool%" replace "cchunk.bin" -spat "|\x00\x00\x00|\x00\x00\x00%%~m\x00\x00\x00\x00\x00\x00\x00\x00|" -quiet -yes> nul
		copy /b "%ModDirFull%\zzz_vpk-index.vpk" + "cchunk.bin" "%ModDirFull%\zzz_vpk-index.vpk"> nul
		call :CountDirs
	)

	cls
	echo.
	echo     Finalizing...
	"%SfkTool%" echo %DirNum% +hex -digits=4 +filter -lsrep "|??||" +hextobin "sbyte1.bin" -quiet> nul
	"%SfkTool%" echo %DirNum% +hex -digits=4 +filter -lerep "|??||" +hextobin "sbyte2.bin" -quiet> nul
	"%SfkTool%" echo 00000000000001 +hextobin "cchunk.bin" -quiet> nul
	copy /b "%ModDirFull%\zzz_vpk-index.vpk" + "sbyte1.bin" + "sbyte2.bin" + "cchunk.bin" "%ModDirFull%\zzz_vpk-index.vpk"> nul

	del /f /q sbyte?.bin cchunk.bin dirlst.lst> nul
	popd
exit /b
	
:CountDirs
	set /A "DirNum=%DirNum%+1"
exit /b

:=======================================
:FinalFileOperations

for %%D in ("%CD%\zzz_?*.vpk") do (
if exist "%%~D" (if %%~zD LEQ 20 (del /f /q "%%~D"> nul)))

:CheckVpkExist
if not exist "%CD%\zzz_?*.vpk" (
	cls
	color 0c
	echo.
	echo     ERROR: VPK files were not created. 
	echo.
    echo     Maybe an error occured or an invalid/empty path was specified.
	echo.
	%Wait% 5
	goto StartMenu
) else (call :ProcessFiles)
exit /b

:ProcessFiles
	set FinalPackNames=
	if exist "%CD%\pack0??.vpk" (
		for %%D in ("pack0??.vpk") do (call :ProcessNamesInDir "%%~D")
	) else (set "ResultNum=-1")
	for %%P in ("zzz_???-??*.vpk") do (call :ProcessNamesInPak "%%~P" 0)
	if exist "%CD%\pack1??.vpk" (
		for %%D in ("pack1??.vpk") do (call :ProcessNamesInDir "%%~D")
	) else (set "ResultNum=-1")
	for %%P in ("zzz_local?*.vpk") do (call :ProcessNamesInPak "%%~P" 1)
exit /b

:ProcessNamesInDir
	set "DecPlHd="
	set "NameTmp=%~n1"
	set "ResultNum=%NameTmp:~-2%"

	if not "%ResultNum:~-1%"=="0" (
	set "ResultNum=%ResultNum:0=%") else (
	set "ResultNum=%ResultNum:00=0%")
exit /b

:ProcessNamesInPak
	set /a "ResultNum=%ResultNum%+1"
	if %ResultNum% LSS 10 (set "DecPlHd=0") else (set "DecPlHd=")
	if defined FinalPackNames (
		set "FinalPackNames=%FinalPackNames%, 'pack%~2%DecPlHd%%ResultNum%.vpk'") else (
		set "FinalPackNames='pack%~2%DecPlHd%%ResultNum%.vpk'"
	)
	move /y "%~1" "pack%~2%DecPlHd%%ResultNum%.vpk"
exit /b

:=======================================
:DelUnpackedVersions
	cls
	color 03
	echo.
	echo     Stopping hindering apps...
	call "%VCHome%\service\KillApps.exe"
	echo     Deleting folders...
	echo.
	if /i not "%~1"=="-locals" (
		for /f "usebackq delims=|" %%f in ("%PackDirsList%") do (
		for /f "usebackq eol=# delims=	= tokens=1,2,3,4" %%w in ("%VCConfig%") do (
			if /i "%%~w"=="Dir" if /i "%%~x"=="%%~f" (
				echo     Deleting "%%~f"...
				"%SfkTool%" del -withdirs "%%~f" %%~z -yes> nul
			)
		))
	) else (
		for /f "usebackq eol=# delims=	= tokens=1,2,3,4" %%l in ("%VCConfig%") do (
			if /i "%%~l"=="Loc" if exist "%CD%\%%~m\%%~n\*" (
				if not "%%~n"=="." (echo     Deleting "%%~m\%%~n"...) else (echo     Deleting "%%~m"...)
				"%SfkTool%" del -withdirs "%%~m\%%~n" %%~o -yes> nul
			)
		)
	)
	echo     Deleting unused trash...
	"%SfkTool%" del! -withdirs "%CD%" .tmp .bak .old .gam~ .dsp> nul
	call :RemEmptyDirs "%CD%"
exit /b

:=======================================
:RemEmptyDirs
	for /D %%A in ("%~1\*") do (
		call :RemEmptyDirs "%%~fA"
	)
	rd "%~f1"> nul 2>&1
exit /b

:=======================================
:WaitFunc
	if "%~1"=="" (
	ping>nul -n 3 "127.0.0.1") else (
	ping>nul -n %~1 "127.0.0.1")
exit /b
