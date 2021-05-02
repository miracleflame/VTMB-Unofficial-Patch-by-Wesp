print "Loading Giovani Level Script..."

import __main__

from __main__ import G
from random import Random
from time import time

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#GIOVANNI MANSION 1: Set all to gone outside the house, changed by wesp
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
        print ( "************* Luca will stay ****************" )
        luca.ScriptHide()
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

#GIOVANNI MANSION 1: Opens Front Doors
def gio1_openFront():
    open = Find("Relay_Open_Front_Door")
    open.Trigger()

#GIOVANNI MANSION 1: Set all to react outside the house, changed by wesp
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
            partygoer.SetRelationship( "player D_FR 5" )

    luca = Find( "Luca" )
    if (luca):
        luca.SetRelationship( "player D_HT 5" )

    victor = Find( "Victor" )
    if (victor):
        victor.SetRelationship( "player D_HT 5" )

    maria = Find( "Maria" )
    if (maria):
        maria.SetRelationship( "player D_FR 5" )
        print "********** Set all outside to react **********"

#GIOVANNI MANSION 2: Set all to hate inside the house, changed by wesp
def gio2_aggroInside():
    G.GioBotchedInside = 1
 
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
    triggers = Finds("Trigger_Follow*")
    for trigger in triggers:
        if trigger: trigger.Kill()
        print "come on killed"

    print "********** Set all Inside to Hate **********"

    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Dirt")
    if (state == 1):
        pc.SetQuest("Dirt", 3)

#GIOVANNI MANSION: Nosferatu Check
def checkNosferatu():
    print "***************** Checking for NOS *****************"
    if( __main__.IsClan( __main__.FindPlayer(), "Nosferatu" ) ):
        print "********** Is NOS **********"
        gio1_aggroOutside()
        gio2_aggroInside()
    else:
        print "********** Not NOS **********"

#GIOVANNI MANSION 1: Set victor and maria to panic
def gio1_panicVictorMaria():
    victor = Find( "Victor" )
    if victor: victor.SetRelationship( "player D_HT 5" )

    mariaSeq = Find( "Sequence_Maria_Panic" )
    mariaSeq.BeginSequence()

#GIOVANNI MANSION 2: Set all guests inside house to flee and die, changed by wesp
def gio2_guestsFlee():

    sounds = Find("Sounds_Party")
    if sounds: sounds.Kill()

    speechs = Finds("Bruno_Speech")
    for speech in speechs:
        if speech: speech.Kill()

    guests = Finds("PartyGuest" )
    for guest in guests:
        if guest: guest.FleeAndDie()

    adam = Find( "Adam" )
    if adam: adam.FleeAndDie()

    chris = Find( "Christopher" )
    if chris: chris.FleeAndDie()

    mira = Find( "Mira" )
    if mira: mira.FleeAndDie()

    nadia = Find( "Nadia" )
    if nadia: nadia.FleeAndDie()
    triggers = Finds("Trigger_Follow*")
    for trigger in triggers:
        if trigger: trigger.Kill()
        print "come on killed"

    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Dirt")
    if (state == 1):
        pc.SetQuest("Dirt", 3)

#GIOVANNI MANSION 2: Starts Nadia leading the PC
def gio2_nadiaLead():
    lead = Find("Relay_FollowMe_1")
    lead.Trigger()

#GIOVANNI MANSION 2: Starts Nadia pissed at the PC and leaves, changed by wesp
def nadiaLeave():
    if (G.Nadia_Leave == 1):
        print ( "***************** leave *****************" )
        leave = Find("Relay_Nadia_Leaves")
        leave.Trigger()

#GIOVANNI MANSION 1: Fires on Giovanni1 Load, changed by wesp
def onGio1Load():
    print ( "***************** Running Gio1 Loading Script *****************" )
    G.GioGuard = 0
    if (G.GioBotchedInside == 1 or G.GioBotchedOutside == 1):
        ambient = Find ("Restaurant")
        if ambient: ambient.Kill()
        luca = Find("Luca")
        if (luca):
            luca.ScriptUnhide()
            luca.SetRelationship( "player D_HT 5" )
        guard5 = Find( "guard_5" )
        if (guard5):
            guard5.SetRelationship( "player D_HT 5" )
        victor = Find( "Victor" )
        if (victor): victor.Kill()
        maria = Find( "Maria" )
        if (maria): maria.Kill()
        partygoers = Finds( "partygoer" )
        for partygoer in partygoers:
            if partygoer: partygoer.Kill()
        limos = Finds( "limo" )
        for limo in limos:
            if limo: limo.Kill()
    print ( "***************** Reset Guard DLGs *****************" )
    if ( G.Story_State == 60 and G.Gio_Cutscene == 0):
        gio1_KillAllOutside()
        G.Gio_Cutscene = 1
        cutscene()
        print ( "***************** Playing Loading Movie *****************" )
        return
    checkNosferatu()
    if ( G.Gio_Cutscene == 1 ):
        truck = Find("truck1")
        truck.ScriptHide()
        transition = Find("trig_to_chambers")
        transition.ScriptHide()
    if ( G.BochedGio == 1 ):
        print ( "***************** Botched Setting Hostile *****************" )
        relay = Find( "Relay_Boched_Level" )
        relay.Trigger()
    else:
        return

#GIOVANNI MANSION 2: Fires on Giovanni2a Load, changed by wesp
def onGio2aLoad():
    G.BeenToGioParty = 1
    if G.Story_State >=60:
        gio2_guestsFlee()
        guests = Finds("PartyGuest" )
        for guest in guests:
            if guest: guest.Kill()
        chris = Find( "Christopher" )
        if chris: chris.Kill()
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Giovanni")
    if (state < 2):
        pc.SetQuest("Giovanni", 2)
        print ( "************* Infiltrated the Giovanni Mansion ****************" )
    if (G.Nadia_G3 == 1):
        Nadia = Find("Nadia")
        if Nadia: Nadia.Kill()
        float = Find("Choreo_FollowMe")
        if float: float.Kill()

#GIOVANNI MANSION 2: Fires on Giovanni2b Load
def onGio2bLoad():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Giovanni")
    if (state < 2):
        pc.SetQuest("Giovanni", 2)
        print ( "************* Infiltrated the Giovanni Mansion ****************" )
    if __main__.G.GioBotchedInside == 1:
        if __main__.G.Dodge_Book == 1:
            dodgebook2 = Find("dodge_book2")
            if dodgebook2: dodgebook2.Kill()
            dodgebook2sparklies = Find("dodge_book2_sparklies")
            if dodgebook2sparklies: dodgebook2sparklies.Kill()
        brunoeventsilent = Find("Bruno_Event_Silent")
        brunoeventsilent.Trigger()
        brunoevent = Find("Bruno_Event")
        if brunoevent: brunoevent.Kill()
    if __main__.G.Bruno_Killed == 1:
        bruno = Find("Bruno")
        if bruno: __main__.ScheduleTask(1.0, "__main__.FindEntityByName(\'Bruno\').Kill()")

#GIOVANNI MANSION 3: Checks to see if zombies are hostile when Nadia takes damage
def damCheck():
    if ( G.zombies_hate == 1):
        flee = Find("Relay_Nadia_Flees")
        flee.Trigger()

#GIOVANNI MANSION 3: Check if allzombies dead, set nadia
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

#GIOVANNI MANSION 3: Check if all zombies dead, set nadia, changed by wesp
def gio3_checkAllZombieDead():
    G.ZombiesDead = ( G.ZombiesDead + 1 )
    counter = 0
    zombies = Finds( "Zombie_Spawned" )
    for zombie in zombies:
        if ( zombie.IsAlive() ):
            counter = counter + 1
            G.Zombies = ( counter )
    if counter == 0 and G.Nadia_Fright == 1:
        relay = Find( "Relay_Zombies_Dead" )
        relay.Trigger()
    else:
        print( "******************** Still More Zombies to Kill ************************" )

#GIOVANNI MANSION 3: Check if nadia should run from zombies yet
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

#GIOVANNI MANSION 3: Progress Nadia to sequence 2b
def nadiaTo2b():
    relayTo2b = Find( "Relay_Nadia_to_2b" )
    relayTo2b.Trigger()

#GIOVANNI MANSION 3/4: Unhide begin nadia dialog, changed by wesp
def gio3_checkNadiaUnhide():
    if ( G.gio_2_nadia_pt == 1 and G.GioBotchedInside == 0 ):
        Nadia = Find( "Nadia" )
        Nadia.ScriptUnhide()
        G.Nadia_G3 = 1
    else:
        Nadia = Find( "Nadia" )
        if Nadia: Nadia.ScriptHide()
        choreo = Find("Relay_Cancel_Chereo")
        if choreo: choreo.Trigger()
        Relay = Find("Relay_Nadia_Flees")
        if Relay: Relay.Kill()
        Relay1 = Find("Relay_Nadia_Escapes")
        if Relay1: Relay1.Kill()
        float = Find("choreo_TooMuch")
        if float: float.ScriptHide()
        float = Find("choreo_Comon")
        if float: float.ScriptHide()
        float = Find("choreo_ThisWay")
        if float: float.ScriptHide()
        float = Find("choreo_InHere")
        if float: float.ScriptHide()
        float = Find("choreo_PointRight1")
        if float: float.ScriptHide()
        float = Find("Choreo_InFear")
        if float: float.ScriptHide()

#GIOVANNI MANSION 1: Set alarm state for g_1
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

#GIOVANNI MANSION 1: Entrance Check for chooseing to go to 2a or 2b, changed by wesp
def entranceFrontCheck():
    if ( G.GioBotchedOutside == 1 or G.GioBotchedInside == 1 ):
        __main__.ChangeMap(1, "frontload_landmark", "frontload_b")
        return
    else:
        __main__.ChangeMap(1, "frontload_landmark", "frontload_a")

def entranceBackCheck():
    if ( G.GioBotchedOutside == 1 or G.GioBotchedInside == 1 ):
        __main__.ChangeMap(1, "backload_landmark", "backload_b")
        return
    else:
        __main__.ChangeMap(1, "backload_landmark", "backload_a")

#GIOVANNI MANSION 1: Activate guard spawners
def gio1_activateSpawners():
    spawner = Find( "maker_guard_east" )
    spawner.Enable()
    spawner = Find( "maker_guard_west" )
    spawner.Enable()
    spawner = Find( "maker_guard_north" )
    spawner.Enable()

#GIOVANNI MANSION 1: Deactivate guard spawners
def gio1_deactivateSpawners():
    spawner = Find( "maker_guard_east" )
    spawner.Enable()
    spawner = Find( "maker_guard_west" )
    spawner.Enable()
    spawner = Find( "maker_guard_north" )
    spawner.Enable()

#GIOVANNI MANSION 1: Happens after killing Victor, changed by wesp
def spawnVictorInvite():
    victor = Find("Victor")
    center = victor.GetCenter()
    point = (center[0], center[1], center[2])
    invitev = __main__.CreateEntityNoSpawn("item_g_giovanni_invitation_victor", point, (0,0,0) )
    invitev.SetName("vic_inv")
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
    sparklies.SetParent("vic_inv")
    if G.Victor_Dominate == 0: 
        __main__.CallEntitySpawn(invitev)
        __main__.CallEntitySpawn(sparklies)

#GIOVANNI MANSION 1: Happens after killing Maria, changed by wesp
def spawnMariaInvite():
    if G.Maria_Dominate == 0:
        maria = Find("Maria")
        center = maria.GetCenter()
        point = (center[0], center[1], center[2])
        invitem = __main__.CreateEntityNoSpawn("item_g_giovanni_invitation_maria", point, (0,0,0) )
        invitem.SetName("mar_inv")
        sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
        sparklies.SetParent("mar_inv")
        __main__.CallEntitySpawn(invitem)
        __main__.CallEntitySpawn(sparklies)

#GIOVANNI MANSION 1: Happens after threatening Victor or Maria
def gio1_victorMariaFlee():
    victor = Find("Victor")
    if victor: victor.SetRelationship( "player D_HT 5" )

    maria = Find("Maria")
    if maria: maria.SetRelationship( "player D_HT 5" )

    flee = Find("Relay_VictorMariaFlee")
    flee.Trigger()

#GIOVANNI MANSION 3: Break door look at
def breakDoorLook():
    print ( "********* Triggered Break Look *************" )
    if ( G.ZombiesDead > 5 ):
        print ( "********* Breaking Door *************" )
        relay = Find( "Relay_break_door" )
        relay.Trigger()
    else:
        print ( "********* No Break *************" )

#GIOVANNI MANSION 4: Zombie kill counter, changed by wesp
def zombieKillCounter():
    G.ZombieKills = G.ZombieKills + 1
    if(G.ZombieKills >= 7):
        openroom = Find("Relay_UnLock_ZombRoom")
        openroom.Trigger()
        closeroom = Find("Relay_LockDown_ZombRoom")
        if closeroom: closeroom.Kill()

#GIOVANNI MANSION 5: Happens after chang brothers are killed, changed by wesp
def gio5_changDefeated():
    G.Story_State = 60
    G.Chunk_Open = 4
    G.gio_2_nadia_pt = 0
    G.GioBotchedInside = 1
    G.GioBotchedOutside = 1 
    trigger = Find("trig_from_4")
    trigger.ScriptUnhide()
    __main__.ChangeMap(3, "truckmark", "trig_shortcut")

#Fix way back from 3 to 2 if started combat on 2

#GIOVANNI MANSION 1: Check for loading sarcophagus into truck cutscene, changed by wesp
def cutscene():
    if G.Story_State == 60:
        pc = Find("playerevents")
        pc.RemoveDisciplinesNow()
        pc = __main__.FindPlayer()
        state = pc.GetQuestState("Dirt")
        if (state == 1):
            pc.SetQuest("Dirt", 3)
        if (pc.HasItem("item_g_giovanni_invitation_victor")):
            __main__.ScheduleTask(1.00, "__main__.FindPlayer().RemoveItem(\"item_g_giovanni_invitation_victor\")")
        if (pc.HasItem("item_g_giovanni_invitation_maria")):
            __main__.ScheduleTask(1.00, "__main__.FindPlayer().RemoveItem(\"item_g_giovanni_invitation_maria\")")
#      logic = Find("logic_scene")
#      logic.Trigger()
        __main__.ScheduleTask(1.0, "__main__.FindEntityByName(\'logic_scene\').Trigger()")
        world = Find("world")
        world.SetNoFrenzyArea(1)
        if G.Patch_Plus == 0: G.Giovanni_Open = 0

#GIOVANNI MANSION: Bodyguard init DLG, changed by wesp
def bodyguardChangeName(name):
    print "changing name from %s to guard_7" % name
    G.Guards_Name = name
    talkguard = Find(name)
    if talkguard: talkguard.SetName("guard_7")

def bodyguardRevertName():
    print "changing name to %s from guard_7" % G.Guards_Name
    talkguard = Find("guard_7")
    if talkguard: talkguard.SetName(G.Guards_Name)

def bodyguardRandResponce():
    R = Random( time() )
    G.GioGuard = R.randint (2, 4)
    bodyguardRevertName()

#GIOVANNI MANSION 5: Found Sarcophagus room 
def foundSarcophagusRoom():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Giovanni")
    if (state < 3):
        pc.SetQuest("Giovanni", 3)
        print ( "************* Found the Sarcophagus Room ****************" )

#GIOVANNI MANSION 5: Called on Chang deaths
def killedChangs():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Giovanni")
    if (state < 4):
        pc.SetQuest("Giovanni", 4)
        print ( "************* Killed the Changs ****************" )

#GIOVANNI MANSION 1: Float Line for Victor
def VictorFloatLeave():
    victor = Find("Victor")
    victor.PlayDialogFile("Character\dlg\Giovanni\Victor\line191_col_e.mp3")

#GIOVANNI MANSION 3: Pisha quest, changed by wesp
def foundGiovanniBook():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Occult")
    if state == 2:
        pc.SetQuest("Occult", 4)
        print ( "************* Found Book for Pisha ****************" )
    elif state == 1:
        pc.SetQuest("Occult", 3)
    else:
        print ( "************* Found Giovanni Book ****************" )

print "... Levelscript Loaded"
