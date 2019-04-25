@echo off
set ProgVersion=1.9-beta

setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title Texture Converter v%ProgVersion%  (c) Psycho-A
pushd "%~dp0"
color 47

:UserDefs
::: For VTF to TTh mode:
set ProcessThumbnails=1
set CompressImageData=1
set AutoFixVtfVersion=1
set DeleteSourceVtfs=1

::: For TTz to Img mode:
set ExportFormat=tga

::: For Any to TTh mode:
set OutputFormat=Auto
: supported values: Auto, Compressed, Uncompressed
set UseTemplates=1
: use Templates.ini to detect format and vmt layout
set AutoCreateVmts=1
: creates .vmt file if source is in materials/ dir


:Vars
set Sfk="..\..\service\sfk.exe"
set MsgBox="..\..\service\msgbox.exe"
set OpenDlg="..\..\service\OpenDlg.exe"
set FileTypes="service\filetypes.bat"
set ZLib="service\zlib1.exe"
set TtzDec="service\Ttz2Vtf.exe"
set VtfCmd="VtfCmd.exe"
set Templates="Templates.ini"
set "TempDir=%cd%\temp"

set Validate=call :Validate
set OpenFile=call %OpenDlg% /f /m

:CheckFiles
for %%m in (
%Sfk% %MsgBox% %ZLib% %OpenDlg% %TtzDec% %VtfCmd% %FileTypes% service\zlib1.dll
) do (
	if not exist "%%~m" (
		color 4e
		echo Can't find "%%~m"!
		echo>>"..\..\..\sdk_errors.log" [%date% %time%] TexConvert Error: Missing "%cd%\%%~m" file.
		ping>nul "127.0.0.1" -n 2
		goto Exit
	)
)

:AssignFiles
if "%~1%~2"=="" call "%FileTypes%" -int



:================================================
:Initialize
call :ShowLogo
if not exist "%TempDir%\" md "%TempDir%"

if /i "%~1"=="-shellmode" set "ShellMode=1"
if /i "%~2"=="-tovtf" set "ConvertMode=ToVtf"
if /i "%~3"=="-tovtf" set "ConvertMode=ToVtf"
if /i "%~2"=="-toimg" set "ConvertMode=ToImg"
if /i "%~3"=="-toimg" set "ConvertMode=ToImg"
if /i "%~2"=="-tottz" set "ConvertMode=ToTtz"
if /i "%~3"=="-tottz" set "ConvertMode=ToTtz"

if "%~x1%~x2"=="" (
	if "%ShellMode%"=="1" goto ShellModeProcs
	set "GUIMode=1"
	echo  Features:
	echo   [1] Compiling Valve's VTFs to Bloodline's TTH+TTZs;
	echo   [2] Decompiling TTH and TTZs back to VTFs and TGAs;
	echo   [3] Creating TTZ/VTF from TGA/DDS/BMP/PNG/JPEG/GIF.
	echo.
	echo  Alternative usage modes:
	echo   [1] Use "SdkBinaries/Tools/Texture Utils/%~n0.bat" "imagefile";
	echo   [2] Use Explorer context menu item [if Bloodlines SDK installed];
	echo   [3] Drag'n'drop source images to %~n0.bat executable.
	echo.
	echo  Please, select input files to convert...
	echo  You may convert multiple files at once.
	echo.
)





:================================================
:RunCmdProc
:================================================

if "%GUIMode%"=="1" (goto GUIMode)
for %%f in (%*) do (call :ConvertAll "%%~f")

echo.
echo Finished.
if not "%ShellMode%"=="1" (
ping>nul -n 4 "127.0.0.1" )
goto Exit





:================================================
:GUIMode
:================================================

set "ClrStScDone=No"
set "ConvProcRan=No"
set "ErrorsFound=No"
set "SomeSuccess=No"

for /f "delims=" %%f in (
'%OpenFile% "/e=*.vtf *.tth *.tga *.dds *.bmp *.png *.jpg *.gif"'
) do (call :ConvertAll "%%~f")
if /i "%ConvProcRan%"=="No" (goto Exit)

if /i "%ErrorsFound%"=="Yes" (
	if /i "%SomeSuccess%"=="Yes" (%MsgBox% Converting textures done. Some errors occured during this procedure, see the console window for details. Select other files? /c:Texture Converter - Information /t:MB_SYSTEMMODAL,MB_ICONWARNING,MB_YESNO)
	if /i "%SomeSuccess%"=="No"  (%MsgBox% Converting textures failed. Some errors occured during this procedure, see the console window for details. Select other files? /c:Texture Converter - Information /t:MB_SYSTEMMODAL,MB_ICONERROR,MB_YESNO)
) else (
	%MsgBox% All textures successfully converted. Select other files? /c:Texture Converter - Information /t:MB_SYSTEMMODAL,MB_ICONINFORMATION,MB_YESNO
)
if "%ErrorLevel%"=="6" goto Initialize
if "%ErrorLevel%"=="7" goto Exit





:================================================
:IMG2TTZ
:================================================

rem Clear startup screen...
if "%ClrStScDone%"=="No" (call :ShowLogo)
set "ClrStScDone=Yes"
set "ConvProcRan=Yes"

rem Check & prepare...
if exist "error.init" (del /f /q "error.init")
echo Converting "%~nx1"...
call :ReadTemplates

rem Run VTFCmd tool...
echo   Pre-compiling to VTF..
call :MakeVtf "%~1" "%TempDir%"
%Validate% "%TempDir%\%~n1.vtf"
if exist "error.init" goto QuitFunc

rem Compile to TTZ...
echo   Compiling to TTh+TTz..
call :VTF2TTZ "%TempDir%\%~n1.vtf" -noinfo
%Validate% "%TempDir%\%~n1.tth"
%Validate% "%TempDir%\%~n1.ttz"
if exist "error.init" goto QuitFunc

rem Move to source folder...
move /y "%TempDir%\%~n1.tth" "%~dp1\"> nul
move /y "%TempDir%\%~n1.ttz" "%~dp1\"> nul
%Validate% "%~dpn1.tth"
%Validate% "%~dpn1.ttz"
if exist "error.init" goto QuitFunc

goto QuitFunc





:================================================
:IMG2VTF
:================================================

rem Clear startup screen...
if "%ClrStScDone%"=="No" (call :ShowLogo)
set "ClrStScDone=Yes"
set "ConvProcRan=Yes"

rem Check & prepare...
if exist "error.init" (
del /f /q "error.init")
echo Converting "%~nx1"...
call :ReadTemplates

rem Run VTFCmd tool...
echo   Running VTF compiling tool...
call :MakeVtf "%~1" "%TgtPath%"
%Validate% "%~dpn1.vtf"
if exist "error.init" goto QuitFunc

rem Get obtained Vtf size...
for %%s in ("%~dpn1.vtf") do (
	echo   Obtained VTF size: %%~zs bytes.
)

goto QuitFunc





:================================================
:VTT2IMG
:================================================

rem Clear startup screen...
if "%ClrStScDone%"=="No" (call :ShowLogo)
set "ClrStScDone=Yes"
set "ConvProcRan=Yes"

rem Check & prepare...
if exist "error.init" (
del /f /q "error.init")
echo Converting "%~nx1"...

rem Decompile to VTF..
set DelTempVtf=0
if /i not "%~x1"==".vtf" (
	if not exist "%~dpn1.vtf" set DelTempVtf=1
	echo   Decompiling to VTF...
	call :TTZ2VTF "%~1" -noinfo
)

rem Run VTFCmd tool...
echo   Converting VTF to %ExportFormat%...
%VtfCmd% -file "%~dpn1.vtf" -exportformat %ExportFormat% -silent
%Validate% "%~dpn1.%ExportFormat%"
if "%DelTempVtf%"=="1" del /f /q "%~dpn1.vtf"> nul
if exist "error.init" goto QuitFunc

rem Get obtained Img size...
for %%s in ("%~dpn1.%ExportFormat%") do (
	echo   Obtained %ExportFormat% size: %%~zs bytes.
)

rem Final actions
set "SomeSuccess=Yes"
goto QuitFunc





:================================================
:TTZ2VTF
:================================================

rem Clear startup screen...
if "%ClrStScDone%"=="No" (call :ShowLogo)
set "ClrStScDone=Yes"
set "ConvProcRan=Yes"
if "%~2"=="-noinfo" set "SMode=> nul"

rem Check on basic errors...
set "TTZFixed=0"
if /i not "%~x1"==".tth" (
if /i not "%~x1"==".ttz" (
	set "ErrorsFound=Yes"
	%Sfk% echo "[Yellow]  "NOT TTH/TTZ FILE!
	goto QuitFunc))
if not exist "%~dpn1.tth" (
	set "ErrorsFound=Yes"
	%Sfk% echo "[Yellow]  "MISSING TTH HEADER!
	goto QuitFunc)
if not exist "%~dpn1.ttz" (
	cd.> "%~dpn1.ttz"
	attrib +H "%~dpn1.ttz"
	set "TTZFixed=1")
if exist "error.init" (
	del /f /q "error.init")

rem Start converter...
%TtzDec% "%~dpn1.ttz" %SMode%
if "%TTZFixed%"=="1" (
	del /f /q /a "%~dpn1.ttz"> nul)
%Validate% "%~dpn1.vtf"
if exist "error.init" goto QuitFunc

rem Get source TTx size...
for %%s in ("%~dpn1.tth") do (
for %%t in ("%~dpn1.ttz") do (
	echo   Source TTZ size:  %%~zs/%%~zt bytes.
))
rem Get obtained VTF size...
for %%s in ("%~dpn1.vtf") do (
	echo   Obtained VTF size:   %%~zs bytes.
) %SMode%

rem Final actions
set "SomeSuccess=Yes"
goto QuitFunc





:================================================
:VTF2TTZ
:================================================

rem Set default TTZ defs...
set "TthSignVer=545448000100"
set "VtfMipsCnt=04"
set "PreCacheCn=00"
set "VtfDfVrStr=56544600070000000100000040000000"
set "VtfDfHdrSz=64"
set "VtfMipsStr=1000000000000000"
set "VHdrSz=40"
set "VTmbSx=10"
set "VTmbSy=10"
set "VTmbSz=128"

rem Clear startup screen...
if "%ClrStScDone%"=="No" (call :ShowLogo)
set "ClrStScDone=Yes"
set "ConvProcRan=Yes"

rem Check & prepare...
set "VtfFile=%~1"
set "VtfBase=%~dpn1"
if not "%~2"=="-noinfo" (
 echo Converting "%~nx1"...
 call :ReadTemplates
)

rem Alias functions...
set TthBuf.Put=call :TthBuf.Put
set TthBuf.Write=call :TthBuf.Write "%VtfBase%.tth"

rem Check conditions...
if /i not "%~x1"==".vtf" (
	set "ErrorsFound=Yes"
	%Sfk% echo "[Yellow]  "NOT VTF FILE!
	goto QuitFunc)
if %~z1 LSS 65 (
	set "ErrorsFound=Yes"
	%Sfk% echo "[Yellow]  "INVALID VTF FILE!
	goto QuitFunc)
if exist "error.init" (del /f /q "error.init")


rem Run main script...

rem Fix VTF version issue...
if "%AutoFixVtfVersion%"=="1" (
	rem Get VTF header size...
	for /f %%s in ('call %Sfk% hexdump -offlen 12 1 -pure -nofile "%VtfFile%"') do (set "VHdrSz=%%~s")
)
if "%AutoFixVtfVersion%"=="1" (
	for /f %%v in ('call %Sfk% dec %VHdrSz%') do (
		if %%~v GEQ 64 (
		if %%~v LEQ 128 (
			set "VHdrSzDec=%%~v"
			if "%%~v"=="%VtfDfHdrSz%" goto fixvtfverfinish
			rem Construct new VTF...
			for %%m in ("%VtfFile%") do (
				%Sfk% echo %VtfDfVrStr% +hextobin "%TempDir%\%%~nm.new.p1"> nul
				%Sfk% partcopy "%%~m" -fromto 16 %VtfDfHdrSz% "%TempDir%\%%~nm.new.p2" -yes> nul
				%Sfk% partcopy "%%~m" -allfrom %%~v "%TempDir%\%%~nm.new.p3" -yes> nul
				%Validate% "%TempDir%\%%~nm.new.p1"
				%Validate% "%TempDir%\%%~nm.new.p2"
				%Validate% "%TempDir%\%%~nm.new.p3"
				if exist "error.init" goto QuitFunc
				copy /y /b "%TempDir%\%%~nm.new.p1" + "%TempDir%\%%~nm.new.p2" + "%TempDir%\%%~nm.new.p3" "%%~m"> nul
				del  /f /q "%TempDir%\%%~nm.new.p?"> nul
				goto fixvtfverfinish
			)
		))
		set "ErrorsFound=Yes"
		%Sfk% echo "[Yellow]  "Invalid VTF header size: ["%%~v/0x%VHdrSz%h"]!
		goto QuitFunc
	)
)
:fixvtfverfinish


rem Get VTF size...
for %%m in ("%VtfFile%") do (
	set "VtfSize=%%~zm"
	if %%~zm GEQ 66 (
	if %%~zm LEQ 268435456 (
		echo   Src VTF file size:	%%~zm bytes.
		goto vtfsizesuccess
	))
	set "ErrorsFound=Yes"
	%Sfk% echo "[Yellow]  "Invalid VTF file size: ["%%~zm"]!
	goto QuitFunc
)
:vtfsizesuccess


rem Process compress condition..
if "%CompressImageData%"=="0" (
	set "VtfMipsCnt=01"
	set "VtfMipsDat=0000000000000000"
	set "TtzNumSize=0"
	goto getbinarysizes
)


rem Get VTF header size...
for /f %%s in ('call %Sfk% hexdump -offlen 12 1 -pure -nofile "%VtfFile%"') do (set "VHdrSz=%%~s")
for /f %%v in ('call %Sfk% dec %VHdrSz%') do (
	if %%~v GEQ 64 (
	if %%~v LEQ 128 (
		set "VHdrSzDec=%%~v"
		echo   VTF Header size:      %%~v bytes [0x%VHdrSz%h].
		goto vtfhdrsuccess
	))
	set "ErrorsFound=Yes"
	%Sfk% echo "[Yellow]  "Invalid VTF header size: ["%%~v/0x%VHdrSz%h"]!
	goto QuitFunc
)
:vtfhdrsuccess


rem Get VTF mipmap data...
for /f %%s in ('call %Sfk% hexdump -offlen 56 1 -pure -nofile "%VtfFile%"') do (set "VtfMipsCnt=%%~s")
for /f %%n in ('call %Sfk% dec %VtfMipsCnt%') do (
	set "mcne=%%~n"
	set /a "mfdt=%%~n*8"
)
if %mcne% LSS 15 (
	echo   VTF MipMaps count:    %mcne% levels [0x%VtfMipsCnt%h].
	echo   TTZ MipFlags data:    %mfdt% bytes [%mcne%*8].
	set mcnc=0
	set VtfMipsDat=
) else (
	set "ErrorsFound=Yes"
	%Sfk% echo "[Yellow]  Invalid MipMap data (%mcne%/0x%VtfMipsCnt%h), >14!"
	goto QuitFunc
)
:mdconstruct
set /a "mcnc=%mcnc%+1"
set "VtfMipsDat=%VtfMipsDat%%VtfMipsStr%"
if not "%mcnc%"=="%mcne%" (
goto mdconstruct)


rem Get VTF thumbnail size...
if not "%ProcessThumbnails%"=="1" (
	set "VTmbSz=0"
	goto getvtfthumbempty
)
for /f %%s in ('call %Sfk% hexdump -offlen 61 1 -pure -nofile "%VtfFile%"') do (set "VTmbSx=%%~s")
for /f %%s in ('call %Sfk% hexdump -offlen 62 1 -pure -nofile "%VtfFile%"') do (set "VTmbSy=%%~s")
for /f %%x in ('call %Sfk% dec %VTmbSx%') do (set "tszx=%%~x")
for /f %%y in ('call %Sfk% dec %VTmbSy%') do (set "tszy=%%~y")
set SzFlag=0
for %%n in (1 2 4 8 16) do (if "%tszx%"=="%%n" (set /a "SzFlag=%SzFlag%+1") )
for %%n in (1 2 4 8 16) do (if "%tszy%"=="%%n" (set /a "SzFlag=%SzFlag%+1") )
if not "%SzFlag%"=="2" (
	%Sfk% echo "[Yellow]  Invalid thumbnail data (%tszx%x%tszy%), using empty."
	set VTmbSz=0
	goto getvtfthumbempty
)
set /a "VTmbSz=(%tszx%*%tszy%)/2"
echo   VTF Thumbnail size:   %VTmbSz% bytes [%tszx%x%tszy%px].
:getvtfthumbempty

	
rem Obtain VTF chunk size...
set /a "VChkSz=%VHdrSzDec%+%VTmbSz%"
if %VChkSz% GEQ 64 if %VChkSz% LEQ 255 (
	echo   Obtained VTF chunk:   %VChkSz% bytes [%VHdrSzDec%+%VTmbSz%].
	goto getchunksuccess
)
%Sfk% echo "[Yellow]  Invalid VTF chunk size (%VChkSz%), using default."
set VChkSz=64
:getchunksuccess
for /f %%h in ('call %Sfk% hex %VChkSz% -digits=2') do (set "VtfChunkSz=%%~h000000")


rem Process heads/tails...
for %%m in ("%VtfFile%") do (
	rem Split VTF chunks...
	%Sfk% partcopy "%%~m" -fromto 0 %VChkSz% "%TempDir%\%%~nxm.head" -yes> nul
	%Sfk% partcopy "%%~m" -allfrom  %VChkSz% "%TempDir%\%%~nxm.tail" -yes> nul
	%Validate% "%TempDir%\%%~nxm.head"
	%Validate% "%TempDir%\%%~nxm.tail"
	if exist "error.init" goto QuitFunc
	rem Compress VTF tail...
	%ZLib% -c "%TempDir%\%%~nxm.tail" "%%~dpnm.ttz" "8"> nul
	del /f /q "%TempDir%\%%~nxm.tail"> nul
	%Validate% "%%~dpnm.ttz"
	if exist "error.init" goto QuitFunc
	rem Get obtained TTZ size...
	for %%x in ("%%~dpnm.ttz") do (
	  set "TtzNumSize=%%~zs"
	  echo   Obtained TTZ size:	%%~zs bytes.
	)
)


rem Prepare TTH header...
:getbinarysizes
call :ConvertSz "%VtfSize%" V
set "VtfBinSize=%VB1%%VB2%%VB3%%VB4%"
echo   VTF binary size:	0x%VtfBinSize%h (int).
call :ConvertSz "%TtzNumSize%" T
set "TtzBinSize=%TB1%%TB2%%TB3%%TB4%"
echo   TTz binary size:	0x%TtzBinSize%h (int).
rem Process compress condition..
if "%CompressImageData%"=="0" (
set "VtfChunkSz=%VtfBinSize%")


rem Write TTH header...
set TthBuf=
for %%c in (
	%TthSignVer%
	%VtfMipsCnt%
	%PreCacheCn%
	%VtfChunkSz%
	%VtfMipsDat%
	%VtfBinSize%
	%TtzBinSize%
) do (
%TthBuf.Put% "%%~c")
%TthBuf.Write% "%TthBuf%"

%Validate% "%VtfBase%.tth"
if exist "error.init" goto QuitFunc


rem Merge headers...
for %%m in ("%VtfFile%") do (
	if "%CompressImageData%"=="0" (
		if exist "%%~dpnm.ttz" del /f /q "%%~dpnm.ttz"> nul
		copy /b "%%~dpnm.tth" + "%%~m" "%%~dpnm.tth"> nul
	) else (
		copy /b "%%~dpnm.tth" + "%TempDir%\%%~nxm.head" "%%~dpnm.tth"> nul
		del /f /q "%TempDir%\%%~nxm.head"> nul
	)
	%Validate% "%%~dpnm.tth"
	if exist "error.init" goto QuitFunc
)


rem GENERATE .VMT if needed...
if not "%AutoCreateVmts%"=="1" goto genvmtfinish
if exist "%TgtPath%\%~n1.vmt" goto genvmtfinish

rem Get path for vmt...
:: moved to :ReadTemplates function
if not defined VmtPath goto genvmtfinish
set "BaseTex=%VmtPath:\=/%/%~n1"

rem Check texname postfix...
set TextureIsMask=
for /f "delims=" %%p in (
'call %Sfk% echo -lit "%~n1" +filter -lerep "|_ref||" -lerep "|_normal||" -lerep "|_bump||" -lerep "|_spec||"' 
) do (if /i not "%%~p"=="%~n1" (set "TextureIsMask=True") )
if defined TextureIsMask (goto genvmtfinish)

rem Set defaults if template not detected...
if not defined VmtShader set VmtShader=LightmappedGeneric
if not defined VmtParams set VmtParams='$surfaceprop' 'default'

rem Generate Vmt file...
echo   VMt material path:   "%BaseTex%".
(echo // created in bloodlines sdk
 echo "%VmtShader%"
 echo {
 echo 	"$baseTexture" "%BaseTex%"
 if defined VmtParams (
 call %Sfk% echo -lit "%VmtParams%" +filter -srep "|'$|\t'$|" -srep "|'|\q|" -srep "|; |\r\n|" -srep "|;|\r\n|")
 echo }
)> "%TgtPath%\%~n1.vmt"

rem Check if .vmt exist...
%Validate% "%TgtPath%\%~n1.vmt"
if exist "error.init" goto QuitFunc
:genvmtfinish


rem Final actions
set "SomeSuccess=Yes"
if not "%~2"=="-noinfo" (
if "%DeleteSourceVtfs%"=="1" (
	del /f /q "%VtfFile%"> nul
)) else (
	del /f /q "%VtfFile%"> nul
)

goto QuitFunc





:================================================
:Function Calls
:================================================

:ShowLogo
	cls
	echo ีออออออออออออออออออออออออออออออออธ
	echo ณ BLOODLINES TEXTURE CONVERTER   ณ
	echo ณ Version: %ProgVersion% (c) Psycho-A ณ
	echo ิออออออออออออออออออออออออออออออออพ
	echo.
exit /b

:ConvertAll
	set "TgtPath=%~dp1"
	if exist "%TgtPath:~0,-1%\" set "TgtPath=%TgtPath:~0,-1%"
	if /i "%~x1"==".vtf" if /i "%ConvertMode%"=="ToImg" (call :VTT2IMG "%~1") else (call :VTF2TTZ "%~1")
	if /i "%~x1"==".tth" if /i "%ConvertMode%"=="ToVtf" (call :TTZ2VTF "%~1") else (call :VTT2IMG "%~1")
	if /i "%~x1"==".ttz" if /i "%ConvertMode%"=="ToVtf" (call :TTZ2VTF "%~1") else (call :VTT2IMG "%~1")
	if /i "%~x1"==".tga" if /i "%ConvertMode%"=="ToVtf" (call :IMG2VTF "%~1") else (call :IMG2TTZ "%~1")
	if /i "%~x1"==".dds" if /i "%ConvertMode%"=="ToVtf" (call :IMG2VTF "%~1") else (call :IMG2TTZ "%~1")
	if /i "%~x1"==".bmp" if /i "%ConvertMode%"=="ToVtf" (call :IMG2VTF "%~1") else (call :IMG2TTZ "%~1")
	if /i "%~x1"==".png" if /i "%ConvertMode%"=="ToVtf" (call :IMG2VTF "%~1") else (call :IMG2TTZ "%~1")
	if /i "%~x1"==".jpg" if /i "%ConvertMode%"=="ToVtf" (call :IMG2VTF "%~1") else (call :IMG2TTZ "%~1")
	if /i "%~x1"==".gif" if /i "%ConvertMode%"=="ToVtf" (call :IMG2VTF "%~1") else (call :IMG2TTZ "%~1")
	if exist "error.init" del /f /q "error.init"
exit /b

:MakeVtf
	if /i "%OutputFormat%"=="Uncompressed" set FormatDefs=-format "BGR888" -alphaformat "BGRA8888"
	if /i "%OutputFormat%"=="Compressed" set FormatDefs=-format "DXT1" -alphaformat "DXT5"
	%VtfCmd% -file "%~1" -output "%~2" %FormatDefs% -flag "trilinear" %FlagDefs% -resize -version 7.1 -silent
exit /b

:ReadTemplates
	set FormatDefs=
	set FlagDefs=
	set TmpSuccess=generic

	rem Generate short path..
	set VmtPath=
	for /f "delims=" %%p in (
	'call %Sfk% echo -lit "%TgtPath%" +filter -rep "|*\materials\||" -rep "|*\materialsrc\||"'
	) do (if /i not "%%~p"=="%TgtPath%" (set "VmtPath=%%~p") )

	rem Read template manifest..
	if "%UseTemplates%"=="1" (
	if exist %Templates% (
		echo   Reading templates...
		set TmpKey=
		set TmpName=
		for /f "usebackq eol=# delims== tokens=1,*" %%a in (%Templates%) do (
			set "TmpKey=%%~a"
			call :ProcTemplates %%b
		)
	))
	if "%UseTemplates%"=="1" (
	if exist %Templates% (
		echo   Format template: %TmpSuccess%
	))
exit /b

:ProcTemplates
	set TmpVal=%*
	if "%TmpKey:~0,1% %TmpKey:~-1,1%"=="[ ]" set TmpName=%TmpKey:~1,-1%
	if /i "%TmpKey%"=="Dirs" (
	for %%m in (%TmpVal%) do (
		if defined VmtPath (
			for /f "delims=" %%p in (
			'call %Sfk% echo -lit "%VmtPath%" +filter -lsrep "|%%~m|\|"'
			) do (if /i not "%%~p"=="%VmtPath%" (set TmpSuccess=%TmpName%) )
		) else (
			for /f "delims=" %%p in (
			'call %Sfk% echo -lit "%TgtPath%" +filter -rep "|\%%~m\|\|"'
			) do (if /i not "%%~p"=="%TgtPath%" (set TmpSuccess=%TmpName%) )
		)
	))
	if /i "%TmpName%"=="%TmpSuccess%" (
	for %%c in (FormatDefs FlagDefs VmtShader VmtParams) do (
		if /i "%TmpKey%"=="%%~c" (set %%~c=%TmpVal%)
	))
exit /b

:ConvertSz
	for /f %%s in ('call %Sfk% hex "%~1" -digits=8 +filter -lsrep "/????//" -lsrep "/??//"') do (set "%~2B1=%%~s")
	for /f %%m in ('call %Sfk% hex "%~1" -digits=8 +filter -lsrep "/????//" -lerep "/??//"') do (set "%~2B2=%%~m")
	for /f %%n in ('call %Sfk% hex "%~1" -digits=8 +filter -lerep "/????//" -lsrep "/??//"') do (set "%~2B3=%%~n")
	for /f %%e in ('call %Sfk% hex "%~1" -digits=8 +filter -lerep "/????//" -lerep "/??//"') do (set "%~2B4=%%~e")
exit /b

:TthBuf.Put
	set "TthBuf=%TthBuf%%~1"
exit /b

:TthBuf.Write
	%Sfk% echo "%~2" +hextobin "%~1"> nul
exit /b

:Validate
if not exist "%~1" (
	set "ErrorsFound=Yes"
	%Sfk% echo "[Yellow]  "UNEXPECTED ERROR!
	%Sfk% echo "[Yellow]  "File \"%~1\" is missing!
	echo "%~1">> "error.init"
	exit /b
)
if %~z1 LSS 4 (
	%Sfk% echo "[Yellow]  "UNEXPECTED ERROR!
	%Sfk% echo "[Yellow]  "File \"%~1\" is incorrect!
	del /f /q /a "%~1"> nul
	echo "%~1">> "error.init"
	exit /b
)
exit /b

:ShellModeProcs
	rem Info Message
	start "" %MsgBox% Usage modes:  1) Run "%~nx0" to choose converting files;	2) Use "SdkBinaries\Tools\Texture Utils\%~nx0" "anyfile.vtf";	3) Use the Explorer context menu item (if the Bloodlines SDK installed);	4) Drag'n'drop VTFs to %~nx0 file.  You may convert multiple files at once. /c:Texture Converter - Information /t:MB_SYSTEMMODAL,MB_ICONINFORMATION
goto Exit

:QuitFunc
set SMode=
if /i not "%~2"=="-noinfo" echo.
exit /b

:Exit
if exist "%TempDir%\" (
rd /s /q "%TempDir%\" )
exit
