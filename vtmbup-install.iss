; -- vtmbup-installer.iss --

[Setup]
AppName=Vampire: The Masquerade - Bloodlines Unofficial Patch 10.1
AppVerName=Vampire: The Masquerade - Bloodlines Unofficial Patch 10.1
VersionInfoDescription=Vampire: The Masquerade - Bloodlines Unofficial Patch
VersionInfoVersion=10.1
AppPublisher=Werner Spahl
DefaultDirName={reg:HKLM\Software\Activision\Vampire - Bloodlines,InstallPath|{pf}\Steam\steamapps\common\vampire the masquerade - bloodlines}
AppendDefaultDirName=no
DirExistsWarning=no
EnableDirDoesntExistWarning=yes
OutputBaseFilename=VTMBup101
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
Name: "extras"; Description: "Patch Extras (Walkthrough, Shaders, SDK and more)"; Flags: checkablealone
                                                                                                    
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
Source: "vtmbup-readme.txt"; DestDir: "{app}"; Components: readme; Flags: isreadme overwritereadonly
Source: "Official_Patch\*"; DestDir: "{app}"; Components: basic; Flags: recursesubdirs ignoreversion overwritereadonly
Source: "Basic_Patch\dlls\*"; DestDir: "{app}\vampire\dlls"; Components: basic; Flags: recursesubdirs ignoreversion overwritereadonly
Source: "Basic_Patch\cl_dlls\*"; DestDir: "{app}\vampire\cl_dlls"; Components: basic; Flags: recursesubdirs ignoreversion overwritereadonly
Source: "Patch_Extras\Developer Tools\Game Mod Loader\*"; DestDir: "{app}"; Components: basic; Flags: recursesubdirs ignoreversion
Source: "Basic_Patch\*"; DestDir: "{app}\Unofficial_Patch"; Components: basic; Flags: recursesubdirs ignoreversion overwritereadonly
Source: "Basic_Local\*"; DestDir: "{app}\Unofficial_Patch"; Components: basic; Flags: recursesubdirs ignoreversion overwritereadonly
Source: "Plus_Patch\*"; DestDir: "{app}\Unofficial_Patch"; Components: plus; Flags: recursesubdirs ignoreversion overwritereadonly
Source: "Plus_Local\*"; DestDir: "{app}\Unofficial_Patch"; Components: plus; Flags: recursesubdirs ignoreversion overwritereadonly
Source: "Patch_Extras\*"; DestDir: "{app}\Patch_Extras"; Components: extras; Flags: ignoreversion overwritereadonly
Source: "Patch_Extras\Developer Tools\*"; DestDir: "{app}\Patch_Extras\Developer Tools"; Components: extras; Flags: recursesubdirs ignoreversion overwritereadonly
Source: "Patch_Extras\Player Mods\*"; DestDir: "{app}\Patch_Extras\Player Mods"; Components: extras; Flags: recursesubdirs ignoreversion overwritereadonly
Source: "Patch_Extras\Developer Tools\Game Mod Loader\Vampire_x64.exe"; DestDir: "{app}"; DestName: "Vampire.exe"; Flags: ignoreversion overwritereadonly; Check: IsWin64
Source: "{app}\*.exe";                          Flags: external dontcopy skipifdoesntexist; Attribs: readonly
Source: "{app}\*.dll";                          Flags: external dontcopy skipifdoesntexist; Attribs: readonly
Source: "{app}\Bin\*.dll";                      Flags: external dontcopy skipifdoesntexist; Attribs: readonly
Source: "{app}\Unofficial_Patch\cl_dlls\*.dll"; Flags: external dontcopy skipifdoesntexist; Attribs: readonly
Source: "{app}\Unofficial_Patch\dlls\*.dll";    Flags: external dontcopy skipifdoesntexist; Attribs: readonly
Source: "{app}\Vampire\cl_dlls\*.dll";          Flags: external dontcopy skipifdoesntexist; Attribs: readonly
Source: "{app}\Vampire\dlls\*.dll";             Flags: external dontcopy skipifdoesntexist; Attribs: readonly
; disabled Source: "{app}\Bin\*"; DestDir: "{app}"; Components: basic; Flags: external skipifsourcedoesntexist overwritereadonly

[InstallDelete]
Type: filesandordirs; Name: "{app}\vampire.dat"
Type: filesandordirs; Name: "{app}\noseqence.txt"
Type: filesandordirs; Name: "{app}\dbghelp.dll.12"
Type: filesandordirs; Name: "{app}\a_basetexture.tth"
Type: filesandordirs; Name: "{app}\Vampire\hl2.tmp"
Type: filesandordirs; Name: "{app}\Vampire\stats.txt"
Type: filesandordirs; Name: "{app}\Vampire\vidcfg.bin"
Type: filesandordirs; Name: "{app}\Vampire\voice_ban.dt"
Type: filesandordirs; Name: "{app}\Unofficial_Patch\hl2.tmp"
Type: filesandordirs; Name: "{app}\Unofficial_Patch\stats.txt"
Type: filesandordirs; Name: "{app}\Unofficial_Patch\vidcfg.bin"
Type: filesandordirs; Name: "{app}\Unofficial_Patch\voice_ban.dt"

[Icons]
Name: "{userdesktop}\VTM Bloodlines Unofficial Patch"; Filename: {app}\vampire.exe; Parameters: "-game Unofficial_Patch"
Name: "{userprograms}\VTM Bloodlines Unofficial Patch"; Filename: {app}\vampire.exe; Parameters: "-game Unofficial_Patch"

[Run]
Filename: {app}\vampire.exe; Parameters: "-game Unofficial_Patch"; Description: Run Bloodlines with the Unofficial Patch; Flags: postinstall runascurrentuser nowait skipifsilent