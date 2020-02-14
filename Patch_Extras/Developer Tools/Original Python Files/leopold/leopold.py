print "loading leopold level script"

import __main__

from __main__ import G 

Find = __main__.FindEntityByName

# HTN - 03/10/04
#soc_exterior: if squad1 was in combat, turn on npc_cameras for squad2
def trigShouldEnableCam():
	print "soc_exterior: checking alarm status..."

	if ( G.soc_alarm_on == 1 ):
		print "soc_exterior: alarm triggered from squad1! enabling npc_cam for squad2..."
		cam1 = Find( "guard2cam1" )
		cam1.ScriptUnhide()
		cam2 = Find( "guard2cam2" )
		cam2.ScriptUnhide()

#SOCIETY 1 : turns off boulder so it doesn't do damage while at rest
def TurnOffBoulder():
	boulder = Find("boulder")
	boulder.SetCausesImpactDamage(0)

#SOCIETY 4 : store timer for use in sp_soc_3
def storeTimer():
	timer = Find("get_out")
	G.Society_Countdown = timer.remaining_time

#SOCIETY 3 : setup timer to continue from sp_soc_4
def setupEscapeTimer():
	timer = Find("escape_timer")
	timer.count_time = G.Society_Countdown
	timer.RestartTimer()
	timer.StartTimer()
	timer.Show()

#SOCIETY : kill the player and end the game if player does not escape
def deathFromExplosion():
	endgame = Find("death_relay")
	endgame.Trigger()

#SOCIETY 3:  spawns Ash's cell key after guard dies.
def spawnAshKey():
    if(G.Ash_Leave == 1):
	    guard = Find("guard_patrol_2")
	    center = guard.GetCenter()
	    point = (center[0], center[1], center[2] +5)
	    key = __main__.CreateEntityNoSpawn("item_k_ash_cell_key", point, (0,0,0) )
	    key.SetName("ash_key")
	    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
	    sparklies.SetParent("ash_key")
	    __main__.CallEntitySpawn(key)
	    __main__.CallEntitySpawn(sparklies)

def SaveJohansen():
	__main__.FindPlayer().HumanityAdd(1)
	__main__.FindPlayer().SetQuest("Johansen", 3)

def BachDeathSpeak():
	bach = Find("bach_2")
	bach.PlayDialogFile("Character\dlg\MAIN CHARACTERS\BACH\line91_col_e.mp3")
	

print "leopold levelscript loaded"
