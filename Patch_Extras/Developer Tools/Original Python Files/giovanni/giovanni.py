print "Loading Giovani Level Script..."

import __main__

from __main__ import G 
from random import Random
from time import time

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

#sp_giovanni_1: set all to gone outside the house
def gio1_KillAllOutside():
	print ( "***************** Starting to Remove NPCs ******************" )
	spawner = Find( "maker_guard_north" )
	if (spawner):
		print ( "************* Killed Spawner North ****************" )
		spawner.Kill()
	else:
		print ( "************* Couldnt Find Spawner North ****************" )

	spawner = Find( "maker_guard_east" )
	if (spawner):
		print ( "************* Killed Spawner East ****************" )
		spawner.Kill()
	else:
		print ( "************* Couldnt Find Spawner East ****************" )

	spawner = Find( "maker_guard_west" )
	if (spawner):
		print ( "************* Killed Spawner West ****************" )
		spawner.Kill()
	else:
		print ( "************* Couldnt Find Spawner West ****************" )

	guard4 = Find( "guard_patrol4" )
	if (guard4):
		print ( "************* Killed Guard 4 ****************" )
		guard4.Kill()
	else:
		print ( "************* Couldnt Find Guard 4 ****************" )

	guards = Finds( "guard_spawned" )
	for guard in guards:
		if (guard):
			print ( "************* Killed Guard guard_spawned ****************" )
			guard.Kill()
		else:
			print ( "************* Couldnt Find Guard Spawned ****************" )

	guard6 = Find( "guard_patrol6" )
	if (guard6):
		print ( "************* Killed Guard 6 ****************" )
		guard6.Kill()
	else:
		print ( "************* Couldnt Find Guard 6 ****************" )

	guard5 = Find( "guard_patrol5" )
	if (guard5):
		guard5.Kill()
		print ( "************* Killed Guard P5 ****************" )
	else:
		print ( "************* Couldnt Find Guard P5 ****************" )

	guard5_b = Find( "guard_patrol5_backyard" )
	if (guard5_b):
		print ( "************* Killed Guard P5_B ****************" )
		guard5_b.Kill()
	else:
		print ( "************* Couldnt Find Guard P5_B ****************" )

	guard3 = Find( "guard_patrol3" )
	if (guard3):
		print ( "************* Killed Guard P3 ****************" )
		guard3.Kill()
	else:
		print ( "************* Couldnt Find Guard P3 ****************" )

	guards = Finds( "guard" )
	for guard in guards:
		if (guard):
			print ( "************* Killed Guard ****************" )
			guard.Kill()
		else:
			print ( "************* Couldnt Find Guard ****************" )

	partygoers = Finds( "partygoer" )
	for partygoer in partygoers:
		if partygoer:
			print ( "************* Killed Partygoer ****************" )
			partygoer.Kill()
		else:
			print ( "************* Couldnt Find Partygoer ****************" )

	luca = Find( "Luca" )
	if (luca):
		print ( "************* Killed Luca 4 ****************" )
		luca.Kill()
	else:
		print ( "************* Couldnt Find Luca****************" )

	victor = Find( "Victor" )
	if (victor):
		print ( "************* Killed Victor ****************" )
		victor.Kill()
	else:
		print ( "************* Couldnt Find Victor ****************" )

	maria = Find( "Maria" )
	if (maria):
		maria.Kill()
		print ( "************* Killed Maria ****************" )
	else:
		print ( "************* Couldnt Find Maria ****************" )
	print ( "******************* Done Removing NPCs *****************" )

#sp_giovanni_1: check for loading sarcophagus into truck cutscene
def cutscene():
	print ( "******************** Starting Cut Scene ********************" )
	logic = Find("logic_scene")
	logic.Trigger()
	world = Find("world")
	world.SetNoFrenzyArea(1)
	G.Giovanni_Open = 0

#Opens Front Doors
def gio1_openFront():
	open = Find("Relay_Open_Front_Door")
	open.Trigger()
	
#sp_giovanni_1: set all to hate outside the house
def gio1_aggroOutside():
	G.GioBotchedOutside = 1
	guard4 = Find( "guard_patrol4" )
	if (guard4):
		guard4.SetRelationship( "player D_HT 5" )

	guard6 = Find( "guard_patrol6" )
	if (guard6):
		guard6.SetRelationship( "player D_HT 5" )

	guard5 = Find( "guard_patrol5" )
	if (guard5):
		guard5.SetRelationship( "player D_HT 5" )

	guard5_b = Find( "guard_patrol5_backyard" )
	if (guard5):
		guard5.SetRelationship( "player D_HT 5" )

	guard3 = Find( "guard_patrol3" )
	if (guard3):
		guard3.SetRelationship( "player D_HT 5" )

	guards = Finds( "guard" )
	for guard in guards:
		if (guard):
			guard.SetRelationship( "player D_HT 5" )

	partygoers = Finds( "partygoer" )
	for partygoer in partygoers:
		if partygoer:
			partygoer.SetRelationship( "player D_HT 5" )

	luca = Find( "Luca" )
	if (luca):
		luca.SetRelationship( "player D_HT 5" )

	victor = Find( "Victor" )
	if (victor):
		victor.SetRelationship( "player D_HT 5" )

	maria = Find( "Maria" )
	if (maria):
		maria.SetRelationship( "player D_HT 5" )
		print "********** Set all Outside to Hate **********"

#sp_giovanni_2: set all to hate inside the house
def gio2_aggroInside():
	adam = Find( "Adam" )
	if (adam):
		adam.SetRelationship( "player D_HT 5" )

	guests = Finds( "Guest" )
	for guest in guests:
		if ( guest ):
			guest.SetRelationship( "player D_HT 5" )

	guard1 = Find( "guard_1" )
	if (guard1):
		guard1.SetRelationship( "player D_HT 5" )

	guard2 = Find( "guard_2" )
	if (guard2):
		guard2.SetRelationship( "player D_HT 5" )

	guard3 = Find( "guard_3" )
	if (guard3):
		guard3.SetRelationship( "player D_HT 5" )

	guard4 = Find( "guard_4" )
	if (guard4):
		guard4.SetRelationship( "player D_HT 5" )

	guard5 = Find( "guard_5" )
	if (guard5):
		guard5.SetRelationship( "player D_HT 5" )

	guard6 = Find( "guard_6" )
	if (guard6):
		guard6.SetRelationship( "player D_HT 5" )

	guard7 = Find( "guard_7" )
	if (guard7):
		guard7.SetRelationship( "player D_HT 5" )

	chris = Find( "Christopher" )
	if (chris):
		chris.SetRelationship( "player D_HT 5" )

	mira = Find( "Mira" )
	if (mira):
		mira.SetRelationship( "player D_HT 5" )

	nadia = Find( "Nadia" )
	if (nadia):
		nadia.SetRelationship( "player D_HT 5" )
		print "********** Set all Inside to Hate **********"

#Nosferatu Check
def checkNosferatu():
	print "***************** Checking for NOS *****************"
	if( __main__.IsClan( __main__.FindPlayer(), "Nosferatu" ) ):
		print "********** Is NOS **********"
		gio1_aggroOutside()
		gio2_aggroInside()
	else:
		print "********** Not NOS **********"

#sp_giovanni_1: set victor and maria to panic
def gio1_panicVictorMaria():
	victor = Find( "Victor" )
	victor.SetRelationship( "player D_HT 5" )

	mariaSeq = Find( "Sequence_Maria_Panic" )
	mariaSeq.BeginSequence()

#sp_giovanni_2: set all guests inside house to flee and die
def gio2_guestsFlee():
	guest = Find( "Guest" )
	for guest in guests:
		if guest:
			guest.FleeAndDie()

	adam = Find( "Adam" )
	adam.FleeAndDie()

	chris = Find( "Christopher" )
	chris.FleeAndDie()

	mira = Find( "Mira" )
	mira.FleeAndDie()

	nadia = Find( "Nadia" )
	nadia.FleeAndDie()

#Starts Nadia leading the PC
def gio2_nadiaLead():
	lead = Find("Relay_FollowMe_1")
	lead.Trigger()

#Starts Nadia pissed at the PC and leaves
def nadiaLeave():
	leave = Find("Relay_Nadia_Leaves")
	leave.Trigger()

#Fires on Giovanni2a Load
def onGio1Load():
	print ( "***************** Running Gio1 Loading Script *****************" )
	G.GioGuard = 0
	print ( "***************** Reset Guard DLGs *****************" ) 
	if ( G.Story_State == 65 ):
		gio1_KillAllOutside()
		cutscene()
		print ( "***************** Playing Loading Movie *****************" )
		return
	checkNosferatu()
	if ( G.BochedGio == 1 ):
		print ( "***************** Botched Setting Hostile *****************" )
		relay = Find( "Relay_Boched_Level" )
		relay.Trigger()
	else:
		return
	
#Fires on Giovanni2a Load
def onGio2aLoad():
	G.BeenToGioParty = 1
	pc = __main__.FindPlayer()
	state = pc.GetQuestState("Giovanni")
	if (state < 2):
		pc.SetQuest("Giovanni", 2)
		print ( "************* Infiltrated the Giovanni Mansion ****************" )

def onGio2bLoad():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Giovanni")
    if (state < 2):
	    pc.SetQuest("Giovanni", 2)
	    print ( "************* Infiltrated the Giovanni Mansion ****************" )
	
#Checks to see if zombies are hostile when Nadia takes damage
def damCheck():
	if ( G.zombies_hate == 1):
		flee = Find("Relay_Nadia_Flees")
		flee.Trigger()

#sp_giovanni_3: check if allzombies dead, set nadia
def gio3_checkAllZombieDeadAndZone():
	counter = 0
	if ( G.gio_2_nadia_pt == 1 ):
		zombies = Finds( "Zombie_Spawned" )
		for zombie in zombies:
			if ( zombie.IsAlive() ):
				counter = counter + 1

		if counter > 0:
			print "sp_giovanni_3: zoning without nadia! kill her!"
			G.gio_3_startzombies = 0
			G.gio_2_nadia_pt = 0
			Nadia = Find( "Nadia" )
			if Nadia:
				Nadia.Kill()

#sp_giovanni_3: check if all zombies dead, set nadia
def gio3_checkAllZombieDead():
	G.ZombiesDead = ( G.ZombiesDead + 1 )
	counter = 0
	zombies = Finds( "Zombie_Spawned" )
	for zombie in zombies:
		if ( zombie.IsAlive() ):
			counter = counter + 1
			G.Zombies = ( counter )
	if counter == 0:
		relay = Find( "Relay_Zombies_Dead" )
		relay.Trigger()
	else:
		print( "******************** Still More Zombies to Kill ************************" )

#sp_giovanni_3: check if nadia should run from zombies yet
def gio3_checkNadiaRunZombie():
	if ( G.gio_3_startzombies == 1 ):
		print "sp_giovanni_3: zombie attack!"
		seq = Find( "seq_nadia2" )
		if seq:
			seq.BeginSequence()
		zombies = Finds( "zombie_1" )
		for zombie in zombies:
			if zombie:
				zombie.ScriptUnhide()

#Giovanni 3 Progress Nadia to sequence 2b
def nadiaTo2b():
	relayTo2b = Find( "Relay_Nadia_to_2b" )
	relayTo2b.Trigger()

#sp_giovanni_3: unhide begin nadia dialog
def gio3_checkNadiaUnhide():
	if ( G.gio_2_nadia_pt == 1 ):
		Nadia = Find( "Nadia" )
		Nadia.ScriptUnhide()

#sp_giovanni_1: set alarm state for g_1
def gio1_setAlarm():
	if ( G.gio_1_alarm == 0 ):
		print "sp_giovanni_1: alarm is set! spawner triggers enabled!"
		G.gio_1_alarm = 1

		#unhide spawner triggers
		triggers = Finds( "trig_spawners" )
		for trigger in triggers:
			if trigger:
				trigger.ScriptUnhide()

		#turn on spawners
		gio1_activateSpawners()

#Entrance Check for chooseing to go to 2a or 2b
def entranceFrontCheck():
	if ( G.BeenToGioParty == 1 ):
		__main__.ChangeMap(1, "frontload_landmark", "frontload_a")
		return
	if ( G.GioBotchedOutside == 1 ):
		__main__.ChangeMap(1, "frontload_landmark", "frontload_b")
		return
	else:
		__main__.ChangeMap(1, "frontload_landmark", "frontload_a")

def entranceBackCheck():
	if ( G.BeenToGioParty == 1 ):
		__main__.ChangeMap(1, "backload_landmark", "backload_a")
		return
	if ( G.GioBotchedOutside == 1 ):
		__main__.ChangeMap(1, "backload_landmark", "backload_b")
		return
	else:
		__main__.ChangeMap(1, "backload_landmark", "backload_a")
		
	
#sp_giovanni_1: activate guard spawners
def gio1_activateSpawners():
	spawner = Find( "maker_guard_east" )
	spawner.Enable()
	spawner = Find( "maker_guard_west" )
	spawner.Enable()
	spawner = Find( "maker_guard_north" )
	spawner.Enable()

#sp_giovanni_1: deactivate guard spawners
def gio1_deactivateSpawners():
	spawner = Find( "maker_guard_east" )
	spawner.Enable()
	spawner = Find( "maker_guard_west" )
	spawner.Enable()
	spawner = Find( "maker_guard_north" )
	spawner.Enable()

#sp_giovanni_1: happens after killing Victor
def spawnVictorInvite():
    victor = Find("Victor")
    center = victor.GetCenter()
    point = (center[0], center[1], center[2])
    invitev = __main__.CreateEntityNoSpawn("item_g_giovanni_invitation_victor", point, (0,0,0) )
    invitev.SetName("vic_inv")
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
    sparklies.SetParent("vic_inv")
    __main__.CallEntitySpawn(invitev)
    __main__.CallEntitySpawn(sparklies)

#sp_giovanni_1: happens after killing Maria
def spawnMariaInvite():
    maria = Find("Maria")
    center = maria.GetCenter()
    point = (center[0], center[1], center[2])
    invitem = __main__.CreateEntityNoSpawn("item_g_giovanni_invitation_maria", point, (0,0,0) )
    invitem.SetName("mar_inv")
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
    sparklies.SetParent("mar_inv")
    __main__.CallEntitySpawn(invitem)
    __main__.CallEntitySpawn(sparklies)
    
#sp_giovanni_1: happens after thretening Victor of Maria
def gio1_victorMariaFlee():
	victor = Find("Victor")
	victor.SetRelationship( "player D_HT 5" )
	
	maria = Find("Maria")
	maria.SetRelationship( "player D_HT 5" )
	
	flee = Find("Relay_VictorMariaFlee")
	flee.Trigger()

#Level3 break door look at
def breakDoorLook():
	print ( "********* Triggered Break Look *************" )
	if ( G.ZombiesDead > 5 ):
		print ( "********* Breaking Door *************" )
		relay = Find( "Relay_break_door" )
		relay.Trigger()
	else:
		print ( "********* No Break *************" )


#Level4 Zombie kill counter
def zombieKillCounter():
	G.ZombieKills = G.ZombieKills + 1
	if(G.ZombieKills == 7):
		openroom = Find("Relay_UnLock_ZombRoom")
		openroom.Trigger()


#sp_giovanni_5: happens after chang brothers are killed
def gio5_changDefeated():
	G.Story_State = 65
	__main__.ChangeMap(3, "truckmark", "trig_shortcut")

#Fix way back from 3 to 2 if started combat on 2

#sp_giovanni_1: check for loading sarcophagus into truck cutscene
def cutscene():
	if G.Story_State == 65:
		pc = Find("playerevents")
		pc.RemoveDisciplinesNow()
##		logic = Find("logic_scene")
##		logic.Trigger()
		__main__.ScheduleTask(1.0, "__main__.FindEntityByName(\'logic_scene\').Trigger()")
		world = Find("world")
		world.SetNoFrenzyArea(1)
		G.Giovanni_Open = 0

#Bodyguard init DLG
def bodyguardChangeName(name):
	print "changing name from %s to guard_7" % name
	G.Guards_Name = name
	talkguard = Find(name)
	talkguard.SetName("guard_7")

def bodyguardRevertName():
	print "changing name to %s from guard_7" % G.Guards_Name   
	talkguard = Find("guard_7")
	talkguard.SetName(G.Guards_Name)    

def bodyguardRandResponce():
	R = Random( time() )
	G.GioGuard = R.randint (2, 4)

def foundSarcophagusRoom():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Giovanni")
    if (state < 3):
	    pc.SetQuest("Giovanni", 3)
	    print ( "************* Found the Sarcophagus Room ****************" )

def killedChangs():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Giovanni")
    if (state < 4):
	    pc.SetQuest("Giovanni", 4)
	    print ( "************* Killed the Changs ****************" )

#SP_GIOVANNI_1 : Float Line for Victor
def VictorFloatLeave():
	victor = Find("Victor")
	victor.PlayDialogFile("Character\dlg\Giovanni\Victor\line191_col_e.mp3")

def foundGiovanniBook():
	pc = __main__.FindPlayer()
	state = pc.GetQuestState("Occult")
	if ( ( state > 0 ) and ( state < 3 ) ):
		pc.SetQuest("Occult", 3)
		print ( "************* Found Book for Pisha ****************" )
	else:
		print ( "************* Found Giovanni Book ****************" )

	

		
	
print "... Levelscript Loaded"
