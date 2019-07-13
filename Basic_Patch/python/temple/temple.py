print "************************** loading kj-temple level script"

import __main__

from __main__ import G

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#TEMPLE 1:
def mingXiaoDialogueTemple1():
    if(G.Ming_Ending):
        door = Find("templedra")
        door.Unlock()
        door = Find("templedrb")
        door.Unlock()

#TEMPLE 2: Botched
def t2botched():
    print ( "****************** Botched Setup ******************" )
    if ( G.Temple2SencondChanceLost == 1 ):
        print ( "****************** Failed Second Chance ******************" )
        triggers = Finds( "Trigger_wheel_room" )
        for trigger in triggers:
            if ( trigger ):
                print ( "****************** Found Triggers ******************" )
                trigger.ScriptUnhide()
                print ( "****************** Unhiding Triggers ******************" )
            else:
                print ( "****************** Cant Find Triggers ******************" )
        guard = Find( "guard_waterwheel4" )
        if ( guard ):
            guard.ScriptUnhide()
            print ( "****************** Unhidding Door Guard 1 ******************" )
        guard = Find( "guard_waterwheel5" )
        if ( guard ):
            guard.ScriptUnhide()
            print ( "****************** Unhidding Door Guard 2 ******************" )
        guards = Finds( "Guard_Start_Botched_6" )
        for guard in guards:
            if ( guard ):
                guard.ScriptUnhide()
        precogcams = Finds( "Botch2_Precog_Cam" )
        for precogcam in precogcams:
            if ( precogcam ):
                precogcam.ScriptUnhide()
    if ( G.Temple2DeepIn == 0 ):
        print ( "****************** Rearanging Funiture ******************" )
        props = Finds( "Furniture_Upright" )
        for prop in props:
            if ( prop ):
                prop.ScriptHide()
        propnews = Finds( "Furniture_Upturned" )
        for propnew in propnews:
            if ( propnews ):
                propnew.ScriptUnhide()
        blocks = Finds( "Furniture_Upturned_Blocks" )
        for block in blocks:
            if ( block ):
                block.ScriptUnhide()
        covers = Finds( "Bottleneck_Cover" )
        for cover in covers:
            if ( cover ):
                cover.EnableHint()
        spawners = Finds( "Guards_BottleNeck_Spawners" )
        for spawner in spawners:
            if ( spawner ):
                spawner.Enable()
    if ( G.Temple2BotchEarly == 1 ):
        guard = Find( "Guard_Start_Botched_3" )
        guard.ScriptUnhide()

#TEMPLE 2: Start Botched, changed by wesp
def t2botchcheck():
    print ( "****************** Starting Level Botched ******************" )
    if (G.Temple1_Botched == 1):
        print ( "****************** Unhidding Extra Guards ******************" )
        guard = Find( "Guard_Start_Botched_1" )
        if ( guard ):
            print ( "**********************Found Guard_Start_Botched_1 and Unhideing **********************"  )
            guard.ScriptUnhide()
        guard = Find( "Guard_Start_Botched_2" )
        if ( guard ):
            print ( "**********************Found Guard_Start_Botched_2 and Unhideing **********************"  )
            guard.ScriptUnhide()
        guard = Find( "Guard_Start_Botched_3" )
        if ( guard ):
            print ( "**********************Found Guard_Start_Botched_3 and Unhideing **********************"  )
            guard.ScriptUnhide()
        guards = Finds( "Guard_Start_Botched_4" )
        for guard in guards:
            if ( guard ):
                print ( "**********************Found Guard_Start_Botched_4 and Unhideing **********************"  )
                guard.ScriptUnhide()
        guard = Find( "Guard_Start_Botched_5" )
        if ( guard ):
            print ( "**********************Found Guard_Start_Botched_5 and Unhideing **********************"  )
            guard.ScriptUnhide()
        print ( "****************** Hidding Stealth Guards ******************" )
        guard = Find( "Guard_1_Patrol")
        if guard: guard.ScriptHide()
        guard = Find( "guard_barracks1")
        if guard: guard.ScriptHide()
        guard = Find( "guard_barracks2")
        if guard: guard.ScriptHide()
        guard = Find( "guard_barracks3")
        if guard: guard.ScriptHide()
        print ( "****************** Unhiding Extra Triggers ******************" )
        trigger = Find( "Trigger_Botched_Previous_1" )
        if trigger: trigger.ScriptUnhide()
        t2botched()

#TEMPLE 2: Check stealth kill event
def stealthKillEvent():
    print ( "***************** Running Stealth Kill Event *****************" )
    if ( G.T2PCInplace == 1 and G.T2NPCInplace == 1 ):
        print ( "***************** Triggering Stealth Kill Event *****************" )
        breakable = Find( "StealthKill_Breakable" )
        breakable.Break()
    else:
        print ( "***************** Failing Stealth Kill Event *****************" )

#TEMPLE2: Start Botched
def t3botchcheck():
    if (G.Temple2_Botched == 1):
        guards = Finds( "Guards_Botch" )
        for guard in guards:
            if ( guard ):
                guard.Enable()
        relay = Find( "Relay_BackUp_Triggers_ON" )
        relay.Trigger()

#TEMPLE 1: Called to see where the player needs to go to
def leaveTemple():
    if(G.Story_State < 100):
        __main__.ChangeMap(2.5, "temple", "trig_temple")
    else:
        __main__.ChangeMap(2.5, "caine_landmark", "caine_teleport")

#TEMPLE 1: Set temple to non-combat state, changed by wesp
def SetTempleState():
    if (G.Story_State < 105):
        print ( "***************** Set Elysium *****************" )
        if (G.Story_State < 100):
            npc = Find("MingXiao")
            if npc:
                npc.ScriptUnhide()
        else:
            print ( "***************** Change out Ming *****************" )
            npc = Find("MingXiao")
            if npc:
                npc.Kill()
            npc = Find("MingXiao2")
            if npc:
                npc.ScriptUnhide()
            door = Find("templedra")
            door.Lock()
            door = Find("templedrb")
            door.Lock()
        world = Find("world")
        if world: world.SetSafeArea(2)    # elysium
    else:
        print ( "***************** Set Combat *****************" )
        blocks = Finds( "Door_Blocks" )
        for block in blocks:
            if block:
                print ( "***************** Removeing Door Blocks *****************" )
                block.Kill()
        print ( "***************** Removeing Door Blocks *****************" )
        mainblock = Find( "Door_Block_Main" )
        mainblock.ScriptUnhide()
        npc = Find("MingXiao")
        if npc: npc.Kill()
        npc = Find("MingXiao2")
        if npc: npc.Kill()
        world = Find("world")
        world.SetSafeArea(0)    # combat
        npc = Find("guard_1")
        if npc: npc.ScriptUnhide()
        npc = Find("guard_2")
        if npc: npc.ScriptUnhide()
        yukie = Find( "Yukie" )
        if (yukie and not __main__.IsDead ("Yukie") and G.Yukie_Leave == 1 and G.Patch_Plus == 1):
            yukie.ScriptUnhide()

#TEMPLE 1: If global set, go to ming xiao human form on arena map
#def tpl1_check_ming_xiao_story_state():
#    if G.Story_State < 110:
#        trans = Find( "temple_arena_transition" )
#        if trans:
#            print "temple1: transitioning to temple4 map!(story state)"
#            trans.ChangeNow()

#TEMPLE 1: Helper func, aggro east guards
def tpl1_east_aggro():
    guards = Finds( "guard_east_quarters" )
    for guard in guards:
        if guard:
            guard.SetRelationship("player D_HT 5")

#TEMPLE 1: Helper func, aggro west guards
def tpl1_west_aggro():
    guards = Finds( "guard_west_quarters" )
    for guard in guards:
        if guard:
            guard.SetRelationship("player D_HT 5")

#TEMPLE 1: If player's stealth <8, wake up sleeping guards in east quarters
def tpl1_eastquarters_check_stealth():
    pc = __main__.FindPlayer()

    if (pc.stealth < 8):
        print "temple1: player stealth <8, east guard wakes!"

        tpl1_east_aggro()

#TEMPLE 1: If player's stealth <7, wake up sleeping guards in west quarters
def tpl1_westquarters_check_stealth():
    pc = __main__.FindPlayer()

    if (pc.stealth < 7):
        print "temple1: player stealth <7, west guard wakes!"
        tpl1_west_aggro()

#TEMPLE 1: Main hall, if trigger alarm, unhide 2 more guards
def tpl1_mainhall_check_alarm():
    print "temple1: mainhall, checking alarm state..."
    if (G.tpl1_alarm == 1):
        guards = Finds( "guard_main_hall_hidden" )
        for guard in guards:
            if guard:
                guard.ScriptUnhide()

#TEMPLE 2: Onload, if trigger alarm, unhide 4 more guards (central corridor)
def tpl2_central_check_alarm():
    print "temple2: onload, checking alarm state..."
    if (G.tpl1_alarm == 1):
        guards = Finds( "guard_central" )
        for guard in guards:
            if guard:
                guard.ScriptUnhide()

#TEMPLE 2: Helper func, aggro barracks guards
def tpl2_barracks_aggro():
    guards = Finds( "guard_barracks" )
    for guard in guards:
        if guard:
            guard.SetRelationship("player D_HT 5")

#TEMPLE 2: Barracks, if trigger alarm, wake guards
def tpl2_barracks_check_alarm():
    print "temple2: barracks, checking alarm state..."
    if (G.tpl1_alarm == 1):
        tpl2_barracks_aggro()

#TEMPLE2: Barracks, if trigger alarm, wake guards
def tpl2_barracks_locker_check_alarm():
    pc = __main__.FindPlayer()
    print "temple2: player stealth <7, barrack guard wakes!"

    if (pc.stealth < 7):
        tpl2_barracks_aggro()

#TEMPLE 2: Helper func, aggro messhall guards
def tpl2_messhall_aggro():
    guards = Finds( "guard_messhall" )
    for guard in guards:
        if guard:
            guard.SetRelationship("player D_HT 5")

    guard = Find( "guard_messhall_patrol" )
    if guard:
        guard.SetRelationship("player D_HT 5")

    guard = Find( "guard_messhall_patrol2" )
    if guard:
        guard.SetRelationship("player D_HT 5")

#TEMPLE 2: Waterwheel, if trigger alarm, unhide guards
def tpl2_waterwheel_check_alarm():
    print "temple2: waterwheel, checking alarm state..."
    if (G.tpl2_alarm == 1):
        guards = Finds( "guard_waterwheel_downstairs" )
        for guard in guards:
            if guard:
                guard.ScriptUnhide()

#TEMPLE 2: Room2, aggro guards
def tpl2_room2_1():
    guards = Finds( "guard_room2_1*" )
    for guard in guards:
        if guard:
            guard.SetRelationship("player D_HT 5")

#TEMPLE 2: Room2, aggro guards
def tpl2_room2_2():
    guards = Finds( "guard_room2_2*" )
    for guard in guards:
        if guard:
            guard.SetRelationship("player D_HT 5")

#TEMPLE 2: Room2, aggro guards
def tpl2_room2_3():
    guards = Finds( "guard_room2_3*" )
    for guard in guards:
        if guard:
            guard.SetRelationship("player D_HT 5")

#TEMPLE 2: Room2, aggro guards
def tpl2_room2_4():
    guards = Finds( "guard_room2_4*" )
    for guard in guards:
        if guard:
            guard.SetRelationship("player D_HT 5")

#TEMPLE 2: dark shrine room, check door
def tpl2_check_pressuredoor():
    door = Find( "temple2_pressure_door" )
    if door:
        if (G.tpl2_pressure1 == 1 and G.tpl2_pressure2 == 1):
            print "temple2: both plates down! (in)"
            door.Open()
        else:
            print "temple2: both plates not down! do not open door"

#TEMPLE 3: Hub, if trigger alarm, unhide guards
def tpl3_hub_check_alarm():
    print "temple3: hub, checking alarm state..."
    if (G.tpl2_alarm == 1):
        print "temple3: unhiding hub guards!"
        guards = Finds( "guard_hub" )
        for guard in guards:
            if guard:
                guard.ScriptUnhide()

#TEMPLE 3: Check if all 4 pedestals are set, changed by wesp
def tpl3_check_pedestals():
    print "temple3: checking pedestal states..."
    if (G.tpl3_elephant_final == 1 and G.tpl3_dragon_final == 1 and G.tpl3_cat_final == 1 and G.tpl3_crane_final == 1):
        print "temple3: pedestals all set!"
        if G.Patch_Plus == 1:
            gong = Find("gong_wesp")
            gong.PlaySound()
        tele_emitter = Find( "teleport_emitter" )
        tele_emitter.TurnOn()
        tele_trigger = Find( "teleport_trigger" )
        tele_trigger.ScriptUnhide()
# wesp        __main__.FindPlayer().SetQuest("Ming", 4)
        torches = Finds( "torch*" )
        for torch in torches:
            if torch:
                torch.TurnOff()

#      torchtrigger = Find( "pedestal_cat_final" )
#      if torchtrigger:
#          torchtrigger.OnDeactivate()

        button = Find("cat_top_brush")
        button.ScriptUnhide()
        button = Find("crane_top_brush")
        button.ScriptUnhide()
        button = Find("dragon_top_brush")
        button.ScriptUnhide()
        button = Find("elephant_top_brush")
        button.ScriptUnhide()

    else:
        print "temple3: not all pedestals set yet..."

#TEMPLE 3: Blow out all torches
def tpl3_torchafter_blowout():
    print "temple3: checking pedestal states..."
    torches = Finds( "torchafter*" )
    for torch in torches:
        if torch:
            print "temple3: torchafter* found!"
            torch.TurnOn()

#TEMPLE 3: Really spawn item on pedestal
def InsertIdol2(pillar, idol):
    if pillar == idol:
        G["tpl3_" + idol + "_final"] = 1
    target = Find(pillar + "_target")
    if target:
        item = __main__.CreateEntityNoSpawn("item_g_idol_" + idol, target.GetCenter(), target.GetAngles())
        if item: __main__.CallEntitySpawn(item)

    button = Find(pillar + "_brush")
    if button: button.ScriptUnhide()

    trig = Find("trig_" + pillar)
    if trig: trig.Enable()

    tpl3_check_pedestals()

#TEMPLE 3: Spawn item on pedestal
def InsertIdol(pillar):
    container = Find("pedestal_" + pillar + "_final")
    if container.HasItem("item_g_idol_cat") and not G.tpl3_cat_final:
        InsertIdol2(pillar, 'cat')
    elif container.HasItem('item_g_idol_crane') and not G.tpl3_crane_final:
        InsertIdol2(pillar, 'crane')
    elif container.HasItem('item_g_idol_dragon') and not G.tpl3_dragon_final:
        InsertIdol2(pillar, 'dragon')
    elif container.HasItem('item_g_idol_elephant') and not G.tpl3_elephant_final:
        InsertIdol2(pillar, 'elephant')

#TEMPLE 3: Really remove item from pedestal
def RemoveIdol2(pillar, idol):
    container = Find("pedestal_" + pillar + "_final")
    container.RemoveItem("item_g_idol_" + idol)
    button = Find(pillar + "_brush")
    button.ScriptHide()
    G["tpl3_" + idol + "_final"] = 0
    trig = Find("trig_" + pillar)
    trig.Disable()

#TEMPLE 3: Remove item from pedestal
def RemoveIdol(pillar):
    container = Find("pedestal_" + pillar + "_final")
    player = __main__.FindPlayer()
    if container.HasItem("item_g_idol_cat") and player.HasItem("item_g_idol_cat"):
        RemoveIdol2(pillar, "cat")
    elif container.HasItem("item_g_idol_crane") and player.HasItem("item_g_idol_crane"):
        RemoveIdol2(pillar, "crane")
    elif container.HasItem("item_g_idol_dragon") and player.HasItem("item_g_idol_dragon"):
        RemoveIdol2(pillar, "dragon")
    elif container.HasItem("item_g_idol_elephant") and player.HasItem("item_g_idol_elephant"):
        RemoveIdol2(pillar, "elephant")

#TEMPLE 4: On ming xiao's death, changed by wesp
def OnMingXiaoDead():
    G.Ming_Dead = 1
    if G.Story_State == 110:
        __main__.FindPlayer().SetQuest("Ming", 5)
        __main__.FindPlayer().SetQuest("Prince", 1)
    else:
        __main__.FindPlayer().SetQuest("Ming", 6)
        __main__.FindPlayer().SetQuest("Prince", 2)

#TEMPLE 4: Teleport player back to hub
def ExitTemple():
    if (G.Story_State == 110):
        __main__.ChangeMap(0.5, "temple_landmark", "trig_arena_to_ending")
    else:
        __main__.ChangeMap(0.5, "caine_landmark", "trig_arena_to_taxi")

def MoveSecretIdol():
    idol = Find( "Idol_Mover" )
    position = 0.0
    if ( G.temple2_PlateA == 1 ):
        position = position + 0.5
    if ( G.temple2_PlateB == 1 ):
        position = position + 0.5
    idol = Find( "Idol_Mover" )
    idol.SetPosition( position )

print "************************** levelscript loaded"
