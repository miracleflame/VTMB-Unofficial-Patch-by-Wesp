print "loading hollywood level script"

import __main__

from __main__ import G

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#609: Hides events that may break with obfuscate, changed by wesp
def malkNosCatchAll():
    if G.Patch_Plus == 2:
        firstRunner = Find("studiodoor1-trigger_event")
        secondRunner = Find("door_bash-trigger_failsafe")
        thirdRunner = Find("inigo_trigger")
        if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu") or __main__.IsClan(__main__.FindPlayer(), "Malkavian")):
            if firstRunner: firstRunner.ScriptHide()
            print "first runner hidden"
            if secondRunner: secondRunner.ScriptHide()
            print "second runner hidden"
            if thirdRunner: thirdRunner.ScriptHide()
            print "third runner hidden"

#609: Update quest log after Andrei dies
def andreiDead():
    __main__.FindPlayer().SetQuest("Kings Way", 2)

#ASPHOLE: Called to swap ash and lookalike clothes
def ashClothingSwap():
    ash = Find("Ash")
    lookalike = Find("ash_lookalike")
    ash.SetModel("models/character/npc/unique/Hollywood/Ash_Lookalike/ash_Lookalike.mdl")
    lookalike.SetModel("models/character/npc/unique/Hollywood/Ash/Ash.mdl")

#ASPHOLE: Determines the results of dialog with ash, changed by wesp
def ashDialog():
    if(G.Ash_Switch==1):
        print "ash_switch ==1"
        lookalike = Find("Ash_lookalike")
        lookalike.WillTalk(1)
    elif(G.Ash_Fake):
        print "ash should go to bathroom"
        ashconvo = Find("ash_convo_01")
        ashbath = Find("ash_bathroom_spot")
        ash = Find("Ash")
        ashconvo.Disable()
        ashbath.Enable()
        ash.WillTalk(0)
        ash.ChangeSchedule("-")
        hunter = Find("Hunter")
        hunter.ScriptUnhide()
        relay = Find("fake_ash_staked_relay")
        relay.Enable()
        pc = __main__.FindPlayer()
        if(pc.humanity >= 4 and G.Patch_Plus == 1):
            pc.HumanityAdd( -1 )

#ASPHOLE: Sets the ash lookalike's disposition to dead
def ashLookalikeDead():
    fakeAsh = Find("Ash_lookalike")
    fakeAsh.SetDisposition("Dead", 1)
    fakeAsh.WillTalk(0)
    fakeAsh.TweakParam("vision 0")
    fakeAsh.TweakParam("hearing 0")

#ASPHOLE: Determines whether Ash is in the Asphole, along with his lookalike, changed by Wesp
def ashSituation():
    ash = Find("Ash")
    lookalike = Find("Ash_lookalike")
    hunter = Find("Hunter")
    if(G.Ash_Know != 1):
        if(lookalike):
            lookalike.WillTalk(0)
    if(G.Ash_Sewers):
        if(ash):
            ash.Kill()
        if(hunter):
            hunter.Kill()
    if(G.Ash_Fake or G.Story_State > 65):
        if(ash):
            ash.Kill()
        if(lookalike):
            lookalike.Kill()
        if(hunter):
            hunter.Kill()
    if G.Doll3_Dead == 1:
        doll3 = Find("Doll3")
        if doll3: doll3.Kill()

#ASPHOLE: Determines whether Ash and lookalike have privacy, changed by Wesp
def ashBathswitch():
    print "ashBathswitch called"
    if(G.Ash_Bathswitch == 1):
        print "Ash in bathroom. Triggering logic_relay."
        logswitch = Find ("bathroom-logic")
        logswitch.Trigger()
        G.Ash_Bathswitch = 2

#ASPHOLE: Determines results of talking to the lookalike
def lookalikeDialog():
    if(G.Ash_Switch == 2):
        spot = Find("lookalike_bathroom_spot")
        spot.Enable()
        lookalike = Find("Ash_lookalike")
        lookalike.WillTalk(0)
        lookalike.UseInteresting(1)
        lookalike.ChangeSchedule("-")

#TJP - 04/08/04
#ASPHOLE: Sends the player to the sewers if Ash is ready to go
def toSewers():
    if(G.Ash_Sewers == 1):
        __main__.ChangeMap(2.5, "AspHole4", "AspHoleTeleportSewers")

#CHINESE THEATER: Set quest on gargoyle death, changed by wesp
def SetGargoyleQuestState():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Gargoyle")
    if state > 0 and state != 2 and state != 5:
        pc.SetQuest("Gargoyle", 3)
    if state == 2:
        pc.SetQuest("Gargoyle", 6)

#JEWELRY: Isaac dialog end
def IsaacDialogEnd():
    #changed by dan_upright 04/12/04
    #if G.Isaac_Kingstart == 1:
    #    __main__.ChangeMap(2.5, "jewelry_mark", "trig_transition")
    #    G.Isaac_Kingstart = 2
    if(G.Isaac_Show == 1):
    #changes end
        video = Find("start_snuff")
        video.Trigger()
    elif(G.Isaac_Movie == 1):
        video = Find("start_half_snuff")
        video.Trigger()

#LUCKYSTAR: Called when the player tries to exit the map
def luckyStarExit():
    if(G.Story_State < 100):
        __main__.ChangeMap(2.5, "luckystar1", "luckystarTeleport1")
    else:
        __main__.ChangeMap(2.5, "caine_landmark", "luckystarCaine")

#LUCKYSTAR: Called when the player grabs the business card, changed by wesp
def junkyardCardPickup():
    if(__main__.FindPlayer().GetQuestState("Serial") < 7):
        __main__.FindPlayer().SetQuest("Serial", 7)

#LUCKYSTAR: Called when the killer gets away
def killerEscape():
    __main__.FindPlayer().SetQuest("Serial", 6)
    __main__.FindPlayer().SetQuest("Muddy", 4)
    G.Muddy_Dead = 1

# TJP - 01/28/04
#LUCKYSTAR: Determines what state the luckystar hotel is in, changed by wesp
def luckyState():
    print ("luckyState called")
    if(G.Story_State >= 115):
        print ("Anarchs present")
        anarchs = Find("luckystate-Anarchs_Present")
        anarchs.Trigger()
        skelter = Find("Skelter")
        if (G.Patch_Plus == 1):
            skelter.ScriptUnhide()
    if(G.Killer_Key == 1):
    #A different flag, tied to the material clue from the downtown murder scene, would be better for the first argument
        print ("Killer present")
        killer = Find("luckystate-Killer_Present")
        killer.Trigger()
    if(G.Lucky_Blood == 1):
        print ("Tape event present")
        tape = Find("luckystate-Horrortape_event")
        tape.Trigger()
    if(G.Lucky_Wolf == 1):
        ww = Find("werewolf")
        ww.ScriptHide()
        G.Lucky_Wolf = 2
        G.LSWW = 0
    #else:
    #    print ("Default Map State")
    #    default = Find("luckystate-Default")
    #    default.Trigger()

# TJP - 03/19/04
#LUCKYSTAR: Useless, really, changed by wesp :)
def lsww():
    print ("wait for it")
    if (G.LSWW > 8):
        print ("yup")
        ww = Find("werewolf")
        ww.ScriptUnhide()
        ww.SetAnimation("dance")
        G.Lucky_Wolf = 1

#LUCKYSTAR: On hatter's death, set quest state, changed by wesp
def onHatterDeath():
    pc = __main__.FindPlayer()
    if pc.GetQuestState("Writer") == 1:
        G.Hatter_Dead = 1
        pc.SetQuest("Writer", 4)
        hatter = Find("DHatter")
        center = hatter.GetCenter()
        point = (center[0], center[1], center[2] + 20)
        script = __main__.CreateEntityNoSpawn("item_g_hatters_screenplay", point, (0,0,0) )
        script.SetName("script")
        sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
        sparklies.SetParent("script")
        __main__.CallEntitySpawn(script)
        __main__.CallEntitySpawn(sparklies)

#LUCKYSTAR: On pickup of netcafe key, set quest state
def OnNetcafeKeyPickup():
    pc = __main__.FindPlayer()
    if pc.GetQuestState("Tape") > 0:
        pc.SetQuest("Tape", 7)

#LUCKYSTAR: Called to look at the werewolf head
def werewolfHeadCamera():
    camera = Find("werewolf_head_camera")
    camera.StartShot()

#METALHEAD: Set Mitnick quest to 10, because Worldcraft doesn't like commas, changed by wesp
def failMitnick():
    pc = __main__.FindPlayer()
    pc.SetQuest("Mitnick", 10)
    G.Shubs_Act = 5

# TJP - 02/06/04
#NETCAFE: Determines if headrunners are present, changed by wesp
def netcafeState():
#    print ("Netcafe function called")
    if G.Lucky_Blood == 1:    #("G.Netcafe_Key == 1"):
#        print ("Tape Event map state")
#        logic = Find("logic_kill_safe_state")
#        if logic: logic.Trigger()
        logic = Find("logic_enable_combat_state")
        if logic: logic.Trigger()
    if G.Baron_Died == 1:
        baron = Find("plus_BaronVonHugeCock")
        if baron: baron.Kill()
    if G.Prissy_Died == 1:
        prissy = Find("plus_PrissyMcButterjizzles")
        if prissy: prissy.Kill()
    scheme1 = Find("soundscheme_netcafe")
    scheme2 = Find("soundscheme_tapetime")
    if G.Netcafe_Key > 1:
        scheme1.FadeOut(0)
        scheme2.FadeIn(0)
    else:
        scheme2.FadeOut(0)
        scheme1.FadeIn(0)

#NETCAFE: Set quest state after picking up tape
def SetTapeQuestState():
    pc = __main__.FindPlayer()
    if pc.GetQuestState("Tape") > 0:
        pc.SetQuest("Tape", 4)

#NETCAFE: Curier's e-mail
def OnCourierEmail():
    G.Courier_QuickBuck = 1
    pc = __main__.FindPlayer()
    if pc.GetQuestState("Courier")== 1:
        pc.SetQuest("Courier", 2)

#NETCAFE: Player has found out about Ginger Swan's crypt
def OnGingerSwanEntry():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Courier")
    if state == 3:
        pc.SetQuest("Courier", 4)
    #changed by dan_upright 02/12/04
    else:
        G.GingerSwanKnowledge = 1
    #changes end

#REDSPOT: Called to choose a float line for spicoli
def spicoliFloat():
    from random import Random
    from time import time
    R = Random( time() )
    Index = R.randint(2,8)
    spicoli = Find("Spicoli")
    if(spicoli):
        spicoli.PlayDialogFile(("\Character\dlg\Hollywood\Spicoli\line%i_col_e.mp3" % Index))

#SEWERS (ASH): Initialization stuff.
def SetSewerNPCs():
    npc = Find("Ash")
    npc.WillTalk(0)

    npcs = Finds("hunter_1") + Finds("hunter_4") + Finds("hunter_4_vision") + Finds("hunter_5")
    for npc in npcs:
        npc.SetRelationship("Ash D_HT 5")

#SEWERS (ASH): End sewers, changed by wesp
def AshDialogEnd():
#    if __main__.IsClan(__main__.FindPlayer(), "Nosferatu"):
        __main__.ChangeMap(0.0, "sewer_map_landmark", "trig_transition_sewer")
#    else:
#        __main__.ChangeMap(2.5, "taxi_landmark", "trig_transition")

# TJP - 01/27/04 update 04/08/04
#SINBIN: Determines if Chastity goes aggro
def checkChastity():
    print ("checkChastity called")
    if (G.Chastity_Attack == 1):
        trigger = Find("Chastity_go_hostile-trigger")
        trigger.Enable()

# TJP - 01/27/04
#SINBIN: Determines when Kerri goes where
def kerriBiz():
    print ("kerriBiz called")
    if (G.Kerri_Nos == 1):
        print ("kerri frightened by nos")
        gotonos = Find("kerri-logic_nos")
        gotonos.Trigger()
    elif(G.Kerri_Mesmerize == 1):
        G.Kerri_Biz = 1
        print ("kerri mesmerized")
        gotomez = Find("Kerri-logic_mesmerized")
        gotomez.Trigger()
    elif(G.Kerri_Biz == 1):
        print ("kerri going to back room")
        gotoroom = Find("Kerri-logic_to_backroom")
        gotoroom.Trigger()
    kerri = Find("Kerri")
    if kerri: kerri.WillTalk(0)

#SINBIN: Won't let Kerri talk to the player unless there is Biz, changed by wesp
def kerriBizCheck():
    if(G.Kerri_Biz == 1):
        kerri = Find("Kerri")
        if kerri: kerri.WillTalk(1)
        timer = Find("kerri_timer")
        if timer: timer.Enable()
        print ("timer started")

# TJP - 01/22/04
#SINBIN: Controls what map state the sin bin is in, depending on if you are on VVs quest or not, changed by wesp
def sinbinMapstate():
    print("sinbinMapstate called")
    kerri = Find("Kerri")
    if kerri: kerri.WillTalk(0)
    if(G.Velvet_Quest <> 1 or G.Hunter_Dead == 1):
        noquest = Find("mapstate_not_on_VV_quest")
        noquest.Trigger()
    elif(G.Velvet_Quest == 1):
        quest = Find("mapstate_on_VV_quest")
        quest.Trigger()
        if (G.Patch_Plus == 1 and G.Chastity_Swap == 0):
            chastity = Find("Chastity")
            chastity.SetName("Chastity_basic")
            chastity.ScriptHide()
            chastity_plus = Find("Chastity_plus")
            chastity_plus.ScriptUnhide()
            chastity_plus.SetName("Chastity")
            G.Chastity_Swap = 1

# TJP - 01/21/04
#SINBIN: Controls whether Peeper_1 deposits coins or goes to get more
def windowIncrement():
    if(G.Window_Count == 3):
        getchange = Find("change_machine-ss")
        coinfeed = Find("Peeper_1-ss_feed_coins")
        coinfeed.CancelSequence()
        getchange.BeginSequence()
        G.Window_Count = 0
    elif(G.Window_Count < 3):
        coinfeed = Find("Peeper_1-ss_feed_coins")
        coinfeed.BeginSequence()
        G.Window_Count = G.Window_Count + 1

# TJP - 01/21/04
#SINBIN: Controls whether Peeper_1 gets change or leaves, depending on what state the change machine is in
def changeMachine():
    print("changeMachine function called")
    if(G.Change_Machine == 0):
        print("G.Change_Machine == 0")
        getchange = Find("get_change-ss")
        #coinfeed = Find("Peeper_1-ss_feed_coins")
        getchange.BeginSequence()
        #coinfeed.Enable()
    elif(G.Change_Machine == 1):
        print("G.Change_Machine == 1")
        G.Sin_Peeper1 = 1
        broken = Find("no_change-ss")
        broken.BeginSequence()

# TJP - 01/23/04
#SINBIN: If both patrons leave the peep booths, the dancers go on break.
def dancersState():
    print("dancersState called")
    if(G.Sin_Peeper1 == 1 and G.Sin_Peeper3 == 1):
        changedancers = Find("Dancers-logic_int_place_state")
        changedancers.Trigger()
        kerri = Find("Kerri")
        if kerri: kerri.WillTalk(1)
    else:
        print("not all patrons out yet")

#SINBIN: Update "Strip to Hunt" quest state after Chastity is killed.
def chastityKilled():
    G.Chastity_Dead = 1
    if (G.Hunter_Dead == 1 and G.Sin_Innocent == 1):
        __main__.FindPlayer().SetQuest("Strip", 2)
    elif (G.Hunter_Dead == 1):
        __main__.FindPlayer().SetQuest("Strip", 2)
        __main__.FindPlayer().AwardExperience("Strip03")
    world = Find("world")
    world.SetSafeArea(1)

#SINBIN: Update "Cover Girl" quest state after Flynn is killed.
def flynnKilled():
    G.Flynn_Dead = 1
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Guy")
    if (state == 1):
        pc.SetQuest("Guy", 5)

#SINBIN: Hacked flynn's computer, got secret message, set flag, quest state.
def gotSecretMessage():
    G.Flynn_Message = 1
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Tape")
    if (state == 1):
        pc.SetQuest("Tape", 3)

#SINBIN: Checks to see if the player can afford to open the window, and removes his money
def windowCheck(int):
    pc = __main__.FindPlayer()
    if(pc.CurrentMoney() >= 5):
        pc.MoneyRemove(5)
        window = Find("peepshw%i" % int)
        window.Open()
    else:
        rejectSound = Find("reject_sound_%i" % int)
        rejectSound.PlaySound()

# TJP - 01/28/04
#VESUVIUS: Determines if Charming Stripper Misti goes to the private room or not. I hope she does! changed by wesp
def mistiState():
    print("mistiState called")
    if(G.Misti_Follow == 1):
        print("shes going!")
        mistigo = Find("Misti-logic_walk_back")
        mistigo.Trigger()
    elif(G.Misti_Dance == 1):
        print("shes dancing!")
        misti = Find("Misti")
        misti.ScriptHide()
        stripper = Find("stripper")
        stripper.ScriptUnhide()
        stripper.SetModel("models/character/npc/unique/Hollywood/Misti/Mistidance.mdl")
        dance = Find("stripper_seq2")
        dance.BeginSequence()
        G.Misti_Dance = 0
    else:
        print("G.Misti_Follow <> 1")
        misti_floor = Find("misti_floor")
        misti_floor.Trigger()

# TJP - 01/12/04
#VESUVIUS: Enables trigger that tells VV to walk upstairs
def velvetRelocate():
    if(G.Velvet_Stairs == 1):
        triggerone = Find("VV_failsafe_1")
        triggertwo = Find("VV_failsafe_2")
        triggerone.Enable()
        triggertwo.Enable()
    if(G.Velvet_Quest == 2):
        trigger = Find("vv_give_quest_2_trigger")
        trigger.ScriptUnhide()
    if(G.Velvet_Quest > 2):
        trigger = Find("vv_give_quest_2_trigger")
        if trigger: trigger.Kill()

#VESUVIUS: Puts VV on stage dancing after all her quests are done
def velvetDance():
    if(G.Velvet_Quest >= 4):
        vv_dance_relay = Find("vv_dance_relay")
        vv_dance_relay.Trigger()
        if(G.Patch_Plus == 1):
            pool_stripper = Find("pool_stripper")
            pool_stripper.ScriptUnhide()

# TJP - 01/13/04
#VESUVIUS: Decides which VV appears, the upstairs instance or the downstairs one
def velvetLocate():
    if(G.Velvet_Stairs > 0 and G.Velvet_Quest < 4):
        teleporter = Find("VV2")
        trigger = Find("VV_forcedlg-trigger")
        teleporter.Teleport()
        if trigger: trigger.Kill()

# TJP - 01/15/04
#VESUVIUS: Randomizes guys sitting around
def randomSitters():
    from random import Random
    from time import time
    R = Random( time() )
    Index = R.randint(0,1)
    if(Index == 0):
        stateone = Find("club_state_1")
        stateone.Trigger()
    elif(Index == 1):
        statetwo = Find("club_state_2")
        statetwo.Trigger()

# TJP - 01/15/04
#VESUVIUS: Randomizes state of Vesuvius
def randomClubstate():
    from random import Random
    from time import time
    R = Random( time() )
    Index = R.randint(0,1)
    if(Index == 0):
        stateone = Find("club_state_1")
        stateone.Trigger()
    elif(Index == 1):
        statetwo = Find("club_state_2")
        statetwo.Trigger()

# TJP - 01/15/04
#VESUVIUS: Randomizes Vesuvius random events, changed by wesp
def randomClubevents():
    from random import Random
    from time import time
    R = Random( time() )
    Index = R.randint(0,10)
    eventone = Find("stripper_from_dressing_room-logic_disable")
    eventtwo = Find("stripper_off_work-logic_disable")
    eventthree = Find("disable_bj_event")
    if(Index < 3):
        eventtwo.Trigger()
        eventthree.Trigger()
        offwork = Find("stripper_off_work")
        if offwork: offwork.Kill()
    elif(Index < 6):
        eventone.Trigger()
        eventthree.Trigger()
    elif(Index < 10):
        eventone.Trigger()
        eventtwo.Trigger()
        if G.Patch_Plus == 0:
            eventthree.Trigger()
    if G.Misti_Dead == 1:
        misti = Find("Misti")
        if misti: misti.Kill()

#HOLLYWOOD: Determines if the sweeper is on the streets and going to talk to the player, changed by wesp
def sweeperPlacement():
    if G.Isaac_Know:
        sweeper = Find("Sweeper")
        if sweeper:
            sweeper.Kill()
            trig = Find("trig_kill_sweeper")
            trig.Kill()
    else:
        __main__.ScheduleTask(3.0, "__main__.FindEntityByName(\"Sweeper\").StartPlayerDialog(256)")

#HOLLYWOOD: Hides/unhides Samantha
def SetSamantha():
    if __main__.IsClan(__main__.FindPlayer(), "Nosferatu"):
        sam = Find("Samantha")
        if sam: sam.Kill()
    elif G.Isaac_Know == 1 and not G.Samantha_Know == 1:
        sam = Find("Samantha")
        sam.ScriptUnhide()
        sam_trig = Find("trig_samantha")
        sam_trig.Enable()
    elif G.Samantha_Stopped or G.Samantha_FinishedCall:
        sam = Find("Samantha")
        if sam: sam.Kill()

#HOLLYWOOD: Hides/unhides Courier
def SetCourier():
    if G.Courier_QuickBuck == 1:
        courier = Find("Courier")
        if courier:
            courier.ScriptUnhide()
            courier.MakeInvincible(1)

#HOLLYWOOD: Sets Anonymous Caller
def SetAnonCaller():
    npc = Find("Anoncaller")
    npc.WillTalk(0)

    if G.Lucky_Blood == 1:
        timer = Find("timer_anoncaller")
        if timer: timer.Kill()

    elif G.Flynn_Message == 1:
        trig = Find("trig_anoncaller")
        if trig: trig.Enable()

#HOLLYWOOD: Checks state of Anonymous Caller
def AnonCallerDialogEnd():
    npc = Find("Anoncaller")
    npc.WillTalk(0)

    timer = Find("timer_anoncaller")
    if timer:
        if G.Lucky_Blood == 1:
            timer.Kill()
        else:
            timer.Enable()

#HOLLYWOOD: Sets Tommy at cafe
def SetTommy():
    tommy = Find("Tommy")
    state = __main__.FindPlayer().GetQuestState("Tommy")
    if tommy:
        if state == 1:
            tommy.ScriptUnhide()
            stuffs = Finds("tommy_table")
            for stuff in stuffs:
                stuff.ScriptUnhide()
        elif state == 2 or state == 3:
            tommy.Kill()
            stuffs = Finds("tommy_table")
            for stuff in stuffs:
                stuff.Kill()
        else:
            tommy.ScriptHide()

#HOLLYWOOD: Kills taxi if player is nosferatu
def SetTaxi():
    if __main__.IsClan(__main__.FindPlayer(), "Nosferatu"):
        logic = Find("logic_kill_taxi")
        if logic: logic.Trigger()
        map = Find("sewer_map")
        if map: map.Unlock()

#HOLLYWOOD: Cleans up after courier's death
def UnsetCourierBlood():
    if __main__.FindPlayer().GetQuestState("Courier") > 4:
        bloods = Finds("courier_blood")
        for blood in bloods:
            blood.Kill()
        arm = Find("courier_arm")
        if arm: arm.Kill()

#HOLLYWOOD: Places NPCs
def SetNPCs():
    sweeperPlacement()
    SetSamantha()
    SetCourier()
    SetAnonCaller()
    SetTommy()
    SetTaxi()
    UnsetCourierBlood()

#HOLLYWOOD: On Tommy's death, set quest state, changed by wesp
def OnTommyDeath():
    pc = __main__.FindPlayer()
    if pc.GetQuestState("Tommy") > 0:
        pc.SetQuest("Tommy", 3)
        G.Tommy_Review = 2
        G.Tommy_Disgusted = 0
        G.Tommy_Hostile = 0
        G.Tommy_Fail = 0

#HOLLYWOOD: Change sam's interesting places
def SetSamBusIPs():
    ips = Finds("ip_sam_phone")
    for ip in ips:
        ip.Disable()
    ips = Finds("ip_sam_bus")
    for ip in ips:
        ip.Enable()

#HOLLYWOOD: On sam's dialogue, check flags
def OnSamEndDialog():
    sam = Find("Samantha")
    sam.UseInteresting(1)
    if G.Samantha_Phone == 0:
        SetSamBusIPs()

    if G.Samantha_Dominated or G.Samantha_Dementated or G.Samantha_Persuaded or G.Samantha_Threat:
        sam.WillTalk(0)
        G.Samantha_Stopped = 1

#HOLLYWOOD: Use right sam float for player
def PlaySamCall():
#    sam = Find("Samantha")
    if __main__.FindPlayer().IsMale():
#        sam.PlayDialogFile("Character/dlg/Hollywood/Samantha/line151_col_e.mp3")
        logic = Find("sound_sam_call_m")
        logic.Start()
    else:
#        sam.PlayDialogFile("Character/dlg/Hollywood/Samantha/line151_col_f.mp3")
        logic = Find("sound_sam_call_f")
        logic.Start()

#HOLLYWOOD: Stop right sam float for player
def StopSamCall():
    if not G.Samantha_Stopped:
        if __main__.FindPlayer().IsMale():
            sound = Find("sound_sam_call_m")
            sound.Cancel()
        else:
            sound = Find("sound_sam_call_f")
            sound.Cancel()
        SetSamBusIPs()
        G.Samantha_Stopped = 1
        if not G.Samantha_FinishedCall:
            __main__.FindPlayer().ChangeMasqueradeLevel(-1)
            logic = Find("logic_sam_masq")
            if logic: logic.Kill()
        sam = Find("Samantha")
        if sam: sam.WillTalk(0)

#HOLLYWOOD: If player leaves map before stopping samantha, player gets masquerade violation
def CheckSamMasqViolation():
    if G.Samantha_Phone and not G.Samantha_Stopped:
        __main__.FindPlayer().ChangeMasqueradeLevel(1)
        logic = Find("logic_sam_masq")
        if logic: logic.Kill()
        sam = Find("Samantha")
        if sam: sam.Kill()

#HOLLYWOOD: Set sam post-call behavior
def SetSamPostCall():
    sam = Find("Samantha")
    if sam:
        if not G.Samantha_Stopped:
            sam.SetFollowerBoss("!player")
            __main__.FindPlayer().ChangeMasqueradeLevel(1)
            logic = Find("logic_sam_masq")
            if logic: logic.Kill()
            ips = Finds("ip_sam_phone")
            for ip in ips:
                ip.Kill()
            if sam: sam.WillTalk(1)
            G.Samantha_FinishedCall = 1
        else:
            SetSamBusIPs()

#TAWNIS PLACE: Checks to see if all cameras have been placed, changed by wesp
def placeCam():
    pc = __main__.FindPlayer()
    if ( pc.HasItem( "item_g_wireless_camera_1" ) ):
        pc.RemoveItem( "item_g_wireless_camera_1" )
    if G.Tawni_Spotted == 0:
        G.Imalia_Cam = G.Imalia_Cam + 1
        if G.Imalia_Cam == 3:
            __main__.FindPlayer().SetQuest("Imalia", 2)

#TAWNIS PLACE: Advance quest to state after activating cams, changed by wesp

def setSpotted():
    if (G.Imalia_Quest > 0 and G.Imalia_Quest < 4):
        G.Tawni_Spotted = 1
        __main__.FindPlayer().SetQuest("Imalia", 7)

def setComp():
    __main__.FindPlayer().SetQuest("Imalia", 3)
    G.Imalia_Quest = 3

def setTawniDead():
    __main__.FindPlayer().SetQuest("Imalia", 4)
    G.Tawni_Dead = 1

# ROMERO PROSTITUTE: Unfinished Ho rest prostitute unless going to cemetery (on trig change level), changed by wesp, RobinHood70
def unfinishedHo( s = "") :
    print ( "*************** Reseting Prostitutes ***************" )
    pc = __main__.FindPlayer()
    if ( s == "cemetery" and G.Romero_Whore == 2 ):
        prostitutes = Finds("Prostitute_*")
        for prostitute in prostitutes:
            if(prostitute.classname != "filter_activator_name"):
                if ( prostitute.IsFollowerOf( pc )):
                    if ( "models/character/npc/common/prostitute/prostitute_1/prostitute_1.mdl" == prostitute.GetModelName() ):
                        print ( "**************************** Is Blond ***********************************" )
                        G.Blondie = 1
                    else:
                        print ( "**************************** Is Not Blond ***********************************" )
                prostitute.SetFollowerBoss( "" )

print "hollywood levelscript loaded"
