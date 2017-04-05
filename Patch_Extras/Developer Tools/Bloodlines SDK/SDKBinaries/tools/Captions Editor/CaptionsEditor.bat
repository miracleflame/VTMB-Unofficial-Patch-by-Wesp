@echo off
title Captions Editor Console
rem Written by: Psycho-A
rem Build: 6:22 04.02.2017 {beta}
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
echo - File: "%LipName%"

:: Normalize Lip files
echo Pre-formatting file...
if not exist "%Temp%\" md "%Temp%"
copy /y "%LipFile%" "%Temp%\%LipName%"> nul
%Sfk% replace "%Temp%\%LipName%" -spat "|\x00||" "|\r\n|\n|" "| \n|\n|" "|\|/|" "|\q|~|" -quiet=2 -yes

:: Process Lip file to get text
echo Reading source data...
set "Sentence=<None>"
set "Phrase=<None>"
set "PhraseLen=0"
set "speaker_name=<None>"
for /f "usebackq eol=/ tokens=1,2,3,*" %%a in ("%Temp%\%LipName%") do (
rem Obtain sentence text
	call :GetSentenceText "%%~a" "%%~b" "%%~c" "%%~d"
rem Get Phrase's duration
	if "%%~a"=="WORD" call :SetPhraseDuration "%%~c" "%%~d"
rem Obtain phrase text
	if "%%~a"=="PHRASE" call :GetPhraseText "%Temp%\%LipName%" "%%~b" "%%~c"
rem Obtain speaker name
	if "%%~a"=="speaker_name" if not "%%~b"=="" (
		set "speaker_name=%%~b"
		if not "%%~c"=="" set "speaker_name=%%~b %%~c"
		if not "%%~d"=="" set "speaker_name=%%~b %%~c %%~d"
	)
)

:: Compute InputBox height
set IBHeight=155
set /a IBHeight=%IBHeight%+(%PhraseLen%/3)

:: Edit Captions text
echo Editing captions text...
set PhraseEdited=0
for /f "delims=" %%a in (
'%InputBox% "Enter new captions text.\n\nSentence text: ''%Sentence%''\n\nCaptions text: ''%Phrase%''" "Captions Editor (%LipName%)" "%Phrase%" /N /W:440 /H:%IBHeight%'
) do (
	if not "%%~a"=="%Phrase%" set "PhraseEdited=1"
	set "Phrase=%%~a"
)
if "%PhraseEdited%"=="0" (
	echo - Text not changed.
) else (
	echo - Editing done.
)

:: Edit Speaker name
echo Editing speaker name...
set speaker_edited=0
for /f "delims=" %%a in (
'%InputBox% "Enter new speaker name.\nCurrent name: ''%speaker_name%''." "Captions Editor (%LipName%)" "%speaker_name%" /N /W:250 /H:122'
) do (
	if not "%%~a"=="%speaker_name%" set "speaker_edited=1"
	set "speaker_name=%%~a"
)
if "%speaker_edited%"=="0" (
	echo - Text not changed.
) else (
	echo - Editing done.
)

:: Check edit conditions
if "%PhraseEdited%/%speaker_edited%"=="0/0" (
	echo Editing wasn't made. Exiting...
	del /f /q "%Temp%\%LipName%"> nul
	exit
) else echo Saving changes to file...

:: Count new phrase's length
set "PhraseLen=0"
for /f "delims=" %%a in ('%Sfk% strlen "%Phrase%"') do set /a "PhraseLen=%%~a+2"

:: Append new text
if not defined StartTime set "StartTime=0.000"
if not defined FinalTime set "FinalTime=0.000"
%Sfk% filter  "%Temp%\%LipName%" -spat -lswhere "PHRASE " -lsrep "|PHRASE *|PHRASE char %PhraseLen% \q$PhraseText$\q %StartTime% %FinalTime%|" -write -yes -quiet=2
%Sfk% filter  "%Temp%\%LipName%" -spat -lsrep "|~||" -lerep "|~||" -lswhere "speaker_name " -lsrep "|speaker_name *|speaker_name %speaker_name%|" -write -yes -quiet=2
%Sfk% replace "%Temp%\%LipName%" -spat "|\q$PhraseText$\q|\q%Phrase%\q|" -yes -quiet=2
move /y "%Temp%\%LipName%" "%LipFile%"> nul

:: Exit program
echo Exiting program...
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
	if "%~2"=="}" set "Sentence=<None>"
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
