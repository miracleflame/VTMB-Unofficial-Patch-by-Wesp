print "loading leopold level script"

import __main__

from __main__ import G

Find = __main__.FindEntityByName

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#SOCIETY 4: This is one of the ugliest hacks i've ever written, added by dan_upright 09/12/04, changed by wesp
def WeDoAThingOfSomekind():
    if (G.Ash_Leave == 1 and G.Ash_Free == 0 and G.Patch_Plus == 1):
        __main__.FindPlayer().SetQuest("Ash", 3)
    print "this is radio rentals, open the pod bay doors hal"
    pc = __main__.FindPlayer()
    if (pc.clan == 5):
        taxi_landmark = Find("taxi_landmark")
        taxi_landmark.SetName("sewer_map_landmark")
        __main__.ChangeMap(2.5, "sewer_map_landmark", "escape_transition_nos")
        print "sailing to the sewers"
        return 0
    else:
        __main__.ChangeMap(2.5, "taxi_landmark", "escape_transition")
        print "sailing to the taxi"
        return 1

# HTN - 03/10/04
#SOCIETY 1: If squad1 was in combat, turn on npc_cameras for squad2
def trigShouldEnableCam():
    print "soc_exterior: checking alarm status..."

    if ( G.soc_alarm_on == 1 ):
        print "soc_exterior: alarm triggered from squad1! enabling npc_cam for squad2..."
        cam1 = Find( "guard2cam1" )
        cam1.ScriptUnhide()
        cam2 = Find( "guard2cam2" )
        cam2.ScriptUnhide()

#SOCIETY 1: Turns off boulder so it doesn't do damage while at rest
def TurnOffBoulder():
    boulder = Find("boulder")
    if boulder: boulder.SetCausesImpactDamage(0)

#SOCIETY 4: Store timer for use in sp_soc_3
def storeTimer():
    timer = Find("get_out")
    G.Society_Countdown = timer.remaining_time

#SOCIETY 3: Setup timer to continue from sp_soc_4
def setupEscapeTimer():
    timer = Find("escape_timer")
    timer.count_time = G.Society_Countdown
    timer.RestartTimer()
    timer.StartTimer()
    timer.Show()

#SOCIETY: Kill the player and end the game if player does not escape
def deathFromExplosion():
    endgame = Find("death_relay")
    endgame.Trigger()

#SOCIETY 3: Spawns Ash's cell key after guard dies, changed by wesp
def spawnAshKey():
    if(G.Ash_Leave == 1 and G.Patch_Plus == 0):
        guard = Find("guard_patrol_2")
        center = guard.GetCenter()
        point = (center[0], center[1], center[2] +5)
        key = __main__.CreateEntityNoSpawn("item_k_ash_cell_key", point, (0,0,0) )
        key.SetName("ash_key")
        sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
        sparklies.SetParent("ash_key")
        __main__.CallEntitySpawn(key)
        __main__.CallEntitySpawn(sparklies)

#SOCIETY 3: Saving Johansen
def SaveJohansen():
    __main__.FindPlayer().HumanityAdd(1)
    __main__.FindPlayer().SetQuest("Johansen", 3)
    #changed by dan_upright 30/11/04
    __main__.FindPlayer().AwardExperience("Society03")
    #changes end

#SOCIETY 4: Bach's speech
def BachDeathSpeak():
    bach = Find("bach_2")
    bach.PlayDialogFile("Character\dlg\MAIN CHARACTERS\BACH\line91_col_e.mp3")
    #changed by dan_upright 30/11/04
    __main__.FindPlayer().AwardExperience("Society01")
    #changes end

print "leopold levelscript loaded"