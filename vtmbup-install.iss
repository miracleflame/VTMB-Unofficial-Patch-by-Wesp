; -- vtmbup-installer.iss --

[Setup]
AppName=Vampire: The Masquerade - Bloodlines Unofficial Patch 9.8
AppVerName=Vampire: The Masquerade - Bloodlines Unofficial Patch 9.8
VersionInfoDescription=Vampire: The Masquerade - Bloodlines Unofficial Patch
VersionInfoVersion=9.8
AppPublisher=Werner Spahl
DefaultDirName={reg:HKLM\Software\Activision\Vampire - Bloodlines,InstallPath|{pf}\Steam\steamapps\common\vampire the masquerade - bloodlines}
AppendDefaultDirName=no
DirExistsWarning=no
EnableDirDoesntExistWarning=yes
OutputBaseFilename=VTMBup98
Uninstallable=no
InfoBeforeFile=vtmbup-readme.txt
InfoAfterFile=vtmbup-after.txt
Compression=lzma2/ultra64
SolidCompression=true
InternalCompressLevel=normal
TimeStampsInUTC=yes
DisableProgramGroupPage=yes
WizardSmallImageFile=vtmbup-small.bmp
WizardImageFile=vtmbup-large.bmp
WizardImageBackColor=clBlack
WizardImageStretch=no

[Types]
Name: "basic"; Description: "Unofficial Patch"; Flags: iscustom

[Components]
Name: "basic"; Description: "Basic Patch"; Types: basic; Flags: fixed checkablealone
Name: "readme"; Description: "Patch Readme"; Types: basic; Flags: fixed checkablealone
Name: "plus"; Description: "Plus Patch (Restorations and Tweaks)"; Flags: checkablealone
Name: "plus\audio"; Description: "No new audio (music pieces and random sounds)"; Flags: dontinheritcheck
Name: "plus\particles"; Description: "No new particles (improved rain and cast effects)"; Flags: dontinheritcheck
Name: "plus\graphics"; Description: "No new graphics (wolf Warform and improved eyes)"; Flags: dontinheritcheck
Name: "plus\disciplines"; Description: "No new Disciplines (cast animations and replaced levels)"; Flags: dontinheritcheck
Name: "extras"; Description: "Patch Extras (Transcripts and Walkthrough)"; Flags: checkablealone
Name: "extras\play"; Description: "Player Mods (Shader suites, Linux script and more)"; Flags: dontinheritcheck
Name: "extras\edit"; Description: "Developer Tools (Unofficial SDK, modding guide and more)"; Flags: dontinheritcheck
                                                                                                    
[Code]
function retail: Boolean; 
var 
  string: String; 
begin 
  result := False; 
  if RegQueryStringValue(HKLM, 'SOFTWARE\Activision\Vampire - Bloodlines','Version',string) then 
  result := True;
end;

[Files]
Source: "{app}\Unofficial_Patch\save\*"; DestDir: "{app}\Unofficial_Patch\save\old"; Components: basic; Flags: external skipifsourcedoesntexist
Source: "{app}\Unofficial_Patch\save\auto*"; DestDir: "{app}\Unofficial_Patch\save"; Components: basic; Flags: external deleteafterinstall skipifsourcedoesntexist
Source: "{app}\Unofficial_Patch\save\quick*"; DestDir: "{app}\Unofficial_Patch\save"; Components: basic; Flags: external deleteafterinstall skipifsourcedoesntexist
Source: "{app}\Unofficial_Patch\save\Vampire-0*"; DestDir: "{app}\Unofficial_Patch\save"; Components: basic; Flags: external deleteafterinstall skipifsourcedoesntexist
Source: "vtmbup-readme.txt"; DestDir: "{app}"; Components: readme; Flags: isreadme
Source: "Official_Patch\*"; DestDir: "{app}"; Components: basic; Flags: recursesubdirs ignoreversion
Source: "Unofficial_Patch\cl_dlls\*"; DestDir: "{app}\vampire\cl_dlls"; Components: basic; Flags: recursesubdirs ignoreversion
Source: "Unofficial_Patch\dlls\*"; DestDir: "{app}\vampire\dlls"; Components: basic; Flags: recursesubdirs ignoreversion
Source: "Unofficial_Patch\*"; DestDir: "{app}\Unofficial_Patch"; Components: basic; Flags: recursesubdirs ignoreversion
Source: "Plus_Patch\Unofficial_Patch\*"; DestDir: "{app}\Unofficial_Patch"; Components: plus; Flags: recursesubdirs ignoreversion
Source: "Unofficial_Patch\sound\schemes\*"; DestDir: "{app}\Unofficial_Patch\sound\schemes"; Components: plus\audio; Flags: ignoreversion
Source: "Unofficial_Patch\materials\models\character\eyes\*"; DestDir: "{app}\Unofficial_Patch\materials\models\character\eyes"; Components: plus\graphics; Flags: ignoreversion
Source: "Unofficial_Patch\models\character\monster\animalism_beastform\animalism_beastform.mdl"; DestDir: "{app}\Unofficial_Patch\models\character\monster\animalism_beastform"; Components: plus\graphics; Flags: ignoreversion
Source: "Unofficial_Patch\particles\*"; DestDir: "{app}\Unofficial_Patch\particles"; Components: plus\particles; Flags: ignoreversion
Source: "Unofficial_Patch\vdata\system\disciplinetgt*"; DestDir: "{app}\Unofficial_Patch\vdata\system"; Components: plus\disciplines; Flags: ignoreversion
Source: "Unofficial_Patch\vdata\system\stats.txt"; DestDir: "{app}\Unofficial_Patch\vdata\system"; Components: plus\disciplines; Flags: ignoreversion
Source: "Patch_Extras\Developer Tools\Game Mod Loader\*"; DestDir: "{app}"; Components: basic; Flags: recursesubdirs ignoreversion
Source: "Patch_Extras\*"; DestDir: "{app}\Patch_Extras"; Components: extras; Flags: ignoreversion
Source: "Patch_Extras\Developer Tools\*"; DestDir: "{app}\Patch_Extras\Developer Tools"; Components: extras\edit; Flags: recursesubdirs ignoreversion
Source: "Patch_Extras\Player Mods\*"; DestDir: "{app}\Patch_Extras\Player Mods"; Components: extras\play; Flags: recursesubdirs ignoreversion

[InstallDelete]
Type: files; Name: "{app}\bin\loader\mods.*"

[Icons]
Name: "{userdesktop}\VTM Bloodlines Unofficial Patch"; Filename: {app}\vampire.exe; Parameters: "-game Unofficial_Patch"
Name: "{userprograms}\VTM Bloodlines Unofficial Patch"; Filename: {app}\vampire.exe; Parameters: "-game Unofficial_Patch"

[Run]
Filename: {app}\vampire.exe; Parameters: "-game Unofficial_Patch"; Description: Run Bloodlines with the Unofficial Patch; Flags: postinstall runascurrentuser nowait skipifsilent