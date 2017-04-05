ENBSeries v0.076s for Vampire - The Masquerade Bloodlines.

Developed for http://vampirebloodlines.ru


In this version new parameter TextureQuality in category [SSAO] added, it's greatly affect
performance and have the range of values from 0 till 2 (0 means the best quality, 2 is the fast)


//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
SYSTEM REQUIREMENTS:
Videocard with support of Shader Model 2.0 or better. Videocards in the list below will not work:
GeForce 5200-5950 and lower
Radeon 9000, 9500-9800, x300-x850 and lower

INSTALLING:
Extract files from archive in to the game directory, where game execution file exist (.exe).

STARTING:
After game start the mod activated by default, to deactivate it use key combination (shift+f12 by default).

SETTING DESCRIPTION:
These parameters are only valid for this game:

[GLOBAL]
UseEffect=1
AllowAntialias=1
BugFixMode=0
SkipShaderOptimization=0
QuadVertexBuffer=0
AdditionalConfigFile=enbseries2.ini
CyclicConfigReading=0
[EFFECT]
EnableBloom=1
EnableOcclusion=1
EnableDepthOfField=1
[INPUT]
KeyUseEffect=123
KeyBloom=120
KeyOcclusion=121
KeyReflection=122
KeyCombination=16
KeyScreenshot=44
KeyShowFPS=106
KeyDepthOfField=118
[BLOOM]
BloomPowerDay=10
BloomFadeTime=1500
BloomConstantDay=0
BloomQuality=0
BloomScreenLevelDay=45
BloomCurveDay=5
BloomPowerNight=30
BloomConstantNight=0
BloomCurveNight=5
BloomScreenLevelNight=15
BloomAdaptationScreenLevel=70
BloomAdaptationMultiplier=20
BloomAllowOversaturation=1
BloomMaxLimit=80
[SSAO]
UseFilter=1
OcclusionQuality=0
FilterQuality=1
DarkeningLevel=30
BrighteningLevel=30
IlluminationLevel=30
AdditiveIlluminationLevel=30
UseAmbientOcclusion=1
UseIndirectLighting=1
FadeDistance=50
UseForAlphaTest=1
UseForAlphaBlend=1
UseNoiseRandomization=1
[COLORCORRECTION]
DarkeningAmountDay=20
ScreenLevelDay=45
ScreenLevelNight=20
DarkeningAmountNight=0
GammaCurveDay=-1
GammaCurveNight=4
ColorSaturationDay=-1
ColorSaturationNight=0
UsePaletteTexture=0
[ENGINE]
ForceAnisotropicFiltering=1
MaxAnisotropy=8
[MOTIONBLUR]
MotionBlurQuality=1
MotionBlurVelocity=40
MotionBlurRotation=40
[DEPTHOFFIELD]
DOFQuality=0
DOFNumberOfPasses=2
DOFFocusRange=50
DOFBlurinessRange=15
DOFFadeTime=200
[OBJECT]
UseExponentialLighting=1

To achieve better performance, turn off SSAO effect by EnableOcclusion=0 or modify quality of this effect and it's filtering by parameters OcclusionQuality FilterQuality.

More detailed description available on the web site.



//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



http://boris-vorontsov.narod.ru
Copyright (c) 2009 Vorontsov Boris (ENB developer)
