@echo off
rem Written by: Psycho-A
rem Build: 13:17 17.05.2017 {beta}
color 80
mode con cols=42 lines=15
echo Initializing...
setlocal EnableExtensions
set "ConTitle=Lip and VCD Editor"
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title Editor Console
pushd "%~dp0"

:: Set required environment
set TargetPath=projectbase\sound
set NirCmd=..\..\service\nircmd.exe
set MsgBox=..\..\service\msgbox.exe
set InputBox=..\..\service\inputbox.exe
set OpenDlg=..\..\service\opendlg.exe
set Sfk=..\..\service\sfk.exe
set FPApp=hlfaceposer.exe
set FPConfigGen=hlfaceposer_cfg.reg
set FPConfigVCD=hlfaceposer_vcd.reg
set LipFormatHl2=patterns\lips_hl2.lst
set LipFormatVtM=patterns\lips_vtm.lst
set LipWavMeta=patterns\wav_meta.bin
set SoX=soxconverter\sox.exe

:: Check required files
for %%m in (
	%NirCmd%
	%MsgBox%
	%OpenDlg%
	%Sfk%
	%SoX%
	%FPConfigGen%
	%FPConfigVCD%
	%FPApp%
	%LipFormatHl2%
	%LipFormatVtM%
	%LipWavMeta%
) do (
	if not exist "%%~m" (
		color 8c
		echo Error: Missing "%%~m" file!
		echo>>"..\..\..\sdk_errors.log" [%date% %time%] LipSync error: Missing "%%~m" file.
		exit
	)
)
taskkill /f /t /im hlfaceposer.exe> nul 2>&1
if exist "%TargetPath%\" rd /s /q "%TargetPath%"> nul
if not exist "%TargetPath%\" md "%TargetPath%\"

:: Set open files behavior
echo Processing input...
set OpenFiles=echo "%~1"
if /i not "%~x1"==".lip" (
if /i not "%~x1"==".vcd" (
if /i not "%~x1"==".wav" (
if /i not "%~x1"==".mp3" (
	echo - Used SDK mode.
	set OpenFiles=call %OpenDlg% /f /m "/e=*.wav *.mp3 *.lip *.vcd"
))))

:: Read SDK GameConfig to get additional project dirs
echo Getting project paths...
set ModDir=empty
set GameDir=empty
if defined VProject (
	if exist "%VProject%\" set "GameDir=%VProject%"
)
if exist "..\..\GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("..\..\GameCfg.ini") do (
	if /i "%%~a"=="ModDir" if exist "%%~b\" (set "ModDir=%%~b")
	if /i "%%~a"=="GameDir" if exist "%%~b\" (set "GameDir=%%~b")
))



:: Show hint about selecting files
echo Open editing files...
if "%~1"=="" start %MsgBox% Select .wav, .mp3, .lip or .vcd file(s) to make or edit lipsyncs, captions or gestures.  If you choose .mp3 or .wav, the program will search matched .lip to edit its data.  If you choose .lip, the program will also load audio file to be used as a voice base.  If you choose .vcd, the Scene Editor will be opened to edit gestures linked to line. /c:%ConTitle%: Tips /t:MB_SYSTEMMODAL

:: Select sound files and import them into program
for /f "delims=" %%a in ('%OpenFiles%') do (
	rem Check extension validity of selection
	if /i not "%%~xa"==".wav" (
	if /i not "%%~xa"==".mp3" (
	if /i not "%%~xa"==".lip" (
	if /i not "%%~xa"==".vcd" (
		%Sfk% echo [red]- Invalid file type!
		goto quit
	))))
	rem Turn-on VCD controls if scene selected
	if /i "%%~xa"==".vcd" set VCDMode=1
	rem Files are valid, perform import script
	call :DoImport "%%~a" "%TargetPath%"
)
%NirCmd% win close process msgbox.exe

rem Script wasn't success, exit program
for %%p in (SourceDir ShortPath) do (
if not defined %%~p (
	%Sfk% echo [yellow]- Canceled by user?
	goto quit
))
if not defined SoundsImported (
if not defined VCDMode (
	%Sfk% echo [red]- File set incomplete!
	%MsgBox% Failed to find required sound files needed to append .lip for it's reading. /c:%ConTitle%: Error /t:MB_SYSTEMMODAL,MB_ICONERROR
	goto quit
))



:: Start FacePoser and its stuff
echo Starting FacePoser application...
rem Inject custom window layout settings...
echo - Injecting layout settings...
reg import "%FPConfigGen%"> nul 2>&1
if "%VCDMode%"=="1" (
	%Sfk% echo [blue]- Program works as VCD Editor.
	reg import "%FPConfigVCD%"> nul 2>&1
) else (
	%Sfk% echo [blue]- Program works as LIP Editor.
)

rem Detect app-launch-time for file-export optimization
for /f %%a in ('call %Sfk% time') do (set "BeforeTime=%%~a")
echo - Starting time: %BeforeTime%.

rem Run FacePoser executable...
%NirCmd% win activate etitle "Editor Console"
start %FPApp% -game projectbase -nop4 -novconfig -noshaderapi

rem Fit and Title the program window [fixme!]
set appshow_stp=0
set loop_count=10
:appwinshow_loop
%NirCmd% wait 100
%NirCmd% win center process hlfaceposer.exe
%NirCmd% win settext process hlfaceposer.exe "Lip/VCD/Captions Editor"
%NirCmd% win activate ititle "Lip/VCD/Captions Editor"
set /a appshow_stp=%appshow_stp%+1
if %appshow_stp% LSS %loop_count% goto appwinshow_loop

rem Show FacePoser usage tutorials...
echo - Showing usage notes...
if not "%VCDMode%"=="1" %MsgBox% To create new closecaption + lipsync data (.lip files), do the following:  1) In existing WAV list double-click desired file;  2) Under the waveform press "Re-extract" button and enter your Phrase text;  3) Right-click on waveform field and press "Commit extraction";  4) Press "Save" button on finish.  5) Do steps 1-4 for other sounds (if exist) and close program. /c:LipSync Editor: Usage Information /t:MB_SYSTEMMODAL,MB_ICONQUESTION
if "%VCDMode%"=="1" %MsgBox% To edit an existing VCD file, double-click it in loaded VCDs list to open.  Use Scene Editor panel to add or edit controls, like sounds, gestures etc.  You can learn details on Valve's Developer Wiki, at the "Choreography" category or "Choreography Tool reference" section about how to do it.  To create a new VCD, use "Scene Editor > New" menu option and save it on the default-suggested location (...\projectbase\sound\) with making sub-directories inside that your Mod will have inside of its sound\ dir. When the program is closed, your .vcd will be moved into your project.  Another way is to create empty .vcd file (just empty text file with .vcd extension) inside your project and then open it in this tool for editings. /c:VCD Editor: Usage Information /t:MB_SYSTEMMODAL,MB_ICONQUESTION

rem Set custom Speaker name...
if "%VCDMode%"=="1" goto setspn_skip
echo - Obtaining Speaker name...
if defined speaker_name (
set SpNCap="%speaker_name%")
:setspn_loop
for /f "delims=" %%a in (
'%InputBox% "Enter speaker's name (e.g. Jeanette) for processing replies.\nIt will be used on screen subtitles when one of reply plays.\nIf you don't want to change an existing one, just leave it as is.\nName must contains english chars, numbers and spaces only!" "Enter speaker name" %SpNCap% /W:340 /H:144'
) do (set "speaker_name=%%~a")
if not defined speaker_name (
	%Sfk% echo "[yellow]  - You must set correct name!"
	goto setspn_loop
)
%Sfk% echo "[green]  - Speaker name: %speaker_name%"
:setspn_skip

rem Wait FacePoser process and make posts...
%NirCmd% waitprocess hlfaceposer.exe
%NirCmd% win close process msgbox.exe
%NirCmd% win close process inputbox.exe
echo FacePoser application closed.
start %MsgBox% Saving changes and closing program... /c:%ConTitle% /t:MB_SYSTEMMODAL
rem Clear settings and dumps as not required...
if exist "hlfaceposer.rf" del /f /q "hlfaceposer.rf"> nul
reg delete "HKCU\Software\Troika\faceposer" /f> nul



:: FP closed, split LIPs from changed files
rem Optimization: clear files being unchanged before FP launched.
echo Clearing unwanted files...
for %%m in ("%TargetPath%\%ShortPath%\*.wav") do (
if exist "%%~dpnm_work.wav" (del /f /q "%%~dpnm_work.wav"> nul) )
if defined BeforeTime call %Sfk% list -before %BeforeTime% "%TargetPath%" *.wav *.vcd -quiet +del! -quiet=2

rem Forge .lip from .wav for loose files [fixme!]...
echo Obtaining new LIP files...
for %%m in ("%TargetPath%\%ShortPath%\*.wav") do (
	%Sfk% replace "%%~m" -bin "|00|0a|" -yes -quiet=2
	%Sfk% filter "%%~m" -inc "VERSION 1." to * -write -yes -quiet=2
	rem Clean-up false empty LIPs...
	for %%s in ("%%~m") do (
		if "%%~zs"=="0" (
		del /f /q "%%~m") else (
		rename "%%~m" "%%~nm.lip")
	)> nul
)



:: Convert obtained LIPs to VtmB format
echo Converting new files to VtmB's...
for %%m in ("%TargetPath%\%ShortPath%\*.lip") do (
	echo - Processing "%%~nxm"

	rem echo - Making base replacements...
	%Sfk% replace "%%~m" -spat -bylist "%LipFormatVtM%" -memlimit=1000m -quiet=2 -yes
	%Sfk% replace "%%~m" -spat "|EMPHASIS\n{\n}\nOPTIONS|EMPHASIS\n{\n}\nCLOSECAPTION\n{\nenglish\n{\nPHRASE char 2 \q\q 0.000 0.000\n}\n}\nOPTIONS|" -quiet=2 -yes
	if defined speaker_name (
	%Sfk% filter "%%~m" -rep "|speaker_name *|speaker_name %speaker_name%|" -write -yes -quiet=2 )

	rem echo - Getting Phrase's duration...
	set StartTime=
	set FinalTime=
	for /f "usebackq tokens=1-4" %%a in ("%%~m") do (
	if /i "%%~a"=="WORD" call :SetPhraseDuration "%%~c" "%%~d" )
	rem call :ShowPhraseDuration

	rem echo - Getting Phrase's text...
	set Phrase=
	set PrevLine1=
	set PrevLine2=
	set PhraseGot=
	set PhraseLen=0
	for /f "usebackq tokens=1,*" %%a in ("%%~m") do (
	call :GetPhraseText "%%~a" "%%~b" )
	rem call :ShowPhraseText

	rem echo - Writing Phrase's text to captions...
	call :WritePhraseToCaps "%%~m"
	rem echo.
)



:: Move edited LIPs ad VCDs back to mod
echo Moving edited files back to game...
for %%m in (
	"%TargetPath%\%ShortPath%\*.lip"
	"%TargetPath%\%ShortPath%\*.vcd"
) do (
	move /y "%%~m" "%SourceDir%\%ShortPath%\"> nul
)



:: Exit launch script
:quit
echo Exiting program...
taskkill /f /im msgbox.exe> nul 2>&1
rd /s /q "%TargetPath%\"> nul
md "%TargetPath%\"
exit



:: Service Functions

:DoImport
	rem Convert input path to FS chunks...
	if not defined ShortPath for /f "delims=" %%s in ('call %Sfk% echo "%~dp1#" +filter -lerep "|\#||" -rep "|*\sound\||"') do (
		if /i not "%%~s\"=="%~dp1" (set "ShortPath=%%~s") else (set "ShortPath=.") )
	if not defined SourceDir for /f "delims=" %%s in ('call %Sfk% echo "%~dp1#" +filter -lerep "|\#||" -rep "|\%ShortPath%||"') do (
		set "SourceDir=%%~s")
	if not exist "%~2\%ShortPath%\" md "%~2\%ShortPath%\"

	rem Search files at all project paths...
	for %%p in ("%SourceDir%" "%ModDir%\sound" "%GameDir%\sound") do (
		rem If found WAV, just copy into the Target dir...
		if exist "%%~p\%ShortPath%\%~n1.wav" (
		if not exist "%~2\%ShortPath%\%~n1.wav" (
			echo   Importing "%~n1.wav"
			copy /y "%%~p\%ShortPath%\%~n1.wav" "%~2\%ShortPath%\"> nul
			set "SoundsImported=1"
		))
		rem If found MP3, convert to WAV into Target dir...
		if exist "%%~p\%ShortPath%\%~n1.mp3" (
		if not exist "%~2\%ShortPath%\%~n1.wav" (
			echo   Importing "%~n1.mp3"
			%SoX% -V1 "%%~p\%ShortPath%\%~n1.mp3" -t wavpcm "%~2\%ShortPath%\%~n1.wav"
			set "SoundsImported=1"
		))
		rem If found LIP, copy into Target dir for the following actions...
		if exist "%%~p\%ShortPath%\%~n1.lip" (
		if not exist "%~2\%ShortPath%\%~n1.lip" (
			echo   Importing "%~n1.lip"
			copy /y "%%~p\%ShortPath%\%~n1.lip" "%~2\%ShortPath%\"> nul
		))
		rem If found VCD, copy into Target dir for future processing...
		if exist "%%~p\%ShortPath%\%~n1.vcd" (
		if not exist "%~2\%ShortPath%\%~n1.vcd" (
			echo   Importing "%~n1.vcd"
			copy /y "%%~p\%ShortPath%\%~n1.vcd" "%~2\%ShortPath%\"> nul
		))
	)

	rem Process imported LIP...
	if exist "%~2\%ShortPath%\%~n1.lip" (
		rem If found WAV pair, append it to...
		if exist "%~2\%ShortPath%\%~n1.wav" (
			rem Convert LIPs to HL2 format to be readable in FP
			%Sfk% replace "%~2\%ShortPath%\%~n1.lip" -spat -bylist "%LipFormatHl2%" -quiet=2 -yes
			copy /b "%~2\%ShortPath%\%~n1.wav" + "%LipWavMeta%" + "%~2\%ShortPath%\%~n1.lip" "%~2\%ShortPath%\%~n1.wav"> nul

			rem Obtain and set speaker_name [optimized]...
			if not defined speaker_name (
				for /f "usebackq tokens=1,*" %%n in ("%~2\%ShortPath%\%~n1.lip") do (
				if "%%~n"=="speaker_name" if not "%%~o"=="" (set "speaker_name=%%~o"))
			)
		) else (
			rem Wav not found, nothing to append, show warning.
			%Sfk% echo "[yellow]  - required .wav/.mp3 not found!"
		)
		rem LIP isn't need anymore, delete it.
		del /f /q "%~2\%ShortPath%\%~n1.lip"> nul
	)

	rem Process imported VCD...
	if exist "%~2\%ShortPath%\%~n1.vcd" (
	rem Search audio links to import too...
	for /f "delims=" %%l in (
	'call %Sfk% filt "%~2\%ShortPath%\%~n1.vcd" -spat -+.wav\q -+.mp3\q -rep "|.???\q*||" -rep "|*\q||" -rep "|/|\|"'
	) do (
		for %%p in ("%SourceDir%" "%ModDir%\sound" "%GameDir%\sound") do (
			rem If found something, import this to Target dir...
			if not exist "%~2\%%~l.wav" (
			for %%f in ("%~2\%%~l.wav") do (
				if exist "%%~p\%%~l.wav" (
					echo   - importing "%%~nf.wav" [vcd]
					if not exist "%%~dpf" md "%%~dpf"
					copy /y "%%~p\%%~l.wav" "%~2\%%~l.wav"> nul
				) else if exist "%%~p\%%~l.mp3" (
					echo   - importing "%%~nf.mp3" [vcd]
					rem Replace .mp3 links to .wav to be playable
					%Sfk% replace "%~2\%ShortPath%\%~n1.vcd" -spat "|.mp3\q|.wav\q|" -quiet=2 -yes
					if not exist "%%~dpf" md "%%~dpf"
					%SoX% -V1 "%%~p\%%~l.mp3" -t wavpcm "%~2\%%~l.wav"
				)
			))
		)
	))
exit /b

:SetPhraseDuration
	if not defined StartTime set "StartTime=%~1"
	if not "%~2"=="0.000" set "FinalTime=%~2"
exit /b

:GetPhraseText
	if defined PhraseGot exit /b
	if "%~1"=="PLAINTEXT" (
		set "PrevLine1=PLAINTEXT"
		exit /b
	)
	if "%~1"=="{" (
	if "%PrevLine1%"=="PLAINTEXT" (
		set "PrevLine2={"
		exit /b
	))
	if "%PrevLine1%"=="PLAINTEXT" (
	if "%PrevLine2%"=="{" (
		if not "%~1"=="}" (
			set "Phrase=%~1 %~2"
			if "%~2"=="" set "Phrase=%~1"
			if /i "%~1"=="[Textless]" (
				set Phrase=
				set FinalTime=0.000
			)
		) else set Phrase=
		set "PhraseGot=1"
		call :NormalizePhrase
		exit /b
	))
exit /b

:NormalizePhrase
	for /f "delims=" %%t in ('call %Sfk% echo -lit "%Phrase%" +filter -rep "|[*]||" -lsrep "| ||" -lerep "| ||" -srep "|\x7c|/|"') do (set "Phrase=%%~t")
	for /f "delims=" %%c in ('call %Sfk% strlen "%Phrase%"') do (set /a "PhraseLen=%%~c+2")
exit /b

:WritePhraseToCaps
	if not defined StartTime set StartTime=0.000
	if not defined FinalTime set FinalTime=0.000
	%Sfk% filter  "%~1" -srep "|PHRASE ???*|PHRASE char 2 \q\q 0.000 0.000|" -case -write -yes -quiet=2
	%Sfk% replace "%~1" -spat "|PHRASE char 2 \q\q 0.000 0.000|PHRASE char %PhraseLen% \q%Phrase%\q %StartTime% %FinalTime%|" -case -yes -quiet=2
exit /b

:ShowPhraseDuration
	echo   # StartTime: %StartTime%
	echo   # FinalTime: %FinalTime%
exit /b

:ShowPhraseText
	%Sfk% echo "  # Text: %Phrase%" +filter -form "$1.68col1.."
	echo   # CharCount: %PhraseLen%
exit /b
