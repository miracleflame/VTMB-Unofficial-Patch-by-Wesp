print "loading griffith park level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#OBSERVATORY 1
def playerEscape():
    pc = __main__.FindPlayer()
    pc.SetQuest( "Alliance", 4 )

#OBSERVATORY 1
def hackAreaChange():
    __main__.ChangeMap(3, "taxi_landmark", "taxi_trigger")

#OBSERVATORY 1
def jackEndDialog():
    G.Story_State = 90
    __main__.ScheduleTask(4.0, "__main__.ChangeMap(3, \"observahaven\", \"changelevel_observahaven\")")

#OBSERVATORY 1: This function alters the way the player can enter/leave the map based on clan
def removeSewerOrTaxi():
    if ( __main__.IsClan(__main__.FindPlayer(), "Nosferatu") ):
        relay = Find("relay_kill_cab")
        relay.Trigger()
    else:
        relay = Find("relay_kill_sewer")
        relay.Trigger()

#OBSERVATORY 2: This function activates the particles, so it can be done in dialog
def startFire():
    fire = Find("when_werewolves_attack_relay")
    fire.Trigger()

#OBSERVATORY 2: This function starts the cable car moving so Nines can curse at it leaving
def startCar():
    cablecar = Find("tram_hide_relay")
    cablecar.Trigger()

#OBSERVATORY 2: This allows Nines to float one line for localization purposes
def float691():
    Nines = Find("Nines")
    Nines.PlayDialogFile("Character/dlg/MAIN CHARACTERS/nines/line691_col_e.mp3")

print "griffith park levelscript loaded"
