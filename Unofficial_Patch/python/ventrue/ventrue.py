print "loading ventrue level script"

import __main__
import random
random.seed()

from __main__ import G
from random import randint

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#PRINCE'S CHAMBERS: Checks story state and unhides correct events, changed by wesp
def setupChamber():
    princeStart = Find("prince1")
    princeEnd = Find("prince2")

    if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
        taxi = Find("taxi")
        if taxi: taxi.Kill()
        cabbie = Find("cabbie")
        if cabbie: cabbie.Kill()

    if(princeStart):
        princeStart.SetDefaultDialogCamera("DialogDefault")

    # check for specific Story State events
    if(G.Story_State == 10):
        princeStart.SetDefaultDialogCamera("Dynamic3")
    elif (G.Story_State == 15):
        if (__main__.IsClan(__main__.FindPlayer(), "Ventrue")):
            torryPrim = Find("toreador_unhide")
            torryPrim.Trigger()
            if(G.Patch_Plus == 1):
                gary = Find("torry_prim_3")
                if gary: gary.SetModel("models/character/npc/unique/Hollywood/Gary/Nosferatu_Gary.mdl")
        else:
            ventPrim = Find("ventrue_unhide")
            ventPrim.Trigger()
            if(G.Patch_Plus == 1):
                gary = Find("vent_prim_3")
                if gary: gary.SetModel("models/character/npc/unique/Hollywood/Gary/Nosferatu_Gary.mdl")
    elif (G.Story_State == 60):
        actCoffin = Find("coffin_state")
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

#PRINCE'S CHAMBERS: Turn prince around on Prince2, line 21
def turnPrinceAround():
    turn = Find("turn_around")
    turn.BeginSequence()

#PRINCE'S CHAMBERS: Pick which prince dialogue should be active
def pickAPrince():
    princeStart = Find("prince1")
    princeEnd = Find("prince2")
    if (G.Story_State < 30):
        princeStart.ScriptUnhide()
        princeEnd.ScriptHide()
    elif (G.Story_State >= 30):
        princeEnd.ScriptUnhide()
        princeStart.ScriptHide()

#PRINCE'S CHAMBERS: Fade out on map change
def changeVent():
    if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
        nosPort = Find("nos_teleport")
        nosPort.Trigger()
    else:
        othersPort = Find("others_teleport")
        othersPort.Trigger()

#PRINCE'S CHAMBERS: Choose which quest to send the player on
def princeQuests():
    if (G.Prince_Escort == 1):
        G.Prince_Escort = 0
        Find("lock_nos_out").Test()
        escort = Find("sheriff_escort")
        escort.BeginSequence()
        changeVent()
    elif (G.Wolf_Ending == 1):
        wereWolf = Find("teen_wolf_trigger")
        wereWolf.Trigger()
        print "YOU DANCING FOOL!!!"
    elif (G.Story_State == 65):
    #changed yet again by dan_upright 09/12/04
        if (G.move_to_sarcophagus_flag == 1):
            print "not doing the move thing"
        else:
            print "doing the move thing"
            relay = Find("move_to_sarcophagus")
            relay.Trigger()
            G.move_to_sarcophagus_flag = 1
    #changes end
    elif (G.Prince_Givekey == 1):
        Find("Start_Give_Prince_Key").Trigger()
    elif (G.Prince_Keepkey == 1):
        Find("Start_PC_Open_Sarc").Trigger()
    elif (G.Prince_Decision == 1):
        Find("Start_Prince_Beatdown").Trigger()
    elif(G.Prince_Regent == 1):
        Find("Start_Prince_Beatdown").Trigger()
    elif(G.Sabbat_Ending == 1):
        Find("Start_Prince_Beatdown_Sabbat").Trigger()
    if(G.Prince_Ending):
        relay = Find("exits_unlock_relay")
        relay.Trigger()

#PRINCE'S CHAMBERS: Sends you to society after talking to Beckett, disabled by wesp
def beckettQuest():
#    if (G.Society_Open == 1):
    if 0:
        changeVent()
        #__main__.ChangeMap(1.5, "society_mark", "society_change")

#PRINCE'S CHAMBERS: Chooses models to use for Camarilla Part1 Ending, changed by wesp
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
    if(G.Patch_Plus == 0):
        Find("Regent_Guard_Spare_Model").Kill()

#PRINCE'S CHAMBERS: Selects the correct ending to transition to from Give Prince Key ending
def checkEnding():
    if(G.Story_State == 125):
        Find("lonewolf_change").ScriptUnhide()
    else:
        Find("epilogue_change").ScriptUnhide()

#VENTRUETOWER: Called after talking to Chunk, opening the elevator to the Prince, changed by wesp
def chunkResults():
    chunk = Find("Chunk2")
    if(G.Chunk_Skip == 2):
        trigger = Find("chamber_transition")
        trigger.Enable()
#    killSafeArea = Find("setcombat")
    if(G.Chunk_Run == 1):
        cower = Find("chunk_cowers_run_1")
        cower.BeginSequence()
        chunk.WillTalk(0)
        chunk.SetRelationship("player D_FR 5")
        Find("base_elev_down_a").Unlock()
#        killSafeArea.Trigger()
    elif(G.Chunk_Attack == 1):
        attack = Find("chunk_attacks_run_1")
        attack.BeginSequence()
        chunk.SetRelationship("player D_HT 5")
        Find("base_elev_down_a").Unlock()
#        killSafeArea.Trigger()
    elif(G.Chunk_Open > 0 and G.Story_State != 65):
        chunkRelay   = Find("chunkRelay")
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

#VENTRUETOWER: Called to switch which camera is active in the Ventrue security room, changed by wesp
def ventrueCameraSwitch():
    G.Ventrue_Camera = G.Ventrue_Camera + 1
    if(G.Ventrue_Camera > 5):
        G.Ventrue_Camera = 1
    monitor = Find("monitor_2")
    monitor.SetCamera("camera_%i" % (G.Ventrue_Camera))

    chunk2 = __main__.Find("chunk2")
    chunk3 = __main__.Find("chunk3")
    
    G.Chunk_Reset = 1
    if(chunk2):
         chunk2.StartPlayerDialogRemote()
    if(chunk3):
         chunk3.StartPlayerDialogRemote()
    else:
        G.Chunk_Reset = 0
        return

#VENTRUETOWER: Called to change to combat for Nosferatu, changed by wesp
def ventrueCombat():
    combatTrigger = Find("combat_change")
    if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
        if (G.Story_State == 100 or G.Story_State == 105 or G.Story_State >= 115):
            combatTrigger.Trigger()
            print "Combat Switched"
            __main__.ScheduleTask(1.0, "Find(\"Chunk2\").ScriptUnhide()")
        taxi = Find("taxi")
        if taxi: taxi.Kill()
        cabbie = Find("cabbie")
        if cabbie: cabbie.Kill()

#VENTRUETOWER: Disables the elevator when the player is not allowed up.
def elevatorStop():
    if (G.Story_State >= 35 and G.Story_State < 60):
        eleButtons = Find("base_elev_down")
        baseButtons = Find("base_btn_up")
        eleButtons.Lock()
        baseButtons.Lock()

#VENTRUETOWER: Spawns the bomb after the bomb guy dies
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

#VENTRUETOWER: Despawns the bomb after placed
def despawnBomb():
    bomb = FindClass("item_g_astrolite")
    center = bomb[0].GetOrigin()
    angles = bomb[0].GetAngles()
    bomb[0].Kill()
    bombProp = Find("bomb_prop")
    bombProp.SetOrigin(center)
    bombProp.SetAngles(angles)
    bombProp.ScriptUnhide()

#ENDSEQUENCES B: Sets up players to avoid PC clan models
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

#ENDSEQUENCES B: Debug printing to find out of sync cameras
def DBprintname(x):
    print x

#VENTRUETOWER 1: Functions for displaying Dominate effect
def dominatePlayer():
    __main__.FindPlayer().PlayHUDParticle("D_Dominate_HUD_Cast_emitter2")

def stopDominatePlayer():
    __main__.FindPlayer().StopHUDParticle(2)

#VENTRUETOWER 1: LaCroix needs to float a line in a cutscene
def LaCroixCutsceneFloat():
    prince = Find("prince1")
    prince.PlayDialogFile("Character/dlg/Downtown LA/prince2/line1278_col_e.mp3")

print "levelscript loaded"
