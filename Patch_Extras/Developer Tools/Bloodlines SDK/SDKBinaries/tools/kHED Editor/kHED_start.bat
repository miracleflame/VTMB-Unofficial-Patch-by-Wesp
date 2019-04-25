@echo off
setlocal ENABLEEXTENSIONS

:: get the manual work
rem reg delete "TODO!"

:: change root directory
pushd "%~dp0"

:: launch program
start kHED.exe

:: quit script
exit
