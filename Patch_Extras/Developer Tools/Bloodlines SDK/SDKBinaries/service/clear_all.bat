@echo off
setlocal ENABLEEXTENSIONS
pushd "%~dp0.."

del /f /s /q /a *.rf
del /f /s /q /a *.vdf
del /f /s /q /a *.log
del /f /a /q ..\*.log
del /f /s /q GameCfg.ini
rd /s /q ..\Vampire
copy /y "service\cmdseq.init" "cmdseq.wc"

exit
