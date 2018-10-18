print "loading theatre level script"

import __main__
import random
random.seed()

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#THEATRE: Fadeout level load after prince dialogue.
def tutorialLoad():
    __main__.ChangeMap(2.5, "tutorial", "tutorial_change")

#THEATRE: Mitnick quest, changed by wesp 
def setMitnickFail():
        state = __main__.FindPlayer().GetQuestState("Muddy")
        if(state < 5):
            __main__.FindPlayer().SetQuest("Mitnick", 10)
            G.Shubs_Act = 5

#THEATRE: Assigns models to the seat fillers during the courtroom scene
def fillSeats():
    pc = __main__.FindPlayer()
    gender = pc.IsMale()
    clan = pc.clan
    chick1 = Find("Vampire3") #clan + 1
    chick2 = Find("Vampire4") #clan + 2
    vampire6 = Find("Vampire6") #clan + 5
    vampire7 = Find("Vampire7") #clan + 1
    vampire8 = Find("Vampire8")#clan + 3
    vampire9 = Find("Vampire9")#clan + 6
    chick3 = Find("Vampire10") #clan + 4
    chick4 = Find("Vampire11")#clan + 6
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
    #BRUJAH
    if(clan == 2):
        chick1.SetModel(gangrel_female)
        chick2.SetModel(malkavian_female)
        vampire6.SetModel(tremere_male)
        vampire7.SetModel(gangrel_male)
        vampire8.SetModel(nosferatu_male)
        vampire9.SetModel(ventrue_male)
        chick3.SetModel(toreador_female)
        chick4.SetModel(ventrue_female)
    #Gangrel
    elif(clan == 3):
        chick1.SetModel(malkavian_female)
        chick2.SetModel(nosferatu_female)
        vampire6.SetModel(ventrue_male)
        vampire7.SetModel(malkavian_male)
        vampire8.SetModel(toreador_male)
        vampire9.SetModel(brujah_male)
        chick3.SetModel(tremere_female)
        chick4.SetModel(brujah_female)
    #MALKAVIAN
    elif(clan == 4):
        chick1.SetModel(nosferatu_female)
        chick2.SetModel(toreador_female)
        vampire6.SetModel(brujah_male)
        vampire7.SetModel(nosferatu_male)
        vampire8.SetModel(tremere_male)
        vampire9.SetModel(gangrel_male)
        chick3.SetModel(ventrue_female)
        chick4.SetModel(gangrel_female)
    #NOSFERATU
    elif(clan == 5):
        chick1.SetModel(toreador_female)
        chick2.SetModel(tremere_female)
        vampire6.SetModel(gangrel_male)
        vampire7.SetModel(toreador_male)
        vampire8.SetModel(ventrue_male)
        vampire9.SetModel(malkavian_male)
        chick3.SetModel(brujah_female)
        chick4.SetModel(malkavian_female)
    #Toreador
    elif(clan == 6):
        chick1.SetModel(tremere_female)
        chick2.SetModel(ventrue_female)
        vampire6.SetModel(malkavian_male)
        vampire7.SetModel(tremere_male)
        vampire8.SetModel(brujah_male)
        vampire9.SetModel(nosferatu_male)
        chick3.SetModel(gangrel_female)
        chick4.SetModel(nosferatu_female)
    #Tremere
    elif(clan == 7):
        chick1.SetModel(ventrue_female)
        chick2.SetModel(brujah_female)
        vampire6.SetModel(nosferatu_male)
        vampire7.SetModel(ventrue_male)
        vampire8.SetModel(gangrel_male)
        vampire9.SetModel(toreador_male)
        chick3.SetModel(malkavian_female)
        chick4.SetModel(toreador_female)
    #Ventrue
    elif(clan == 8):
        chick1.SetModel(brujah_female)
        chick2.SetModel(gangrel_female)
        vampire6.SetModel(toreador_male)
        vampire7.SetModel(brujah_male)
        vampire8.SetModel(malkavian_male)
        vampire9.SetModel(tremere_male)
        chick3.SetModel(nosferatu_female)
        chick4.SetModel(tremere_female)

#THEATRE: Changes the sire's model to nos if appropriate, changed by wesp
def nosferatuRevealer():
    clan = __main__.FindPlayer().clan
    if(clan == 5):
        fade = Find("nosferatu_change_fade")
        fade.Fade()
        sire = Find("Sire2")
        if(__main__.FindPlayer().IsMale()):
            sire.SetModel("models/character/pc/female/nosferatu/armor0/nosferatu_female_armor_0.mdl")
            if __main__.G.Player_Homo == 1:
                sire.SetModel("models/character/pc/male/nosferatu/armor2/nosferatu_male_armor_2.mdl")
        else:
            sire.SetModel("models/character/pc/male/nosferatu/armor0/Nosferatu.mdl")
            if __main__.G.Player_Homo == 1:
                sire.SetModel("models/character/pc/female/nosferatu/armor2/nosferatu_female_armor_2.mdl")

#MASQUERADE: Setup the actors to avoid clan duplicates
def setupMasqueradeActors():
    dude1 = Find("Ventrue")
    dude2 = Find("Nosferatu")
    dude3 = Find("Toreador")
    if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu")) :
        dude3.SetName("extra_vampire")
        dude3.ScriptUnhide()
        dude1.SetName("hair_holder")
        dude1.ScriptUnhide()
    elif (__main__.IsClan(__main__.FindPlayer(), "Ventrue")) :
        dude2.SetName("extra_vampire")
        dude2.ScriptUnhide()
        dude3.SetName("hair_holder")
        dude3.ScriptUnhide()
    else :
        dude2.SetName("extra_vampire")
        dude2.ScriptUnhide()
        dude1.SetName("hair_holder")
        dude1.ScriptUnhide()

#THEATRE: Remove a webcam from your inventory, changed by wesp
def removeCamera():
    pc = __main__.FindPlayer()
    if(pc.HasItem("item_g_wireless_camera_1")):
        pc.RemoveItem("item_g_wireless_camera_1")

#EMBRACE: Assigns a player model to the player_understudy
def castUnderstudy():
    understudy = Find("player_understudy")
    pc = __main__.FindPlayer()
    clan = pc.clan
    player_model = pc.GetModelName()
    #NOS
    if(clan == 5):
        if(pc.IsMale()):
            understudy.SetModel("models/character/pc/male/brujah/armor0/brujah_Male_Armor_0.mdl")
        else:
            understudy.SetModel("models/character/pc/female/brujah/armor3/brujah_female_armor_3.mdl")
    else:
        understudy.SetModel(player_model)

#EMBRACE: Transforms the understudy into a hideous creature if the player has chosen Nosferatu
def nosferatuTransform():
    understudy = Find("player_understudy")
    pc = __main__.FindPlayer()
    clan = pc.clan
    if(clan == 5):
        if(pc.IsMale()):
            understudy.SetModel("models/character/pc/male/nosferatu/armor0/Nosferatu.mdl")
        else:
            understudy.SetModel("models/character/pc/female/nosferatu/armor0/nosferatu_Female_Armor_0.mdl")

#COURTROOM SCENE: Choose sire for the courtroom scene, changed by wesp
def courtroomSire():
    pc = __main__.FindPlayer()
    gender = pc.IsMale()
    clan = pc.clan
    sire = Find("Sire2")
    staker1 = Find("Vampire1_2")
    staker2 = Find("Vampire2_2")
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

print "levelscript loaded"