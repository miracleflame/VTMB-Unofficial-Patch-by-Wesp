print "loading griffith park level script"

import __main__


import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

def playerEscape():
    pc = __main__.FindPlayer()
    pc.SetQuest( "Alliance", 4 )

def hackAreaChange():
    __main__.ChangeMap(3, "taxi_landmark", "taxi_trigger")

def jackEndDialog():
    G.Story_State = 90
    __main__.ScheduleTask(4.0, "__main__.ChangeMap(3, \"observahaven\", \"changelevel_observahaven\")")

#SP_OBSERVATORY_1 : This function alters the way the player can enter/leave the map based on clan
def removeSewerOrTaxi() :
    if ( __main__.IsClan(__main__.FindPlayer(), "Nosferatu") ):
        relay = Find("relay_kill_cab")
        relay.Trigger() 
    else:
        relay = Find("relay_kill_sewer")
        relay.Trigger()
        

#SP_OBSERVATORY_2 : This function activates the particles, so it can be done in dialog
def startFire() :
    fire = Find("when_werewolves_attack_relay")
    fire.Trigger()

#SP_OBSERVATORY_2 : This function starts the cable car moving so Nines can curse at it leaving
def startCar() :
    cablecar = Find("tram_hide_relay")
    cablecar.Trigger()

#SP_OBSERVATORY_2 : This allows Nines to float one line for localization purposes
def float691():
    Nines = Find("Nines")
    Nines.PlayDialogFile("Character/dlg/MAIN CHARACTERS/nines/line691_col_e.mp3")

    
print "griffith park levelscript loaded"
