@echo off
title kHED launcher
setlocal ENABLEEXTENSIONS

:: change working dir
pushd "%~dp0"

:: get the manual work
reg add "HKCU\Software\kHED\kHED\Settings" /v "DirOpenSave" /d "%CD%" /f> nul

:: launch program
start kHED.exe

:: quit launch script
exit
