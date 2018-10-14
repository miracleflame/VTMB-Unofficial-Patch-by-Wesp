@echo off
setlocal ENABLEEXTENSIONS

:: change root directory
pushd "%~dp0"

:: launch program
start kHED.exe

:: quit script
exit
