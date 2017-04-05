$cd "."
$modelname "example/MalkLifeTube_trims.mdl"
$cdmaterials "models/scenery/structural/malkavian"
$surfaceprop "glass"
$model "Body" "MalkLifeTube_trims.smd"
{
}
$hboxset "default"
$sequence "idle" "MalkLifeTube_@idle" activity "" 1.0 fps 1.0
$collisionmodel	"MalkLifeTube_trims.smd"
{
	$mass "200.0"
}
