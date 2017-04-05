print "loading ventrue level script"

import __main__
import random
random.seed()

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass





#PRINCE'S CHAMBERS:  Checks story state and unhides correct events.
def setupChamber():
    actCoffin = Find("coffin_state")
    ventPrim = Find("ventrue_unhide")
    torryPrim = Find("toreador_unhide")
    princeStart = Find("prince1")
    princeEnd = Find("prince2")

    if(princeStart):
        princeStart.SetDefaultDialogCamera("DialogDefault")
    
    # check for specific Story State events
    if(G.Story_State == 10):
        princeStart.SetDefaultDialogCamera("Dynamic3")
    elif (G.Story_State == 15):
        if (__main__.IsClan(__main__.FindPlayer(), "Ventrue")):
            torryPrim.Trigger()
        else:
            ventPrim.Trigger()
    elif (G.Story_State == 65):
        actCoffin.Trigger()

    # check to make sure the correct Prince is active
    if (G.Story_State < 30):
        princeStart.ScriptUnhide()
        princeEnd.ScriptHide()
    elif (G.Story_State == 30):
        princeEnd.ScriptUnhide()
        if(princeStart):
            princeStart.Kill()
        window = Find("prince_window")
        window.BeginSequence()
    elif (G.Story_State > 30):
        princeEnd.ScriptUnhide()
        if(princeStart):
            princeStart.Kill()

    # check to see if Beckett should be gone from Venture Tower
    if(G.Story_State >= 80):
        beckett = Find("beckett")
        if(beckett):
            beckett.Kill()


    if(G.Story_State == 110):
        relay = Find("exits_lock_relay")
        relay.Trigger()


#PRINCE'S CHAMBERS: turn prince around on Prince2, line 21
def turnPrinceAround():
    turn = Find("turn_around")
    turn.BeginSequence()
        
#PRINCE'S CHAMBERS:  pick which prince dialogue should be active
def pickAPrince():
    princeStart = Find("prince1")
    princeStartTrig = Find("prince1_trigger")
    princeEnd = Find("prince2")
    princeEndTrig = Find("prince2_trigger")
    if (G.Story_State < 30):
        princeStart.ScriptUnhide()
        princeEnd.ScriptHide()
    elif (G.Story_State >= 30):
        princeEnd.ScriptUnhide()
        princeStart.ScriptHide()

#PRINCE'S CHAMBERS:  fade out on map change
def changeVent():
    nosPort = Find("nos_teleport")
    othersPort = Find("others_teleport")
    if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
        nosPort.Trigger()
    else:
        othersPort.Trigger()

#PRINCE'S CHAMBERS:  choose which quest to send the player on
def princeQuests():
    wereWolf = Find("teen_wolf_trigger")
    if (G.Prince_Refuse == 1):
        G.Prince_Refuse = 0
        Find("lock_nos_out").Test()
        escort = Find("sheriff_escort")
        escort.BeginSequence()
        changeVent()
    elif (G.Wolf_Ending == 1):
        wereWolf.Trigger()
        print "YOU DANCING FOOL!!!"
    elif (G.Story_State == 65):
        relay = Find("move_to_sarcophagus")
        relay.Trigger()
    elif (G.Prince_Givekey == 1):
        Find("Start_Give_Prince_Key").Trigger()
    elif (G.Prince_Keepkey == 1):
        Find("Start_PC_Open_Sarc").Trigger()
    elif (G.Prince_Decision == 1):
        Find("Start_Prince_Beatdown").Trigger()
    elif(G.Prince_Regent == 1):
        Find("Start_Prince_Beatdown").Trigger()
    if(G.Prince_Ending):
        relay = Find("exits_unlock_relay")
        relay.Trigger()

#PRINCE'S CHAMBERS:  sends you to society after talking to Beckett.
def beckettQuest():
    if (G.Society_Open == 1):
        changeVent()
        #__main__.ChangeMap(1.5, "society_mark", "society_change")

#PRINCE'S CHAMBERS: Chooses models to use for Camarilla Part1 Ending
def chooseCamarilla():
    if(__main__.IsClan(__main__.FindPlayer(), "Toreador")):
        change = Find("Regent_Guard_1")
        change.SetModel("models/character/pc/male/nosferatu/armor0/Nosferatu.mdl")
    elif(__main__.IsClan(__main__.FindPlayer(), "Tremere")):
        change = Find("Regent_Guard_2")
        change.SetModel("models/character/pc/male/nosferatu/armor0/Nosferatu.mdl")
    elif(__main__.IsClan(__main__.FindPlayer(), "Gangrel")):
        change = Find("Regent_Guard_3")
        change.SetModel("models/character/pc/male/nosferatu/armor0/Nosferatu.mdl")

#PRINCE'S CHAMBERS: Selects the correct ending to transition to from Give Prince Key ending
def checkEnding():
    if(G.Story_State == 125):
        Find("lonewolf_change").ScriptUnhide()
    else:
        Find("epilogue_change").ScriptUnhide()

#VENTRUETOWER:  Called after talking to Chunk, opening the elevator to the Prince.
def chunkResults():
    chunkRelay   = Find("chunkRelay")
    cower = Find("chunk_cowers_run_1")
    chunk = Find("Chunk2")
    attack = Find("chunk_attacks_run_1")
    killSafeArea = Find("setcombat")
    if(G.Chunk_Run == 1):
        cower.BeginSequence()
        killSafeArea.Trigger()
        chunk.SetRelationship("player D_FR 5")
        Find("base_elev_down_a").Unlock()
    elif(G.Chunk_Attack == 1):
        attack.BeginSequence()
        killSafeArea.Trigger()
        chunk.SetRelationship("player D_HT 5")
        Find("base_elev_down_a").Unlock()
    elif(G.Chunk_Open > 0):
        chunkRelay.Trigger()

#VENTRUETOWER: Called when the player leaves the level
def leaveVentrue():
    if(G.Story_State == 110):
        __main__.ChangeMap(2.5, "caine_landmark", "VentrueTower_caine")
    else:
        __main__.ChangeMap(2.5, "VentrueTower_mark", "VentrueTower_hub")        

#VENTRUETOWER: Called when the player leaves the level
def leaveVentrueNos():
    if(G.Story_State == 110):
        __main__.ChangeMap(2.5, "caine_nos_landmark", "VentrueTower_caine")
    else:
        __main__.ChangeMap(2.5, "ventrue_nosferatu_entrance", "ventrue_sewers") 

#VENTRUETOWER: Called to switch which camera is active in the Ventrue security room
def ventrueCameraSwitch():
    G.Ventrue_Camera = G.Ventrue_Camera + 1
    if(G.Ventrue_Camera > 5):
        G.Skyline_Camera = 1
    monitor = Find("monitor_2")
    monitor.SetCamera("camera_%i" % (G.Ventrue_Camera))

#VENTRUETOWER:  Called to change to combat for Nosferatu.
def ventrueCombat():
    combatTrigger = Find("combat_change")
    if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
        if (G.Story_State == 100 or G.Story_State >= 115):
            combatTrigger.Trigger()
            print "Combat Switched"
            __main__.ScheduleTask(1.0, "Find(\"Chunk2\").ScriptUnhide()")

#VENTRUETOWER:  Disables the elevator when the player is not allowed up.
def elevatorStop():
    eleButtons = Find("base_elev_down")
    baseButtons = Find("base_btn_up")
    if (G.Story_State >= 35 and G.Story_State <= 64):
        eleButtons.Lock()
        baseButtons.Lock()

#VENTRUETOWER:  Spawns the bomb after the bomb guy dies
def spawnBomb():
    bombGuy = Find("bomberman")
    center = bombGuy.GetCenter()
    point = (center[0] + 25, center[1] + 25, center[2])
    bomb = __main__.CreateEntityNoSpawn("item_g_astrolite", point, (0,0,0) )
    bomb.SetName("astrolite_bomb")
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
    sparklies.SetParent("astrolite_bomb")
    __main__.CallEntitySpawn(bomb)
    __main__.CallEntitySpawn(sparklies)
    

#VENTRUETOWER:  Despawns the bomb after placed
def despawnBomb():    
    bomb = FindClass("item_g_astrolite")    
    center = bomb[0].GetOrigin()    
    angles = bomb[0].GetAngles()    
    bomb[0].Kill()    
    bombProp = Find("bomb_prop")    
    bombProp.SetOrigin(center)    
    bombProp.SetAngles(angles)    
    bombProp.ScriptUnhide()

#SP_ENDSEQUENCES_B: Sets up players to avoid PC clan models
def setupCamarillaPart2():
    dude1 = Find("Gangrel_Pusher")
    dude2 = Find("Brujah_Pusher")
    dude3 = Find("Toreador_Pusher")
    dude4 = Find("Malkavian_Pusher")
    if (__main__.IsClan(__main__.FindPlayer(), "Gangrel")) :
        dude4.SetName("Regent2")
        dude4.ScriptUnhide()
        dude2.SetName("pusher1")
        dude2.ScriptUnhide()
        dude3.SetName("pusher2")
        dude3.ScriptUnhide()
    elif (__main__.IsClan(__main__.FindPlayer(), "Brujah")) :
        dude1.SetName("Regent2")
        dude1.ScriptUnhide()
        dude3.SetName("pusher1")
        dude3.ScriptUnhide()
        dude4.SetName("pusher2")
        dude4.ScriptUnhide()
    elif (__main__.IsClan(__main__.FindPlayer(), "Toreador")) :
        dude2.SetName("Regent2")
        dude2.ScriptUnhide()
        dude1.SetName("pusher1")
        dude1.ScriptUnhide()
        dude4.SetName("pusher2")
        dude4.ScriptUnhide()
    else :
        dude3.SetName("Regent2")
        dude3.ScriptUnhide()
        dude1.SetName("pusher1")
        dude1.ScriptUnhide()
        dude2.SetName("pusher2")
        dude2.ScriptUnhide()

#LA_VENTRUETOWER_1: functions for displaying Dominate effect
def dominatePlayer():
    __main__.FindPlayer().PlayHUDParticle("D_Dominate_HUD_Cast_emitter2")

def stopDominatePlayer():
    __main__.FindPlayer().StopHUDParticle(2)

#LA_VENTRUETOWER_1: LaCroix needs to float a line in a cutscene
def LaCroixCutsceneFloat():
    prince = Find("prince1")
    prince.PlayDialogFile("Character/dlg/Downtown LA/prince2/line1278_col_e.mp3")

#SP_ENSEQUENCES_B: Debug printing to find out of sync cameras
def DBprintname(x):
    print x


    
print "levelscript loaded"
