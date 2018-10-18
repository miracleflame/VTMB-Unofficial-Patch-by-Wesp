print "loading tutorial level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName
FindPlayer = __main__.FindPlayer
IsClan = __main__.IsClan

G_tut = {}      # version of G saved for reset

popuppath = "vdata/Signs/tutorial_popup_"
cAnimalism1 = 0x0001
cAnimalism2 = 0x0002
cAuspex = 0x0004
cCelerity = 0x0008
cDementation1 = 0x0010
cDementation2 = 0x0020
cDominate1 = 0x0040
cDominate2 = 0x0080
cFortitude = 0x0100
cObfuscate = 0x0200
cPotence = 0x0400
cPresence = 0x0800
cProtean = 0x1000
cThaumaturgy1 = 0x2000
cThaumaturgy2 = 0x4000
cBloodBuff = 0x8000

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#TUTORIAL: Jack to different reset points
statemap = {0:'logic_reset_very_beginning',
            1:'logic_reset_blueblood',
            2:'logic_reset_chopshop_door',
            4:'logic_reset_lockpick',
            5:'logic_reset_hack',
#            5:'logic_reset_back_alley',
            18:'logic_reset_back_alley',
            6:'logic_reset_bum',
            7:'logic_reset_rat',
            8:'logic_reset_sneak',
            9:'logic_reset_unarmed',
            11:'logic_reset_melee',     # stealth guy
            12:'logic_reset_disc1',
            13:'logic_reset_physics',
            14:'logic_reset_firearms',
            15:'logic_reset_disc2',
            16:'logic_reset_disc3'}

def DialogPostProcess():
    if not G_tut.has_key('Tut_Jack'):
        saveState()
    elif G_tut['Tut_Jack'] != G.Tut_Jack:
        saveState()

#    popup = Find("signcounter")     # 1 - 16
#    popup.SetValue(0)
#    popup2 = Find("signcounter2")   # 17 - 32
#    popup2.SetValue(0)
#    popup3 = Find("signcounter3")   # 33 - 48
#    popup3.SetValue(0)
#    popup4 = Find("signcounter4")   # 49 - 64
#    popup4.SetValue(0)
#
    # player skips tutorial
    if (G.Tut_Jack == 0):
        jack = Find("Jack")
        jack.WillTalk(0)
        #changes made by dan_upright 29/11/04 and wesp
        G.Story_State = -2
    #  G.Jack_Faction = G.Jack_Faction + 1
        pc = __main__.FindPlayer()
        if pc:
            pc.SetQuest("Tutorial",1)
    #      pc.GiveItem("item_w_thirtyeight")
    #      pc.GiveItem("item_g_lockpick")
            pc.MakePlayerKillable()
        __main__.ChangeMap(2.5, "newgame", "trig_leave_tutorial")
        #changes end

    # the first time
    elif (G.Tut_Jack == 1 and G.Tutorial_Blueblood == 0 and G.Tutorial_Feeding == 0):
#        popup.SetValue(2)
#        popup = Find("popup_2")
#        popup.OpenWindow()
        Find("popup_2").OpenWindow()
        ip = Find("ip_lean_1")
        if ip: ip.Kill()
        ip = Find("ip_0b2")
        if ip: ip.Enable()
        trig = Find("trig_off_porch")
        if trig: trig.Kill()
        G.Tutorial_Feeding = 1 

    # outside the chopshop door, after the blueblood
    elif (G.Tut_Jack == 2 and G.Tutorial_Blueblood == 1):
        script = Find("script_1b")
        if script: script.BeginSequence()
        door = Find("tutchopdoora")
        door.Unlock()
        trig = Find("trig_popup_use")
        trig.Enable()

    # chopshop hall, before scripted event
    elif G.Tut_Jack == 3:
#        logic = Find("logic_raid_start_2")
        logic = Find("logic_scene_1")
        logic.Trigger()

    # in the chopshop, side hall by the windows, after scripted event
    elif G.Tut_Jack == 4:
        script = Find("script_2c")
        if script: script.BeginSequence()
        popup = Find("popup_11")
        popup.OpenWindow()

    # inside chopshop office, after jack jumps through window
    elif (G.Tut_Jack == 5 and G.Tut_Officedoor == 1):
        popup = Find("popup_14")
        popup.OpenWindow()

    # inside chopshop, got the key, leaves safe ui
    elif G.Tut_Jack == 18:
        popup = Find("popup_21")
        popup.OpenWindow()

    # two sabbat killed, before feeding on bum
    elif G.Tut_Jack == 6 and G.Tutorial_Bum == 0:
        player = FindPlayer()

    # after bum feeding, before rat feeding
    elif G.Tut_Jack == 7 and G.Tutorial_Bum == 1:
        player = FindPlayer()
        if IsClan(player, "Nosferatu"):
            popup = Find("popup_26")
            popup.OpenWindow()
        else:
            popup = Find("popup_25")
            popup.OpenWindow()

    # outside gate to thug, after feeding on bum, after rats
    elif (G.Tut_Jack == 8 and G.Tutorial_Bum == 1):
        script = Find("script_4d")
        script.BeginSequence()
        door = Find("tutalleydoora")
        door.Unlock()
        popup = Find("popup_27")
        popup.OpenWindow()

    # inside warehouse area, after sneaking in, before unarmed combat
    elif G.Tut_Jack == 9 and G.Tut_Aggfeed == 0:
        door = Find("door_garage")
        door.Open()
        script = Find("script_5b")
        if script: script.BeginSequence()
        popup = Find("popup_30")
        popup.OpenWindow()

    # thug killed, jack in front of bathroom door
    elif G.Tut_Jack == 11 and G.Tut_Melee == 0:
        door = Find("tutwareportal01")
        door.Unlock()

    # melee done, about to enter stealth room
    elif G.Tut_Jack == 12 and G.Tut_Stealthkill == 0:
        door = Find("tutwareportal03")
        door.Unlock()
        logic = Find("logic_enable_in_melee")
        logic.Enable()
        trig = Find("trig_popup_buff")
        trig.Enable()

    # stealth killed, about to enter physics room
    elif G.Tut_Jack == 13:
        door = Find("tutwareportal04")
        door.Unlock()
        logic = Find("logic_enable_in_stealth")
        logic.Enable()

    # jack hands gun, changed by wesp
    elif G.Tut_Jack == 14:
        if G.Tut_Gun == 0:
            Find("popup_45").OpenWindow()
            G.Tut_Gun = 1
        if G.Jack_Ammo == 0:
            G.Jack_Ammo = 1
            pc = FindPlayer()
            pc.GiveAmmo("item_w_thirtyeight", 12)

    # end of tutorial, changed by wesp
    elif G.Tut_Jack >= 15:
        __main__.ScheduleTask(5, "__main__.FindEntityByName(\'popup_58\').OpenWindow()")
#        Find("popup_58").OpenWindow()
        __main__.ScheduleTask(2, "__main__.FindEntityByName(\"end_fade\").Fade()")
        jack = Find("Jack")
        jack.WillTalk(0)

#TUTORIAL: Set clan-specific popups
def SetPassivePopup(disc, popup, popup2, popupfail):
    popup.ChangeFile(popuppath + disc + "1.txt")
    popup2.ChangeFile(popuppath + disc + "2.txt")
    SetDiscFailurePopup(disc, 1, popupfail)

def SetActivePopup(disc, level, popup, popup2, popupfail):
    popup.ChangeFile(popuppath + disc + "1.txt")
    if level == 1:
        popup2.ChangeFile(popuppath + disc + "2.txt")
    else:
        popup2.ChangeFile(popuppath + disc + "3.txt")
    SetDiscFailurePopup(disc, level, popupfail)

def SetDiscFailurePopup(disc, level, popup):
    if level == 1:
        popup.ChangeFile(popuppath + "fail_" + disc + "_1.txt")
    else:
        popup.ChangeFile(popuppath + "fail_" + disc + "_2.txt")

# special case
def SetObfuscatePopup(level, popup, popup2, popupfail):
    if level == 1:
        popup.ChangeFile(popuppath + "obfuscate1.txt")
        popup2.ChangeFile(popuppath + "obfuscate2.txt")
    else:
        popup.ChangeFile(popuppath + "obfuscate3.txt")
        popup2.ChangeFile(popuppath + "obfuscate4.txt")
    SetDiscFailurePopup("obfuscate", 1, popupfail)

# set file for clan specific popups
def SetClanPopups():
    popupclan = Find("popup_37")
    popupdisc1 = Find("popup_38")
    popupdisc12 = Find("popup_39")
    popupdisc2 = Find("popup_40")
    popupdisc22 = Find("popup_41")
    popupdisc3 = Find("popup_42")
    popupdisc32 = Find("popup_43")
    popupdisc1fail = Find("popup_55")
    popupdisc2fail = Find("popup_54")
    popupdisc3fail = Find("popup_51")
    player = FindPlayer()
    if IsClan(player, "Brujah"):
        popupclan.ChangeFile(popuppath + "brujahdisc1.txt")
        SetPassivePopup("presence", popupdisc1, popupdisc12, popupdisc1fail)
        SetPassivePopup("potence", popupdisc2, popupdisc22, popupdisc2fail)
        SetPassivePopup("celerity", popupdisc3, popupdisc32, popupdisc3fail)
        SetKillDisc3()
    elif IsClan(player, "Gangrel"):
        popupclan.ChangeFile(popuppath + "gangreldisc1.txt")
        SetPassivePopup("fortitude", popupdisc1, popupdisc12, popupdisc1fail)
        SetActivePopup("protean", player.base_protean, popupdisc2, popupdisc22, popupdisc2fail)
        SetActivePopup("animalism", player.base_animalism, popupdisc3, popupdisc32, popupdisc3fail)
        if player.base_animalism >= 2:
            SetKillDisc3()
    elif IsClan(player, "Malkavian"):
        popupclan.ChangeFile(popuppath + "malkaviandisc1.txt")
        SetPassivePopup("auspex", popupdisc1, popupdisc12, popupdisc1fail)
        SetObfuscatePopup(player.base_obfuscate, popupdisc2, popupdisc22, popupdisc2fail)
        SetActivePopup("dementation", player.base_dementation, popupdisc3, popupdisc32, popupdisc3fail)
        SetObfuscateDisc2()
        if player.base_dementation >= 2:
            SetKillDisc3()
        popup = Find("popup_59")
        popup.ChangeFile(popuppath + "dialogue_dementate.txt")
    elif IsClan(player, "Nosferatu"):
        popupclan.ChangeFile(popuppath + "nosferatudisc1.txt")
        SetPassivePopup("potence", popupdisc1, popupdisc12, popupdisc1fail)
        SetObfuscatePopup(player.base_obfuscate, popupdisc2, popupdisc22, popupdisc2fail)
        SetActivePopup("animalism", player.base_animalism, popupdisc3, popupdisc32, popupdisc3fail)
        SetObfuscateDisc2()
        if player.base_animalism >= 2:
            SetKillDisc3()
        popup = Find("popup_59")
        popup.ChangeFile(popuppath + "dialogue_nosferatu.txt")
    elif IsClan(player, "Toreador"):
        popupclan.ChangeFile(popuppath + "toreadordisc1.txt")
        SetPassivePopup("auspex", popupdisc1, popupdisc12, popupdisc1fail)
        SetPassivePopup("presence", popupdisc2, popupdisc22, popupdisc2fail)
        SetPassivePopup("celerity", popupdisc3, popupdisc32, popupdisc3fail)
        SetKillDisc3()
    elif IsClan(player, "Tremere"):
        popupclan.ChangeFile(popuppath + "tremeredisc1.txt")
        SetPassivePopup("auspex", popupdisc1, popupdisc12, popupdisc1fail)
        SetActivePopup("thaumaturgy", player.base_thaumaturgy, popupdisc2, popupdisc22, popupdisc2fail)
        SetActivePopup("dominate", player.base_dominate, popupdisc3, popupdisc32, popupdisc3fail)
        if G.Patch_Plus == 1:
            popup = Find("popup_59")
            popup.ChangeFile(popuppath + "dialogue_dominate.txt")
        if player.base_dominate >= 2:
            SetKillDisc3()
    else:  # "Ventrue"
        popupclan.ChangeFile(popuppath + "ventruedisc1.txt")
        SetPassivePopup("fortitude", popupdisc1, popupdisc12, popupdisc1fail)
        SetPassivePopup("presence", popupdisc2, popupdisc22, popupdisc2fail)
        SetActivePopup("dominate", player.base_dominate, popupdisc3, popupdisc32, popupdisc3fail)
        if player.base_dominate >= 2:
            SetKillDisc3()
        popup = Find("popup_59")
        popup.ChangeFile(popuppath + "dialogue_dominate.txt")

#TUTORIAL: Leave tutorial with pretty fade, changed by wesp
def LeaveTutorial():
    G.Story_State = -2
    __main__.ChangeMap(2.5, "newgame", "trig_leave_tutorial")
    pc = Find("pc_0")
    if pc: pc.MakePlayerKillable()

def LeaveTutorialShort():
    G.Story_State = -2
    __main__.ChangeMap(2.5, "newgame", "trig_leave_tutorial_short")
    pc = Find("pc_0")
    if pc: pc.MakePlayerKillable()

#TUTORIAL: After killing blueblood
def OnBluebloodDeath():
    if G.Tut_Jack == 1:
        logic = Find("logic_failed_blueblood")
        logic.Trigger()
    else:
        FindPlayer().HumanityAdd(-1)

#TUTORIAL: Sounds sabbat make before entering the chopshop (called in dialogue)
def OnPreRaidSounds():
    sound = Find("logic_sound_1")
    sound.Trigger()
    fire = Find("fire_behind_gate")
    fire.TurnOn()

#TUTORIAL: Jack ports away from chopshop door to check things out
def jackflashChopshopDoor():
    if int(FindPlayer().GetAngles()[1]) in range(-135, 45):
        logic = Find("logic_jackflash_chopshop_door")
        logic.Trigger()
        trig = Find("trig_port_chopshop_door")
        trig.Disable()

#TUTORIAL: Come here... stay away from the window...
def OnJackFloat():
    jack = Find("Jack")
    jack.PlayDialogFile("Character/dlg/MAIN CHARACTERS/jack_tutorial/line251_col_e.mp3")

#TUTORIAL: After the masquerade pop-up in the chopshop office
def OnMasqueradeEnd():
    if IsClan(FindPlayer(), "Nosferatu"):
        popup = Find("popup_24")
        popup.OpenWindow()
    else:
        popup = Find("popup_15")
        popup.OpenWindow()

    trig = Find("trig_popup_masquerade")
    trig.Enable()

#TUTORIAL: Use the key in the door popup
def OnSafeEnd():
    if G.Tut_Key == 1 and G.Tut_Jack == 5:
        Jack = Find("Jack")
        Jack.StartPlayerDialog(128)

#TUTORIAL: Jack teleports away while in chopshop office
def jackflashChopshopOffice():
    if int(FindPlayer().GetAngles()[1]) in range(45, 135):
        logic = Find("logic_jack_teleport_3")
        logic.Trigger()
        trig = Find("trig_jack_teleport_3")
        trig.Disable()

#TUTORIAL: Check if player needs ventrue feeding popup
def OnPopupFrenzy():
    if IsClan(FindPlayer(), "Ventrue"):
        Find("popup_60").OpenWindow()
        trig = Find("trig_popup_frenzy2")
        if trig: trig.Enable()
    else:
        trig = Find("trig_popup_frenzy2")
        if trig: trig.Kill()

#TUTORIAL: After killing bum
def OnBumDeath():
    if G.Tut_Jack == 6:
        logic = Find("logic_failed_bum")
        logic.Trigger()
    else:
        FindPlayer().HumanityAdd(-1)

#TUTORIAL: Spawn two guys if two blood points, changed by wesp
def OnDiscGuys():
    player = FindPlayer()
    if (IsClan(player, "Tremere") and player.base_thaumaturgy > 1):
        makers = Finds("disc2_maker")
        for maker in makers:
            maker.ScriptUnhide()
        counter = Find("disc2_count_2")
        counter.ScriptUnhide()
        counter = Find("disc2_count_1")
        counter.ScriptHide()
        print 'spawning two guys in room 2'

    if not(IsClan(player, "Brujah")) and not(IsClan(player, "Toreador")):
        if player.base_dementation > 1 or player.base_dominate > 1:
            makers = Finds("disc3_maker")
            for maker in makers:
                maker.ScriptUnhide()
            counter = Find("disc3_count_2")
            counter.ScriptUnhide()
            counter = Find("disc3_count_1")
            counter.ScriptHide()
            print 'spawning two guys in room disc3'

def UnlockDoorDisc1():
    logic = Find("logic_7")
    logic.Trigger()

def OnKillDisc1():
    print 'onkilldisc1'
    player = FindPlayer()
    if IsClan(player, "Brujah") and (G.Tutorial_Discflags & cPresence):
        UnlockDoorDisc1()
    elif (IsClan(player, "Gangrel") or IsClan(player, "Ventrue")) \
         and (G.Tutorial_Discflags & cFortitude):
        UnlockDoorDisc1()
    elif IsClan(player, "Nosferatu") and (G.Tutorial_Discflags & cPotence):
        UnlockDoorDisc1()
    elif (IsClan(player, "Malkavian") or IsClan(player, "Toreador") or IsClan(player, "Tremere")) \
        and (G.Tutorial_Discflags & cAuspex):
        UnlockDoorDisc1()
    else:
        logic = Find("logic_disc1_nodisc")
        logic.Trigger()

def SetObfuscateDisc2():
    logic = Find("logic_disc2_found")
    logic.Enable()
    UnlockDoorDisc2()

def UnlockDoorDisc2():
    door = Find("anotherfuckingtutorialdoor")
    door.Unlock()

# check whatever if disc2 guy(s) killed
def OnKillDisc2():
    print 'onkilldisc2'
    player = FindPlayer()
    if IsClan(player, "Brujah") and (G.Tutorial_Discflags & cPotence):
        UnlockDoorDisc2()
    elif (IsClan(player, "Toreador") or IsClan(player, "Ventrue")) \
        and (G.Tutorial_Discflags & cPresence):
            UnlockDoorDisc2()
    elif IsClan(player, "Gangrel") and (G.Tutorial_Discflags & cProtean):
        UnlockDoorDisc2()
    elif IsClan(player, "Tremere") \
         and player.base_thaumaturgy == 1 and (G.Tutorial_Discflags & cThaumaturgy1):
        UnlockDoorDisc2()
    elif IsClan(player, "Tremere") \
         and player.base_thaumaturgy >= 2 and (G.Tutorial_Discflags & cThaumaturgy2):
        UnlockDoorDisc2()
    elif (IsClan(player, "Malkavian") or IsClan(player, "Nosferatu")) \
         and ( G.Tutorial_Discflags & cObfuscate ):
        "do not have to do anything... yet"
    else:
        logic = Find("logic_disc2_nodisc")
        logic.Trigger()

def OnOpenDoorDisc2():
    player = FindPlayer()
    if ( IsClan(player, "Malkavian") or IsClan(player, "Nosferatu") ) \
         and not ( G.Tutorial_Discflags & cObfuscate ) :
        logic = Find("logic_disc2_nodisc")
        logic.Trigger()
    else:
        logic = Find("logic_check_disc2")
        logic.Disable()

def SetKillDisc3():
    door = Find("yetanotherfuckingdoor")
    door.Lock()
    logic = Find("logic_disc3_found")
    logic.Disable()

def UnlockDoorDisc3():
    door = Find("yetanotherfuckingdoor")
    door.Unlock()
#    logic = Find("logic_check_disc3")
#    logic.Trigger()

def OnOpenDoorDisc3():
    if not UsedDisc3():
        Find("popup_51").OpenWindow()
    else:
        logic = Find("logic_check_disc3")
        logic.Disable()

def OnKillDisc3():
    if UsedDisc3():
        UnlockDoorDisc3()
        logic = Find("logic_check_disc3")
        logic.Disable()
    else:
        Find("popup_51").OpenWindow()

def UsedDisc3():
    player = FindPlayer()
    if IsClan(player, "Malkavian") \
         and player.base_dementation == 1 and (G.Tutorial_Discflags & cDementation1):
        return 1
    elif IsClan(player, "Malkavian") \
         and player.base_dementation >= 2 and (G.Tutorial_Discflags & cDementation2):
        return 1
    elif (IsClan(player, "Toreador") or IsClan(player, "Brujah")) \
       and (G.Tutorial_Discflags & cCelerity):
        return 1
    elif (IsClan(player, "Gangrel") or IsClan(player, "Nosferatu")) \
         and player.base_animalism == 1 and (G.Tutorial_Discflags & cAnimalism1):
        return 1
    elif (IsClan(player, "Gangrel") or IsClan(player, "Nosferatu")) \
         and player.base_animalism >= 2 and (G.Tutorial_Discflags & cAnimalism2):
        return 1
    elif (IsClan(player, "Tremere") or IsClan(player, "Ventrue")) \
         and player.base_dominate == 1 and (G.Tutorial_Discflags & cDominate1):
        return 1
    elif (IsClan(player, "Tremere") or IsClan(player, "Ventrue")) \
         and player.base_dominate >= 2 and (G.Tutorial_Discflags & cDominate2):
        return 1
    else:
        return 0

#TUTORIAL: Respawn cans
def spawnCans():
    for i in range(1, 4):
        target = Find("can_target_%d" %i)
        can = __main__.CreateEntityNoSpawn("prop_physics", target.GetCenter(), target.GetAngles())
        can.SetName("can")
        can.SetModel("models/scenery/PHYSICS/sardine/sardine.mdl")
        __main__.CallEntitySpawn(can)

#TUTORIAL:  reset stuff
def saveState():
    ks = G.keys()
    for k in ks:
        G_tut[k] = G[k]

def resetState():
    teleport = Find(statemap[G.Tut_Jack])
    ks = G.keys()
    for k in ks:
        if not G_tut.has_key(k):
            G[k] = 0
        else:
            G[k] = G_tut[k]
    teleport.Trigger()
    player = FindPlayer()
    player.Bloodgain(10)
    player.ClearActiveDisciplines()

def ResetDiscBlood():
    player = FindPlayer()
    if player.bloodpool < 10:
        player.Bloodgain(15)
        player.Bloodloss(5)

def ResetBlood():
    player = FindPlayer()
    if player.bloodpool > 10:
        player.Bloodgain(15)
        player.Bloodloss(5)

# put lockpicks back on top of the box if player was idiot.
def spawnLockpicks():
    player = FindPlayer()
    if player.HasItem("item_g_lockpick"):
        player.RemoveItem("item_g_lockpick")
        node = Find("pt_lockpicks")
        center = node.GetCenter()
        key = __main__.CreateEntityNoSpawn("item_g_lockpick", center, (0,0,0) )
        __main__.CallEntitySpawn(key)

# put keycard back into safe if player was idiot.
def spawnKeycard():
    safe = Find("tutsafelock")
    safe.Lock()
    player = FindPlayer()
    if player.HasItem("item_k_tutorial_chopshop_stairs_key"):
        player.RemoveItem("item_k_tutorial_chopshop_stairs_key")
        safe.SpawnItemInContainer("item_k_tutorial_chopshop_stairs_key")

print "levelscript loaded"
