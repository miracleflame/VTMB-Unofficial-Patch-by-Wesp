ENBSeries v0.076a для игры Vampire - The Masquerade Bloodlines.

Разработано для http://vampirebloodlines.ru


В данной версии добавлен новый параметр TextureQuality в категории [SSAO], который сильно
влияет на скорость отрисовки screen space ambient occlusions. Он принимает значения от 0 до 2,
0 - высокое качество, 2 - высокая скорость.


//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
СИСТЕМНЫЕ ТРЕБОВАНИЯ:
Видеокарта с поддержкой Shader Model 3.0 и выше. Видеокарты нижеуказанных серий не совместимы:
GeForce 5200-5950 и ниже
Radeon 9000, 9500-9800, x300-x850 и ниже

УСТАНОВКА:
Извлечь файлы из архива в папку игры, где находится exe файл

ЗАПУСК:
После запуска игры мод активирован, выключается комбинацией клавиш (по умолчанию SHIFT F12).

НАСТРОЙКИ:
В игре работоспособны следующие параметры:
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

Для повышения производительности следует отключить SSAO через параметр EnableOcclusion=0 или снизить качество эффекта и его фильтрации через параметры OcclusionQuality FilterQuality.

Детальное описание доступно на сайте.



//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



http://boris-vorontsov.narod.ru
Copyright (c) 2009 Воронцов Борис (ENB developer)
