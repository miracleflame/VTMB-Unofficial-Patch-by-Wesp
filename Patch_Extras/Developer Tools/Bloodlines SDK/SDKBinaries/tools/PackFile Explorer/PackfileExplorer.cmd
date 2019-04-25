@echo off
setlocal enableextensions
pushd "%~dp0"

rem To hide console window, use "start /b"...
start /b PackfileExplorer.exe

popd
exit /b