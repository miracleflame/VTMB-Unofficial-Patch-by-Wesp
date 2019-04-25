@echo off
title Clear dir from trash

del /a /s /q *.bsp
del /a /s /q *.prt
del /a /s /q *.lin
del /a /s /q *.gl 
del /a /s /q *.vmx
del /a /s /q *.log

echo Trash deleted.
exit
