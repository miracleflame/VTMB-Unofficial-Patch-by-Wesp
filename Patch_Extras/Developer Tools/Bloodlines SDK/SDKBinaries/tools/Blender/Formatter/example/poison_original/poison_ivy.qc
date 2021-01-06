// Created by Crowbar 0.62

$modelname "Poison_ivy2.mdl"

$model "model" "poison_ivy_Refrence1.smd" {

	eyeball "eye_right" "Bip01_Head" -1.067195 1.959986 66.998864 "eyeball_r" 1 4 "iris_unused" 0.63
	eyeball "eye_left" "Bip01_Head" 1.272804 1.959986 67.001149 "eyeball_l" 1 -4 "iris_unused" 0.63


	mouth 0 "mouth" "Bip01_Head" 0 1 0

	flexfile "poison_ivy_01.vta" 
	{
		defaultflex frame 0
		flex "Blink" frame 1
		flex "Smile" frame 2
		flex "Angry" frame 3
		flex "Mouth_open" frame 4
		flex "Eyebrow_inner_L_down" frame 5
		flex "Eyebrow_inner_R_down" frame 6
		flex "Eyebrow_inner_L_up" frame 7
		flex "Eyebrow_inner_R_up" frame 8
		flex "Eyebrow_outter_L_up" frame 9
		flex "Eyebrow_outter_R_up" frame 10
		flex "Eyebrow_outter_L_down" frame 11
		flex "Eyebrow_outter_R_down" frame 12
		flex "Eyelid_close_R" frame 13
		flex "eyelid_open_R" frame 14
		flex "eyelid_open_L" frame 15
		flex "Eyelid_close_L" frame 16
		flex "Eyelid_bottem_R_up" frame 17
		flex "Eyelid_bottem_L_up" frame 18
		flex "Lip_top_corner_L" frame 19
		flex "Lip_top_corner_R" frame 20
		flex "Lip_corner_L_up" frame 21
		flex "Lip_corner_R_up" frame 22
		flex "Lip_corner_L_down" frame 23
		flex "Lip_corner_R_down" frame 24
		flex "Lip_bottem_corner_R" frame 25
		flex "Lip_corner_extend" frame 26
		flex "Tongue_Fold" frame 27
		flex "Tongue_extend" frame 28
	}

	flexcontroller phoneme range 0 1 "blank"
	flexcontroller phoneme range 0 1 "Blink"
	flexcontroller phoneme range 0 1 "Smile"
	flexcontroller phoneme range 0 1 "Angry"
	flexcontroller phoneme range 0 1 "Mouth_open"
	flexcontroller phoneme range 0 1 "Eyebrow_inner_L_down"
	flexcontroller phoneme range 0 1 "Eyebrow_inner_R_down"
	flexcontroller phoneme range 0 1 "Eyebrow_inner_L_up"
	flexcontroller phoneme range 0 1 "Eyebrow_inner_R_up"
	flexcontroller phoneme range 0 1 "Eyebrow_outter_L_up"
	flexcontroller phoneme range 0 1 "Eyebrow_outter_R_up"
	flexcontroller phoneme range 0 1 "Eyebrow_outter_L_down"
	flexcontroller phoneme range 0 1 "Eyebrow_outter_R_down"
	flexcontroller phoneme range 0 1 "Eyelid_close_R"
	flexcontroller phoneme range 0 1 "eyelid_open_R"
	flexcontroller phoneme range 0 1 "eyelid_open_L"
	flexcontroller phoneme range 0 1 "Eyelid_close_L"
	flexcontroller phoneme range 0 1 "Eyelid_bottem_R_up"
	flexcontroller phoneme range 0 1 "Eyelid_bottem_L_up"
	flexcontroller phoneme range 0 1 "Lip_top_corner_L"
	flexcontroller phoneme range 0 1 "Lip_top_corner_R"
	flexcontroller phoneme range 0 1 "Lip_corner_L_up"
	flexcontroller phoneme range 0 1 "Lip_corner_R_up"
	flexcontroller phoneme range 0 1 "Lip_corner_L_down"
	flexcontroller phoneme range 0 1 "Lip_corner_R_down"
	flexcontroller phoneme range 0 1 "Tongue_Fold"
	flexcontroller phoneme range 0 1 "Tongue_extend"
	flexcontroller phoneme range 0 1 "Lip_bottem_corner_R"
	flexcontroller phoneme range 0 1 "Lip_corner_extend"

	localvar blank
	%blank = blank
	%Blink = Blink
	%Smile = Smile
	%Angry = Angry
	%Mouth_open = Mouth_open
	%Eyebrow_inner_L_down = Eyebrow_inner_L_down
	%Eyebrow_inner_R_down = Eyebrow_inner_R_down
	%Eyebrow_inner_L_up = Eyebrow_inner_L_up
	%Eyebrow_inner_R_up = Eyebrow_inner_R_up
	%Eyebrow_outter_L_up = Eyebrow_outter_L_up
	%Eyebrow_outter_R_up = Eyebrow_outter_R_up
	%Eyebrow_outter_L_down = Eyebrow_outter_L_down
	%Eyebrow_outter_R_down = Eyebrow_outter_R_down
	%Eyelid_close_R = Eyelid_close_R
	%eyelid_open_R = eyelid_open_R
	%eyelid_open_L = eyelid_open_L
	%Eyelid_close_L = Eyelid_close_L
	%Eyelid_bottem_R_up = Eyelid_bottem_R_up
	%Eyelid_bottem_L_up = Eyelid_bottem_L_up
	%Lip_top_corner_L = Lip_top_corner_L
	%Lip_top_corner_R = Lip_top_corner_R
	%Lip_corner_L_up = Lip_corner_L_up
	%Lip_corner_R_up = Lip_corner_R_up
	%Lip_corner_L_down = Lip_corner_L_down
	%Lip_corner_R_down = Lip_corner_R_down
	%Tongue_Fold = Tongue_Fold
	%Tongue_extend = Tongue_extend
	%Lip_bottem_corner_R = Lip_bottem_corner_R
	%Lip_corner_extend = Lip_corner_extend
}


$surfaceprop "Flesh"

$contents "solid"

$illumposition 0.134 8.483 37.187

$eyeposition 0 0 70

$cdmaterials "models\textures\PoisonIvy\"
$cdmaterials "models\character\pc\female\poisonivy\"

$attachment "eyes" "Bip01_Head" 0.21 1.95 67 absolute
//$attachment "eyes" "Bip01_Head" 2.06 3.37 0.01 rotate -0.04 90.07 89.97
$attachment "mouth" "Bip01_Head" 0.8 -5.8 -0.15 rotate 0 -80 -90

$cbox 0 0 0 0 0 0

$bbox -21.255 -24.225 -0.07 4.288 24.494 74.445

$definebone "Bip01_Pelvis" "" 0.133744 5.288572 39.156391 -89.97202 -179.959913 0 0 0 0 0 0 0
$definebone "Bip01_Spine" "Bip01_Pelvis" 3.547272 1.246854 -0.000872 0.003151 4.513188 -0.039821 0 0 0 0 0 0
$definebone "Bip01_Spine1" "Bip01_Spine" 4.298733 -0.003356 -0.000001 0 -13.037884 -0.000344 0 0 0 0 0 0
$definebone "Bip01_Spine2" "Bip01_Spine1" 4.299057 -0.003383 -0.000001 0.000057 -7.430917 0.000115 0 0 0 0 0 0
$definebone "Bip01_Spine3" "Bip01_Spine2" 4.300041 -0.003371 0.000001 -0.000057 9.266564 -0.000458 0 0 0 0 0 0
$definebone "Bip01_Neck" "Bip01_Spine3" 5.124729 0.31403 0.000003 -0.000115 20.998963 0.000229 0 0 0 0 0 0
$definebone "Bip01_Head" "Bip01_Neck" 4.565876 -0.040794 0.000002 -0.000057 -14.381122 -0.036669 0 0 0 0 0 0
$definebone "FcFX_Jaw" "Bip01_Head" 1.028221 0.578407 0.004742 -89.862928 -80.888176 -99.058275 0 0 0 0 0 0
$definebone "Hair_ROOT" "Bip01_Head" -0.162727 -0.560422 -0.000374 0 0.023036 0.008995 0 0 0 0 0 0
$definebone "HairBone_224" "Hair_ROOT" 0.763382 -0.669316 2.764023 -60.149221 10.044357 -45.931616 0 0 0 0 0 0
$definebone "HairBone_223" "Hair_ROOT" 0.076683 -0.857722 1.159083 -79.606928 5.783499 -47.9058 0 0 0 0 0 0
$definebone "HairBone_220" "Hair_ROOT" 1.515251 -0.49749 -3.643223 -36.961029 -165.966427 127.907997 0 0 0 0 0 0
$definebone "HairBone_219" "Hair_ROOT" 2.860924 -0.005849 -4.37781 -12.728123 -164.380306 135.778261 0 0 0 0 0 0
$definebone "HairBone_218" "Hair_ROOT" 3.016624 1.490776 -2.951019 0.508328 38.10468 -116.611001 0 0 0 0 0 0
$definebone "HairBone_217" "Hair_ROOT" 2.061295 0.7585 -2.803611 13.293368 42.154056 -112.468997 0 0 0 0 0 0
$definebone "HairBone_216" "Hair_ROOT" 6.056816 1.117692 3.466377 38.921143 19.508187 -35.765917 0 0 0 0 0 0
$definebone "HairBone_215" "Hair_ROOT" 4.688667 0.765981 4.287884 15.886744 16.72642 -34.514288 0 0 0 0 0 0
$definebone "HairBone_214" "Hair_ROOT" 3.607849 1.898101 2.859509 -17.982797 -149.368329 60.028791 0 0 0 0 0 0
$definebone "HairBone_212" "Hair_ROOT" 6.752129 1.412381 -2.556164 60.810848 -152.044916 153.704748 0 0 0 0 0 0
$definebone "HairBone_211" "Hair_ROOT" 7.266617 1.790926 -1.041841 79.97429 -142.841277 169.280762 0 0 0 0 0 0
$definebone "HairBone_209" "Hair_ROOT" 5.328438 2.859709 -1.421484 -61.569006 85.05845 167.869468 0 0 0 0 0 0
$definebone "HairBone_208" "Hair_ROOT" 5.150749 2.677885 1.82959 -61.598348 -95.003622 -14.328759 0 0 0 0 0 0
$definebone "HairBone_206" "Hair_ROOT" 7.318932 1.885924 0.601716 79.928589 37.347393 -8.01522 0 0 0 0 0 0
$definebone "HairBone_205" "Hair_ROOT" 6.923012 1.587714 2.172895 60.87482 28.030192 -22.001981 0 0 0 0 0 0
$definebone "HairBone_202" "Hair_ROOT" 2.721863 1.983485 0.421252 86.751599 134.817034 6.043559 0 0 0 0 0 0
$definebone "HairBone_198" "Hair_ROOT" 3.397453 2.549569 -0.416214 -86.750322 135.465069 175.920321 0 0 0 0 0 0
$definebone "HairBone_197" "Hair_ROOT" 3.454651 2.370828 -1.618299 -75.818454 114.185027 -169.082577 0 0 0 0 0 0
$definebone "HairBone_196" "Hair_ROOT" 1.687126 0.751121 -2.036773 -13.293347 -137.846005 105.816693 0 0 0 0 0 0
$definebone "HairBone_195" "Hair_ROOT" 2.574905 1.540911 -2.105668 -0.508366 -141.895323 103.08179 0 0 0 0 0 0
$definebone "HairBone_117" "Hair_ROOT" 2.747353 -0.672194 4.92795 12.758053 -164.311922 43.477529 0 0 0 0 0 0
$definebone "HairBone_114" "Hair_ROOT" 4.454193 -0.418395 5.050203 -15.886745 -163.273488 20.746401 0 0 0 0 0 0
$definebone "HairBone_113" "Hair_ROOT" 6.08535 -0.104727 4.360658 -38.921202 -160.491675 9.520897 0 0 0 0 0 0
$definebone "HairBone_78" "Hair_ROOT" 7.345367 0.210416 3.04809 -60.874881 -151.970522 -3.095233 0 0 0 0 0 0
$definebone "HairBone_77" "Hair_ROOT" 8.029312 0.425924 1.312246 -79.928705 -142.654239 -16.486402 0 0 0 0 0 0
$definebone "HairBone_74" "Hair_ROOT" 8.144226 0.431238 -0.594832 -79.97431 37.157578 163.060236 0 0 0 0 0 0
$definebone "HairBone_73" "Hair_ROOT" 7.688202 0.226947 -2.422968 -60.81093 27.947396 175.748965 0 0 0 0 0 0
$definebone "HairBone_38" "Hair_ROOT" 6.653725 -0.076781 -3.926522 -38.835367 19.469169 -171.205919 0 0 0 0 0 0
$definebone "HairBone_37" "Hair_ROOT" 5.123497 -0.41223 -4.868546 -15.818278 16.686658 -163.1306 0 0 0 0 0 0
$definebone "HairBone_34" "Hair_ROOT" 3.391144 -0.72048 -5.058829 12.728145 15.619751 -151.261835 0 0 0 0 0 0
$definebone "HairBone_33" "Hair_ROOT" 1.746063 -0.929947 -4.42308 36.961046 14.033573 -132.920072 0 0 0 0 0 0
$definebone "HairBone_14" "Hair_ROOT" 3.499916 2.221948 2.001583 -75.825919 -65.873596 1.750386 0 0 0 0 0 0
$definebone "HairBone_13" "Hair_ROOT" 3.392708 2.484137 0.78309 -86.751996 -45.185977 -7.527862 0 0 0 0 0 0
$definebone "HairBone_12" "Hair_ROOT" 1.715546 0.5308 2.560017 13.316171 -137.769192 68.507303 0 0 0 0 0 0
$definebone "HairBone_11" "Hair_ROOT" 2.630463 1.232542 2.900033 0.614841 -141.823893 64.548737 0 0 0 0 0 0
$definebone "HairBone_10" "Hair_ROOT" 3.254189 0.246978 4.458487 -12.758053 15.688106 -37.214696 0 0 0 0 0 0
$definebone "HairBone_09" "Hair_ROOT" 1.877098 -0.273623 3.914257 -37.105382 14.052655 -40.869882 0 0 0 0 0 0
$definebone "HairBone_08" "Hair_ROOT" 6.059311 1.121884 -3.44963 28.372358 -47.75529 -135.938893 0 0 0 0 0 0
$definebone "HairBone_07" "Hair_ROOT" 5.066734 2.239162 -2.610055 26.587941 -36.303067 -124.44449 0 0 0 0 0 0
$definebone "HairBone_06" "Hair_ROOT" 3.609352 1.900779 -2.846711 -61.517431 105.780875 -175.892413 0 0 0 0 0 0
$definebone "HairBone_05" "Hair_ROOT" 3.995804 1.052848 -4.052112 -38.410276 110.658409 170.848537 0 0 0 0 0 0
$definebone "HairBone_02" "Hair_ROOT" -0.039345 -0.892212 -0.625157 -79.844345 -173.645841 129.992476 0 0 0 0 0 0
$definebone "HairBone_01" "Hair_ROOT" 0.486664 -0.789834 -2.315691 -60.154303 -169.792821 125.233828 0 0 0 0 0 0
$definebone "Bip01_L_Clavicle" "Bip01_Neck" -2.08905 0.46661 0.861666 -74.224848 167.044941 -8.401566 0 0 0 0 0 0
$definebone "Bip01_L_UpperArm" "Bip01_L_Clavicle" 5.389013 0 0.000004 24.650481 5.211168 12.914811 0 0 0 0 0 0
$definebone "Bip01_LUpArmTwist1" "Bip01_L_UpperArm" 4.680197 0.000002 -0.000008 -0.000055 0.000002 0.000001 0 0 0 0 0 0
$definebone "Bip01_L_Forearm" "Bip01_LUpArmTwist1" 4.680189 0 0 0.000061 -24.417856 0.645206 0 0 0 0 0 0
$definebone "Bip01_L_Foretwist1" "Bip01_L_Forearm" 5.310394 -0.000004 0.000008 -0.000051 -0.000001 0.645203 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Hand" "Bip01_L_Foretwist1" 5.310405 -0.000002 -0.000019 -0.129425 -5.561532 -89.357767 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger0" "ValveBiped.Bip01_L_Hand" 0.788815 0.492153 -0.800477 36.948045 28.505568 71.991465 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger01" "ValveBiped.Bip01_L_Finger0" 1.376484 -0.000002 -0.000004 -0.000055 14.758309 -0.000063 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger02" "ValveBiped.Bip01_L_Finger01" 1.271763 -0.000006 0.000004 0.000061 13.65691 -0.000006 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger1" "ValveBiped.Bip01_L_Hand" 3.031596 -0.250698 -1.182723 11.304455 17.576631 21.709948 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger11" "ValveBiped.Bip01_L_Finger1" 1.670164 -0.000004 -0.000005 -0.000002 18.45916 0.000007 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger12" "ValveBiped.Bip01_L_Finger11" 1.171265 -0.000006 -0.000004 0.000054 11.302567 0.000003 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger2" "ValveBiped.Bip01_L_Hand" 3.211712 -0.259224 -0.342309 3.537156 12.641403 8.679858 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger21" "ValveBiped.Bip01_L_Finger2" 1.706472 0 -0.000002 0.000002 19.534713 0.000002 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger22" "ValveBiped.Bip01_L_Finger21" 1.155331 -0.000004 -0.000004 0.000001 13.368999 0 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger3" "ValveBiped.Bip01_L_Hand" 3.179646 -0.271179 0.530161 -3.511486 11.641937 7.53801 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger31" "ValveBiped.Bip01_L_Finger3" 1.6311 0.000004 -0.000001 0 26.723042 0.000002 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger32" "ValveBiped.Bip01_L_Finger31" 1.025364 0 -0.000002 -0.000001 13.368997 0.000002 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger4" "ValveBiped.Bip01_L_Hand" 3.072542 -0.125546 1.254084 -16.501298 18.87547 0.81498 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger41" "ValveBiped.Bip01_L_Finger4" 1.302765 0.000008 -0.000002 -0.000001 21.649904 0.000002 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_L_Finger42" "ValveBiped.Bip01_L_Finger41" 0.680267 0 -0.000001 -0.000001 8.636996 0.000114 0 0 0 0 0 0
$definebone "Bip01_R_Clavicle" "Bip01_Neck" -2.089058 0.466612 -0.861665 74.224732 167.044422 8.400994 0 0 0 0 0 0
$definebone "Bip01_R_UpperArm" "Bip01_R_Clavicle" 5.389013 -0.000001 0 -24.650368 5.210597 -12.915037 0 0 0 0 0 0
$definebone "Bip01_RUpArmTwist1" "Bip01_R_UpperArm" 4.680191 0.000002 -0.000004 -0.000063 0.000002 0.000003 0 0 0 0 0 0
$definebone "Bip01_R_Forearm" "Bip01_RUpArmTwist1" 4.680197 0.000001 0 0.000056 -24.41786 -0.645262 0 0 0 0 0 0
$definebone "Bip01_R_Foretwist1" "Bip01_R_Forearm" 5.310389 -0.000002 -0.000011 -0.000002 -0.000002 -0.645205 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Hand" "Bip01_R_Foretwist1" 5.310395 0.000001 -0.000004 0.129489 -5.561646 89.357808 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger0" "ValveBiped.Bip01_R_Hand" 0.788813 0.492165 0.800473 -36.947984 28.505571 -71.991465 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger01" "ValveBiped.Bip01_R_Finger0" 1.376486 0.000002 -0.000006 -0.000004 14.758311 0.000003 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger02" "ValveBiped.Bip01_R_Finger01" 1.27177 -0.000002 0.000002 0.000053 13.656971 0.000003 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger1" "ValveBiped.Bip01_R_Hand" 3.0316 -0.25069 1.182717 -11.304456 17.576691 -21.709948 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger11" "ValveBiped.Bip01_R_Finger1" 1.67016 0 0.000002 0.000053 18.459165 -0.000003 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger12" "ValveBiped.Bip01_R_Finger11" 1.171276 0.000004 -0.000002 -0.000003 11.302576 -0.000003 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger2" "ValveBiped.Bip01_R_Hand" 3.21172 -0.259216 0.342302 -3.537099 12.641461 -8.679857 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger21" "ValveBiped.Bip01_R_Finger2" 1.706465 -0.000004 -0.000001 0.000001 19.534662 0.000058 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger22" "ValveBiped.Bip01_R_Finger21" 1.155338 -0.000004 0 0.000001 13.369006 0.000002 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger3" "ValveBiped.Bip01_R_Hand" 3.179649 -0.271168 -0.530169 3.511543 11.641935 -7.538009 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger31" "ValveBiped.Bip01_R_Finger3" 1.631102 -0.000011 0 0 26.723105 -0.000002 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger32" "ValveBiped.Bip01_R_Finger31" 1.025364 0.000004 -0.000001 0.000001 13.369009 0 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger4" "ValveBiped.Bip01_R_Hand" 3.072538 -0.125542 -1.254087 16.501298 18.875532 -0.814978 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger41" "ValveBiped.Bip01_R_Finger4" 1.302752 0 -0.000003 0 21.649912 -0.000002 0 0 0 0 0 0
$definebone "ValveBiped.Bip01_R_Finger42" "ValveBiped.Bip01_R_Finger41" 0.680264 0.000004 0.000002 0 8.637007 -0.000003 0 0 0 0 0 0
$definebone "Breast_Leftb" "Bip01_Spine2" 2.018768 3.462392 2.388151 -20.733229 136.452701 -13.241685 0 0 0 0 0 0
$definebone "Breast_Right" "Bip01_Spine2" 2.018768 3.462403 -2.388041 -20.733169 -43.547374 -13.241628 0 0 0 0 0 0
$definebone "Bip01_L_Thigh" "Bip01_Spine" -3.634377 -0.963854 3.905175 0.3728 173.814929 170.58888 0 0 0 0 0 0
$definebone "Bip01_LThighTwist1" "Bip01_L_Thigh" 9.348627 -0.000026 -0.000002 0 0.000058 0.006361 0 0 0 0 0 0
$definebone "Bip01_L_Calf" "Bip01_LThighTwist1" 9.348623 -0.000031 -0.000002 0.000573 -4.967429 -0.136478 0 0 0 0 0 0
$definebone "Bip01_LCalfTwist1" "Bip01_L_Calf" 8.695895 -0.000058 -0.000006 0 0.000058 -0.143182 0 0 0 0 0 0
$definebone "Bip01_L_Foot" "Bip01_LCalfTwist1" 8.695902 -0.000064 -0.000007 0.617992 3.415745 -0.082334 0 0 0 0 0 0
$definebone "Bip01_L_Toe0" "Bip01_L_Foot" 2.4181 5.975538 -0.002442 0.023434 89.999751 0 0 0 0 0 0 0
$definebone "Bip01_R_Thigh" "Bip01_Spine" -3.634388 -0.963858 -3.905168 -0.372855 173.815257 -170.588429 0 0 0 0 0 0
$definebone "Bip01_RThighTwist1" "Bip01_R_Thigh" 9.348619 0.000028 0 0 0 -0.006647 0 0 0 0 0 0
$definebone "Bip01_R_Calf" "Bip01_RThighTwist1" 9.348619 0.000024 -0.000001 -0.000573 -4.967659 0.136249 0 0 0 0 0 0
$definebone "Bip01_RCalfTwist1" "Bip01_R_Calf" 8.695895 0.000035 -0.000003 0 0.000057 0.142895 0 0 0 0 0 0
$definebone "Bip01_R_Foot" "Bip01_RCalfTwist1" 8.695901 0.000024 0 -0.617992 3.415745 -1.205045 0 0 0 0 0 0
$definebone "Bip01_R_Toe0" "Bip01_R_Foot" 2.418039 5.974 0.13673 -1.311157 90.000386 0 0 0 0 0 0 0

$jigglebone "HairBone_224"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_223"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_220"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_219"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_218"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_217"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_216"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_215"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_214"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_212"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_211"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_209"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_208"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_206"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_205"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_202"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_198"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_197"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_196"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_195"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_117"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_114"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_113"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_78"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_77"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_74"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_73"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_38"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_37"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_34"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_33"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_14"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_13"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_12"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_11"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_10"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_09"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_08"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_07"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_06"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_05"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_02"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "HairBone_01"
{
	is_flexible
	{
		length 190
		tip_mass 15
		pitch_stiffness 500
		pitch_damping 2
		yaw_stiffness 500
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 5
	}
}
$jigglebone "Breast_Leftb"
{
	is_flexible
	{
		length 10
		tip_mass 15
		pitch_stiffness 200
		pitch_damping 2
		yaw_stiffness 200
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 10
	}
}
$jigglebone "Breast_Right"
{
	is_flexible
	{
		length 10
		tip_mass 15
		pitch_stiffness 200
		pitch_damping 2
		yaw_stiffness 200
		yaw_damping 2
		along_stiffness 100
		along_damping 0
		angle_constraint 10
	}
}

$sequence "ragdoll" {
	"poison_ivy_anims\ragdoll.smd"
	activity "ACT_DIERAGDOLL" 1
	fadein 0.2
	fadeout 0.2
	fps 30
}

$collisionjoints "poison_ivy_physics.smd"
{
	$mass 60
	$inertia 10
	$damping 0.01
	$rotdamping 1.5
	$rootbone "hips2"
	$concave
	$maxconvexpieces 1


	$jointconstrain "Bip01_L_Thigh" x limit -10 10 0
	$jointconstrain "Bip01_L_Thigh" y limit -3 93 0
	$jointconstrain "Bip01_L_Thigh" z limit -66 66 0

	$jointconstrain "Bip01_L_Calf" x limit -12 12 0
	$jointconstrain "Bip01_L_Calf" y limit -3 3 0
	$jointconstrain "Bip01_L_Calf" z limit -135 3 0

	$jointconstrain "Bip01_R_Thigh" x limit -10 10 0
	$jointconstrain "Bip01_R_Thigh" y limit -93 3 0
	$jointconstrain "Bip01_R_Thigh" z limit -66 66 0

	$jointconstrain "Bip01_R_Calf" x limit -12 12 0
	$jointconstrain "Bip01_R_Calf" y limit -3 3 0
	$jointconstrain "Bip01_R_Calf" z limit -135 3 0

	$jointconstrain "Bip01_R_Foot" x limit -50 50 0
	$jointconstrain "Bip01_R_Foot" y limit -37 37 0
	$jointconstrain "Bip01_R_Foot" z limit -39 10 0

	$jointconstrain "Bip01_Spine" x limit -32 32 0
	$jointconstrain "Bip01_Spine" y limit -19 19 0
	$jointconstrain "Bip01_Spine" z limit -41 61 0

	$jointconstrain "Bip01_Spine2" x limit -35 35 0
	$jointconstrain "Bip01_Spine2" y limit -23 23 0
	$jointconstrain "Bip01_Spine2" z limit -32 32 0

	$jointconstrain "Bip01_R_Clavicle" x limit -15 15 0
	$jointconstrain "Bip01_R_Clavicle" y limit -6 23 0
	$jointconstrain "Bip01_R_Clavicle" z limit -28 28 0

	$jointconstrain "Bip01_R_UpperArm" x limit -35 35 0
	$jointconstrain "Bip01_R_UpperArm" y limit -64 88 0
	$jointconstrain "Bip01_R_UpperArm" z limit -88 73 0

	$jointconstrain "Bip01_R_Forearm" x limit -48 48 0
	$jointconstrain "Bip01_R_Forearm" y limit -6 6 0
	$jointconstrain "Bip01_R_Forearm" z limit -129 23 0

	$jointconstrain "ValveBiped.Bip01_R_Hand" x limit -46 46 0
	$jointconstrain "ValveBiped.Bip01_R_Hand" y limit -37 37 0
	$jointconstrain "ValveBiped.Bip01_R_Hand" z limit -59 59 0

	$jointconstrain "Bip01_L_Clavicle" x limit -15 15 0
	$jointconstrain "Bip01_L_Clavicle" y limit -23 6 0
	$jointconstrain "Bip01_L_Clavicle" z limit -28 28 0

	$jointconstrain "Bip01_L_UpperArm" x limit -35 35 0
	$jointconstrain "Bip01_L_UpperArm" y limit -88 64 0
	$jointconstrain "Bip01_L_UpperArm" z limit -88 73 0

	$jointconstrain "Bip01_L_Forearm" x limit -48 48 0
	$jointconstrain "Bip01_L_Forearm" y limit -6 6 0
	$jointconstrain "Bip01_L_Forearm" z limit -129 23 0

	$jointconstrain "ValveBiped.Bip01_L_Hand" x limit -46 46 0
	$jointconstrain "ValveBiped.Bip01_L_Hand" y limit -37 37 0
	$jointconstrain "ValveBiped.Bip01_L_Hand" z limit -59 59 0

	$jointconstrain "Bip01_Head" x limit -50 50 0
	$jointconstrain "Bip01_Head" y limit -37 37 0
	$jointconstrain "Bip01_Head" z limit -35 35 0

	$jointconstrain "Breast_Right" x limit -23 23 0
	$jointconstrain "Breast_Right" y limit -12 12 0
	$jointconstrain "Breast_Right" z limit -19 19 0

	$jointconstrain "Breast_Leftb" x limit -23 23 0
	$jointconstrain "Breast_Leftb" y limit -12 12 0
	$jointconstrain "Breast_Leftb" z limit -19 19 0

	$jointconstrain "Bip01_L_Foot" x limit -50 50 0
	$jointconstrain "Bip01_L_Foot" y limit -37 37 0
	$jointconstrain "Bip01_L_Foot" z limit -39 10 0
}
