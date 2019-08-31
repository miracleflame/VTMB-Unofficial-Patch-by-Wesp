@echo off
@color 61
title Blender Console
setlocal enableextensions
pushd "%~dp0"

rem To hide Blender console window, use "start /b" instead...
start /b /max blender.exe

popd
exit /b