print "loading ocean house level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindEnts = __main__.FindEntitiesByName

def ToggleSteam():
    if (G.GeneratorOn == 1):
        E = __main__.FindEntityByName( "SteamHurt" )
        E.Enable()
        E = __main__.FindEntityByName( "ValveSteam1" )
        E.TurnOn()
        E = __main__.FindEntityByName( "SoundSteam1" )
        E.PlaySound()
	E = __main__.FindEntityByName( "TriggerSteam1" )
	E.Kill()
	E = __main__.FindEntityByName( "SoundValveBreak1" )
	E.PlaySound()
 	E = __main__.FindEntityByName( "SteamValveConstraint1" )
	E.Break()

def TriggerLaundryEvent():
    if ( G.GeneratorOn and G.SprinklersOn ):
        E = __main__.FindEntityByName( "laundry_constraint_1" )
        E.Break()
        E = __main__.FindEntityByName( "laundry_constraint_2" )
        E.Break()
        E = __main__.FindEntityByName( "laundry_constraint_3" ) 
        E.Break()
        E = __main__.FindEntityByName( "falling_basement_light" )
        E.FadeToPattern("a")
        __main__.HW = __main__.FindEntityByName( "HurtWater" )
        __main__.ScheduleTask( 2, "HW.Enable()" )
        __main__.LS  = __main__.FindEntityByName( "laundry_ballsocket" )
	__main__.ScheduleTask( 1.8, "LS.Break()" )
 	E = Find("falling_basement_light_spark")
	E.SparkOnce()
	E = Find("laundry_tear_sound")
	E.PlaySound()
        E = Find("laundry_wire_sound")
	E.PlaySound()
 


def Trigger_Hellcat():
    if ( 1 ): ## TODO: Make this a local flag
        __main__.Shake_HC = Find("Shake_HC")
        __main__.ScheduleTask(2, "Shake_HC.Kill()")
        __main__.HC_ClipBox = Find("HC_ClipBox")
        __main__.ScheduleTask(2, "HC_ClipBox.Kill()")
        __main__.Thrust_HC = Find("Thrust_HC")
        __main__.ScheduleTask(2, "Thrust_HC.Activate()")
        E = Find("Sound_HC_EngineLoop")
        E.StopSound()
        E = Find("Sound_HC_Charge")
        E.PlaySound()


def Doors_Think():
    from random import Random
    from time import time
    R = Random( time() )
    EntList = FindEnts("haunt_impact")
    for E in EntList:
        Action = R.randint(1,4) # allow for a random chance of this door not being triggered
        if (Action != 2 ):   
            E.Impact()

                


print "levelscript loaded"
