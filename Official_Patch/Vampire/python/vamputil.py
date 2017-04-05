import __main__
from random import Random
from time import time
from string import atoi

huntersDead = [0, 0, 0]

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

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
    char.GiveItem(ItemName)

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

#called on the hubs (and possibly other maps?) to place hunters if the player violates the masquerade
def checkMasquerade():
    level = __main__.FindPlayer().GetMasqueradeLevel()
    print "level %i" % level
    if(level >= 2 and level < 5):
        i = 2
        while(i <= level):
            if(huntersDead[i - 2] == 0):
                spawner = __main__.FindEntityByName("hunter_maker_%i" % (i - 1))
                spawner.Spawn()
            i = i + 1

#spawns in the appropriate cop car given the input
def spawnCopCar(i):
    Find = __main__.FindEntityByName
    ent = Find("cop_car_%i" % (i))
    if(ent):
       ent.ScriptUnhide()
    ent = Find("cop_front_%i" % (i))
    if(ent):
       ent.Spawn()
    ent = Find("cop_rear_%i" % (i))
    if(ent):
       ent.Spawn()
    ent = Find("red%i" % (i))
    if(ent):
       ent.TurnOn()
    ent = Find("blue%i" % (i))
    if(ent):
       ent.TurnOn()
    ent = Find("cover_front_%i" % (i))
    if(ent):
       ent.ScriptUnhide()
    ent = Find("cover_rear_%i" % (i))
    if(ent):
       ent.ScriptUnhide()

#removes cop cars that may have been spawned onto the map previously
#argument specifies the total number of cop cars on the given hub
def removeCopCar(total):
    i = 1
    while(i <= total):
       Find = __main__.FindEntityByName
       ent = Find("cop_car_%i" % (i))
       if(ent):
           ent.ScriptHide()
       ent = Find("red%i" % (i))
       if(ent):
           ent.TurnOff()
       ent = Find("blue%i" % (i))
       if(ent):
           ent.TurnOff()
       ent = Find("cover_front_%i" % (i))
       if(ent):
           ent.ScriptHide()
       ent = Find("cover_rear_%i" % (i))
       if(ent):
           ent.ScriptHide()
       i = i + 1
    cops = __main__.FindEntitiesByName("stake_out_cop")
    for cop in cops:
        cop.Kill()
    cops = __main__.FindEntitiesByName("cop")
    for cop in cops:
        cop.Kill()
    cops = __main__.FindEntitiesByName("patrol_cop_1")
    for cop in cops:
        cop.Kill()
    cops = __main__.FindEntitiesByName("patrol_cop_2")
    for cop in cops:
        cop.Kill()                

#returns the distanceSquared between two 3D points
def distanceSquared(p1, p2):
    xDistance = (p1[0] - p2[0]) * (p1[0] - p2[0])
    yDistance = (p1[1] - p2[1]) * (p1[1] - p2[1])
    zDistance = (p1[2] - p2[2]) * (p1[2] - p2[2])
    return (xDistance + yDistance + zDistance)
    
#starts the BloodDoll on a random line
def doll1dlg():
    doll = __main__.FindEntityByName("Doll1")
    if(__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
        return 121
    elif(__main__.G.Doll_Seduce == 1):
        return 91
    elif(1):
        return RandomLine([1, 31, 61])

#HAVEN: Used to place heather in the various player havens
def heatherHaven():
    Find = __main__.FindEntityByName
    G = __main__.G
    IsDead = __main__.IsDead
    heather = Find("Heather")
    if(G.Heather_Haven and not IsDead("Heather") and heather):
        heather.ScriptUnhide()
    if((G.Heather_Gone or G.Story_State >= 75) and heather):
        heather.Kill()
    if(G.Story_State >= 30 and G.Heather_Haven and not IsDead("Heather") and G.Heather_Gone == 0 and G.Story_State < 75 and not G.Heather_Lure):
        G.Mcfly_Present = 1
        mcfly = Find("McFly")
        if(mcfly):
            mcfly.ScriptUnhide()
    if(G.Mcfly_Leave or G.Mcfly_Feed or G.Mcfly_Dominated or G.Mcfly_Dementated or IsDead("McFly")):
        mcfly = Find("McFly")
        if(mcfly):
            mcfly.Kill()
    if(G.Heather_Clothes and heather):
        if(G.Heather_Outfit == 0):
            heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather_goth.mdl")
        elif(G.Heather_Outfit == 1):
            heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather_3.mdl")
        else:
            heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather.mdl")            
        G.Heather_Outfit = G.Heather_Outfit + 1
        if(G.Heather_Outfit > 2):
            G.Heather_Outfit = 0
        G.Heather_Clothes = 0
    if(IsDead("Heather") and heather):
        heather.Kill()
        mcfly = Find("mcfly")
        if(mcfly):
            mcfly.Kill()

#HAVEN: called to see if Heather needs to leave the haven
def heatherLeaves():
    Find = __main__.FindEntityByName
    G = __main__.G
    if(G.Heather_Gone):
        relay = Find("heather_leaves_relay")
        relay.Trigger()

#HAVEN: called to see if mcfly leaves
def mcflyDialog():
    Find = __main__.FindEntityByName
    G = __main__.G
    if(G.Mcfly_Leave or G.Mcfly_Dominated or G.Mcfly_Dementated):
        relay = Find("mcfly_leaves_relay")
        relay.Trigger()
        
#HAVEN: Used for mailbox events for email quests at the haven
def putStuffInMailBox():
    Find = __main__.FindEntityByName
    mailbox = Find("Mailbox_haven")
    if(mailbox):
        G = __main__.G
        if(G.Shubs_Email == 1 and G.Shubs_Email_Read < 1):
            mailbox.SpawnItemInContainer("item_k_shrekhub_one_key")
            G.Shubs_Email_Read = 1
        elif(G.Shubs_Email == 2 and G.Shubs_Email_Read < 2):
            mailbox.SpawnItemInContainer("item_g_wireless_camera_4")
            G.Shubs_Email_Read = 2
        elif(G.Shubs_Email == 3 and G.Shubs_Email_Read < 3):
            mailbox.SpawnItemInContainer("item_k_shrekhub_three_key")
            G.Shubs_Email_Read = 3
        elif(G.Shubs_Email == 4 and G.Shubs_Email_Read < 4):
            mailbox.SpawnItemInContainer("item_k_shrekhub_four_key")
            G.Shubs_Email_Read = 4
        if((G.Tommy_Disgusted == 1 or G.Tommy_Review == 1) and (G.Tommy_Payoff == 0)):
            origin = mailbox.GetOrigin()
            angles = mailbox.GetAngles()
            money = __main__.CreateEntityNoSpawn("item_m_money_envelope", origin, angles )
            money.SetModel( "models/items/MoneyEnvelope/Ground/MoneyEnvelope.mdl" )
            __main__.CallEntitySpawn( money )
            money.SetName( "Tommy_Payoff" )
            money.SetMoney( 300 )
            mailbox.AddEntityToContainer( "Tommy_Payoff" )
            G.Tommy_Payoff = 1
        
#HAVEN: used to determine if the player has collected any posters
def posterCheck():
    G = __main__.G
    Find = __main__.FindEntityByName
    if(G.Gary_Voerman):
        poster = Find("poster_jeanette")
        poster.ScriptUnhide()
    if(G.Gary_Damsel):
        poster = Find("poster_damsel")
        poster.ScriptUnhide()
    if(G.Velvet_Poster):
        poster = Find("poster_vv")
        poster.ScriptUnhide()
    if(G.Gary_Photochop):
        poster = Find("poster_ming")
        poster.ScriptUnhide()

#HAVEN: Updates the player's mailbox and flags if he has sent the blood in the mail
def mailboxExitCheck():
    G = __main__.G
    Find = __main__.FindEntityByName
    container = Find("mailbox_haven")
    if(container):
        if(G.Heather_Lure and G.Mcfly_Present and not (G.Mcfly_Leave or G.Mcfly_Feed or G.Mcfly_Dominated or G.Mcfly_Dementated)):
            G.Mcfly_Leave = 1
            pc = __main__.FindPlayer()
            pc.ChangeMasqueradeLevel(1)
            mcfly = Find("Mcfly")
            if(mcfly):
                mcfly.Kill()
        if ( container.HasItem("item_g_werewolf_bloodpack") ):
            container.AddEntityToContainer("werewolf_reward")
            container.RemoveItem("item_g_werewolf_bloodpack")
            G.Werewolf_Quest = 4
            pc = __main__.FindPlayer()
            pc.SetQuest("Werewolf blood", 3)
            pc.ChangeMasqueradeLevel(-1)
        if(container.HasItem("item_g_garys_film") and G.Story_State >= 45):
            container.RemoveItem("item_g_garys_film")
            G.Gary_Voerman = 1
        if(container.HasItem("item_g_garys_cd") and G.Gary_Voerman == 1):
            container.RemoveItem("item_g_garys_cd")
            G.Gary_Damsel = 1
        if(container.HasItem("item_g_garys_tape") and G.Gary_Damsel == 1 and G.Velvet_Poster == 1):
            container.RemoveItem("item_g_garys_tape")
            G.Gary_Photochop = 1    
        if(container.HasItem("item_g_garys_photo") and G.Gary_Damsel == 1):
            container.RemoveItem("item_g_garys_photo")
            G.Velvet_Poster = 1
        
#HAVEN: updates the player's quest when he gets the email about werewolf blood
def werewolfBloodQuestAssigned():
    Find = __main__.FindEntityByName
    G = __main__.G
    if(G.Werewolf_Quest == 0):
        G.Werewolf_Quest = 1
        __main__.FindPlayer().SetQuest("Werewolf blood", 1)

#HAVEN: updates the player's quest when he takes the reward for the werewolf blood
def werewolfBloodQuestDone():
    __main__.FindPlayer().SetQuest("Werewolf blood", 4)
    

#HAVEN:Setting Quest State Two for Mitnick Quest
def mitSetQuestTwo():
	__main__.FindPlayer().SetQuest("Mitnick", 2)

#HAVEN:Setting Quest State Three for Mitnick Quest
def mitSetQuestThree():
	__main__.FindPlayer().SetQuest("Mitnick", 3)

#HAVEN:Setting Quest State Four for Mitnick Quest
def mitSetQuestFour():
	__main__.FindPlayer().SetQuest("Mitnick", 4)

#HAVEN:Setting Quest State Five for Mitnick Quest
def mitSetQuestFive():
	__main__.FindPlayer().SetQuest("Mitnick", 5)

#HAVEN:Setting Quest State Six for Mitnick Quest
def mitSetQuestSix():
	__main__.FindPlayer().SetQuest("Mitnick", 6)

#HAVEN:Setting Quest State Seven for Mitnick Quest
def mitSetQuestSeven():
	__main__.FindPlayer().SetQuest("Mitnick", 7)

#HAVEN:Setting Quest State Eight for Mitnick Quest
def mitSetQuestEight():
	__main__.FindPlayer().SetQuest("Mitnick", 8)

#HAVEN:Setting Quest State Nine for Mitnick Quest
def mitSetQuestNine():
	__main__.FindPlayer().SetQuest("Mitnick", 9)

#HAVEN:Setting Quest State One for Tommy Quest
def tomSetQuest():
	__main__.FindPlayer().SetQuest("Tommy", 1)

#HAVEN: called to cause the malk newscaster conversation
def malkTalkToTV():
    G = __main__.G
    Find = __main__.FindEntityByName
    pc = __main__.FindPlayer()
    if(IsClan(pc,"Malkavian") and G.Story_State >= 65 and G.News_Spoke == 0):
        newscaster = Find("newscaster")
        malkcaster = Find("newscaster_malkavian")
        malkcaster.ScriptUnhide()
        newscaster.ScriptHide()
        newscaster.SetName("newscaster_break")
        malkcaster.SetName("newscaster")
        trigger = Find("malk_tv_trigger")
        trigger.ScriptUnhide()

#HAVEN: called after the malkavian talks to the TV
def malkTvDone():
    Find = __main__.FindEntityByName
    newscaster = Find("newscaster_break")
    malkcaster = Find("newscaster")
    malkcaster.Kill()
    newscaster.ScriptUnhide()
    newscaster.SetName("newscaster")


## Sets a Global for the hub you are in should be on each hubs logic_auto
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

#EMBRACE: determines which models the sire and stakers should use.
def chooseSire():
    pc = __main__.FindPlayer()
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
        #GANGREL
        elif(clan == 3):
            sire.SetModel(gangrel_female)
            staker1.SetModel(nosferatu_male)
            staker2.SetModel(tremere_male)
        #MALKAVIAN
        elif(clan == 4):
            sire.SetModel(malkavian_female)
            staker1.SetModel(toreador_male)
            staker2.SetModel(ventrue_male)
        #NOSFERATU
        elif(clan == 5):
            sire.SetModel(toreador_female)
            staker1.SetModel(tremere_male)
            staker2.SetModel(brujah_male)
        #TOREADOR
        elif(clan == 6):
            sire.SetModel(toreador_female)
            staker1.SetModel(ventrue_male)
            staker2.SetModel(gangrel_male)
        #TREMERE
        elif(clan == 7):
            sire.SetModel(tremere_female)
            staker1.SetModel(brujah_male)
            staker2.SetModel(malkavian_male)
        #VENTRUE
        elif(clan == 8):
            sire.SetModel(ventrue_female)
            staker1.SetModel(gangrel_male)
            staker2.SetModel(nosferatu_male)
    else:
        #BRUJAH
        if(clan == 2):
            sire.SetModel(brujah_male)
            staker1.SetModel(malkavian_male)
            staker2.SetModel(toreador_male)
        #GANGREL
        elif(clan == 3):
            sire.SetModel(gangrel_male)
            staker1.SetModel(nosferatu_male)
            staker2.SetModel(tremere_male)
        #MALKAVIAN
        elif(clan == 4):
            sire.SetModel(malkavian_male)
            staker1.SetModel(toreador_male)
            staker2.SetModel(ventrue_male)
        #NOSFERATU
        elif(clan == 5):
            sire.SetModel(toreador_male)
            staker1.SetModel(tremere_male)
            staker2.SetModel(brujah_male)
        #TOREADOR
        elif(clan == 6):
            sire.SetModel(toreador_male)
            staker1.SetModel(ventrue_male)
            staker2.SetModel(gangrel_male)
        #TREMERE
        elif(clan == 7):
            sire.SetModel(tremere_male)
            staker1.SetModel(brujah_male)
            staker2.SetModel(malkavian_male)
        #VENTRUE
        elif(clan == 8):
            sire.SetModel(ventrue_male)
            staker1.SetModel(gangrel_male)
            staker2.SetModel(nosferatu_male)        
    #FINISH THIS FUNCTION

#PROSTITUTES: Called when initiating dialogue with a prostitute to change her name to "prostitute"
#              MUST BE CALLED AS THE DIALOG SCRIPT and pass in the original name of the prositute (prostitute_x)
def changeProstituteName(name):
    print "change name from %s" % name
    G = __main__.G
    Find = __main__.FindEntityByName
    G.Prostitute_Name = name
    hooker = Find(name)
    hooker.SetName("prostitute")
    return 0
    
## PROSTITUTES: disband and feed (dialogue)
def disbandFeed():
    G = __main__.G    
    print ( "*************** Disband and Feed ***************" )
    __main__.npc.SetFollowerBoss( "" )
    __main__.pc.SeductiveFeed( __main__.npc )
    G.In_Alley = 0
    resetHos()

## PROSTITUTES: Prostitute make whore your ho (from dlg)
def makeFollower():
    print ( "*************** Make Follower ***************" )
    __main__.npc.SetFollowerBoss( "!player" )

## PROSTITUTES: Causes prostitutes to flee(on events_world for each hub)
def fleeingHos():
    print ( "*************** Prostitute Flees Check ***************" )
    pc = __main__.FindPlayer()
    prostitutes = FindList("prostitut*")
    for prostitute in prostitutes:
        if ( prostitute.IsFollowerOf( pc )):
            print ( "*************** Prostitute Flees ***************" )
            G.Whore_Follower = 0
            if ( G.Romero_Whore == 2 ):
                G.Romero_Whore = 1
            prostitute.SetFollowerBoss( "" )
            prostitute.SetRelationship("player D_FR 5")

## PROSTITUTES: Reset Hos, needs to be put on all trigger_change_levels on each hub
def resetHos():
    G = __main__.G
    Find = __main__.FindEntityByName
    prostitutes = FindList("prostitut*")
    for prostitute in prostitutes:
        prostitute.SetFollowerBoss( "" )
    G.Whore_Follower = 0
    if (G.Romero_Whore == 2):
        G.Romero_Whore = 1

#PROSTITUTES: Revert's hooker's name at end of dialogue
def revertHookerName():
    G = __main__.G
    Find = __main__.FindEntityByName
    print "change name to %s" % G.Prostitute_Name   
    hooker = Find("prostitute")
    hooker.SetName(G.Prostitute_Name)    

## PROSTITUTES: Prostitute Inits Dialogue (on alley triggers)
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
            if (prostitute.IsFollowerOf( pc )):
                prostitute.StartPlayerDialog(0)

## Refills ammo for the guns the PC has
def masterRefill(param):
    paramlist = param.split()
    quantity = atoi(paramlist[1])    
    container = __main__.Find( paramlist[0] )
    player = __main__.FindPlayer()
    gotammo = 0
    chance = 0
    if (container):
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
##        if ( player.HasItem("item_w_flamethrower") ):
##            quantityv = quantity
##            gotammo = 1
##            while (quantityv > 0):
##                print ( "****************** Flamethrower Fuel ********************" )
##                container.SpawnItemInContainer("item_w_flamethrower")
##                quantityv = quantityv - 1
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
