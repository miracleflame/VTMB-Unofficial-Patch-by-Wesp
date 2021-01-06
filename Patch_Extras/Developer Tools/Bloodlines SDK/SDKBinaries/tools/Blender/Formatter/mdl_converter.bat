@echo off
cd /d "%~dp0"

set "BaseDir=U:\win_xp4\patch102rc1\Patch_Extras\Developer_Tools\Bloodlines_SDK\SDKContent\" 
set "ModDir=U:\win_xp4\patch102rc1\Patch_Extras\Developer_Tools\Bloodlines_SDK\SDKContent\"
set "AlienSwarm=C:\program files (x86)\steam\steamapps\common\alien swarm\swarm\"

set "BaseDir=%~dp0"
set "ModDir=%~dp0"

echo %BaseDir%
echo %ModDir%
echo %1


studiovtmb49g.exe dummy %BaseDir% %ModDir% %1

echo
echo
echo Conversion finished, look in %ModDir%

pause
