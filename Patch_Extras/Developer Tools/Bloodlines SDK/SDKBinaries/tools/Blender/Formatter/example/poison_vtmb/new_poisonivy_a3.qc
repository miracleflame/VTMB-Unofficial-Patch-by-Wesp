// Created by Crowbar 0.62

$modelname "character/pc/female/poisonivy/poisonivy_a3.mdl"

$model "girl" "brujahFH_poison_female_Armor_0_REF"{

	eyeball "eye_right" "Bip01 Head" -1.03 -2.89104 65.64 "eyeball_r" 1 4 "iris_unused" 0.63
	eyeball "eye_left" "Bip01 Head" 1.31 -2.89104 65.64 "eyeball_l" 1 -4 "iris_unused" 0.63
}


$illumposition 0 0 38

$eyeposition 0 0 65

$surfaceprop "flesh"

$cdmaterials "models\character\pc\female\poisonivy\"
$cdmaterials "models\character\eyes\"
$cdmaterials "models\character\teeth\"

$attachment "mouth" "Bip01 Head" 1.399998 4.500001 0
$attachment "eyes" "Bip01 Head" 0.14 -2.89 65.64 absolute 
$attachment "0" "Bip01 R Hand" 0 0.000001 0


$sequence "Brujah_Female_Idle2" {
	"poisonivy_a3_anims\Brujah_Female_Idle2.smd"
	activity "ACT_CHARSHEET_FIDGET" 4
	fps 30
}
$sequence "Brujah_Female_ArmOut2" {
	"poisonivy_a3_anims\Brujah_Female_ArmOut2.smd"
	activity "ACT_CHARSHEET_FIDGET" 1
	fps 30
}
$sequence "ragdoll" {
	"poisonivy_a3_anims\ragdoll.smd"
	activity "ACT_DIERAGDOLL" 1
	fps 30
}

$includemodel "character/shared/female/pcidles_allsequences.mdl"
$includemodel "character/shared/female/frenzy.mdl"

