@echo off
setlocal EnableExtensions
pushd "%~dp0"

set Version=0.65
set ProgramExe=CroVtmb.exe
set "CfgPath=%AppData%\ZeqMacaw\CroVtmb %Version%"
set "ProgSettings=%CfgPath%\Crowbar Settings.xml"
if exist "ProjectDir.ini" (
for /f "usebackq delims=" %%a in ("ProjectDir.ini") do (set "ProjectDir=%%~a"))
if not defined ProjectDir set ProjectDir=NULL

pushd ..\..
set "SDKBinaries=%cd%"
set Sfk="%cd%\helpers\sfk.exe"
set GameCfg="%cd%\GameCfg.ini"
if exist "GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in (%GameCfg%) do (set "%%~a=%%~b"))
if defined GameDir (for %%m in ("%GameDir%") do (set "SDKContent=%%~dpm"))
popd

for %%m in (%Sfk% %GameCfg%) do (if not exist "%%~m" (
	echo>>"..\sdk_errors.log" [%date% %time%] Crowbar tool: Missing "%%~m" file.
	goto RunProgram
))


:CheckIfCfgResetNeeded
echo "%ModDir%"> "ProjectDir.ini"
if /i "%ModDir%"=="%ProjectDir%" goto RunProgram


:ParseDefaultConfig
if exist "%ProgSettings%" (
del /f /q "%ProgSettings%")

rem MDL Decompiler as default tab...
%Sfk% filter "Settings.xml" -where "<MainWindowSelectedTabIndex>" -rep "|<MainWindowSelectedTabIndex>*|<MainWindowSelectedTabIndex>4</MainWindowSelectedTabIndex>|" -write -yes -quiet=2

rem Game paths setup...
for %%m in ("%ModDir%") do (
%Sfk% filter "Settings.xml" -where "<GameAppOptions>" -rep "|<GameAppOptions>*|<GameAppOptions>-game %%~nxm</GameAppOptions>|" -write -yes -quiet=2)
%Sfk% filter "Settings.xml" -where "<GameName>" -rep "|<GameName>*|<GameName>%Name%</GameName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<GameAppPathFileName>" -rep "|<GameAppPathFileName>*|<GameAppPathFileName>%GameExe%</GameAppPathFileName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<GamePathFileName>" -rep "|<GamePathFileName>*|<GamePathFileName>%SDKBinaries%\GameCfg.ini</GamePathFileName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<CompilerPathFileName>" -rep "|<CompilerPathFileName>*|<CompilerPathFileName>%SDKBinaries%\StudioMDL.bat</CompilerPathFileName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<ViewerPathFileName>" -rep "|<ViewerPathFileName>*|<ViewerPathFileName>%SDKBinaries%\HLMV.exe</ViewerPathFileName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<MappingToolPathFileName>" -rep "|<MappingToolPathFileName>*|<MappingToolPathFileName>%SDKBinaries%\Hammer.exe</MappingToolPathFileName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<PackerPathFileName>" -rep "|<PackerPathFileName>*|<PackerPathFileName>%SDKBinaries%\BspZip.exe</PackerPathFileName>|" -write -yes -quiet=2

rem VPK extraction settings...
%Sfk% filter "Settings.xml" -where "<UnpackPackagePathFolderOrFileName>" -rep "|<UnpackPackagePathFolderOrFileName>*|<UnpackPackagePathFolderOrFileName>%GameExeDir%\Vampire</UnpackPackagePathFolderOrFileName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<UnpackOutputSamePath>" -rep "|<UnpackOutputSamePath>*|<UnpackOutputSamePath>%GameExeDir%\Vampire</UnpackOutputSamePath>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<UnpackOutputFullPath>" -rep "|<UnpackOutputFullPath>*|<UnpackOutputFullPath>%GameDir%</UnpackOutputFullPath>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<UnpackOutputFolderOption>" -rep "|<UnpackOutputFolderOption>*|<UnpackOutputFolderOption>WorkFolder</UnpackOutputFolderOption>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<UnpackOutputSubfolderName>" -rep "|<UnpackOutputSubfolderName>*|<UnpackOutputSubfolderName>Unpacked</UnpackOutputSubfolderName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<UnpackMode>" -rep "|<UnpackMode>*|<UnpackMode>Folder</UnpackMode>|" -write -yes -quiet=2

rem Model view/preview settings...
if exist "%ModDir%\" (
%Sfk% filter "Settings.xml" -where "<PreviewMdlPathFileName>" -rep "|<PreviewMdlPathFileName>*|<PreviewMdlPathFileName>%ModDir%\models\path\file.mdl</PreviewMdlPathFileName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<ViewMdlPathFileName>" -rep "|<ViewMdlPathFileName>*|<ViewMdlPathFileName>%ModDir%\models\path\file.mdl</ViewMdlPathFileName>|" -write -yes -quiet=2) else (
%Sfk% filter "Settings.xml" -where "<PreviewMdlPathFileName>" -rep "|<PreviewMdlPathFileName>*|<PreviewMdlPathFileName>%GameDir%\models\path\file.mdl</PreviewMdlPathFileName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<ViewMdlPathFileName>" -rep "|<ViewMdlPathFileName>*|<ViewMdlPathFileName>%GameDir%\models\path\file.mdl</ViewMdlPathFileName>|" -write -yes -quiet=2)

rem Model decompiler settings...
if exist "%ModDir%\" (
%Sfk% filter "Settings.xml" -where "<DecompileMdlPathFileName>" -rep "|<DecompileMdlPathFileName>*|<DecompileMdlPathFileName>%ModDir%\models\path\file.mdl</DecompileMdlPathFileName>|" -write -yes -quiet=2) else (
%Sfk% filter "Settings.xml" -where "<DecompileMdlPathFileName>" -rep "|<DecompileMdlPathFileName>*|<DecompileMdlPathFileName>%GameDir%\models\path\file.mdl</DecompileMdlPathFileName>|" -write -yes -quiet=2)
%Sfk% filter "Settings.xml" -where "<DecompileOutputFullPath>" -rep "|<DecompileOutputFullPath>*|<DecompileOutputFullPath>%SDKContent%ModelSrc</DecompileOutputFullPath>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<DecompileOutputFolderOption>" -rep "|<DecompileOutputFolderOption>*|<DecompileOutputFolderOption>WorkFolder</DecompileOutputFolderOption>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<DecompileOutputSubfolderName>" -rep "|<DecompileOutputSubfolderName>*|<DecompileOutputSubfolderName>Decompiled</DecompileOutputSubfolderName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<DecompileQcFileIsChecked>" -rep "|<DecompileQcFileIsChecked>*|<DecompileQcFileIsChecked>true</DecompileQcFileIsChecked>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<DecompileFolderForEachModelIsChecked>" -rep "|<DecompileFolderForEachModelIsChecked>*|<DecompileFolderForEachModelIsChecked>true</DecompileFolderForEachModelIsChecked>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<DecompileQcUseMixedCaseForKeywordsIsChecked>" -rep "|<DecompileQcUseMixedCaseForKeywordsIsChecked>*|<DecompileQcUseMixedCaseForKeywordsIsChecked>true</DecompileQcUseMixedCaseForKeywordsIsChecked>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<DecompileBoneAnimationPlaceInSubfolderIsChecked>" -rep "|<DecompileBoneAnimationPlaceInSubfolderIsChecked>*|<DecompileBoneAnimationPlaceInSubfolderIsChecked>true</DecompileBoneAnimationPlaceInSubfolderIsChecked>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<DecompileGroupIntoQciFilesIsChecked>" -rep "|<DecompileGroupIntoQciFilesIsChecked>*|<DecompileGroupIntoQciFilesIsChecked>false</DecompileGroupIntoQciFilesIsChecked>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<DecompilePrefixFileNamesWithModelNameIsChecked>" -rep "|<DecompilePrefixFileNamesWithModelNameIsChecked>*|<DecompilePrefixFileNamesWithModelNameIsChecked>true</DecompilePrefixFileNamesWithModelNameIsChecked>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<DecompileStricterFormatIsChecked>" -rep "|<DecompileStricterFormatIsChecked>*|<DecompileStricterFormatIsChecked>true</DecompileStricterFormatIsChecked>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<DecompileMode>" -rep "|<DecompileMode>*|<DecompileMode>File</DecompileMode>|" -write -yes -quiet=2

rem Model compiler settings...
%Sfk% filter "Settings.xml" -where "<CompileQcPathFileName>" -rep "|<CompileQcPathFileName>*|<CompileQcPathFileName>%SDKContent%ModelSrc\MyMode\file.qc</CompileQcPathFileName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<CompileOutputFullPath>" -rep "|<CompileOutputFullPath>*|<CompileOutputFullPath>%ModDir%</CompileOutputFullPath>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<CompileOutputFolderOption>" -rep "|<CompileOutputFolderOption>*|<CompileOutputFolderOption>WorkFolder</CompileOutputFolderOption>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<CompileOutputSubfolderName>" -rep "|<CompileOutputSubfolderName>*|<CompileOutputSubfolderName>Compiled</CompileOutputSubfolderName>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<CompileOptionDefineBonesIsChecked>" -rep "|<CompileOptionDefineBonesIsChecked>*|<CompileOptionDefineBonesIsChecked>false</CompileOptionDefineBonesIsChecked>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<CompileOptionNoP4IsChecked>" -rep "|<CompileOptionNoP4IsChecked>*|<CompileOptionNoP4IsChecked>false</CompileOptionNoP4IsChecked>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<CompileMode>" -rep "|<CompileMode>*|<CompileMode>File</CompileMode>|" -write -yes -quiet=2

rem Unused stuff overrides...
%Sfk% filter "Settings.xml" -where "<DownloadOutputWorkPath>" -rep "|<DownloadOutputWorkPath>*|<DownloadOutputWorkPath>%SDKContent%</DownloadOutputWorkPath>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<PackOutputPath>" -rep "|<PackOutputPath>*|<PackOutputPath>%ModDir%</PackOutputPath>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<PackMode>" -rep "|<PackMode>*|<PackMode>Folder</PackMode>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<PackOutputFolderOption>" -rep "|<PackOutputFolderOption>*|<PackOutputFolderOption>ParentFolder</PackOutputFolderOption>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<UpdateDownloadPath>" -rep "|<UpdateDownloadPath>*|<UpdateDownloadPath>%cd%\update</UpdateDownloadPath>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<UpdateUpdateDownloadPath>" -rep "|<UpdateUpdateDownloadPath>*|<UpdateUpdateDownloadPath>%cd%\update</UpdateUpdateDownloadPath>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<UpdateCopySettingsIsChecked>" -rep "|<UpdateCopySettingsIsChecked>*|<UpdateCopySettingsIsChecked>true</UpdateCopySettingsIsChecked>|" -write -yes -quiet=2
%Sfk% filter "Settings.xml" -where "<LibraryPath*>" -rep "|<LibraryPath*|<LibraryPath />|" -write -yes -quiet=2


:RunProgram
if not exist "%ProgSettings%" (
if not exist "%CfgPath%\" md "%CfgPath%"
copy /y "Settings.xml" "%ProgSettings%")
start %ProgramExe% %*


:Quit
popd
exit