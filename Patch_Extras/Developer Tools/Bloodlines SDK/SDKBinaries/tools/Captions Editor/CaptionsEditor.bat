@echo off
title Captions Editor Console
rem Written by: Psycho-A
rem Build: 3:10 10.03.2017 {beta}
setlocal EnableExtensions
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
color 81
mode con cols=34 lines=12
echo Initializing...
if not "%~1"=="" if /i not "%~x1"==".lip" exit
chcp 1251> nul
pushd "%~dp0"

:: Required assets
set InputBox=..\..\service\inputbox.exe
set Sfk=..\..\service\sfk.exe
set OpenFile=..\..\service\opendlg.exe /f "/e=*.lip *.txt"

:: Read LIP file
echo Reading input...
if "%~1"=="" (
	rem SDK mode with FileOpenDlg
	if exist "service\filetypes.bat" (
	rem Register file types for Context
	call "service\filetypes.bat"> nul )
	echo - Open file to edit!
	for /f "delims=" %%a in ('%OpenFile%') do (
	set "LipFile=%%~a"
	set "LipName=%%~nxa")
) else (
	rem Context menu mode
	set "LipFile=%~1"
	set "LipName=%~nx1"
)
if not defined LipFile exit
%Sfk% echo [green]- File: "%LipName%"

:: Normalize Lip files
echo Pre-formatting file...
copy /y "%LipFile%" "%CD%\TempFile.lip"> nul
%Sfk% replace "%CD%\TempFile.lip" -spat "|\x00||" "|\r\n|\n|" "| \n|\n|" "|\|/|" "|\q|~|" -quiet=2 -yes

:: Process Lip file to get text
echo Reading source data...
for /f "usebackq eol=/ tokens=1,2,3,*" %%a in ("%CD%\TempFile.lip") do (
rem Obtain sentence text
	call :GetSentenceText "%%~a" "%%~b" "%%~c" "%%~d"
rem Get Phrase's duration
	if "%%~a"=="WORD" call :SetPhraseDuration "%%~c" "%%~d"
rem Obtain phrase text
	if "%%~a"=="PHRASE" call :GetPhraseText "%CD%\TempFile.lip" "%%~b" "%%~c"
rem Obtain speaker name
	if "%%~a"=="speaker_name" if not "%%~b"=="" (
		set "speaker_name=%%~b"
		if not "%%~c"=="" set "speaker_name=%%~b %%~c"
		if not "%%~d"=="" set "speaker_name=%%~b %%~c %%~d"
	)
)
if defined Sentence (set "SentenceInfo=%Sentence%") else (set "SentenceInfo=<None>")
if defined Phrase (set "PhraseInfo=%Phrase%") else (set "PhraseInfo=<None>")
if defined speaker_name (set "SpeakerInfo=%speaker_name%") else (set "SpeakerInfo=<None>")
if not defined PhraseLen (set "PhraseLen=0")
if not defined StartTime (set "StartTime=0.000")
if not defined FinalTime (set "FinalTime=0.000")

:: Compute InputBox height
set IBHeight=155
set /a IBHeight=%IBHeight%+(%PhraseLen%/3)

:: Edit Captions text
echo Editing captions text...
set PhraseEdited=0
set PhraseOutput=0
for /f "delims=" %%a in (
'%InputBox% "Enter new captions text.\n\nSentence text: ''%SentenceInfo%''\n\nCaptions text: ''%PhraseInfo%''" "Captions Editor (%LipName%)" "%PhraseInfo%" /N /L:"OK=Submit;Cancel=Turn subs off" /W:440 /H:%IBHeight%'
) do (
	set PhraseOutput=1
	if not "%%~a"=="%PhraseInfo%" (
		set PhraseEdited=1
		set "Phrase=%%~a"
	)
)
if "%PhraseOutput%"=="1" (
	if "%PhraseEdited%"=="0" (
		%Sfk% echo [blue]- Text not changed.
	) else (
		%Sfk% echo [cyan]- Editing done.
	)
) else (
	set PhraseEdited=1
	set Phrase=
	%Sfk% echo [yellow]- Captions disabled.
)

:: Edit Speaker name
echo Editing speaker name...
:edit_speaker_name
set SpeakerEdited=0
set SpeakerOutput=0
for /f "delims=" %%a in (
'%InputBox% "Enter new speaker name.\nCurrent name: ''%SpeakerInfo%''." "Captions Editor (%LipName%)" "%SpeakerInfo%" /N /L:"OK=Submit;Cancel=Disable" /W:250 /H:122'
) do (
	set SpeakerOutput=1
	if not "%%~a"=="%SpeakerInfo%" (
		set SpeakerEdited=1
		set "speaker_name=%%~a"
	)
)
if "%SpeakerOutput%"=="1" (
	if "%SpeakerEdited%"=="0" (
		%Sfk% echo [blue]- Text not changed.
	) else (
		%Sfk% echo [cyan]- Editing done.
	)
) else (
	set SpeakerEdited=1
	set speaker_name=
	%Sfk% echo [yellow]- Speaker disabled.
)
if not defined speaker_name if defined Phrase (
	%Sfk% echo [red]- Captions found, set speaker!
	set "SpeakerInfo=<None>"
	goto edit_speaker_name
)

:: Check edit conditions
if "%PhraseEdited%/%SpeakerEdited%"=="0/0" (
	echo Editing wasn't commit!
	del /f /q "%CD%\TempFile.lip"> nul
	goto exit
) else echo Saving changes to file...

:: Count new phrase's length
for /f "delims=" %%a in ('%Sfk% strlen "%Phrase%"') do set /a "PhraseLen=%%~a+2"

:: Append new text
%Sfk% filter  "%CD%\TempFile.lip" -spat -lsrep "|~||" -lerep "|~||" -rep "|~|\q|" -write -yes -quiet=2
if defined Phrase (
	%Sfk% replace "%CD%\TempFile.lip" -spat "|\nCLOSECAPTION\n{\n}|\nCLOSECAPTION\n{\nenglish\n{\nPHRASE char 2 \q\q 0.000 0.000\n}\n}|" -yes -quiet=2
	%Sfk% replace "%CD%\TempFile.lip" -spat "|\nCLOSECAPTION\n{\nenglish\n{\n}\n}|\nCLOSECAPTION\n{\nenglish\n{\nPHRASE char 2 \q\q 0.000 0.000\n}\n}|" -yes -quiet=2
	%Sfk% replace "%CD%\TempFile.lip" -spat "|\nEMPHASIS\n{\n}\nOPTIONS\n|\nEMPHASIS\n{\n}\nCLOSECAPTION\n{\nenglish\n{\nPHRASE char 2 \q\q 0.000 0.000\n}\n}\nOPTIONS\n|" -yes -quiet=2
	%Sfk% filter  "%CD%\TempFile.lip" -spat -lsrep "|PHRASE *|PHRASE char %PhraseLen% \q$PhraseText$\q %StartTime% %FinalTime%|" -write -yes -quiet=2
	%Sfk% replace "%CD%\TempFile.lip" -spat "|\r\n|\n|" -spat "|\q$PhraseText$\q|\q%Phrase%\q|" -yes -quiet=2
) else (
	%Sfk% filter  "%CD%\TempFile.lip" -spat -ls!"PHRASE ????" -write -yes -quiet=2
	%Sfk% replace "%CD%\TempFile.lip" -spat "|\r\n|\n|" -spat "|\nCLOSECAPTION\n{\nenglish\n{\n}\n}|\nCLOSECAPTION\n{\n}|" -yes -quiet=2
)
if defined speaker_name (
	%Sfk% replace "%CD%\TempFile.lip" -spat "|\nvoice_duck 0\n}|\nvoice_duck 0\nspeaker_name Somebody\n}|" -yes -quiet=2
	%Sfk% replace "%CD%\TempFile.lip" -spat "|\nvoice_duck 1\n}|\nvoice_duck 1\nspeaker_name Somebody\n}|" -yes -quiet=2
	%Sfk% filter  "%CD%\TempFile.lip" -lsrep "|speaker_name *|speaker_name Somebody|" -write -yes -quiet=2
	%Sfk% replace "%CD%\TempFile.lip" -spat "|\r\n|\n|" -spat "|speaker_name Somebody|speaker_name %speaker_name%|" -yes -quiet=2
) else (
	%Sfk% filter  "%CD%\TempFile.lip" -spat -ls!"speaker_name" -write -yes -quiet=2
	%Sfk% replace "%CD%\TempFile.lip" -spat "|\r\n|\n|" -yes -quiet=2
)
move /y "%CD%\TempFile.lip" "%LipFile%"> nul

:: Exit program
:exit
echo Exiting program...
ping>nul 127.0.0.1 -n 1
exit


:: Service functions

:SetPhraseDuration
	if not defined StartTime set "StartTime=%~1"
	set "FinalTime=%~2"
exit /b

:GetSentenceText
	if defined SentenceGot exit /b
	if "%~1"=="PLAINTEXT" (
		set "PrevLine1=%~1"
		exit /b
	)
	if "%~1"=="{" (
	if "%PrevLine1%"=="PLAINTEXT" (
		set "PrevLine2=%~1"
		exit /b
	))
	if "%PrevLine1%"=="PLAINTEXT" (
	if "%PrevLine2%"=="{" (
		set "SentenceGot=1"
		call :NormalizeSentence "%~1" "%~2" "%~3" "%~4"
		exit /b
	))
exit /b

:NormalizeSentence
	set "Sentence=%~1 %~2 %~3 %~4"
	if "%~2"=="}" set "Sentence="
	for /f "delims=" %%a in (
	'%Sfk% echo -lit "%Sentence%" +filter -lerep "| ||" -lerep "| ||" -lerep "| ||" -rep "|~||"'
	) do set "Sentence=%%~a"
exit /b

:GetPhraseText
	set "PhraseLenSrc=%~3"
	set "PhraseLen=%~3"
	if /i "%~2"=="unicode" set /a "PhraseLen=%~3/2"
	for /f "delims=" %%a in (
	'%Sfk% filter "%~1" -+"PHRASE " -rep "|PHRASE %~2 %PhraseLenSrc% ||" -form "$0.%PhraseLen%col1" -rep "|~||"'
	) do set "Phrase=%%~a"
exit /b
