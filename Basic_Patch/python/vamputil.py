import nt
import __main__
import fileutil
from random import Random
from random import randint
from time import time
from string import atoi
from zvtool.zvtool import *

huntersDead = [0, 0, 0]

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

##############################################################################
# Unofficial Patch Functions
##############################################################################

#Switching between Basic and Plus patch, added by wesp

def setBasic():
    G  = __main__.G
    G.PP = 0
    G.Patch_Plus = 0
    G.Jack_Extra = 0
    G.Flynn_Extra = 0
    G.Extra_Lines = 0
    G.Linux_Wine = 1
    __main__.ccmd.detailfade=""
    __main__.ccmd.detaildist=""
    __main__.ccmd.clothes=""
    pc = __main__.FindPlayer()
    if not (pc.HasItem("item_w_fists")):
        pc.GiveItem("item_w_fists")
        pc.GiveItem("weapon_physcannon")
        pc.GiveItem("item_g_wallet")
        pc.GiveItem("item_g_keyring")
        pc.GiveItem("item_a_lt_cloth")
    if G.Patch_Plus == 0:
        print "Basic Patch"
        Find("idle_timer").Disable()
        musicplus = Find("music_plus")
        if musicplus: musicplus.StopSound()
        door = Find("phonographdoor")
        if door: door.Lock()
        backdoor = Find("reddrbckknob")
        if backdoor: backdoor.Unlock()
        doggate1 = Find("dog_gate1")
        if doggate1: doggate1.Unlock()
        doggate2 = Find("dog_gate2")
        if doggate2: doggate2.Unlock()
        door2knob1 = Find("nextdoor2knob1")
        if door2knob1:
            door2knob1.Unlock()
            door2knob2 = Find("nextdoor2knob2")
            door2knob2.Unlock()
        pad = Find("padlock")
        if pad: pad.Kill()
        gate = Find("gasstationgate")
        if gate and not (G.Tourette_Wins == 1 or G.Therese_Dead == 1 or G.Jeanette_Dead == 1): gate.Lock()
        axe = Find("wesp_axe")
        if axe: axe.ScriptUnhide()
        if axe: axe.Kill()
        axenode = Find("wesp_axenode")
        if axenode: axenode.ScriptUnhide()
        if axenode: axenode.Kill()
        miau = Find("plus_miau")
        if miau: miau.Kill()
        cammandarin = Find("cam_mandarin")
        if cammandarin:
            world = Find("world")
            world.SetSafeArea(0)
        heli1 = Find("plus_helisound1")
        if heli1: heli1.Kill()
        heli2 = Find("plus_helisound2")
        if heli2: heli2.Kill()
        blade = Find("wesp_blade")
        if blade: blade.Kill()
        bladenode = Find("wesp_bladenode")
        if bladenode: bladenode.Kill()
        bladebros = Find("ChangBrosBlade_basic")
        if bladebros and G.Chang_Swap == 0:
            bladebros.SetName("ChangBrosBlade")
            bladebrosplus = Find("ChangBrosBlade_plus")
            if bladebrosplus: bladebrosplus.Kill()
            clawbros = Find("Chang_basic")
            clawbros.SetName("Chang")
            clawbrosplus = Find("Chang_plus")
            if clawbrosplus: clawbrosplus.Kill()
            G.Chang_Swap = 1

def setPlus():
    G  = __main__.G
    G.PP = 1
    G.Patch_Plus = 1
    G.Jack_Extra = 1
    G.Flynn_Extra = 1
    G.Extra_Lines = 1
    G.Linux_Wine = 1
    __main__.ccmd.detailfade=""
    __main__.ccmd.detaildist=""
    __main__.ccmd.clothes=""
    if G.Player_Insane == 1:
        __main__.ccmd.ropestop=""
    pc = __main__.FindPlayer()
    if not (pc.HasItem("item_w_fists")):
        pc.GiveItem("item_w_fists")
        pc.GiveItem("weapon_physcannon")
        pc.GiveItem("item_g_wallet")
        pc.GiveItem("item_g_keyring")
        pc.GiveItem("item_a_lt_cloth")
    if (G.Vampire_Hunter == 0 and (pc.clan == 9 or pc.clan == 10 or pc.clan == 11)):
        print "Vampire to Hunter"
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\stats_hunter.txt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\stats.txt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\strings_hunter.txt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\strings.txt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\traiteffects000_hunter.txt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\traiteffects000.txt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\faith_heal.tth"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\bloodheal.tth"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\faith_heal.ttz"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\bloodheal.ttz"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\faith_heal_base.tth"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\bloodheal_base.tth"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\faith_heal_base.ttz"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\bloodheal_base.ttz"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\faith_bar.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\bloodbar.vmt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\faith_barbottom.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\bloodbarbottom.vmt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\faith_barfill.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\bloodbarfill.vmt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\faith_useglow.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\blooduseglow.vmt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\faith_useiconglow.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\blooduseiconglow.vmt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\bloodbar\\faith_bar.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\bloodbar\\bloodbar.vmt"
        fileutil.copyfile(src, dst)
        G.Vampire_Hunter = 1
    elif G.Vampire_Hunter == 1 and not (pc.clan == 9 or pc.clan == 10 or pc.clan == 11):
        print "Hunter to Vampire"
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\stats_vampire.txt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\stats.txt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\strings_vampire.txt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\strings.txt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\traiteffects000_vampire.txt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\vdata\\system\\traiteffects000.txt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\blood_heal.tth"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\bloodheal.tth"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\blood_heal.ttz"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\bloodheal.ttz"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\blood_heal_base.tth"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\bloodheal_base.tth"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\blood_heal_base.ttz"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\disciplines\\bloodheal_base.ttz"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\blood_bar.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\bloodbar.vmt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\blood_barbottom.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\bloodbarbottom.vmt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\blood_barfill.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\bloodbarfill.vmt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\blood_useglow.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\blooduseglow.vmt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\blood_useiconglow.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\blooduseiconglow.vmt"
        fileutil.copyfile(src, dst)
        src = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\bloodbar\\blood_bar.vmt"
        dst = fileutil.getcwd() + "\\" + fileutil.moddir + "\\materials\\hud\\new_ui\\bloodbar\\bloodbar.vmt"
        fileutil.copyfile(src, dst)
        G.Vampire_Hunter = 0
    if G.Patch_Plus == 1:
        print "Plus Patch"
        plus = __main__.FindEntitiesByName("plus_*")
        for p in plus:
            p.ScriptUnhide()
        basic = __main__.FindEntitiesByName("basic_*")
        for b in basic:
            b.ScriptHide()
        FixKeyBindings()
        IsIdling()
        G.No_Idle = 0
        musicbasic = Find("music_basic")
        if musicbasic:musicbasic.StopSound()
        cop = Find("Cop_Deck1_Guard2")
        if cop: cop.SetModel("models/character/npc/common/Cop_Variant/rookied_cop/Rookied_Cop.mdl")
        cop = Find("Cop_Deck3_Guard2")
        if cop: cop.SetModel("models/character/npc/common/Cop_Variant/rookied_cop/Rookied_Cop.mdl")
        cop = Find("Cop_Deck2_Guard2")
        if cop: cop.SetModel("models/character/npc/common/Cop_Variant/rookied_cop/Rookied_Cop.mdl")
        cop = Find("Cop_Deck4_Guard2")
        if cop: cop.SetModel("models/character/npc/common/Cop_Variant/rookied_cop/Rookied_Cop.mdl")
        cop = Find("Cop_Deck5_Guard")
        if cop: cop.SetModel("models/character/npc/common/Cop_Variant/rookied_cop/Rookied_Cop.mdl")
        cop = Find("Cop_Deck6_Guard2")
        if cop: cop.SetModel("models/character/npc/common/Cop_Variant/rookied_cop/Rookied_Cop.mdl")
        cop = Find("Cop_Deck4_Guard2")
        if cop: cop.SetModel("models/character/npc/common/Cop_Variant/rookied_cop/Rookied_Cop.mdl")
        cop = Find("Cop_Deck4_Guard3")
        if cop: cop.SetModel("models/character/npc/common/Cop_Variant/rookied_cop/Rookied_Cop.mdl")
        tong = Find("tong_sidekick_1")
        if tong: tong.SetModel("models/character/npc/unique/Chinatown/Tong_Leader/Tong_Leader.mdl")
        tong = Find("Tong_Floor2_Patrol")
        if tong: tong.SetModel("models/character/npc/unique/Chinatown/Tong_Leader/Tong_Leader.mdl")
        lasombra = Find("LaSombra")
        if lasombra: lasombra.SetModel("models/character/npc/common/doppleganger/doppleganger_female.mdl")
        lasombra = Find("LaSombra_2")
        if lasombra: lasombra.SetModel("models/character/npc/common/doppleganger/doppleganger_female.mdl")
        lasombra = Find("LaSombra_3")
        if lasombra: lasombra.SetModel("models/character/npc/common/doppleganger/doppleganger_female.mdl")
        shovel = Find("f2_m_potence_1")
        if shovel: shovel.SetModel("models/character/npc/common/Shovelhead/shovelhead_short.mdl")
        shovel = Find("f2_m_potence_2")
        if shovel: shovel.SetModel("models/character/npc/common/Shovelhead/shovelhead_short.mdl")
        shovel = Find("f1_m_potence_1")
        if shovel: shovel.SetModel("models/character/npc/common/Shovelhead/shovelhead_short.mdl")
        shovel = Find("f1_m_potence_2")
        if shovel: shovel.SetModel("models/character/npc/common/Shovelhead/shovelhead_short.mdl")
        shovel = Find("f3_m_potence_1")
        if shovel: shovel.SetModel("models/character/npc/common/Shovelhead/shovelhead_short.mdl")
        shovel = Find("f3_m_potence")
        if shovel: shovel.SetModel("models/character/npc/common/Shovelhead/shovelhead_short.mdl")
        nines = Find("Nines")
        if (G.Story_State == 115 and nines): nines.SetModel("models/character/npc/unique/Downtown/Nines/Nines_damagedw.mdl")
        flunky3 = Find("flunky3")
        if flunky3: flunky3.SetModel("models/character/npc/unique/Downtown/Damsel/Damsel.mdl")
        flunky4 = Find("flunky4")
        if flunky4: flunky4.SetModel("models/character/npc/unique/Downtown/Skelter/Skelter.mdl")
        flunky5 = Find("flunky5")
        if flunky5 and (IsDead("Sweeper")):
            if (IsClan(pc,"Toreador")): flunky5.SetModel("models/character/pc/male/gangrel/armor_1/Gangrel_Male_Armor_1.mdl")
            else: flunky5.SetModel("models/character/pc/male/toreador/armor1/Toreador_Male_Armor_1.mdl")
        flunky6 = Find("flunky6")
        if (flunky6 and G.Copper_Nines == 0):
            if (IsClan(pc,"Brujah")): flunky6.SetModel("models/character/pc/male/gangrel/armor_1/Gangrel_Male_Armor_1.mdl")
            else: flunky6.SetModel("models/character/pc/male/brujah/armor1/Brujah_Male_Armor_1.mdl")
        flunky7 = Find("flunky7")
        if (flunky7 and G.Killer_Nines == 0):
            if (IsClan(pc,"Malkavian")): flunky7.SetModel("models/character/pc/male/gangrel/armor_1/Gangrel_Male_Armor_1.mdl")
            else: flunky7.SetModel("models/character/pc/male/malkavian/armor1/Malkavian_Male_Armor_1.mdl")
        flunky8 = Find("flunky8")
        if flunky8 and (IsClan(pc,"Toreador") and not pc.IsMale()): flunky8.SetModel("models/character/pc/female/brujah/armor0/Brujah_Female_Armor_0.mdl")
        gargoyleguard = Find("gargoyleguard")
        if (gargoyleguard and G.Gargoyle_Convinced == 0):
            gargoyleguard.ScriptHide()
        clothes = Find("plus_clothing")
        condoms = Find("plus_condoms")
        if clothes and G.Player_Homo == 1:
            gender = pc.IsMale()
            if gender: clothes.ScriptHide()
            else: condoms.ScriptHide()
        box = Find("plus_cigarbox")
        if box: box.AddEntityToContainer("money_basic")
        stumpy = Find("stumpy")
        if (stumpy and G.Gimble_Dead == 1):
            stumpy.ScriptHide()
        tub = Find("plus_tub")
        if (tub and (G.Killer_Hostile > 0 or G.Killer_Freed > 0)):
            junkteleport = Find("JunkyardTeleport2")
            junkteleport.ScriptHide()
            junkdoor = Find("jnkshkb")
            junkdoor.Unlock()
        asianvamp = Find("AsianVamp")
        if asianvamp and G.Asian_Swap == 0:
            asianvamp.ScriptHide()
            asianvamp.SetName("AsianVamp_basic")
            asianvampplus = Find("AsianVamp_plus")
            asianvampplus.ScriptUnhide()
            asianvampplus.SetName("AsianVamp")
            G.Asian_Swap = 1
        copperremains = Find("wesp_copper")
        copperstake = Find("wesp_stake") 
        if (copperremains and G.Copper_Prince == 1 and G.Copper_Seen == 0):
            copperremains.ScriptUnhide()
            copperstake.ScriptUnhide()
            G.Copper_Seen = 1
        elif (G.Copper_Seen == 1):
            if copperremains: copperremains.Kill()
            if copperstake: copperstake.Kill()
        doll6 = Find("plus_Doll6")
        if doll6 and G.Doll6_Dead == 1:
            doll6.Kill()
        vendor = Find("Smoke_Vendor")
        if vendor and G.Vendor_Dead == 1:
            vendor.Kill()
        spotdoor = Find("redspotstorage")
        if spotdoor and G.Spot_Door == 0:
            knobs = __main__.FindEntitiesByName("dancer_door-doorknob")
            for knob in knobs:
                knob.Unlock()
            G.Spot_Door = 1
        locke = Find("Jezebel_Locke")
        if locke and G.Locke_Swap == 0:
            locke.ScriptHide()
            locke.SetName("Jezebel_Locke_basic")
            lockeplus = Find("Jezebel_Locke_plus")
            lockeplus.ScriptUnhide()
            lockeplus.SetName("Jezebel_Locke")
            G.Locke_Swap = 1
        bladebros = Find("ChangBrosBlade_plus")
        if bladebros and G.Chang_Swap == 0:
            bladebros.SetName("ChangBrosBlade")
            bladebrosbasic = Find("ChangBrosBlade_basic")
            if bladebrosbasic: bladebrosbasic.Kill()
            clawbros = Find("Chang_plus")
            clawbros.SetName("Chang")
            clawbrosbasic = Find("Chang_basic")
            if clawbrosbasic: clawbrosbasic.Kill()
            G.Chang_Swap = 1
        sarc = Find("sarc_plus")
        if sarc and G.Story_State >= 60:
            sarc.ScriptHide()
            sarcbasic = Find("sarc_basic")
            sarcbasic.ScriptHide()
        museumteleport = Find("museum_teleport")
        if museumteleport:
            museumcabbie = Find("cabbie")
            museumcabbie.WillTalk(0)
            doorfire = Find("door_fire")
            doorfire.Unlock()
            museumteleport = Find("museum_teleport")
            museumteleport.Enable()
            if G.Story_State >= 30:
                beckett = Find("Beckett")
                beckett.ScriptHide()
                if IsClan(pc,"Nosferatu"):
                    manholefake = Find("Manhole_Museum_Fake")
                    manhole = Find("Manhole_Museum")
                    manholefake.ScriptHide()
                    manhole.ScriptUnhide()
                else: museumcabbie.WillTalk(1)
        giovannimanhole = Find("Manhole_Giovanni")
        if giovannimanhole:
            giovannicabbie = Find("cabbie")
            giovannicabbie.WillTalk(0)
            if G.Story_State >= 60:
                if IsClan(pc,"Nosferatu"):
                    manholefake = Find("Manhole_Giovanni_Fake")
                    manhole = Find("Manhole_Giovanni")
                    manholefake.ScriptHide()
                    manhole.ScriptUnhide()
                else: giovannicabbie.WillTalk(1)
        shortcut = Find("shortcut_open")
        shortcut_off = Find("shortcut_closed")
        if G.Shortcut_Unlocked == 1:
            if shortcut: shortcut.ScriptUnhide()
            if shortcut_off: shortcut_off.ScriptHide()
        else:
            if shortcut: shortcut.ScriptHide()
            if shortcut_off: shortcut_off.ScriptUnhide()
        if G.Jumbles_Removed == 1 and G.LaSombra_Seen == 1 and G.Chinatown_Open == 1:
            G.Library_Ready = 1
        smokenote = Find("smoke_note")
        smokenotenode = Find("smoke_note_node")
        if G.Library_Smoke == 1:
            if smokenote: smokenote.ScriptUnhide()
            if smokenotenode: smokenotenode.ScriptUnhide()
        else:
            if smokenote: smokenote.ScriptHide()
            if smokenotenode: smokenotenode.ScriptHide()
        coffeedoor = Find("plus_coffee_door")
        if G.Library_Coffee > 0:
            if coffeedoor: coffeedoor.Unlock()
        else:
            if coffeedoor: coffeedoor.Lock()
        libraryopen = Find("library_open")
        libraryclosed = Find("library_closed")
        if G.Library_Open > 0:
            if libraryopen: libraryopen.ScriptUnhide()
            if libraryclosed: libraryclosed.ScriptHide()
        else:
            if libraryopen: libraryopen.ScriptHide()
            if libraryclosed: libraryclosed.ScriptUnhide()
        andrei = Find("Andrei")
        if andrei: andrei.ScriptHide()
        andreiplus = Find("plus_Andrei")
        if (andreiplus and G.Andrei_Talked == 1): andreiplus.ScriptHide()
        andreisabbat = Find("AndreiSabbat")
        if (andreisabbat and G.Player_Sabbat == 1):
            world = Find("world")
            world.SetSafeArea(2)
            andreisabbat.ScriptUnhide()
            triggertrap = Find("Trigger_Trap")
            triggertrap.ScriptHide()
        watchman = Find("watchman")
        if (watchman and G.LaSombra_Seen == 0):
            Find("watchman").ScriptUnhide()
            __main__.ScheduleTask(2.0, "__main__.FindEntityByName(\"teleport_sequence\").BeginSequence()")
            G.LaSombra_Seen = 1
        plus = __main__.FindEntitiesByName("plus_ChangCoffin*")
        n = 1
        #print "renaming"
        for b in plus:
            b.SetName("ChangCoffin%d"%n)
            n = n+1
        basic = __main__.FindEntitiesByName("basic_ChangCoffin*")
        n = 1
        #print "renaming"
        for b in basic:
            b.SetName("ChangCoffin%d"%n)
            n = n+1
        if (__main__.IsClan(__main__.FindPlayer(), "Malkavian") and G.Stop_Shake == 0 and G.Player_Insane == 0):
            G.Player_Malkavian = 1
            __main__.ccmd.ropeshake=""
        else:
            G.Stop_Shake = 0
            __main__.ccmd.ropestop=""
        events = __main__.FindEntityByName("events_player_plus")
        if events: events.EnableOutputs()

def unhidePlus():
    c  = __main__.ccmd
    c.patchtype=""

#609: Andrei intro for Tremere, added by EntenSchreck
def WhatIsThatSmell():
    pc = __main__.FindPlayer()
    clan = pc.clan
    if clan == 7:	#Tremere
        andrei = Find("plus_Andrei")
        andrei.PlayDialogFile("Character/dlg/hollywood/andrei/line5_col_e.mp3")

#609: Starts Dialog with Andrei while he's walking, added by EntenSchreck
def HelloYoungCainite():
    pc = __main__.FindPlayer()
    clan = pc.clan
    if clan == 7:	#Tremere
        andrei = Find("plus_Andrei")
        andrei.PlayDialogFile("Character/dlg/hollywood/andrei/line151_col_e.mp3")
    else:
        andrei = Find("plus_Andrei")
        andrei.PlayDialogFile("Character/dlg/hollywood/andrei/line11_col_e.mp3")

#BAILBONDS: Starts Arthurs monologue on the phone, added by wesp
def arthurPhones():
    if __main__.G.Arthur_Phoned == 0:
        arthur = Find("plus_Arthur")
        arthur.PlayDialogFile("character/dlg/santa monica/arthur/line1_col_e.mp3")
        __main__.G.Arthur_Phoned = 1

#CLINIC: Sets Heather quest states, added by wesp
def heatherQuest1():
    pc = __main__.FindPlayer()
    if __main__.G.Patch_Plus == 1:
        pc.SetQuest("Heather",1)
def heatherQuest2():
    pc = __main__.FindPlayer()
    if __main__.G.Patch_Plus == 1:
        pc.SetQuest("Heather",2)
def heatherQuest3():
    pc = __main__.FindPlayer()
    if __main__.G.Patch_Plus == 1:
        pc.SetQuest("Heather",3)

#CLINIC: Checks sneaking, added by wesp
def sneakTest():
    pc = __main__.FindPlayer()
    npc = __main__.Find("clinic_guard")
    pos1 = pc.GetOrigin()
    pos2 = npc.GetOrigin()
    if (__main__.G.Patch_Plus == 1 and ((pc.GetCenter()[2] - pc.GetOrigin()[2]) <= 18) and pc.CalcFeat("Sneaking") > 4 and distanceSquared(pos1, pos2) > 18000):
        return
    else:
        relay = __main__.Find("guard_warning")
        relay.Trigger()

#CLINIC: Sets Heather quest, added by wesp
def heatherSetQuest():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Heather")
    if (__main__.G.Patch_Plus == 1 and state == 1):
        __main__.G.Morgue_Heather = 1
        __main__.FindPlayer().SetQuest("Heather", 3)

#CLINIC: Updates Thin Blood quest, added by wesp
def freezerCode():
    pc = __main__.FindPlayer()
    if (__main__.G.Phil_Persuade == 0 and __main__.G.Phil_Drop == 0 and __main__.G.Phil_Code == 0):
        __main__.G.Phil_Code = 1
        pc.AwardExperience("Thinned05")

#CLINIC: Spawns Vandal blood pack, added by RobinHood70
def spawnVandalBlood():
    pc = __main__.FindPlayer()
    if (pc.AmmoCount("item_g_bluebloodpack") == 0):
        pc.GiveItem("item_g_bluebloodpack")
    elif (pc.AmmoCount("item_g_bluebloodpack") >= 10):
        vandal = Find("Vandal")
        center = vandal.GetCenter()
        point = (center[0], center[1], center[2] + 20)
        blood = __main__.CreateEntityNoSpawn("item_g_bluebloodpack", point, (0,0,0) )
        blood.SetName("vandal_blood")
        sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
        sparklies.SetParent("vandal_blood")
        __main__.CallEntitySpawn(blood)
        __main__.CallEntitySpawn(sparklies)
    else:
        pc.GiveAmmo("item_g_bluebloodpack",1)
        if __main__.G.Patch_Plus == 1:
            c  = __main__.ccmd
            c.showSpawn=""

#CLOUD: Chooses reward from Mr. Ox, added by wesp
def oxReward1():
    pc = __main__.FindPlayer()
    if __main__.G.Patch_Plus == 1:
        pc.GiveItem("item_p_occult_strength")
    else:
        pc.MoneyAdd(150)
def oxReward2():
    pc = __main__.FindPlayer()
    if __main__.G.Patch_Plus == 1:
        pc.GiveItem("item_p_occult_lockpicking")
    else:
        pc.MoneyAdd(250)

#DANA and DRAGON: cellphone and walkie_talkie, added by DDLullu
def SetCellUnhide():
    phone = __main__.Find("cell_hand")
    if phone: phone.ScriptUnhide()
def SetCellHide():
    phone = __main__.Find("cell_hand")
    if phone: phone.ScriptHide()

#DINER: talking to the thugs, added by wesp
def thugState():
    if (__main__.G.Thugs_Attack == 1):
        thug_1 = Find("assassin_e")
        thug_2 = Find("assassin_s")
        thug_3 = Find("assassin_w")
        thug_4 = Find("assassin_n")
        thug_1.SetRelationship("player D_HT 5")
        thug_2.SetRelationship("player D_HT 5")
        thug_3.SetRelationship("player D_HT 5")
        thug_4.SetRelationship("player D_HT 5")
    elif (__main__.G.Thugs_Peace == 1):
        thug_2 = Find("assassin_s")
        thug_2.WillTalk(0)
        trigger1 = Find("trigger_attack")
        trigger1.Disable()
        trigger2 = Find("go_attack")
        trigger2.Disable()
        __main__.thugsAllDead()

#DOWNTOWN: Get Beckett unstuck, added by wesp
def checkBeckettStuck():
    if (__main__.G.Beckett_Talk == 0):
        beckett = Find("Beckett")
        if beckett:
            org = __main__.FindPlayer().GetOrigin()
            rx = org[0] + 50
            beckett.SetOrigin((rx,org[1],org[2]))

#EMPIRE: Cardprinter, added by wesp
def cardPrinterEnablePlus():
    if (__main__.G.Hannah_Jezebel == 1 and __main__.G.Patch_Plus == 1):
        printer = Find("card_printer")
        printer.ScriptUnhide()

#EXHAUST PIPE: (un)Hide Nines gun, added by vladdmaster
def deagleNines():
    gun = Find("deagle")
    gun.ScriptUnhide()
    __main__.ScheduleTask(3.00, "__main__.Find(\"deagle\").ScriptHide()")

#GALLERY: Gives the player the money, added by wesp
def playerGotBox():
    pc = __main__.FindPlayer()
    if (__main__.G.Got_Cash == 0):
        __main__.G.Got_Cash = 1
        pc.MoneyAdd(250)
        box_spark = Find("box_sparklies")
        if box_spark: box_spark.ScriptHide()
        if (pc.humanity >= 6 and __main__.G.Charity_Know == 0):
            pc.HumanityAdd(-1)

#GIOVANNI MANSION 2: Feedback for killing Bruno, added by wesp
def brunoDeath():
    __main__.G.Bruno_Killed = 1
    pc = __main__.FindPlayer()
    status = __main__.FindPlayer().GetQuestState("Sarcophagus")
    if(status < 4):
        pc.SetQuest("Sarcophagus", 5)

#GIOVANNI MANSION 2: Spawns watch, added by wesp
def spawnWatch():
    pc = __main__.FindPlayer()
    if (pc.AmmoCount("item_g_watch_fancy") == 0):
        pc.GiveItem("item_g_watch_fancy")
    else:
        pc.GiveAmmo("item_g_watch_fancy",1)
        if __main__.G.Patch_Plus == 1:
            c  = __main__.ccmd
            c.showSpawn=""

#GIOVANNI MANSION 2: Spawns ring, added by wesp
def spawnGold():
    pc = __main__.FindPlayer()
    if (pc.AmmoCount("item_g_ring_gold") == 0):
        pc.GiveItem("item_g_ring_gold")
    else:
        pc.GiveAmmo("item_g_ring_gold",1)
        if __main__.G.Patch_Plus == 1:
            c  = __main__.ccmd
            c.showSpawn=""

#GIOVANNI MANSION 3: Keep door open, added by wesp
def changeLevelCheck():
    map2a = Find("giovanni_2a")
    map2b = Find("giovanni_2b")
    if (__main__.G.BeenToGioParty == 1 and not (__main__.G.GioBotchedOutside == 1 or __main__.G.GioBotchedInside == 1) ):
        map2b.Disable()
        map2a.Enable()
        print "2b disabled"
    else:
        map2a.Disable()
        map2b.Enable()
        print "2a disabled"
    if (__main__.G.Nadia_Fright == 1):
        print ( "********* cleaning up *************" )
        door = Find("door_fake")
        door.ScriptHide()
        block = Find("door_block")
        block.ScriptHide()
        float = Find("Nadia_Motioning1")
        float.ScriptHide()
        float = Find("choreo_thisway")
        float.ScriptHide()
        float = Find("choreo_comon")
        float.ScriptHide()
        Nadia = Find("Nadia")
        Nadia.ScriptHide()
    else:
        door = Find("door_fake")
        door.ScriptUnhide()
        block = Find("door_block")
        block.ScriptUnhide()

#HALLOWBROOK HOTEL: Changes Models of the Spiderchicks, added by EntenSchreck
def MabelleneModel():
    M = Find("Mabellene I Hofteholder")
    M.SetModel("models/character/monster/tzimisce/creation1/creation1_full.mdl")
    Mcenter = M.GetOrigin()
    Mpoint = (Mcenter[0], Mcenter[1], Mcenter[2] + 20)
    M.SetOrigin(Mpoint)
def EvelynModel():
    E = Find("Evelyn")
    E.SetModel("models/character/monster/tzimisce/creation1/creation1_full.mdl")
    Ecenter = E.GetOrigin()
    Epoint = (Ecenter[0], Ecenter[1], Ecenter[2] + 20)
    E.SetOrigin(Epoint)

#HALLOWBROOK HOTEL: Changes firemage gender, added by wesp
def genderTremere():
    pc = __main__.FindPlayer()
    gender = pc.IsMale()
    clan = pc.clan
    mage = Find("Tremere_FireMage")
    female_mage = Find("Tremere_FireMage_Female")
    if (gender == 1 and clan == 7):
        female_mage.ScriptUnhide()
    else:
        mage.ScriptUnhide()

#HAVEN: Used to trigger library quest log, added by wesp
def librarySetQuest():
    pc = __main__.FindPlayer()
    if (__main__.G.Library_Smoke == 0):
        pc.SetQuest("Library", 1)
        __main__.G.Library_Smoke = 1
    if (__main__.G.Library_Smoke == 2):
        pc.SetQuest("Library", 2)
        __main__.G.Library_Note = 1
        __main__.G.Library_Smoke = 3
    if (__main__.G.Library_Note == 2):
        pc.SetQuest("Library", 3)
        __main__.G.Library_Coffee = 1
        __main__.G.Library_Note = 3
    if (__main__.G.Library_Coffee == 2 and __main__.G.Library_Open == 0):
        pc.SetQuest("Library", 4)
        __main__.G.Library_Open = 1
        __main__.G.Library_Coffee = 3
    if (__main__.G.Library_Open == 2):
        if (__main__.G.Guard1_Killed == 0 and __main__.G.Guard2_Killed == 0):
            __main__.FindPlayer().AwardExperience("Library02")

#HAVEN: Used to give silver ring, added by wesp
def spawnRing():
    pc = __main__.FindPlayer()
    if (pc.AmmoCount("item_g_ring_silver") == 0):
        pc.GiveItem("item_g_ring_silver")
    else:
        pc.GiveAmmo("item_g_ring_silver",1)
        if __main__.G.Patch_Plus == 1:
            c  = __main__.ccmd
            c.showSpawn=""

#HOSPITAL: Called to unhide the business card, added by wesp
def milliganCard():
    world = Find("world")
    world.SetSafeArea(2)
    if (not __main__.IsDead("Milligan")):
        card = Find("card")
        if card: card.ScriptUnhide()
        sparklies = Find("card_sparklies")
        if sparklies: sparklies.ScriptUnhide()

#HOSPITAL: Called when Pisha leaves, added by wesp
def pishaGone():
    if (__main__.G.Pisha_Know > 0 and __main__.G.Pisha_Corpse == 0):
        corpse = Find("corpse1")
        if corpse: corpse.Kill()
        __main__.G.Pisha_Corpse = 1 
    if (__main__.G.Story_State >= 85 and __main__.G.Pisha_Know > 0 and not __main__.IsDead("Pisha")):
        pisha = Find("Pisha")
        if pisha: pisha.Kill()
        book = Find("book")
        if book: book.Kill()

#JEWELRY: Isaac gift, added by wesp
def IsaacGift():
    if (__main__.G.Isaac_Gift == 1):
        __main__.G.Isaac_Gift = 2

#KAMIKAZE ZEN: Turns timer off and light on, added by wesp
def checkTimer():
    timer = Find("virus_timer")
    power = Find("poweron")
    if (__main__.G.Shubs_Act == 4):
        power.Trigger()
        if timer: timer.Hide()

#LIBRARY: Removing vacuum tube box and library card, added by wesp
def useBox():
    pc = __main__.FindPlayer()
    if (pc.HasItem("item_w_claws_protean5")):
        pc.RemoveItem("item_w_claws_protean5")
        pc.SetQuest("Library", 5)
def useCard():
    pc = __main__.FindPlayer()
    if (pc.HasItem("item_w_claws_protean4")):
        pc.RemoveItem("item_w_claws_protean4")
        __main__.G.Card_Inserted = 1

#LIBRARY: Unhiding and hiding the library level switch, added by wesp
def unhideKey():
    pc = __main__.FindPlayer()
    switch = Find("cult_switch")
    switch.ScriptUnhide()
    switch_off = Find("cult_switch_off")
    switch_off.ScriptHide()
    __main__.G.Switch_Unlocked = 1
    if (__main__.G.Switch_Found == 0):
        pc.SetQuest("Library", 6)
        __main__.G.Switch_Found = 1
def hideKey():
    switch = Find("cult_switch")
    switch.ScriptHide()
    switch_off = Find("cult_switch_off")
    switch_off.ScriptHide()
    __main__.G.Switch_Unlocked = 0

#LIBRARY: Ritual chamber, added by wesp and EntenSchreck
def foundRitualChamber():
    __main__.G.Andrei_Library = 1
    __main__.FindPlayer().SetQuest("Library", 7)
    if __main__.G.Guard1_Killed == 2:
        guard = Find("guard1")
        guard.ScriptHide()
        gun = Find("gun")
        gun.ScriptUnhide()
        gun_node = Find("gun_node")
        gun_node.ScriptUnhide()
        dead_guard = __main__.CreateEntityNoSpawn("prop_ragdoll", (-50, 1300, 576), (0, 70, 0))
        dead_guard.SetModel("models/character/npc/common/security_guard/security_guard_skinny/security_guard_skinny.mdl")
        __main__.CallEntitySpawn(dead_guard)
def PersonalStuntman():
    pc = __main__.FindPlayer()
    E = Find("Stuntman")
    E.SetModel(pc.model)
    #E.SetOrigin(pc.GetOrigin())
    E.ScriptUnhide()
    Find("player_approach_Priest").BeginSequence()
    Find("!playerController").SetOrigin(Find("LovelyPlace").GetOrigin())
def TurnAroundBrother():
    Find("Priest").SetAngles(Find("Execution_Priest").GetAngles())
def defeatedAndrei():
    __main__.FindPlayer().SetQuest("Library", 8)
    __main__.G.Jumbles_Removed = 2
    __main__.ccmd.vamplight=""
    __main__.ccmd.vampexpo=""

#LOTUS: Bad luck farmer quest, added by wesp
def OnShuDealt():
    G  = __main__.G
    if G.Shu_Sleep == 0 and G.Shu_Frog == 0 and G.Shu_Dealt == 0:
        __main__.FindPlayer().SetQuest("Ox", 3)
        G.Shu_Dealt = 1

#MALKAVIAN 2: Fix for candle skins, added by vladdmaster
def librarySwitcherLightToggle( number ):
    switch = __main__.Find("library_light_switch_%d" % number )
    if (__main__.G.MalkavianMansion_Library_Lights[number-1] == 1):
        switch.skin = 1
    else:
        switch.skin = 0

#OBSERVATORY 2: Near werewolf, added by wesp
def fightWerewolf():
    pc = __main__.FindPlayer()
    if (pc.HasWeaponEquipped("item_w_avamp_blade") or pc.HasWeaponEquipped("item_w_bush_hook") or
pc.HasWeaponEquipped("item_w_claws") or pc.HasWeaponEquipped("item_w_fireaxe") or pc.HasWeaponEquipped("item_w_katana") or pc.HasWeaponEquipped("item_w_occultblade") or pc.HasWeaponEquipped("item_w_sledgehammer")):
        __main__.G.Player_Melee = 1
    else:
        __main__.G.Player_Melee = 0
    if (pc.HasWeaponEquipped("item_w_colt_anaconda") or pc.HasWeaponEquipped("item_w_crossbow") or pc.HasWeaponEquipped("item_w_crossbow_flaming") or pc.HasWeaponEquipped("item_w_deserteagle") or pc.HasWeaponEquipped("item_w_flamethrower") or pc.HasWeaponEquipped("item_w_ithaca_m_37") or pc.HasWeaponEquipped("item_w_rem_m_700_bach") or pc.HasWeaponEquipped("item_w_remington_m_700") or pc.HasWeaponEquipped("item_w_steyr_aug") or pc.HasWeaponEquipped("item_w_supershotgun")):
        __main__.G.Player_Ranged = 1
    else:
        __main__.G.Player_Ranged = 0
        
#OBSERVATORY 2: Kill werewolf, added by wesp
def killWerewolf():
    werewolf = Find("werewolf")
    center = werewolf.GetCenter()
    point = (center[0], center[1], center[2])
    dead_werewolf = __main__.CreateEntityNoSpawn("prop_ragdoll", point, (0,0,0) )
    dead_werewolf.SetModel("models/character/monster/werewolf/werewolf.mdl")
    dead_werewolf.SetName("dead_werewolf")
    __main__.CallEntitySpawn(dead_werewolf)
    __main__.G.Werewolf_Dead = 1
    if werewolf: werewolf.Kill()
    tramtimer = Find("tram_timer")
    tramtimer.Hide()
    tramtrigger = Find("tram_to_station")
    tramtrigger.Trigger() 

#OCEANHOUSE: Swaps Dodge powerup and book, added by wesp
def dodgeState():
    if (__main__.G.Patch_Plus == 1):
        trunk = Find("Occult_Container")
        trunk.SpawnItemInContainer("item_p_research_lg_dodge")
    else:
        trunk = Find("Occult_Container")
        trunk.SpawnItemInContainer("item_p_occult_dodge")

#PIER: Killed Copper when quest is active, added by wep
def copperDeath():
    if (__main__.G.Patch_Plus == 1):
        copstatus = __main__.FindPlayer().GetQuestState("Copper")
        if(copstatus == 1):
            __main__.FindPlayer().SetQuest("Copper", 3)

#RAMEN SHOP: If threatening yukie, added by wesp
def onYukieThreat():
    sword = Find("sword")
    if (__main__.G.Yukie_Threat == 1):
        if sword: sword.Kill()

#RED DRAGON: Float in elevator, added by wesp
def floatElevator():
    hos = Find("Hostess")
    if (not __main__.IsDead("Hostess")):
        if (__main__.G.Hos_Float == 0):
            if (__main__.IsClan(__main__.FindPlayer(), "Malkavian") and __main__.G.Player_Insane == 0):
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line1_col_n.mp3")
            else:
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line1_col_e.mp3")
        if (__main__.G.Hos_Float == 1):
            if (__main__.IsClan(__main__.FindPlayer(), "Malkavian") and __main__.G.Player_Insane == 0):
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line2_col_n.mp3")
            else:
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line2_col_e.mp3")
        if (__main__.G.Hos_Float == 2):
            if (__main__.IsClan(__main__.FindPlayer(), "Malkavian") and __main__.G.Player_Insane == 0):
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line3_col_n.mp3")
            else:
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line3_col_e.mp3")
        if (__main__.G.Hos_Float == 3):
            if (__main__.IsClan(__main__.FindPlayer(), "Malkavian") and __main__.G.Player_Insane == 0):
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line4_col_n.mp3")
            else:
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line4_col_e.mp3")
        __main__.G.Hos_Float = __main__.G.Hos_Float + 1
        if (__main__.G.Hos_Float == 4):
            __main__.G.Hos_Float = 0

#REDSPOT: Called to see if Slater and Spicoli are alive, added by wesp
def slaterAlive():
    slater = Find("Slater")
    spicoli = Find("Spicoli")
    if (__main__.IsDead("Slater")):
        if(slater): slater.Kill()
    if (__main__.IsDead("Spicoli")):
        if(spicoli): spicoli.Kill()

#SANTA MONICA: Spawns blueblood watch, added by wesp
def spawnWatch():
    pc = __main__.FindPlayer()
    if (pc.AmmoCount("item_g_watch_fancy") == 0):
        pc.GiveItem("item_g_watch_fancy")
    else:
        pc.GiveAmmo("item_g_watch_fancy",1)
        if __main__.G.Patch_Plus == 1:
            c  = __main__.ccmd
            c.showSpawn=""

#SEWERS: Shortcut door, added by wesp
def unhideShortcut():
    shortcut = Find("shortcut_open")
    shortcut.ScriptUnhide()
    shortcut_off = Find("shortcut_closed")
    shortcut_off.ScriptHide()
    sound = Find("shortcut_sound")
    if sound: sound.PlaySound()
    __main__.G.Shortcut_Unlocked = 1
def hideShortcut():
    shortcut = Find("shortcut_open")
    shortcut.ScriptHide()
    shortcut_off = Find("shortcut_closed")
    shortcut_off.ScriptUnhide()
    sound = Find("shortcut_sound")
    if sound: sound.PlaySound()
    __main__.G.Shortcut_Unlocked = 0

#SEWERS: Changes model of running Nosferatu, added by wesp
def nosCheck():
    nos = Find("scene_nos")
    nos_model = "models/character/pc/female/nosferatu/armor0/Nosferatu_Female_Armor_0.mdl"
    pc = __main__.FindPlayer()
    gender = pc.IsMale()
    if (gender == 1):
        nos.SetModel(nos_model)
    if (__main__.G.Patch_Plus == 1):
        nos.SetName("scenenos")

#SEWERS: Gives Humanity on saving running Nosferatu, added by wesp
def nosAlive():
    nos = Find("scenenos")
    pc = __main__.FindPlayer()
    gender = pc.IsMale()
    if __main__.G.Nossie_Dead == 0:
        if (gender == 1):
            nos.PlayDialogFile("\Character\dlg\warrens\imalia\line407_col_e.mp3")
        else:
            nos.PlayDialogFile("\Character\dlg\warrens\mitnick\line277_col_e.mp3")
        __main__.FindPlayer().HumanityAdd( 1 )

#SKYLINE: Called to add glow to elevator pointing arrows and mark floors, button G, added by vladdmaster
def callbuttonground():
    elev = __main__.Find("skyelev")
    height = elev.GetOrigin()
    pointarr = __main__.Find("elevarr")
    fsix = __main__.Find("sixtoground")
    ffive = __main__.Find("fivetoground")
    ffour = __main__.Find("fourtoground")
    fthree = __main__.Find("threetoground")
    ftwo = __main__.Find("twotoground")
    fground = __main__.Find("onground")
    if height[2] >= 1584:
        fsix.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 1278:
        ffive.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 974:
        ffour.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 670:
        fthree.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 366:
        ftwo.Trigger()
        pointarr.SetSkin( 2 )
    else:
        fground.Trigger()
        pointarr.SetSkin( 2 )

#SKYLINE: Called to add glow to elevator pointing arrows and mark floors, button 1, added by vladdmaster
def callbuttonone():
    elev = __main__.Find("skyelev")
    height = elev.GetOrigin()
    pointarr = __main__.Find("elevarr")
    fsix = __main__.Find("sixtoone")
    ffive = __main__.Find("fivetoone")
    ffour = __main__.Find("fourtoone")
    fthree = __main__.Find("threetoone")
    fone = __main__.Find("onfirst")
    if height[2] >= 1584:
        fsix.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 1278:
        ffive.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 974:
        ffour.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 670:
        fthree.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 366:
        fone.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 62:
        fone.Trigger()
    else:
        fone.Trigger()
        pointarr.SetSkin( 1 )

#SKYLINE: Called to add glow to elevator pointing arrows and mark floors, button 2, added by vladdmaster
def callbuttontwo():
    elev = __main__.Find("skyelev")
    height = elev.GetOrigin()
    pointarr = __main__.Find("elevarr")
    fsix = __main__.Find("sixtotwo")
    ffive = __main__.Find("fivetotwo")
    ffour = __main__.Find("fourtotwo")
    ftwo = __main__.Find("onsecond")
    fground = __main__.Find("groundtotwo")
    if height[2] >= 1584:
        fsix.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 1278:
        ffive.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 974:
        ffour.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 670:
        ftwo.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 366:
        ftwo.Trigger()
    elif height[2] >= 62:
        ftwo.Trigger()
        pointarr.SetSkin( 1 )
    else:
        fground.Trigger()
        pointarr.SetSkin( 1 )

#SKYLINE: Called to add glow to elevator pointing arrows and mark floors, button 3, added by vladdmaster
def callbuttonthree():
    elev = __main__.Find("skyelev")
    height = elev.GetOrigin()
    pointarr = __main__.Find("elevarr")
    fsix = __main__.Find("sixtothree")
    ffive = __main__.Find("fivetothree")
    fthree = __main__.Find("onthird")
    fone = __main__.Find("onetothree")
    fground = __main__.Find("groundtothree")
    if height[2] >= 1584:
        fsix.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 1278:
        ffive.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 974:
        fthree.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 670:
        fthree.Trigger()
    elif height[2] >= 366:
        fthree.Trigger()
        pointarr.SetSkin( 1 )
    elif height[2] >= 62:
        fone.Trigger()
        pointarr.SetSkin( 1 )
    else:
        fground.Trigger()
        pointarr.SetSkin( 1 )

#SKYLINE: Called to add glow to elevator pointing arrows and mark floors, button 4, added by vladdmaster
def callbuttonfour():
    elev = __main__.Find("skyelev")
    height = elev.GetOrigin()
    pointarr = __main__.Find("elevarr")
    fsix = __main__.Find("sixtofour")
    ffour = __main__.Find("onfourth")
    ftwo = __main__.Find("twotofour")
    fone = __main__.Find("onetofour")
    fground = __main__.Find("groundtofour")
    if height[2] >= 1584:
        fsix.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 1278:
        ffour.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 974:
        ffour.Trigger()
    elif height[2] >= 670:
        ffour.Trigger()
        pointarr.SetSkin( 1 )
    elif height[2] >= 366:
        ftwo.Trigger()
        pointarr.SetSkin( 1 )
    elif height[2] >= 62:
        fone.Trigger()
        pointarr.SetSkin( 1 )
    else:
        fground.Trigger()
        pointarr.SetSkin( 1 )

#SKYLINE: Called to add glow to elevator pointing arrows and mark floors, button 5, added by vladdmaster
def callbuttonfive():
    elev = __main__.Find("skyelev")
    height = elev.GetOrigin()
    pointarr = __main__.Find("elevarr")
    ffive = __main__.Find("onfifth")
    fthree = __main__.Find("threetofive")
    ftwo = __main__.Find("twotofive")
    fone = __main__.Find("onetofive")
    fground = __main__.Find("groundtofive")
    if height[2] >= 1584:
        ffive.Trigger()
        pointarr.SetSkin( 2 )
    elif height[2] >= 1278:
        ffive.Trigger()
    elif height[2] >= 974:
        ffive.Trigger()
        pointarr.SetSkin( 1 )
    elif height[2] >= 670:
        fthree.Trigger()
        pointarr.SetSkin( 1 )
    elif height[2] >= 366:
        ftwo.Trigger()
        pointarr.SetSkin( 1 )
    elif height[2] >= 62:
        fone.Trigger()
        pointarr.SetSkin( 1 )
    else:
        fground.Trigger()
        pointarr.SetSkin( 1 )

#SKYLINE: Called to add glow to elevator pointing arrows and mark floors, button 6, added by vladdmaster
def callbuttonsix():
    elev = __main__.Find("skyelev")
    height = elev.GetOrigin()
    pointarr = __main__.Find("elevarr")
    fsix = __main__.Find("onsixth")
    ffour = __main__.Find("fourtosix")
    fthree = __main__.Find("threetosix")
    ftwo = __main__.Find("twotosix")
    fone = __main__.Find("onetosix")
    fground = __main__.Find("groundtosix")
    if height[2] >= 1584:
        fsix.Trigger()
    elif height[2] >= 1278:
        fsix.Trigger()
        pointarr.SetSkin( 1 )
    elif height[2] >= 974:
        ffour.Trigger()
        pointarr.SetSkin( 1 )
    elif height[2] >= 670:
        fthree.Trigger()
        pointarr.SetSkin( 1 )
    elif height[2] >= 366:
        ftwo.Trigger()
        pointarr.SetSkin( 1 )
    elif height[2] >= 62:
        fone.Trigger()
        pointarr.SetSkin( 1 )
    else:
        fground.Trigger()
        pointarr.SetSkin( 1 )

#SOCIETY 3: Ash's cell key, added by wesp
def keyState():
    if (__main__.G.Ash_Leave == 1 and __main__.G.Patch_Plus == 1):
        key = Find("ashkey")
        keynode = Find("ashkeynode")
        if key: key.ScriptUnhide()
        if keynode: keynode.ScriptUnhide()

#SOCIETY 3: Saving Ash, added by wesp
def ashDies():
    if (__main__.G.Patch_Plus == 1):
        pc = __main__.FindPlayer()
        state = pc.GetQuestState("Ash")
        if (state == 1):
            pc.SetQuest("Ash", 3)
        if (pc.humanity >= 4):
            pc.HumanityAdd( -1 )

#SOCIETY 4: Bach dropping weapons, added by wesp
def bachSwap():
    if(__main__.G.Patch_Plus == 1):
        bach = Find("Bach")
        bach.SetName("Bach_basic")
        bach.ScriptHide()
        bach_plus = Find("Bach_plus")
        bach_plus.ScriptUnhide()
        bach_plus.SetName("Bach")
        bach_plus.SignalVulnerable(1)

#SOCIETY 4: Bach dropping weapons, added by wesp
def bachDeath():
    if (__main__.G.Patch_Plus == 2):
        bach = Find("Bach")
        center = bach.GetCenter()
        point = (center[0], center[1], center[2] + 20)
        blade = __main__.CreateEntityNoSpawn("item_w_katana", point, (0,0,0) )
        blade.SetName("katana")
        sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
        sparklies.SetParent("katana")
        __main__.CallEntitySpawn(blade)
        __main__.CallEntitySpawn(sparklies)
        swat = __main__.CreateEntityNoSpawn("item_w_rem_m_700_bach", point, (0,0,0) )
        swat.SetName("rifle")
        sparklies1 = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
        sparklies1.SetParent("rifle")
        __main__.CallEntitySpawn(swat)
        __main__.CallEntitySpawn(sparklies1)

#TEMPLE 1: Yukie, added by wesp
def YukieFloat(n):
    yukie = Find("Yukie")
    if (yukie and __main__.G.Patch_Plus == 1):
        yukie.PlayDialogFile("Character/dlg/Chinatown/yukie/line%d_col_e.mp3" %n)

#TUTORIAL: Remove MAC-10 of Sabbat
def RemoveMac10():
    redshirt = __main__.Find ("sabbat_redshirt_5")
    redshirt.RemoveItem("item_w_mac_10")

#TUTORIAL: Dialogue popups, added by wesp
def testGuard():
    if __main__.G.Tut_Secg == 1:
        pc = __main__.FindPlayer()
        if IsClan(pc,"Ventrue") or IsClan(pc, "Tremere"):
            Find("popup_65").OpenWindow()
        elif IsClan(pc, "Malkavian"):
            Find("popup_66").OpenWindow()
        elif IsClan(pc, "Nosferatu"):
            Find("popup_67").OpenWindow()
        elif IsClan(pc, "Brujah") or IsClan(pc, "Toreador"):
            Find("popup_68").OpenWindow()
        else:
            Find("popup_59").OpenWindow()
    else:
        guard = Find("Tutorial_Security_Guard")
        guard.WillTalk(0)
        if __main__.G.Tut_Secg == 2:
            script = Find("sTalkguy_move")
            if script: script.BeginSequence()

#VENTRUETOWER 1: Collateral damage after Sabbat attack, added by Malkav
def collateral():
    G = __main__.G
    if(G.Story_State >= 70 and G.Clean_Rubble == 0 and G.Guard_Drop == 0):
        cop = __main__.CreateEntityNoSpawn("prop_ragdoll", (33.1819, 829.631, -7358.53), (28, 220, 0))
        cop.SetModel("models/character/npc/common/security_guard/security_guard_skinny/security_guard_skinny.mdl")
        __main__.CallEntitySpawn(cop)
        cop = __main__.CreateEntityNoSpawn("prop_ragdoll", (115.954, 801.695, -7358.01), (-47.9903, 178.89, 91.4943))
        cop.SetModel("models/character/npc/common/security_guard/security_guard_skinny/security_guard_skinny.mdl")
        __main__.CallEntitySpawn(cop)
        cop = __main__.CreateEntityNoSpawn("prop_ragdoll", (-22.5817, 783.453, -7356.66), (-25.386, 310.587, -20.1677))
        cop.SetModel("models/character/npc/common/security_guard/security_guard_skinny/security_guard_skinny.mdl")
        __main__.CallEntitySpawn(cop)
        cop = __main__.CreateEntityNoSpawn("prop_ragdoll", (-43.8232, 234.327, -7343.78), (-36.9034, 21.6965, 0.91747))
        cop.SetModel("models/character/npc/common/security_guard/security_guard_skinny/security_guard_skinny.mdl")
        __main__.CallEntitySpawn(cop)
        cop = __main__.CreateEntityNoSpawn("prop_ragdoll", (-174.511, 320.242, -7327.69), (0, 291, 0))
        cop.SetModel("models/character/npc/common/security_guard/security_guard_skinny/security_guard_skinny.mdl")
        __main__.CallEntitySpawn(cop)
        cop = __main__.CreateEntityNoSpawn("prop_ragdoll", (-312.208, 407.893, -7351.82), (10, 300, 0))
        cop.SetModel("models/character/npc/common/super_swat/super_swat.mdl")
        __main__.CallEntitySpawn(cop)
        cop = __main__.CreateEntityNoSpawn("prop_ragdoll", (-360.484, 466.291, -7351.82), (0, 309, 60))
        cop.SetModel("models/character/npc/common/super_swat/super_swat.mdl")
        __main__.CallEntitySpawn(cop)
        cop = __main__.CreateEntityNoSpawn("prop_ragdoll", (-625.617, 612.877, -7520.29), (-62.9957, 179.019, -88.8988))
        cop.SetModel("models/character/npc/common/security_guard/security_guard_skinny/security_guard_skinny.mdl")
        __main__.CallEntitySpawn(cop)
        cop = __main__.CreateEntityNoSpawn("prop_ragdoll", (-521.79, 835.889, -7397.78), (-62.9957, 266.519, -88.8988))
        cop.SetModel("models/character/npc/common/security_guard/security_guard_skinny/security_guard_skinny.mdl")
        __main__.CallEntitySpawn(cop)
        G.Guard_Drop = 1
    elif(G.Story_State >= 70 and G.Clean_Rubble == 1):
        bodies = FindClass("prop_ragdoll")
        for body in bodies: body.Kill()

#VENTRUETOWER 2: Setup timer for plus patch, added by wesp
def setupTimer():
    if (__main__.G.Patch_Plus == 1):
        timer = Find("explosion_timer")
        timer.count_time = 30
        timer.RestartTimer()
        timer.StartTimer()
        timer.Show()

#VENTRUETOWER 2: Check if player has the astrolite, added by wesp
def checkBomb():
    pc = __main__.FindPlayer()
    explosion_timer = __main__.Find("explosion_timer")
    if pc.HasItem("item_g_astrolite") and __main__.G.Story_State >= 100 and __main__.G.Bomb_Disarmed == 0:
        if explosion_timer: explosion_timer.Kill()
        sound = __main__.Find("disarm_bomb")
        if sound: sound.PlaySound()
        __main__.G.Bomb_Disarmed = 1

#VENTRUETOWER 2: Gender of Ventrue enemies, added by wesp
def genderVentrue():
    pc = __main__.FindPlayer()
    gender = pc.IsMale()
    clan = pc.clan
    sniper1 = Find("sniper_1")
    sniper2 = Find("sniper_2")
    patrol4 = Find("patroller_4")
    office1 = Find("office_guard_1")
    office2 = Find("office_guard_2")
    ventrue_female = "models/character/pc/female/ventrue/armor3/ventrue_female_armor_3.mdl"
    if(gender == 1 and clan == 8):
        sniper1.SetModel(ventrue_female)
        sniper2.SetModel(ventrue_female)
        patrol4.SetModel(ventrue_female)
        office1.SetModel(ventrue_female)
        office2.SetModel(ventrue_female)
    if __main__.G.Patch_Plus == 1:
        patrol4.SetScriptedDiscipline("presence 3")
        office1.SetScriptedDiscipline("fortitude 3")
        office2.SetScriptedDiscipline("fortitude 3")

#VENTRUETOWER 3: Sheriff uses Bat's Communion, added by EntenSchreck
def SheriffBatsIn():
    if not Find("Bats") and __main__.G.BatsIn == 0:
        pc = __main__.FindPlayer()
        Bats=__main__.CreateEntityNoSpawn("npc_VHuman",pc.GetOrigin(),pc.GetAngles())
        Bats.SetName("Bats")
        __main__.CallEntitySpawn(Bats)
        Bats = Find("Bats")
        if Bats:
# wesp            Bats.MakeInvincible(1)
            Bats.SetParent("!player")
            Bats.SetModel("models/weapons/disciplines/animalism/world/bats_group_01.mdl")
            Find("bats_in").BeginSequence()
def SheriffBatsOut():
    if Find("Bats"):
        pc = __main__.FindPlayer()
        Bats2=__main__.CreateEntityNoSpawn("npc_VHuman",pc.GetOrigin(),pc.GetAngles())
        Bats2.SetName("Bats2")
        __main__.CallEntitySpawn(Bats2)
        Bats = Find("Bats2")
        if Bats2:
# wesp            Bats2.MakeInvincible(1)
            Bats2.SetParent("!player")
            Bats2.SetModel("models/weapons/disciplines/animalism/world/bats_group_01.mdl")
            Find("bats_out").BeginSequence()
	    __main__.G.Sheriff_Hits=0
	    #Find("Bats").Kill()
	    __main__.ScheduleTask(0.2,'Find("Bats").Kill()')
	    __main__.G.BatsIn = 0
def EffectOnPlayer():
    pc = __main__.FindPlayer()
    i = randint(2, 4)
    pc.Bloodloss(i)	#damages player as well!
    SheriffBatsOut()
    print "No creepy bats that spawned out of nowhere were hurt in this fight..."
def HitCounter():
    G = __main__.G
    if G.Patch_Plus == 1:
        G.Sheriff_Hits = G.Sheriff_Hits + 1
        print(__main__.G.Sheriff_Hits)
        i = randint(5, 7)
        if G.Sheriff_Hits > i:
        #if G.Sheriff_Hits == 1:	#TEST
            SheriffBatsIn()
            G.BatsIn = 1	#prevents bats from spawning too often if player uses machine gun
def SheriffBatsSummon():
    Find("Swarm_1").ScriptUnhide()
    Find("Swarm_2").ScriptUnhide()
    Find("Swarm_3").ScriptUnhide()
    Find("Swarm_4").ScriptUnhide()
    Find("Swarm_5").ScriptUnhide()
    Find("Swarm_6").ScriptUnhide()
    Find("Swarm_7").ScriptUnhide()
    Find("Swarm_8").ScriptUnhide()
    Find("Swarm_9").ScriptUnhide()
    Find("Swarm_10").ScriptUnhide()
    Find("Swarm_11").ScriptUnhide()
    Find("Swarm_12").ScriptUnhide()
    Find("Swarm_13").ScriptUnhide()
    Find("Swarm_14").ScriptUnhide()

#WARRENS: Updates Bertram quest, added by wesp
def checkCD():
    if (__main__.G.Patch_Plus == 1 and __main__.G.Bertram_RAM == 1):
        pc = __main__.FindPlayer()
        pc.SetQuest("BertramCD", 2)

#WARRENS: Made Gary give Bloodpacks, added by wesp
def spawnPack():
    if __main__.G.Patch_Plus == 0:
        return
    pc = __main__.FindPlayer()
    if (IsClan(pc,"Toreador")):
        if (pc.AmmoCount("item_g_bloodpack") == 0):
            pc.GiveItem("item_g_bloodpack")
        else:
            pc.GiveAmmo("item_g_bloodpack",1)
            c  = __main__.ccmd
            c.showSpawn=""
    elif (IsClan(pc,"Nosferatu")):
        if (pc.AmmoCount("item_g_eldervitaepack") == 0):
            pc.GiveItem("item_g_eldervitaepack")
        else:
            pc.GiveAmmo("item_g_eldervitaepack",1)
            c  = __main__.ccmd
            c.showSpawn=""
    else:
        if (pc.AmmoCount("item_g_bluebloodpack") == 0):
            pc.GiveItem("item_g_bluebloodpack")
        else:
            pc.GiveAmmo("item_g_bluebloodpack",1)
            c  = __main__.ccmd
            c.showSpawn=""

#Toggle walking/running, added by wesp
def toggleSpeed():
    G = __main__.G
    c = __main__.ccmd
    if(G.Walk == 1):
        c.run=""
        G.Walk = 0
    else:
        c.walk=""
        G.Walk = 1

#Toggle automatic moving, added by wesp
def toggleMove():
    G = __main__.G
    c = __main__.ccmd
    if(G.Go == 1):
        c.stop=""
        G.Go = 0
    else:
        c.go=""
        G.Go = 1

#Particles for dialogue Domination and Presence, added by wesp
def dialogParticles():
    if __main__.G.Dialog_Presence == 1:
        __main__.npc.SpawnTempParticle("presence_particles")
        __main__.G.Dialog_Presence = 0
    else:
        __main__.npc.SpawnTempParticle("dominate_particles")

#Humanity loss on killing civilians, added by wesp
def civilianDeath():
    pc = __main__.FindPlayer()
    if (pc.humanity >= 4 and __main__.G.Patch_Plus == 1):
        pc.HumanityAdd( -1 )

#Masquerade violation for killing kindred in public, added by Malkav and wesp
def checkFieryDeath(name):
    masq = 0
    dist = 600      #normal vision range for open spaces
    p1 = Find(name).GetCenter()
    alleys = FindList("Trigger_Prostitut*") + FindList("jewbkdr")
    for alley in alleys:
        p2 = alley.GetCenter()
        if (distanceSquared(p1, p2) < 40000): dist = 150     #40000 -> 200 around trigger, 150 reduced visibility in alleys
    distsq = dist * dist
    guys = FindClass("npc_VCop") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VPedestrian") + FindClass("npc_VHuman") + FindClass("npc_VHumanCombatant")
    for guy in guys:
        p2 = guy.GetCenter()
        if (distanceSquared(p1, p2) < distsq): masq = 1
    if (masq == 1 and __main__.G.Patch_Plus == 1): __main__.FindPlayer().ChangeMasqueradeLevel(1)

#Checking Research for occult items, added by wesp
def checkOccult():
    pc = __main__.FindPlayer()
    __main__.G.Player_Research = pc.CalcFeat("research")
    #print(__main__.G.Player_Research)
    if pc.HasItem("item_w_zombie_fists") and __main__.G.Player_Research >= 4:
        pc.RemoveItem("item_w_zombie_fists")
        pc.GiveItem("item_p_occult_passive_durations")
        print "Galdjum swapped"
    if pc.HasItem("item_w_werewolf_attacks") and __main__.G.Player_Research >= 6:
        pc.RemoveItem("item_w_werewolf_attacks")
        pc.GiveItem("item_p_occult_obfuscate")
        print "Zharalketh swapped"
    if pc.HasItem("item_w_tzimisce3_claw") and __main__.G.Player_Research >= 2:
        pc.RemoveItem("item_w_tzimisce3_claw")
        pc.GiveItem("item_p_occult_frenzy")
        print "Tarulfang swapped"
    if pc.HasItem("item_w_tzimisce_melee") and __main__.G.Player_Research >= 8:
        pc.RemoveItem("item_w_tzimisce_melee")
        pc.GiveItem("item_p_occult_experience")
        print "Saulocept swapped"
    if pc.HasItem("item_w_sabbatleader_attack") and __main__.G.Player_Research >= 8:
        pc.RemoveItem("item_w_sabbatleader_attack")
        pc.GiveItem("item_p_occult_hacking")
        print "Braid Talisman swapped"
    if pc.HasItem("item_w_manbat_claw") and __main__.G.Player_Research >= 2:
        pc.RemoveItem("item_w_manbat_claw")
        pc.GiveItem("item_p_occult_dodge")
        print "Weekapaug Thistle swapped"
    if pc.HasItem("item_w_hengeyokai_fist") and __main__.G.Player_Research >= 6:
        pc.RemoveItem("item_w_hengeyokai_fist")
        pc.GiveItem("item_p_occult_heal_rate")
        print "Mummywrap Fetish swapped"
    if pc.HasItem("item_w_gargoyle_fist") and __main__.G.Player_Research >= 4:
        pc.RemoveItem("item_w_gargoyle_fist")
        pc.GiveItem("item_p_occult_thaum_damage")
        print "Daimonori swapped"

#Vendor cleanup to fix book exploit, added by Norrwin
def preBarter(vendor=""):
    G  = __main__.G
    G.pc_barter_loc = __main__.FindPlayer().GetAngles()
    G.ip_vendor = vendor
    barterWait()
def barterWait():
    G  = __main__.G
    for item in booklist:
        if len(__main__.FindEntitiesByClass(item)) == 2:
            vendor = G.ip_vendor
            cleanInventory(vendor)
    if __main__.FindPlayer().GetAngles() == G.pc_barter_loc:
        __main__.ScheduleTask(0.15,"barterWait()")
saleitems = ("item_p_research_hg_computers", "item_p_research_hg_dodge", "item_p_research_hg_firearms", "item_p_research_hg_melee", "item_p_research_mg_brawl", "item_p_research_mg_finance", "item_p_research_mg_melee", "item_p_research_mg_security", "item_p_research_lg_firearms", "item_p_research_lg_dodge", "item_p_research_lg_stealth", "item_p_research_lg_computers")
booklist = ("item_p_research_hg_computers", "item_p_research_hg_dodge", "item_p_research_hg_firearms", "item_p_research_hg_melee", "item_p_research_mg_brawl", "item_p_research_mg_finance", "item_p_research_mg_melee", "item_p_research_mg_security", "item_p_research_lg_firearms", "item_p_research_lg_dodge", "item_p_research_lg_stealth", "item_p_research_lg_computers")
def cleanInventory(vendor=""):
    npc = Find(vendor)
    rst = "item_p_research_"
    if npc:
        for item in saleitems:
            try:
                item.index(rst)
                # print "trying substring"
            except ValueError:
                while npc.HasItem(item): npc.RemoveItem(item)
                # print "no substring"
            else:
                if __main__.FindPlayer().HasItem(item):
                    while npc.HasItem(item): npc.RemoveItem(item)
                # print "found substring"

#Player learns new Discipline, added by Entenschreck
def newDiscipline(x):
    c  = __main__.ccmd
    pc = __main__.FindPlayer()
    if x == 1:
        c.incAnimalism=""
    elif x == 2:
        c.incAuspex=""
    elif x == 3:
        c.incCelerity=""
    elif x == 4:
        c.incDementate=""
    elif x == 5:
        c.incDominate=""
    elif x == 6:
        c.incFortitude=""
    elif x == 7:
        c.incObfuscate=""
    elif x == 8:
        c.incPotence=""
    elif x == 9:
        c.incPresence=""
    elif x == 10:
        c.incProtean=""
    elif x == 11:
        c.incThaumaturgy=""    #should actually never get this
    c.showDiscipline=""

#Fix Discipline key, copied from Dheu's ModDev Guide, changed by Entenschreck
def FixKeyBindings():
    data = ''
    fin = None
    try:
        config = nt.getcwd() + "\\Unofficial_Patch\\cfg\\config.cfg"
        fin = open(config,"r")
        line = fin.readline()
        while line:
            dsc = line.rfind('"vdiscipline_last"')
            if -1 != dsc:
                r = dsc
                dsc = line.find(' ')
                data='%sbind %s "vm_discipline"\n' % (data,line[dsc:r].strip())
            line=fin.readline()
    finally:
        if fin: fin.close()
    if 0 != len(data):
        console = nt.getcwd() + "\\Unofficial_Patch\\cfg\\console.cfg"
        cfg=open(console, 'w')
        try: cfg.write(data)
        finally: cfg.close()
        __main__.ccmd.execonsole=""

#Animations for firstperson Thaumaturgy hand, added by Entenschreck, improved by wesp
def checkDiscipline():
    c  = __main__.ccmd
    pc = __main__.FindPlayer()
    if (pc.HasItem("item_w_tzimisce2_head")):
        print "YOU SHALL NOT CAST!"
    else:
        c.vdiscipline_last=""
        __main__.ScheduleTask(1.0,"BloodHealTest()")
        VThaumaturgy(1)

def BloodHealTest():		# added by wesp
    c  = __main__.ccmd
    pc = __main__.FindPlayer()
    if (pc.active_blood_healing > 0 and (pc.clan == 9 or pc.clan == 10 or pc.clan == 11)):
        c.faithheal=""
    elif (pc.active_blood_healing > 0):
        c.vm_bloodheal=""

def VThaumaturgy(x):
    G    = __main__.G
    pc   = __main__.FindPlayer()
    c    = __main__.ccmd
    cvar = __main__.cvar
    ST   = __main__.ScheduleTask

    #called when activating a discipline EVERY TIME
    if x == 1:
        c.vm_clearlist=""
        c.vm_lower=""    #first animation in the list is always skipped!
        c.vm_charge=""

        #Need a delay here!
        ST(0.05,"VThaumaturgy(2)")

    elif x == 2:

        #c.disallowAttacking=""

        VIEWMODEL  = FindClass("viewmodel")[2]
        HANDSMODEL = FindClass("viewmodel")[3]

        #vdebug_wpn_anims_cycle is set to 1 via DisciplineFX by default.
        #If the target resists the discipline it will be set to 2.

        if cvar.vdebug_wpn_anims_cycle == 1:
            c.vm_continue=""
            c.vm_hold=""
            c.vm_reset=""
            c.vm_lower=""

            HANDSMODEL.SetModel("models/null.mdl")

            if pc.clan == 5:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_nosferatu/v_thaumaturgy.mdl")

            elif pc.IsMale() == 1 and pc.clan == 2:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_male_brujah/v_thaumaturgy.mdl")

            elif pc.IsMale() == 0 and pc.clan == 6:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_female_toreador/v_thaumaturgy.mdl")

            elif pc.IsMale() == 0 and pc.clan == 7:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_female_tremere/v_thaumaturgy.mdl")

            elif pc.IsMale() == 0 and pc.clan == 8:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_female_ventrue/v_thaumaturgy.mdl")

            elif pc.IsMale() == 0:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_female/v_thaumaturgy.mdl")

            elif pc.IsMale() == 1:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_male/v_thaumaturgy.mdl")

        elif cvar.vdebug_wpn_anims_cycle == 2:
            c.vm_chargehold=""
            c.vm_chargehold=""
            c.vm_chargehold=""
            c.vm_lower=""

            HANDSMODEL.SetModel("models/null.mdl")

            if pc.clan == 5:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_nosferatu/v_thaumaturgy.mdl")

            elif pc.IsMale() == 1 and pc.clan == 2:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_male_brujah/v_thaumaturgy.mdl")

            elif pc.IsMale() == 0 and pc.clan == 6:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_female_toreador/v_thaumaturgy.mdl")

            elif pc.IsMale() == 0 and pc.clan == 7:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_female_tremere/v_thaumaturgy.mdl")

            elif pc.IsMale() == 0 and pc.clan == 8:
                VIEWMODEL.SetModel("models/weapons/thaumaturgy/view_female_ventrue/v_thaumaturgy.mdl")

        c.vdebug_wpn_anims_cycle_list=""

        ST(2.2,"VThaumaturgy(3)")

    elif x == 3:
#For some reason the game crashes for some players if the model's name is stored in a G variable...
#Using this method now instead.

        VIEWMODEL  = FindClass("viewmodel")[2]
        HANDSMODEL = FindClass("viewmodel")[3]

        #Brujah
        if pc.IsMale() == 0 and pc.clan == 2:
            HANDSMODEL.SetModel("models/hands/female/shared/v_shared_female_hands.mdl")
        elif pc.IsMale() == 1 and pc.clan == 2:
            HANDSMODEL.SetModel("models/hands/male/brujah/v_brujah_male_hands.mdl")

        #Nosferatu
        elif pc.IsMale() == 0 and pc.clan == 5:
            HANDSMODEL.SetModel("models/hands/female/nosferatu/v_nosferatu_fem_hands.mdl")
        elif pc.IsMale() == 1 and pc.clan == 5:
            HANDSMODEL.SetModel("models/hands/male/nosferatu/v_nosferatu_male_hands.mdl")

        #Toreador
        elif pc.IsMale() == 0 and pc.clan == 6:
            HANDSMODEL.SetModel("models/hands/female/toreador/v_toreador_fem_hands.mdl")
        elif pc.IsMale() == 1 and pc.clan == 6:
            HANDSMODEL.SetModel("models/hands/male/shared/v_shared_male_hands.mdl")

        #Tremere
        elif pc.IsMale() == 0 and pc.clan == 7:
            HANDSMODEL.SetModel("models/hands/female/tremere/v_tremere_fem_hands.mdl")
        elif pc.IsMale() == 1 and pc.clan == 7:
            HANDSMODEL.SetModel("models/hands/male/shared/v_shared_male_hands.mdl")

        #Ventrue
        elif pc.IsMale() == 0 and pc.clan == 8:
            HANDSMODEL.SetModel("models/hands/female/ventrue/v_ventrue_fem_hands.mdl")
        elif pc.IsMale() == 1 and pc.clan == 8:
            HANDSMODEL.SetModel("models/hands/male/shared/v_shared_male_hands.mdl")

        else:
            if pc.IsMale() == 0:
                HANDSMODEL.SetModel("models/hands/female/shared/v_shared_female_hands.mdl")
            elif pc.IsMale() == 1:
                HANDSMODEL.SetModel("models/hands/male/shared/v_shared_male_hands.mdl")


#Clan specific idle animations, added by EntenSchreck, improved by malkav and wesp
def IsIdling():
    checkOccult()
    checkBomb()
    pc = __main__.FindPlayer()
    G  = __main__.G
    G.Pos_One = pc.GetOrigin()
    cal = Find("Cal")
    if cal:
        scheme1 = Find("sound_default")
        scheme2 = Find("sound_override_1")
        music = Find("music")
        if (pc.GetOrigin()[2] > -100):
            music.Volume (1)
            scheme1.FadeOut(0)
            scheme2.FadeIn(0)
        else:
            music.Volume (8)
            scheme1.FadeIn(0)
            scheme2.FadeOut(0)
    __main__.ScheduleTask(1.0,"AThingOfSomeKind()")
    #__main__.ScheduleTask(1.0,"game_mechanics.AnotherThingOfSomeKind()")
    #timer = __main__.FindEntityByName("idle_timer")
    #if timer: timer.Disable()
    #Animal Friendship
    #if G.FeatValue == G.FeatValueHelper: pass
    #else: game_mechanics.GetFeatValue() 
def AThingOfSomeKind():
    pc = __main__.FindPlayer()
    G  = __main__.G
    ST = __main__.ScheduleTask
    c  = __main__.ccmd
    notIdle = 0
    gender = 0
    clan = 1  #Human
    postwo = pc.GetOrigin()
    if(postwo[0] != G.Pos_One[0] or postwo[1] != G.Pos_One[1]):
        notIdle = 1
        print "no anims, moving"
    elif(G.InCombat == 1):
        notIdle = 1
        print "no anims, in combat"
    elif(G.No_Idle == 1):
        notIdle = 1
        print "no anims, outside conditions"
    elif((pc.GetCenter()[2] - pc.GetOrigin()[2]) <= 18):
        notIdle = 1
        print "no anims, crouched or prone"
    elif(G.Anims_Disabled == 0):
        npcs = FindClass("npc_V*")
        for npc in npcs:
            p2 = npc.GetOrigin()
            dist = distanceSquared(postwo, p2)
            if(dist < 20000):	#distance: npcs can't be closer than 40. Player is most likely feeding if any npc is closer. Changed because of dialogues.
                notIdle = 1
                G.Delay = 1 #how many times animations are skipped after feeding
                print "no anims, pc near npc"
    if(notIdle == 0 and pc.active_protean < 2 and pc.HasWeaponEquipped("item_w_unarmed")):
        #This version supports custom models
        BruM1="models/character/pc/male/brujah/armor0/brujah_male_armor_0.mdl"
        BruM2="models/character/pc/male/brujah/armor1/brujah_male_armor_1.mdl"
        BruM3="models/character/pc/male/brujah/armor2/brujah_male_armor_2.mdl"
        BruM4="models/character/pc/male/brujah/armor3/brujah_male_armor_3.mdl"
        BruF1="models/character/pc/female/brujah/armor0/brujah_female_armor_0.mdl"
        BruF2="models/character/pc/female/brujah/armor1/brujah_female_armor_1.mdl"
        BruF3="models/character/pc/female/brujah/armor2/brujah_female_armor_2.mdl"
        BruF4="models/character/pc/female/brujah/armor3/brujah_female_armor_3.mdl"
        GanM1="models/character/pc/male/gangrel/armor_0/Gangrel_Male_Armor_0.mdl"
        GanM2="models/character/pc/male/gangrel/armor_1/Gangrel_Male_Armor_1.mdl"
        GanM3="models/character/pc/male/gangrel/armor_2/Gangrel_Male_Armor_2.mdl"
        GanM4="models/character/pc/male/gangrel/armor_3/Gangrel_Male_Armor_3.mdl"
        GanF1="models/character/pc/female/gangrel/armor0/Gangrel_female_Armor_0.mdl"
        GanF2="models/character/pc/female/gangrel/armor1/Gangrel_female_Armor_1.mdl"
        GanF3="models/character/pc/female/gangrel/armor2/Gangrel_female_Armor_2.mdl"
        GanF4="models/character/pc/female/gangrel/armor3/Gangrel_female_Armor_3.mdl"
        MalM1="models/character/pc/male/malkavian/armor0/Malkavian_Male_Armor_0.mdl"
        MalM2="models/character/pc/male/malkavian/armor1/Malkavian_Male_Armor_1.mdl"
        MalM3="models/character/pc/male/malkavian/armor2/Malkavian_Male_Armor_2.mdl"
        MalM4="models/character/pc/male/malkavian/armor3/Malkavian_Male_Armor_3.mdl"
        MalF1="models/character/pc/female/malkavian/armor0/Malkavian_Female_Armor_0.mdl"
        MalF2="models/character/pc/female/malkavian/armor1/Malk_girl_Armor_1.mdl"
        MalF3="models/character/pc/female/malkavian/armor2/Malk_girl_Armor_2.mdl"
        MalF4="models/character/pc/female/malkavian/armor3/Malk_girl_Armor_3.mdl"
        NosM1="models/character/pc/male/nosferatu/armor0/Nosferatu.mdl"
        NosM2="models/character/pc/male/nosferatu/armor1/Nosferatu_Male_armor_1.mdl"
        NosM3="models/character/pc/male/nosferatu/armor2/Nosferatu_Male_armor_2.mdl"
        NosM4="models/character/pc/male/nosferatu/armor3/Nosferatu_Male_armor_3.mdl"
        NosF1="models/character/pc/female/nosferatu/armor0/nosferatu_Female_Armor_0.mdl"
        NosF2="models/character/pc/female/nosferatu/armor1/nosferatu_Female_Armor_1.mdl"
        NosF3="models/character/pc/female/nosferatu/armor2/nosferatu_Female_Armor_2.mdl"
        NosF4="models/character/pc/female/nosferatu/armor3/nosferatu_Female_Armor_3.mdl"
        TorM1="models/character/pc/male/toreador/armor0/toreador_Male_Armor_0.mdl"
        TorM2="models/character/pc/male/toreador/armor1/toreador_Male_Armor_1.mdl"
        TorM3="models/character/pc/male/toreador/armor2/toreador_Male_Armor_2.mdl"
        TorM4="models/character/pc/male/toreador/armor3/toreador_Male_Armor_3.mdl"
        TorF1="models/character/pc/female/toreador/armor0/toreador_Female_Armor_0.mdl"
        TorF2="models/character/pc/female/toreador/armor1/toreador_Female_Armor_1.mdl"
        TorF3="models/character/pc/female/toreador/armor2/toreador_Female_Armor_2.mdl"
        TorF4="models/character/pc/female/toreador/armor3/toreador_Female_Armor_3.mdl"
        TreM1="models/character/pc/male/tremere/armor0/tremere_Male_Armor_0.mdl"
        TreM2="models/character/pc/male/tremere/armor1/tremere_Male_Armor_1.mdl"
        TreM3="models/character/pc/male/tremere/armor2/tremere_Male_Armor_2.mdl"
        TreM4="models/character/pc/male/tremere/armor3/tremere_Male_Armor_3.mdl"
        TreF1="models/character/pc/female/tremere/armor0/tremere_Female_Armor_0.mdl"
        TreF2="models/character/pc/female/tremere/armor1/tremere_Female_Armor_1.mdl"
        TreF3="models/character/pc/female/tremere/armor2/tremere_Female_Armor_2.mdl"
        TreF4="models/character/pc/female/tremere/armor3/tremere_Female_Armor_3.mdl"
        VenM1="models/character/pc/male/ventrue/armor0/ventrue_Male_Armor_0.mdl"
        VenM2="models/character/pc/male/ventrue/armor1/ventrue_Male_Armor_1.mdl"
        VenM3="models/character/pc/male/ventrue/armor2/ventrue_Male_Armor_2.mdl"
        VenM4="models/character/pc/male/ventrue/armor3/ventrue_Male_Armor_3.mdl"
        VenF1="models/character/pc/female/ventrue/armor0/ventrue_Female_Armor_0.mdl"
        VenF2="models/character/pc/female/ventrue/armor1/ventrue_Female_Armor_1.mdl"
        VenF3="models/character/pc/female/ventrue/armor2/ventrue_Female_Armor_2.mdl"
        VenF4="models/character/pc/female/ventrue/armor3/ventrue_Female_Armor_3.mdl"
        #Beast="models/character/monster/animalism_beastform/animalism_beastform.mdl" #Protean
        if pc.model==BruM1 or pc.model==BruM2 or pc.model==BruM3 or pc.model==BruM4:
            clan=2
            gender=1
        elif pc.model==BruF1 or pc.model==BruF2 or pc.model==BruF3 or pc.model==BruF4:
            clan=2
        elif pc.model==GanM1 or pc.model==GanM2 or pc.model==GanM3 or pc.model==GanM4:
            clan=3
            gender=1
        elif pc.model==GanF1 or pc.model==GanF2 or pc.model==GanF3 or pc.model==GanF4:
            clan=3
        elif pc.model==MalM1 or pc.model==MalM2 or pc.model==MalM3 or pc.model==MalM4:
            clan=4
            gender=1
        elif pc.model==MalF1 or pc.model==MalF2 or pc.model==MalF3 or pc.model==MalF4:
            clan=4
        elif pc.model==NosM1 or pc.model==NosM2 or pc.model==NosM3 or pc.model==NosM4:
            clan=5
            gender=1
        elif pc.model==NosF1 or pc.model==NosF2 or pc.model==NosF3 or pc.model==NosF4:
            clan=5
        elif pc.model==TorM1 or pc.model==TorM2 or pc.model==TorM3 or pc.model==TorM4:
            clan=6
            gender=1
        elif pc.model==TorF1 or pc.model==TorF2 or pc.model==TorF3 or pc.model==TorF4:
            clan=6
        elif pc.model==TreM1 or pc.model==TreM2 or pc.model==TreM3 or pc.model==TreM4:
            clan=7
            gender=1
        elif pc.model==TreF1 or pc.model==TreF2 or pc.model==TreF3 or pc.model==TreF4:
            clan=7
        elif pc.model==VenM1 or pc.model==VenM2 or pc.model==VenM3 or pc.model==VenM4:
            clan=8
            gender=1
        elif pc.model==VenF1 or pc.model==VenF2 or pc.model==VenF3 or pc.model==VenF4:
            clan=8
        #elif pc.model==Beast:
        i = randint(1, 5)
        gender = pc.IsMale()                                                             
        clan = pc.clan
        if(gender == 1):
            #Human
            if(clan == 1 and i == 1): c.ArmsCrossed=""
            elif(clan == 1 and i == 2): c.Pissed=""
            elif(clan == 1 and i == 3): c.Pray=""
            elif(clan == 1 and i > 3): c.Lost=""
            #Brujah
            if(clan == 2 and i == 1): c.BruAnim2=""
            elif(clan == 2 and i == 2): c.BruAnim3=""
            elif(clan == 2 and i == 3): c.Lost=""
            elif(clan == 2 and i > 3): c.BruAnim1=""
            #Gangrel
            if(clan == 3 and i == 1): c.GanAnim3=""
            elif(clan == 3 and i == 2): c.GanAnim2=""
            if(clan == 3 and i == 3): c.Lost=""
            elif(clan == 3 and i > 2): c.GanAnim1=""
            #Malkavian
            if(clan == 4 and i == 1): c.MalAnim2=""
            elif(clan == 4 and i == 2): c.Lost=""
            elif(clan == 4 and i == 3): c.Jittery=""
            elif(clan == 4 and i > 3): c.MalAnim1=""
            #Nosferatu
            if(clan == 5 and i == 1): c.NosAnim2=""
            elif(clan == 5 and i == 2): c.NosAnim3=""
            elif(clan == 5 and i == 3): c.Lost=""
            elif(clan == 5 and i > 3): c.NosAnim1=""
            #Toreador
            if(clan == 6 and i == 1): c.TorAnim2=""
            elif(clan == 6 and i == 2): c.TorAnim3=""
            elif(clan == 6 and i == 3): c.TorAnim4=""
            elif(clan == 6 and i == 4): c.Lost=""
            elif(clan == 6 and i > 4): c.TorAnim1=""
            #Tremere
            if(clan == 7 and i == 1): c.TreAnim2=""
            elif(clan == 7 and i == 2): c.TreAnim3=""
            elif(clan == 7 and i == 3): c.Lost=""
            elif(clan == 7 and i > 3): c.TreAnim1=""
            #Ventrue
            if(clan == 8 and i == 1): c.VenAnim2=""
            elif(clan == 8 and i == 2): c.VenAnim3=""
            elif(clan == 8 and i == 3): c.Lost=""
            elif(clan == 8 and i > 3): c.VenAnim1=""
        elif(gender == 0):
            #Human
            if(clan == 1 and i == 1): c.ArmsCrossed=""
            elif(clan == 1 and i == 2): c.Pissed=""
            elif(clan == 1 and i == 3): c.Pray=""
            elif(clan == 1 and i > 3): c.Lost=""
            #Brujah
            if(clan == 2 and i == 1): c.BrufemAnim2=""
            elif(clan == 2 and i == 2): c.BrufemAnim2=""
            elif(clan == 2 and i == 3): c.Lost=""
            elif(clan == 2 and i > 3): c.BrufemAnim1=""
            #Gangrel
            if(clan == 3 and i == 1): c.GanfemAnim1=""
            elif(clan == 3 and i == 2): c.Lost=""
# disabled by wesp            elif(clan == 3 and i > 2): c.GanfemAnim2=""
            #Malkavian
            if(clan == 4 and i == 1): c.MalfemAnim2=""
            elif(clan == 4 and i == 2): c.MalfemAnim3=""
            elif(clan == 4 and i == 3): c.MalfemAnim4=""
            elif(clan == 4 and i == 4): c.Lost=""
            elif(clan == 4 and i > 4): c.MalfemAnim1=""
            #Nosferatu
            if(clan == 5 and i == 1): c.NosfemAnim2=""
            elif(clan == 5 and i == 2): c.NosfemAnim3=""
            elif(clan == 5 and i == 3): c.Lost=""
            elif(clan == 5 and i > 3): c.NosfemAnim1=""
            #Toreador
            if(clan == 6 and i == 1): c.TorfemAnim2=""
            elif(clan == 6 and i == 2): c.TorfemAnim3=""
            elif(clan == 6 and i == 3): c.Lost=""
            elif(clan == 6 and i > 3): c.TorfemAnim1=""
            #Tremere
            if(clan == 7 and i == 1): c.TrefemAnim2=""
            elif(clan == 7 and i == 2): c.TrefemAnim3=""
            elif(clan == 7 and i == 3): c.Lost=""
            elif(clan == 7 and i > 3): c.TrefemAnim1=""
            #Ventrue
            if(clan == 8 and i == 1): c.VenfemAnim2=""
            elif(clan == 8 and i == 2): c.VenfemAnim3=""
            elif(clan == 8 and i == 3): c.Lost=""
            elif(clan == 8 and i > 3): c.VenfemAnim1=""
#Durations - unused, but kept them if needed in future
#Brujah_HitHands2		1.30
#Brujah_Female_ArmOut2		4.00
#Gangrel_Sniff2			4.50
#Gangrel_Female_Nails1		3.20
#Malkavian_Look2		3.85
#Malk_Female_Stretch2		5.50
#Nos_Howl2			2.50
#Nos_Female_Howl2		2.50
#Toreador_Checknails2		3.22
#Toreador_Female_Nails2		4.35
#Tremere_Rubhands2		5.00
#Tremere_Female_Think2		5.80
#Ventrue_CheckNails2		3.25
#Ventrue_Female_Sexy2		4.90
#Brujah_Bringit2		2.90
#Gangrel_Look2			4.50
#Gangrel_Female_Stretch2	5.50
#Malk_Female_Bend2		5.00
#Nos_Crouch2			5.20
#Nos_Female_Crouch2		5.20
#Toreador_Posing2		3.90
#Toreador_Female_Hair2		3.20
#Tremere_Spell2			5.00
#Tremere_Female_Spell2		5.00
#Ventrue_PhoneCall2		9.90
#Ventrue_Female_Nails2		4.15
#Brujah_Idle2			1.90
#Gangrel_Idle2			2.40
#Malkavian_Idle2		1.90
#Nos_Idle2			2.20
#Toreador_Idle2			2.00
#Tremere_Idle2			2.00
#Ventrue_Idle2			2.00
#Brujah_Female_Idle2		4.00
#Gangrel_Female_Idle2		2.00
#Malk_Female_Idle2		3.00
#Nos_Female_Idle2		2.20
#toreador_Female_Idle2		2.00
#Tremere_Female_Idle2		2.00
#Ventrue_Female_Idle2		2.00
#Malk_Female_Sultry2		11.00
#Toreador_FixHair2		3.07
    elif(notIdle == 0 and pc.active_protean > 1 and pc.HasWeaponEquipped("item_w_unarmed")):
        i = randint(1, 6)
        if(i == 1): c.Howl=""
#        elif(i == 2):
#            c.Alert_Front_into=""
#            ST(3.00,'__main__.ccmd.Alert_Front_outof=""')
#        elif(i == 3):
#            c.Alert_90l_into=""
#            ST(3.00,'__main__.ccmd.Alert_90l_outof=""')
#        elif(i == 4):
#            c.Alert_90r_into=""
#            ST(3.00,'__main__.ccmd.Alert_90r_outof=""')
#        elif(i == 5):
#            c.Alert_180_into=""
#            ST(3.00,'__main__.ccmd.Alert_180_outof=""')
        elif(i == 6): c.Alert_Lookaround=""
    elif G.Delay != 0:
        G.Delay = G.Delay - 1
#    timer = __main__.FindEntityByName("idle_timer")
#    if timer: timer.Enable()

#Adds random whispers to malkavian lookaround animation, "Ambiguous" or "Danger", added by Entenschreck, changed by wesp
def RandomWhisper():
    pc = __main__.FindPlayer()
    if not (__main__.IsClan(pc, "Malkavian") or __main__.G.Player_Insane == 1):
        return
    print "Selecting Whisper"
    NonHostile = 0
    #Disallow Danger whispers in these areas:
    if Find("Caine"): NonHostile=1
    elif Find("Cabbie"): NonHostile=1
    elif Find("haven_pc"): NonHostile=1
    elif Find("ox"): NonHostile=1
    elif Find("WongHo"): NonHostile=1
    elif Find("Isaac"): NonHostile=1
    elif Find("Damsel"): NonHostile=1
    elif Find("Slater"): NonHostile=1
    elif Find("VV"): NonHostile=1
    elif Find("plus_DJ"): NonHostile=1
    elif Find("Carson_Computer"): NonHostile=1
    elif Find("Vandal"): NonHostile=1
    elif Find("Victor"): NonHostile=1   
    if NonHostile == 1 and __main__.G.InCombat == 0:
        print "Nonhostile area"
        i = randint(0,5)
        if i == 0: pc.Whisper("Crying")
        elif i == 1: pc.Whisper("Gibberish")
        elif i == 2: pc.Whisper("Moaning")
        else: pc.Whisper("Ambiguous")
    else:
        print "Hostile area"
        i = randint(0,5)
        if i == 0: pc.Whisper("Crying")
        elif i == 1: pc.Whisper("Gibberish")
        elif i == 2: pc.Whisper("Moaning")
        else: pc.Whisper("Danger")

#Called by "events_player_plus", added by EntenSchreck
def OnActivateThaumLvl2():
    print "Thaumaturgy Level 2 activated"
def OnActivateThaumLvl1():
    print "Thaumaturgy Level 1 activated"
def OnActivateDominateLvl2():
    print "Dominate Level 2 activated"
def OnActivateDominateLvl1():
    print "Dominate Level 1 activated"
def OnActivateDementationLvl2():
    print "Dementation Level 2 activated"
def OnActivateDementationLvl1():
    print "Dementation Level 1 activated"
def OnActivateAnimalismLvl2():
    print "Animalism Level 2 activated"
def OnActivateAnimalismLvl1():
    print "Animalism Level 1 activated"
def OnActivatePresence():
    print "Presence Level %s activated" % __main__.FindPlayer().base_presence
def OnWolfMorphBegin():
    print "Wolf Morph Begin"
def OnWolfMorphEnd():
    print "Wolf Morph End"
def OnActivateCelerity():
    print "Celerity Level %s activated" % __main__.FindPlayer().base_celerity
def OnActivatePotence():
    print "Potence Level %s activated" % __main__.FindPlayer().base_potence
def OnActivateObfuscate():
    print "Obfuscate Level %s activated" % __main__.FindPlayer().base_obfuscate
def OnActivateFortitude():
    print "Fortitude Level %s activated" % __main__.FindPlayer().base_fortitude
def OnActivateAuspex():
    print "Auspex Level %s activated" % __main__.FindPlayer().base_auspex
def OnActivateProtean():
    print "Protean Level %s activated" % __main__.FindPlayer().base_protean
    if __main__.FindPlayer().base_protean == 5:
        __main__.ScheduleTask(2.0,"__main__.ccmd.setClaws=\"\"")
        __main__.ScheduleTask(2.2,"__main__.ccmd.useClaws=\"\"")
def OnFrenzyBegin():
    print "Frenzy Begin"
    pc = __main__.FindPlayer()
    if pc.HasItem("item_w_tzimisce2_head"):
        pc.RemoveItem("item_w_tzimisce2_head")
    if pc.HasItem("item_i_written"):
        pc.RemoveItem("item_i_written")
# added by EntenSchreck to correct Frenzy stats
    if __main__.G.Patch_Plus == 1:
        f=FindClass("Npc_VFrenzyShadow")[0]    #This is the frenzying clone
        if f:
            f.SetName("FrenzyShadow")
            f.SetScriptedDiscipline("Corpus_Vampirus 2")
            if IsClan(pc, "Gangrel"):
                f.SetScriptedDiscipline("Corpus_Vampirus 3")
def OnFrenzyEnd():
    print "Frenzy End"
def OnPlayerKilled():
    print "Player Dead"
def OnPlayerTookDamage():
    print "Took Damage"

#Called by events_world, added by EntenSchreck
def OnCopsOutside():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnCopsComing():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnStartCopPursuitMode():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnStartCopAlertMode():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnEndCopPursuitMode():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnEndCopAlertMode():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnStartHunterPursuitMode():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnEndHunterPursuitMode():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnMasqueradeLevel1():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnMasqueradeLevel2():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnMasqueradeLevel3():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnMasqueradeLevel4():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnMasqueradeLevel5():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnMasqueradeLevelChanged():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnPlayerHasNoBlood():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnCombatMusicStart():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnCombatMusicEnd():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnAlertMusicStart():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnAlertMusicEnd():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnNormalMusicStart():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnNormalMusicEnd():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnUseBegin():
    if (__main__.G.Patch_Plus == 1):
        pass
def OnUseEnd():
    if (__main__.G.Patch_Plus == 1):
        pass

#Athletics Feat, added by EntenSchreck, unused at the moment
def CalcFeat_Athletics():
    pc   = __main__.FindPlayer()
    cvar = __main__.cvar
    #default values:
    #sv_rollangle 2
    #sv_runscale 1.00
    #sv_sneakscale 2.1
    if pc.CalcFeat("Jumping") == 1:
        cvar.sv_runscale="0.80"
        cvar.sv_rollangle="1"
        cvar.sv_sneakscale="1.55"
    elif pc.CalcFeat("Jumping") == 2:
        cvar.sv_runscale="0.90"
        cvar.sv_rollangle="2"
        cvar.sv_sneakscale="1.7"
    elif pc.CalcFeat("Jumping") == 3:
        cvar.sv_runscale="1.00"
        cvar.sv_rollangle="3"
        cvar.sv_sneakscale="1.85"
    elif pc.CalcFeat("Jumping") == 4:
        cvar.sv_runscale="1.10"
        cvar.sv_rollangle="4"
        cvar.sv_sneakscale="2.0"
    elif pc.CalcFeat("Jumping") == 5:
        cvar.sv_runscale="1.15"
        cvar.sv_rollangle="5"
        cvar.sv_sneakscale="2.2"
    elif pc.CalcFeat("Jumping") == 6:
        cvar.sv_runscale="1.20"
        cvar.sv_rollangle="6"
        cvar.sv_sneakscale="2.4"
    elif pc.CalcFeat("Jumping") == 7:
        cvar.sv_runscale="1.25"
        cvar.sv_rollangle="7"
        cvar.sv_sneakscale="2.6"
    elif pc.CalcFeat("Jumping") == 8:
        cvar.sv_runscale="1.30"
        cvar.sv_rollangle="8"
        cvar.sv_sneakscale="2.8"
    elif pc.CalcFeat("Jumping") == 9:
        cvar.sv_runscale="1.35"
        cvar.sv_rollangle="9"
        cvar.sv_sneakscale="3.0"
    elif pc.CalcFeat("Jumping") == 10:
        cvar.sv_runscale="1.40"
        cvar.sv_rollangle="10"
        cvar.sv_sneakscale="3.2"
    #Just in case...
    elif pc.CalcFeat("Jumping") == 11:
        cvar.sv_runscale="1.45"
        cvar.sv_rollangle="10"
        cvar.sv_sneakscale="3.4"
    elif pc.CalcFeat("Jumping") == 12:
        cvar.sv_runscale="1.50"
        cvar.sv_rollangle="10"
        cvar.sv_sneakscale="3.5"

#Animal Friendship Feat, added by EntenSchreck, unused at the moment
#zur Aktivierung: Animal_Friendship.AnimalRadar()
from __main__ import Character
def _Near(self,loc,r=200):
    # Avoid square root function. very inefficient
    # if (Distance)^2 > (x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2
    loc2=self.GetOrigin()
    xd=loc2[0]-loc[0]
    yd=loc2[1]-loc[1]
    zd=loc2[2]-loc[2]
    return (r*r) > (xd*xd) + (yd*yd) + (zd*zd)
Character.Near=_Near
#makes animals deaf and blind...
def BefriendAnimal(animal):
    animal.SetRelationship("player D_LI 5")
    animal.TweakParam("hearing 0.00")
    animal.TweakParam("vision 0.00")
    animal.pl_investigate=0
    animal.pl_criminal_flee=0
    animal.pl_criminal_attack=0
    animal.pl_supernatural_flee=0
    animal.pl_supernatural_attack=0
    animal.SetInvestigateMode(0)
    animal.SetInvestigateModeCombat(0)
    print "Befriending Animal"
    #print(animal)
#Dogs' Reaction
def OnDogFoundPlayer(Dog):
    print("OnDogFoundPlayer() called by:")
    print(Dog)
    Dog.SetRelationship("player D_NU 0")
    Dog.ChangeSchedule("SCHED_VDOG_SNARL")
def AnimalRadar():
    pc = __main__.FindPlayer()
    PlayerPos = pc.GetOrigin()
    rats=FindClass("Npc_VRat")
    for r in rats:
        if r.Near(pc.GetOrigin(),r.detection_distance) == 1:
            AnimalFriendship(r,1,r.friendship_level)
    cats=FindClass("Npc_VAnimal") #TEMPORARY
    for c in cats:
        if c.Near(pc.GetOrigin(),c.warn_range) == 1:
            AnimalFriendship(r,1,c.friendship_level)
    dogs=FindClass("Npc_VDog")
    for d in dogs:
        if d.Near(pc.GetOrigin(),d.warn_range) == 1:
            #d.ChangeSchedule("SCHED_VDOG_SNARL")
            AnimalFriendship(r,1,d.friendship_level)
def AnimalFriendship(Name,Animal,FriendshipLevel=0):
    pc = __main__.FindPlayer()
    G  = __main__.G
    #Level=pc.CalcFeat("Animal_Friendship")
    #Level=pc.base_charisma+pc.base_seduction
    Level = 10 #TEST
    #Rat
    if Animal == 1:
        if Level >= FriendshipLevel or Level == FriendshipLevel:
            BefriendAnimal(Name)
    #Cat
    if Animal == 2:
        if Level >= FriendshipLevel or Level == FriendshipLevel:
            BefriendAnimal(Name)
            # call scripted_sequence "sit" here!
        else:
            pass
            # call scripted_sequence "cower" here!
    #Dog
    if Animal == 3:
        AnimalName = "%s" % Name
        print(AnimalName)
        if Level >= FriendshipLevel or Level == FriendshipLevel:
            BefriendAnimal(Name)
            Find(AnimalName).ChangeSchedule("SCHED_VDOG_MADEFRIEND")
            E = Find("plus_befriend_"+AnimalName)
            if E: E.BeginSequence()
            E = Find(AnimalNamee+"_hurt")
            if E: E.Disable()
        else:
            Find(AnimalName).ChangeSchedule("SCHED_VDOG_SNARL")
    #Zombie
    if Animal == 4:
        if Level >= FriendshipLevel or Level == FriendshipLevel:
            BefriendAnimal(Name)

#Map patch error messages fix, by Psycho-A
def ch_cloud_1_patch():
	print "map patcher loaded"
	# some actions...
def ch_dragon_1_patch():
	print "map patcher loaded"
	# some actions...
def ch_fishmarket_1_patch():
	print "map patcher loaded"
	# some actions...
def ch_fulab_1_patch():
	print "map patcher loaded"
	# some actions...
def ch_glaze_1_patch():
	print "map patcher loaded"
	# some actions...
def ch_hub_1_patch():
	print "map patcher loaded"
	# some actions...
def ch_lotus_1_patch():
	print "map patcher loaded"
	# some actions...
def ch_ramen_1_patch():
	print "map patcher loaded"
	# some actions...
def ch_shrekhub_patch():
	print "map patcher loaded"
	# some actions...
def ch_temple_1_patch():
	print "map patcher loaded"
	# some actions...
def ch_temple_2_patch():
	print "map patcher loaded"
	# some actions...
def ch_temple_3_patch():
	print "map patcher loaded"
	# some actions...
def ch_temple_4_patch():
	print "map patcher loaded"
	# some actions...
def ch_tsengs_1_patch():
	print "map patcher loaded"
	# some actions...
def ch_zhaos_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_609_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_ash_sewer_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_asphole_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_cemetery_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_chinese_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_hub_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_jewelry_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_luckystar_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_metalhead_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_netcafe_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_redspot_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_sinbin_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_tawni_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_vesuvius_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_warrens_1_patch():
	print "map patcher loaded"
	# some actions...
def hw_warrens_2_patch():
	print "map patcher loaded"
	# some actions...
def hw_warrens_2b_patch():
	print "map patcher loaded"
	# some actions...
def hw_warrens_3_patch():
	print "map patcher loaded"
	# some actions...
def hw_warrens_4_patch():
	print "map patcher loaded"
	# some actions...
def hw_warrens_5_patch():
	print "map patcher loaded"
	# some actions...
def la_abandoned_building_1_patch():
	print "map patcher loaded"
	# some actions...
def la_bradbury_1_patch():
	print "map patcher loaded"
	# some actions...
def la_bradbury_2_patch():
	print "map patcher loaded"
	# some actions...
def la_bradbury_3_patch():
	print "map patcher loaded"
	# some actions...
def la_chantry_1_patch():
	print "map patcher loaded"
	# some actions...
def la_confession_1_patch():
	print "map patcher loaded"
	# some actions...
def la_crackhouse_1_patch():
	print "map patcher loaded"
	# some actions...
def la_dane_1_patch():
	print "map patcher loaded"
	# some actions...
def la_empire_1_patch():
	print "map patcher loaded"
	# some actions...
def la_empire_2_patch():
	print "map patcher loaded"
	# some actions...
def la_empire_3_patch():
	print "map patcher loaded"
	# some actions...
def la_expipe_1_patch():
	print "map patcher loaded"
	# some actions...
def la_hospital_1_patch():
	print "map patcher loaded"
	# some actions...
def la_hub_1_patch():
	print "map patcher loaded"
	# some actions...
def la_library_1_patch():
	print "map patcher loaded"
	# some actions...
def la_malkavian_1_patch():
	print "map patcher loaded"
	# some actions...
def la_malkavian_2_patch():
	print "map patcher loaded"
	# some actions...
def la_malkavian_3_patch():
	print "map patcher loaded"
	# some actions...
def la_malkavian_3b_patch():
	print "map patcher loaded"
	# some actions...
def la_malkavian_4_patch():
	print "map patcher loaded"
	# some actions...
def la_malkavian_5_patch():
	print "map patcher loaded"
	# some actions...
def la_museum_1_patch():
	print "map patcher loaded"
	# some actions...
def la_parkinggarage_1_patch():
	print "map patcher loaded"
	# some actions...
def la_plaguebearer_sewer_1_patch():
	print "map patcher loaded"
	# some actions...
def la_skyline_1_patch():
	print "map patcher loaded"
	# some actions...
def la_ventruetower_1_patch():
	print "map patcher loaded"
	# some actions...
def la_ventruetower_1b_patch():
	print "map patcher loaded"
	# some actions...
def la_ventruetower_2_patch():
	print "map patcher loaded"
	# some actions...
def la_ventruetower_3_patch():
	print "map patcher loaded"
	# some actions...
def sm_apartment_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_apartment_1b_patch():
	print "map patcher loaded"
	# some actions...
def sm_asylum_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_bailbonds_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_bailbonds_1_patch_patch():
	print "map patcher loaded"
	# some actions...
def sm_basement_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_beachhouse_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_coffee_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_diner_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_gallery_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_hub_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_hub_2_patch():
	print "map patcher loaded"
	# some actions...
def sm_junkyard_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_medical_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_oceanhouse_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_oceanhouse_2_patch():
	print "map patcher loaded"
	# some actions...
def sm_pawnshop_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_pawnshop_2_patch():
	print "map patcher loaded"
	# some actions...
def sm_pier_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_shreknet_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_smoke_1_patch():
	print "map patcher loaded"
	# some actions...
def sm_tattoo_patch():
	print "map patcher loaded"
	# some actions...
def sm_vamparena_patch():
	print "map patcher loaded"
	# some actions...
def sm_warehouse_1_patch():
	print "map patcher loaded"
	# some actions...
def sp_endsequences_a_patch():
	print "map patcher loaded"
	# some actions...
def sp_endsequences_b_patch():
	print "map patcher loaded"
	# some actions...
def sp_epilogue_patch():
	print "map patcher loaded"
	# some actions...
def sp_genesisdevice_1_patch():
	print "map patcher loaded"
	# some actions...
def sp_giovanni_1_patch():
	print "map patcher loaded"
	# some actions...
def sp_giovanni_2a_patch():
	print "map patcher loaded"
	# some actions...
def sp_giovanni_2b_patch():
	print "map patcher loaded"
	# some actions...
def sp_giovanni_3_patch():
	print "map patcher loaded"
	# some actions...
def sp_giovanni_4_patch():
	print "map patcher loaded"
	# some actions...
def sp_giovanni_5_patch():
	print "map patcher loaded"
	# some actions...
def sp_masquerade_1_patch():
	print "map patcher loaded"
	# some actions...
def sp_ninesintro_patch():
	print "map patcher loaded"
	# some actions...
def sp_observatory_1_patch():
	print "map patcher loaded"
	# some actions...
def sp_observatory_2_patch():
	print "map patcher loaded"
	# some actions...
def sp_soc_1_patch():
	print "map patcher loaded"
	# some actions...
def sp_soc_2_patch():
	print "map patcher loaded"
	# some actions...
def sp_soc_3_patch():
	print "map patcher loaded"
	# some actions...
def sp_soc_4_patch():
	print "map patcher loaded"
	# some actions...
def sp_taxiride_patch():
	print "map patcher loaded"
	# some actions...
def sp_theatre_patch():
	print "map patcher loaded"
	# some actions...
def sp_tutorial_1_patch():
	print "map patcher loaded"
	# some actions...

##############################################################################
# General Utility Functions
##############################################################################

def Whisper(soundfile):
    from __main__ import pc
    pc.Whisper(soundfile)

def GiveItem(char, ItemName):
    char.GiveItem(ItemName)

def HasItem(char, ItemName):
    return char.HasItem(ItemName)

def RemoveItem(char, ItemName):
    char.RemoveItem(ItemName)

def FrenzyTrigger(char):
    char.FrenzyTrigger(1)

def IsClan(char, ClanName):
    if (char.clan == 0 and ClanName == "None"):
        return 1
    elif (char.clan == 2 and ClanName == "Brujah"):
        return 1
    elif (char.clan == 3 and ClanName == "Gangrel"):
        return 1
    elif (char.clan == 4 and ClanName == "Malkavian"):
        return 1
    elif (char.clan == 5 and ClanName == "Nosferatu"):
        return 1
    elif (char.clan == 6 and ClanName == "Toreador"):
        return 1
    elif (char.clan == 7 and ClanName == "Tremere"):
        return 1
    elif (char.clan == 8 and ClanName == "Ventrue"):
        return 1
    return 0

def IsMale(char):
    return char.IsMale()

def IsDead(charname):
    return __main__.G.morgue.has_key(charname)

def MarkAsDead(charname):
    __main__.G.morgue[charname] = 1

def CheckFrenzy(char, value):
    char.FrenzyCheck(value)
    return None

def NumTimesTalkedTo(num):
    if ( npc.times_talked == num ):
        return 1
    else:
        return 0

def RandomLine( NumList ):
    R = Random( time() )
    Index = R.randint(0, len(NumList)-1)
    return NumList[Index]

#Called on the hubs (and possibly other maps?) to place hunters if the player violates the masquerade
def checkMasquerade():
    level = __main__.FindPlayer().GetMasqueradeLevel()
    print "level %i" % level
    if(level >= 2 and level < 5):
        #changed by dan_upright 07/12/04
        G = __main__.G
        if (G.In_Hollywood != 1 or G.Courier_QuickBuck != 1):
            i = 2
            while(i <= level):
                if(huntersDead[i - 2] == 0):
                    spawner = Find("hunter_maker_%i" % (i - 1))
                    spawner.Spawn()
                i = i + 1
        #changes end

#Spawns in the appropriate cop car given the input
def spawnCopCar(i):
    ent = Find("cop_car_%i" % (i))
    if ent: ent.ScriptUnhide()
    ent = Find("cop_front_%i" % (i))
    if ent: ent.Spawn()
    ent = Find("cop_rear_%i" % (i))
    if ent: ent.Spawn()
    ent = Find("red%i" % (i))
    if ent: ent.TurnOn()
    ent = Find("blue%i" % (i))
    if ent: ent.TurnOn()
    ent = Find("cover_front_%i" % (i))
    if ent: ent.ScriptUnhide()
    ent = Find("cover_rear_%i" % (i))
    if ent: ent.ScriptUnhide()

#Removes cop cars that may have been spawned onto the map previously argument specifies the total number of cop cars on the given hub
def removeCopCar(total):
    i = 1
    while(i <= total):
       ent = Find("cop_car_%i" % (i))
       if ent: ent.ScriptHide()
       ent = Find("red%i" % (i))
       if ent: ent.TurnOff()
       ent = Find("blue%i" % (i))
       if ent: ent.TurnOff()
       ent = Find("cover_front_%i" % (i))
       if ent: ent.ScriptHide()
       ent = Find("cover_rear_%i" % (i))
       if ent: ent.ScriptHide()
       i = i + 1
    cops = FindList("stake_out_cop")
    for cop in cops:
        cop.Kill()
    cops = FindList("cop")
    for cop in cops:
        cop.Kill()
    cops = FindList("patrol_cop_1")
    for cop in cops:
        cop.Kill()
    cops = FindList("patrol_cop_2")
    for cop in cops:
        cop.Kill()

#Returns the distanceSquared between two 3D points
def distanceSquared(p1, p2):
    xDistance = (p1[0] - p2[0]) * (p1[0] - p2[0])
    yDistance = (p1[1] - p2[1]) * (p1[1] - p2[1])
    zDistance = (p1[2] - p2[2]) * (p1[2] - p2[2])
    return (xDistance + yDistance + zDistance)

#Starts the BloodDoll on a random line
def doll1dlg():
    doll = Find("Doll1")
    if(__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
        return 121
    elif(__main__.G.Doll_Seduce == 1):
        return 91
    else:
        return RandomLine([1, 31, 61])

#HAVEN: Called if heather should change her skin, added by vladdmaster
def heatherSkin():
    G = __main__.G
    IsDead = __main__.IsDead
    heather = Find("Heather")
    if(G.Heather_Outfit == 1):
        heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather_goth.mdl")
    elif(G.Heather_Outfit == 2):
        heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather_3.mdl")
    else:
        heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather.mdl")
    G.Heather_Clothes = 0

#HAVEN: Used to place heather in the various player havens, changed by wesp and vladdmaster
def heatherHavenP():
    G = __main__.G
    IsDead = __main__.IsDead
    heather = Find("Heather")
    if(G.Heather_Haven and not IsDead("Heather") and heather):
        heather.ScriptUnhide()
    if((G.Heather_Gone or (G.Story_State >= 75 and G.Heather_Indoors == 0 and G.Player_Sabbat < 3)) and heather):
        heather.ScriptHide()
    if(G.Story_State >= 30 and G.Heather_Haven and not IsDead("Heather") and G.Heather_Gone == 0 and G.Story_State < 75 and not G.Heather_Lure):
        G.Mcfly_Present = 1
        mcfly = Find("McFly")
        if mcfly: mcfly.ScriptUnhide()
    if(G.Mcfly_Leave or G.Mcfly_Feed or G.Mcfly_Dominated or G.Mcfly_Dementated or IsDead("McFly")):
        mcfly = Find("McFly")
        if mcfly: mcfly.Kill()
    if(G.Heather_Clothes and heather):
        if not(G.Prince_Skyline or G.Gary_Haven or G.Regent_Family == 3):
            heatherSkin()
#        G.Heather_Outfit = G.Heather_Outfit + 1
#        if(G.Heather_Outfit > 2):
#            G.Heather_Outfit = 0
        G.Heather_Clothes = 0
    if(IsDead("Heather") and heather):
        heather.Kill()
        mcfly = Find("mcfly")
        if mcfly: mcfly.Kill()

#HAVEN: Used to place heather in the various player havens, changed by wesp and vladdmaster
def heatherHavenS():
    G = __main__.G
    IsDead = __main__.IsDead
    heather = Find("Heather")
    if(G.Heather_Haven and not IsDead("Heather") and heather):
        heather.ScriptUnhide()
    if((G.Heather_Gone or (G.Story_State >= 75 and G.Heather_Indoors == 0 and G.Player_Sabbat < 3)) and heather):
        heather.ScriptHide()
    if(G.Story_State >= 30 and G.Heather_Haven and not IsDead("Heather") and G.Heather_Gone == 0 and G.Story_State < 75 and not G.Heather_Lure):
        G.Mcfly_Present = 1
        mcfly = Find("McFly")
        if mcfly: mcfly.ScriptUnhide()
    if(G.Mcfly_Leave or G.Mcfly_Feed or G.Mcfly_Dominated or G.Mcfly_Dementated or IsDead("McFly")):
        mcfly = Find("McFly")
        if mcfly: mcfly.Kill()
    if(G.Heather_Clothes and heather):
        if (G.Prince_Skyline):
            heatherSkin()
#        G.Heather_Outfit = G.Heather_Outfit + 1
#        if(G.Heather_Outfit > 2):
#            G.Heather_Outfit = 0
        G.Heather_Clothes = 0
    if(IsDead("Heather") and heather):
        heather.Kill()
        mcfly = Find("mcfly")
        if mcfly: mcfly.Kill()

#HAVEN: Used to place heather in the various player havens, changed by wesp and vladdmaster
def heatherHavenC():
    G = __main__.G
    if(G.Story_State >= 100 and G.Regent_Ending == 0):
        doorl = Find("chantry_door_left")
        doorl.Lock()
        doorr = Find("chantry_door_right")
        doorr.Lock()
    IsDead = __main__.IsDead
    heather = Find("Heather")
    if(G.Heather_Haven and not IsDead("Heather") and heather):
        heather.ScriptUnhide()
    if((G.Heather_Gone or (G.Story_State >= 75 and G.Heather_Indoors == 0 and G.Player_Sabbat < 3)) and heather):
        heather.ScriptHide()
    if(G.Story_State >= 30 and G.Heather_Haven and not IsDead("Heather") and G.Heather_Gone == 0 and G.Story_State < 75 and not G.Heather_Lure):
        G.Mcfly_Present = 1
        mcfly = Find("McFly")
        if mcfly: mcfly.ScriptUnhide()
    if(G.Mcfly_Leave or G.Mcfly_Feed or G.Mcfly_Dominated or G.Mcfly_Dementated or IsDead("McFly")):
        mcfly = Find("McFly")
        if mcfly: mcfly.Kill()
    if(G.Heather_Clothes and heather):
        if (G.Regent_Family == 3):
            heatherSkin()
#        G.Heather_Outfit = G.Heather_Outfit + 1
#        if(G.Heather_Outfit > 2):
#            G.Heather_Outfit = 0
        G.Heather_Clothes = 0
    if(IsDead("Heather") and heather):
        heather.Kill()
        mcfly = Find("mcfly")
        if mcfly: mcfly.Kill()

#HAVEN: Used to place heather in the various player havens, changed by wesp and vladdmaster
def heatherHavenN():
    G = __main__.G
    IsDead = __main__.IsDead
    heather = Find("Heather")
    if(G.Heather_Haven and not IsDead("Heather") and heather):
        heather.ScriptUnhide()
    if((G.Heather_Gone or (G.Story_State >= 75 and G.Heather_Indoors == 0 and G.Player_Sabbat < 3)) and heather):
        heather.ScriptHide()
    if(G.Story_State >= 30 and G.Heather_Haven and not IsDead("Heather") and G.Heather_Gone == 0 and G.Story_State < 75 and not G.Heather_Lure):
        G.Mcfly_Present = 1
        mcfly = Find("McFly")
        if mcfly: mcfly.ScriptUnhide()
    if(G.Mcfly_Leave or G.Mcfly_Feed or G.Mcfly_Dominated or G.Mcfly_Dementated or IsDead("McFly")):
        mcfly = Find("McFly")
        if mcfly: mcfly.Kill()
    if(G.Heather_Clothes and heather):
        if (G.Gary_Haven):
            heatherSkin()
#        G.Heather_Outfit = G.Heather_Outfit + 1
#        if(G.Heather_Outfit > 2):
#            G.Heather_Outfit = 0
        G.Heather_Clothes = 0
    if(IsDead("Heather") and heather):
        heather.Kill()
        mcfly = Find("mcfly")
        if mcfly: mcfly.Kill()

#HAVEN: Called to see if Heather needs to leave the haven
def heatherLeaves():
    G = __main__.G
    if(G.Heather_Gone):
        relay = Find("heather_leaves_relay")
        relay.Trigger()

#HAVEN: Called to see if McFly leaves
def mcflyDialog():
    G = __main__.G
    if(G.Mcfly_Leave or G.Mcfly_Dominated or G.Mcfly_Dementated):
        relay = Find("mcfly_leaves_relay")
        relay.Trigger()

#HAVEN: Used for mailbox events for email quests at the haven, changed by wesp
def putStuffInMailBox():
    mailbox = Find("mailbox_haven")
    if mailbox:
        G = __main__.G
        if(G.Shubs_Email == 1 and G.Shubs_Email_Read < 1):
            mailbox.SpawnItemInContainer("item_k_shrekhub_one_key")
            G.Shubs_Email_Read = 1
        elif(G.Shubs_Email == 2 and G.Shubs_Email_Read < 2):
            mailbox.SpawnItemInContainer("item_g_wireless_camera_1")
            G.Shubs_Email_Read = 2
        elif(G.Shubs_Email == 3 and G.Shubs_Email_Read < 3):
            mailbox.SpawnItemInContainer("item_k_shrekhub_three_key")
            G.Shubs_Email_Read = 3
        elif(G.Shubs_Email == 4 and G.Shubs_Email_Read < 4):
            mailbox.SpawnItemInContainer("item_k_shrekhub_four_key")
            G.Shubs_Email_Read = 4

#HAVEN: Used to determine if the player has collected any posters, changed by wesp
def posterCheck():
    G = __main__.G
    newgame = Find("newgame")
    if (newgame and G.Haven_Empty == 1):
        print "no posters"
        if(G.Gary_Voerman):
            poster = Find("poster_jeanette")
            poster.ScriptHide()
        if(G.Velvet_Poster):
            poster = Find("poster_vv")
            poster.ScriptHide()
        if(G.Gary_Photochop):
            poster = Find("poster_ming")
            poster.ScriptHide()
        if(G.Gary_Damsel):
            poster = Find("poster_damsel")
            poster.ScriptHide()
        if(G.Gary_Tawni):
            poster = Find("poster_tawni")
            poster.ScriptHide()
        if(G.Gary_Imalia):
            poster = Find("poster_imalia")
            poster.ScriptHide()
        if(G.Gary_Cross):
            poster = Find("poster_cross")
            poster.ScriptHide()
        if(G.Gary_Blind):
            poster = Find("poster_blind")
            poster.ScriptHide()
    else:
        if(G.Gary_Voerman):
            poster = Find("poster_jeanette")
            poster.ScriptUnhide()
        if(G.Velvet_Poster):
            poster = Find("poster_vv")
            poster.ScriptUnhide()
        if(G.Gary_Photochop):
            poster = Find("poster_ming")
            poster.ScriptUnhide()
        if(G.Gary_Damsel):
            poster = Find("poster_damsel")
            poster.ScriptUnhide()
        if(G.Gary_Imalia):
            poster = Find("poster_imalia")
            poster.ScriptUnhide()
        if(G.Gary_Tawni):
            poster = Find("poster_tawni")
            poster.ScriptUnhide()
        if(G.Gary_Cross):
            poster = Find("poster_cross")
            poster.ScriptUnhide()
        if(G.Gary_Blind):
            poster = Find("poster_blind")
            poster.ScriptUnhide()
            if(G.Ball_Taken < 2):
                __main__.FindPlayer().SetQuest("Gary", 9)
                G.Ball_Taken = 2

#HAVEN: Updates the player's mailbox and flags if he has sent the blood in the mail, changed by wesp
def mailboxExitCheck():
    G = __main__.G
    pc = __main__.FindPlayer()
    container = Find("mailbox_haven")
    if container:
        if(G.Heather_Lure and G.Mcfly_Present and not (G.Mcfly_Leave or G.Mcfly_Feed or G.Mcfly_Dominated or G.Mcfly_Dementated)):
            G.Mcfly_Leave = 1
            pc.ChangeMasqueradeLevel(1)
            mcfly = Find("McFly")
            if mcfly: mcfly.Kill()
        if (container.HasItem("item_g_werewolf_bloodpack")):
            container.AddEntityToContainer("werewolf_reward")
            container.RemoveItem("item_g_werewolf_bloodpack")
            G.Werewolf_Quest = 4
            pc.SetQuest("Werewolf Blood", 3)
            pc.ChangeMasqueradeLevel(-1)
        if(container.HasItem("item_g_garys_film") and G.CD > 0 and G.Gary_Voerman == 0):
            container.RemoveItem("item_g_garys_film")
            G.Gary_Voerman = 1
        if(container.HasItem("item_g_garys_photo") and G.Gary_Voerman == 1 and G.Velvet_Poster == 0):
            container.RemoveItem("item_g_garys_photo")
            G.Velvet_Poster = 1
            if G.Patch_Plus == 1:
                pc.ChangeMasqueradeLevel(-1)
        if(container.HasItem("item_g_garys_tape") and G.Velvet_Poster == 1 and G.Gary_Photochop == 0):
            container.RemoveItem("item_g_garys_tape")
            G.Gary_Photochop = 1
        if(container.HasItem("item_g_garys_cd") and G.Gary_Photochop == 1 and G.Gary_Damsel == 0):
            container.RemoveItem("item_g_garys_cd")
            G.Gary_Damsel = 1
        if(container.HasItem("item_g_wireless_camera_2") and G.Gary_Damsel == 1 and G.Gary_Imalia == 0):
            container.RemoveItem("item_g_wireless_camera_2")
            G.Gary_Imalia = 1
        if(container.HasItem("item_g_wireless_camera_4") and G.Gary_Imalia == 1 and G.Gary_Tawni == 0):
            container.RemoveItem("item_g_wireless_camera_4")
            G.Gary_Tawni = 1
        if(container.HasItem("item_g_wireless_camera_3") and G.Gary_Tawni == 1 and G.Gary_Cross == 0):
            container.RemoveItem("item_g_wireless_camera_3")
            G.Gary_Cross = 1
        if(container.HasItem("item_g_jumbles_flyer") and G.Gary_Cross == 1 and G.Gary_Blind == 0):
            container.RemoveItem("item_g_jumbles_flyer")
            G.Gary_Blind = 1

#HAVEN: Updates the player's quest when he gets the email about werewolf blood
def werewolfBloodQuestAssigned():
    G = __main__.G
    if(G.Werewolf_Quest == 0):
        G.Werewolf_Quest = 1
        __main__.FindPlayer().SetQuest("Werewolf Blood", 1)

#HAVEN: Updates the player's quest when he takes the reward for the werewolf blood
def werewolfBloodQuestDone():
    __main__.FindPlayer().SetQuest("Werewolf Blood", 4)

#HAVEN: Setting Quest State Two for Mitnick Quest
def mitSetQuestTwo():
    __main__.FindPlayer().SetQuest("Mitnick", 2)

#HAVEN: Setting Quest State Three for Mitnick Quest
def mitSetQuestThree():
    __main__.FindPlayer().SetQuest("Mitnick", 3)

#HAVEN: Setting Quest State Four for Mitnick Quest
def mitSetQuestFour():
    __main__.FindPlayer().SetQuest("Mitnick", 4)

#HAVEN: Setting Quest State Five for Mitnick Quest
def mitSetQuestFive():
    __main__.FindPlayer().SetQuest("Mitnick", 5)

#HAVEN: Setting Quest State Six for Mitnick Quest
def mitSetQuestSix():
    __main__.FindPlayer().SetQuest("Mitnick", 6)

#HAVEN: Setting Quest State Seven for Mitnick Quest
def mitSetQuestSeven():
    __main__.FindPlayer().SetQuest("Mitnick", 7)

#HAVEN: Setting Quest State Eight for Mitnick Quest
def mitSetQuestEight():
    __main__.FindPlayer().SetQuest("Mitnick", 8)

#HAVEN: Setting Quest State Nine for Mitnick Quest, changed by wesp
def mitSetQuestNine():
    __main__.FindPlayer().SetQuest("Mitnick", 9)
    __main__.G.Shubs_Act = 4

#HAVEN: Setting Quest State One for Gary Quest, added by wesp
def garySetQuestOne():
    __main__.FindPlayer().SetQuest("Gary", 1)

#HAVEN: Setting Quest State Two for Gary Quest, added by wesp
def garySetQuestTwo():
    __main__.FindPlayer().SetQuest("Gary", 2)

#HAVEN: Setting Quest State Three for Gary Quest, added by wesp
def garySetQuestThree():
    __main__.FindPlayer().SetQuest("Gary", 3)

#HAVEN: Setting Quest State Four for Gary Quest, added by wesp
def garySetQuestFour():
    __main__.FindPlayer().SetQuest("Gary", 4)

#HAVEN: Setting Quest State Five for Gary Quest, added by wesp
def garySetQuestFive():
    __main__.FindPlayer().SetQuest("Gary", 5)

#HAVEN: Setting Quest State Six for Gary Quest, added by wesp
def garySetQuestSix():
    __main__.FindPlayer().SetQuest("Gary", 6)

#HAVEN: Setting Quest State Seven for Gary Quest, added by wesp
def garySetQuestSeven():
    __main__.FindPlayer().SetQuest("Gary", 7)

#HAVEN: Setting Quest State Seven for Gary Quest, added by wesp
def garySetQuestEight():
    __main__.FindPlayer().SetQuest("Gary", 8)

#HAVEN: Setting Quest State One for Bertram Quest, added by wesp
def bertramSetQuest():
    __main__.FindPlayer().SetQuest("BertramCD", 4)

#HAVEN: Setting Quest State One for Tommy Quest
def tomSetQuest():
    __main__.FindPlayer().SetQuest("Tommy", 1)

#HAVEN:Setting Quest State Four for Tommy Quest, changes made by dan_upright 29/11/04
def tomSetQuestFour():
    __main__.FindPlayer().SetQuest("Tommy", 4)
    container = Find("mailbox_haven")
    if container:
        cash = __main__.CreateEntityNoSpawn("item_m_money_envelope", (0, 0, 0), (0,0,0) )
        cash.SetName("critic_reward")
        cash.SetMoney(100)
        __main__.CallEntitySpawn(cash)
        container.AddEntityToContainer("critic_reward")
#changes end

#HAVEN: Called to cause the malk newscaster conversation
def malkTalkToTV():
    G = __main__.G
    pc = __main__.FindPlayer()
    if(IsClan(pc,"Malkavian") and G.Story_State >= 65 and G.News_Spoke == 0 and G.Player_Insane == 0):
        newscaster = Find("newscaster")
        newscaster.ScriptHide()
        newscaster.SetName("newscaster_break")
        malkcaster = Find("newscaster_malkavian")
        malkcaster.ScriptUnhide()
        malkcaster.SetName("newscaster")
        trigger = Find("malk_tv_trigger")
        trigger.ScriptUnhide()

#HAVEN: Called after the malkavian talks to the TV
def malkTvDone():
    newscaster = Find("newscaster_break")
    malkcaster = Find("newscaster")
    if malkcaster: malkcaster.Kill()
    newscaster.ScriptUnhide()
    newscaster.SetName("newscaster")

#HUBS: Sets a Global for the hub you are in should be on each hubs logic_auto
def setArea( s ):
    G = __main__.G
    G.In_Santa_Monica = 0
    G.In_Downtown = 0
    G.In_Hollywood = 0
    G.In_Chinatown = 0
    G.Whore_Follower = 0
    if ( s == "santa_monica" ):
        print ( "*** In Santa Monica ***" )
        G.In_Santa_Monica = 1
    elif ( s == "downtown" ):
        print ( "*** In Downtown ***" )
        G.In_Downtown = 1
    elif ( s == "hollywood" ):
        print ( "*** In Hollywood ***" )
        G.In_Hollywood = 1
    elif ( s == "chinatown" ):
        print ( "*** In Chinatown ***" )
        G.In_Chinatown = 1

#EMBRACE: Determines which models the sire and stakers should use, changed by wesp
def chooseSire():
    pc = __main__.FindPlayer()
    if(pc.HasItem("item_i_written")):
        pc.RemoveItem("item_i_written")
        __main__.G.Player_Homo = 1
    else: __main__.G.Player_Homo = 0
    if(pc.HasItem("item_w_tzimisce2_head")):
        pc.RemoveItem("item_w_tzimisce2_head")
        __main__.G.Player_Insane = 1
    else: __main__.G.Player_Insane = 0
    gender = pc.IsMale()
    clan = pc.clan
    sire = Find("Sire")
    staker1 = Find("Vampire1")
    staker2 = Find("Vampire2")
    brujah_female = "models/character/pc/female/brujah/armor3/brujah_female_armor_3.mdl"
    gangrel_female = "models/character/pc/female/gangrel/armor2/Gangrel_female_Armor_2.mdl"
    malkavian_female = "models/character/pc/female/malkavian/armor3/Malk_Girl_Armor_3.mdl"
    nosferatu_female = "models/character/pc/female/nosferatu/armor0/nosferatu_Female_Armor_0.mdl"
    toreador_female = "models/character/pc/female/toreador/armor2/toreador_female_armor_2.mdl"
    tremere_female = "models/character/pc/female/tremere/armor2/tremere_female_Armor_2.mdl"
    ventrue_female = "models/character/pc/female/ventrue/armor1/ventrue_female_Armor_1.mdl"
    brujah_male = "models/character/pc/male/brujah/armor0/brujah_Male_Armor_0.mdl"
    gangrel_male = "models/character/pc/male/gangrel/armor_2/Gangrel_Male_Armor_2.mdl"
    malkavian_male = "models/character/pc/male/malkavian/armor0/Malkavian_Male_Armor_0.mdl"
    nosferatu_male = "models/character/pc/male/nosferatu/armor0/Nosferatu.mdl"
    tremere_male = "models/character/pc/male/tremere/armor1/tremere_Male_armor_1.mdl"
    toreador_male = "models/character/pc/male/toreador/armor0/toreador_Male_Armor_0.mdl"
    ventrue_male = "models/character/pc/male/ventrue/armor1/ventrue_Male_Armor_1.mdl"
    #MALE
    if(gender):
        #BRUJAH
        if(clan == 2):
            sire.SetModel(brujah_female)
            staker1.SetModel(malkavian_male)
            staker2.SetModel(toreador_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(gangrel_male)
        #GANGREL
        elif(clan == 3):
            sire.SetModel(gangrel_female)
            staker1.SetModel(nosferatu_male)
            staker2.SetModel(tremere_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(brujah_male)
        #MALKAVIAN
        elif(clan == 4):
            sire.SetModel(malkavian_female)
            staker1.SetModel(toreador_male)
            staker2.SetModel(ventrue_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(toreador_male)
        #NOSFERATU
        elif(clan == 5):
            sire.SetModel(toreador_female)
            staker1.SetModel(tremere_male)
            staker2.SetModel(brujah_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(toreador_male)
        #TOREADOR
        elif(clan == 6):
            sire.SetModel(toreador_female)
            staker1.SetModel(ventrue_male)
            staker2.SetModel(gangrel_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(malkavian_male)
        #TREMERE
        elif(clan == 7):
            sire.SetModel(tremere_female)
            staker1.SetModel(brujah_male)
            staker2.SetModel(malkavian_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(ventrue_male)
        #VENTRUE
        elif(clan == 8):
            sire.SetModel(ventrue_female)
            staker1.SetModel(gangrel_male)
            staker2.SetModel(nosferatu_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(tremere_male)
    else:
        #BRUJAH
        if(clan == 2):
            sire.SetModel(brujah_male)
            staker1.SetModel(malkavian_male)
            staker2.SetModel(toreador_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(gangrel_female)
        #GANGREL
        elif(clan == 3):
            sire.SetModel(gangrel_male)
            staker1.SetModel(nosferatu_male)
            staker2.SetModel(tremere_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(brujah_female)
        #MALKAVIAN
        elif(clan == 4):
            sire.SetModel(malkavian_male)
            staker1.SetModel(toreador_male)
            staker2.SetModel(ventrue_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(toreador_female)
        #NOSFERATU
        elif(clan == 5):
            sire.SetModel(toreador_male)
            staker1.SetModel(tremere_male)
            staker2.SetModel(brujah_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(toreador_female)
        #TOREADOR
        elif(clan == 6):
            sire.SetModel(toreador_male)
            staker1.SetModel(ventrue_male)
            staker2.SetModel(gangrel_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(malkavian_female)
        #TREMERE
        elif(clan == 7):
            sire.SetModel(tremere_male)
            staker1.SetModel(brujah_male)
            staker2.SetModel(malkavian_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(ventrue_female)
        #VENTRUE
        elif(clan == 8):
            sire.SetModel(ventrue_male)
            staker1.SetModel(gangrel_male)
            staker2.SetModel(nosferatu_male)
            if __main__.G.Player_Homo == 1:
                sire.SetModel(tremere_female)
    #FINISH THIS FUNCTION

#PROSTITUTES: Called when initiating dialogue with a prostitute to change her name to "prostitute"
#MUST BE CALLED AS THE DIALOG SCRIPT and pass the original name (prostitute_x), changed by wesp
def changeProstituteName(name):
    G = __main__.G
    if G.In_Cemetery == 0:
        print "change name from %s" % name
        G.Prostitute_Name = name
        hooker = Find(name)
        hooker.SetName("prostitute")
        return 0

#PROSTITUTES: Disband and feed (dialogue)
def disbandFeed():
    G = __main__.G
    print ( "*************** Disband and Feed ***************" )
    __main__.npc.SetFollowerBoss( "" )
    __main__.pc.SeductiveFeed( __main__.npc )
    G.In_Alley = 0
    resetHos()

#PROSTITUTES: Prostitute make whore your ho (from dlg)
def makeFollower():
    print ( "*************** Make Follower ***************" )
    __main__.npc.SetFollowerBoss( "!player" )

#PROSTITUTES: Causes prostitutes to flee(on events_world for each hub), fixed by RobinHood70
def fleeingHos():
    print ( "*************** Prostitute Flees Check ***************" )
    pc = __main__.FindPlayer()
    prostitutes = FindList("prostitut*")
    for prostitute in prostitutes:
        if(prostitute.classname != "filter_activator_name"):
            if prostitute.IsFollowerOf(pc):
                print ( "*************** Prostitute Flees ***************" )
                G = __main__.G
                G.Whore_Follower = 0
                if ( G.Romero_Whore == 2 ):
                    G.Romero_Whore = 1
                prostitute.SetFollowerBoss("")
                prostitute.SetRelationship("player D_FR 5")

#PROSTITUTES: Reset Hos, needs to be put on all trigger_change_levels on each hub, fixed by RobinHood70
def resetHos():
    G = __main__.G
    prostitutes = FindList("prostitut*")
    for prostitute in prostitutes:
        if(prostitute.classname != "filter_activator_name"): prostitute.SetFollowerBoss("")
    G.Whore_Follower = 0
    if (G.Romero_Whore == 2):
        G.Romero_Whore = 1
    prophet = Find("Prophet")
    if (prophet and G.Prophet_Dead == 0):
        print "Prophetfix"
        lines = FindList("line*")
        for line in lines:
            if line: line.Cancel()
        rant1 = Find("prophet_rant_sequence_1")
        if rant1: rant1.CancelSequence()
        rant2 = Find("prophet_rant_sequence_2")
        if rant2: rant2.CancelSequence()
        rant3 = Find("prophet_rant_sequence_3")
        if rant3: rant3.CancelSequence()

#PROSTITUTES: Revert's hooker's name at end of dialogue, changed by wesp
def revertHookerName():
    G = __main__.G
    if G.In_Cemetery == 0:
        print "change name to %s" % G.Prostitute_Name
        hooker = Find("prostitute")
        hooker.SetName(G.Prostitute_Name)

#PROSTITUTES: Prostitute Inits Dialogue (on alley triggers), fixed by RobinHood70
def prostituteInit():
    G = __main__.G
    print ( "*************** Check if Prostitue is Follower ***************" )
    if (G.Romero_Whore == 2):
        return
    if (G.Whore_Follower == 1):
        pc = __main__.FindPlayer()
        G.In_Alley = 1
        prostitutes = FindList("prostitut*")
        for prostitute in prostitutes:
            if(prostitute.classname != "filter_activator_name"):
                if (prostitute.IsFollowerOf( pc )):
                    prostitute.StartPlayerDialog(0)

#Refills ammo for the guns the PC has
def masterRefill(param):
    paramlist = param.split()
    quantity = atoi(paramlist[1])
    container = Find( paramlist[0] )
    player = __main__.FindPlayer()
    gotammo = 0
    chance = 0
    if container:
        print ( "****************** Found Container ********************" )
        container.DeleteItems()
        if ( player.HasItem("item_w_colt_anaconda") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Anaconda Ammo ********************" )
                container.SpawnItemInContainer("item_w_colt_anaconda")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_crossbow") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Bolts ********************" )
                container.SpawnItemInContainer("item_w_crossbow")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_crossbow_flaming") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Fire Bolts ********************" )
                container.SpawnItemInContainer("item_w_crossbow_flaming")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_deserteagle") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Deagle Clip ********************" )
                container.SpawnItemInContainer("item_w_deserteagle")
                quantityv = quantityv - 1
#        if ( player.HasItem("item_w_flamethrower") ):
#            quantityv = quantity
#            gotammo = 1
#            while (quantityv > 0):
#                print ( "****************** Flamethrower Fuel ********************" )
#                container.SpawnItemInContainer("item_w_flamethrower")
#                quantityv = quantityv - 1
        if ( player.HasItem("item_w_glock_17c") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Glock Clip ********************" )
                container.SpawnItemInContainer("item_w_glock_17c")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_ithaca_m_37") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Shotgun Shells ********************" )
                container.SpawnItemInContainer("item_w_ithaca_m_37")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_mac_10") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Mac-10 Clip ********************" )
                container.SpawnItemInContainer("item_w_mac_10")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_rem_m_700_bach") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Bach Ammo ********************" )
                container.SpawnItemInContainer("item_w_rem_m_700_bach")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_remington_m_700") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Remington Ammo ********************" )
                container.SpawnItemInContainer("item_w_remington_m_700")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_steyr_aug") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Steyr-Aug Clip ********************" )
                container.SpawnItemInContainer("item_w_steyr_aug")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_supershotgun") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Shotgun Clip ********************" )
                container.SpawnItemInContainer("item_w_supershotgun")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_thirtyeight") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** .38 Rounds ********************" )
                container.SpawnItemInContainer("item_w_thirtyeight")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_uzi") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Uzi Clip ********************" )
                container.SpawnItemInContainer("item_w_uzi")
                quantityv = quantityv - 1
        if ( gotammo == 1 ):
            print ( "****************** Filled Container ********************" )
            return
        else:
            print ( "****************** PC has no Guns ********************")
            R = Random( time() )
            chance = R.randint (1, 3)
            if ( chance == 1 or chance == 2 ):
                print ( "****************** Cheap Watch ********************" )
                container.SpawnItemInContainer("item_g_watch_normal")
            if ( chance == 3 ):
                print ( "****************** Nice Watch ********************" )
                container.SpawnItemInContainer("item_g_watch_fancy")
    else:
        print ( "****************** No Container ********************" )

##############################################################################
# Classes
##############################################################################
