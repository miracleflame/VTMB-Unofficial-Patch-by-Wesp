print "loading bradbury level script"

import __main__

from __main__ import G
from random import Random
from time import time

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#HALLOBROOK HOTEL 3: Fired when andrei found
def andreiFound():
    __main__.FindPlayer().SetQuest("Shangrila", 2)

#HALLOBROOK HOTEL 3: Fired when andrei dies
def andreiDeath():
    __main__.FindPlayer().SetQuest("Shangrila", 3)

#HALLOBROOK HOTEL 2: Checks the shadows for inhabitants
def checkShadows():
    i = 0
    while(i < 5):
        trigger = Find("shadow_check_%i" % i)
        trigger.Enable()
        __main__.ScheduleTask(1.0, "__main__.FindEntityByName(\"shadow_check_%i\" % i).Disable()")
        i = i + 1

#HALLOBROOK HOTEL 2: Chooses a shadow to send this Lasombra to, based upon which are occupied.
def chooseDestinationShadow():
    R = Random( time() )
    Index = R.randint(0, 4)
    shadowFree = 0
    while(shadowFree != 1):
        if(Index == 4):
            Index = 0
        else:
            Index = Index + 1
        #spot = Find("shadow_trigger_%i" % (Index)).GetOrigin()
        #if(isUnoccupied(spot)):
        #    shadowFree = 1
        if(G.shadowList[Index] == 0):
            shadowFree = 1
    #script = Find("go_to_shadow_%i" % (Index))
    #script.BeginSequence()
    chooser = Find("shadow_chooser")
    IndexString = "%i" % (Index)
    print "choosing shadow " + IndexString
    chooser.InValue(IndexString)
    #G.shadowList = [0, 0, 0, 0, 0]

#HALLOBROOK HOTEL 2: Counts the number of dead lasombra, and causes the level to continue after they are all dead
def deadLasombra():
    G.deadShadowMages = G.deadShadowMages + 1
    if(G.deadShadowMages == 3):
        relay = Find("Lasombra_dead_relay")
        relay.Trigger()

#HALLOBROOK HOTEL 2: Enables the appropriate encounter based upon whether or not the player has kept Heather as a ghoul, changed by Wesp
def heatherCheck():
    if(G.Heather_Drank == 1 and G.Heather_Haven == 1 and G.Heather_Gone == 0 and G.Heather_Kill == 0 and G.Heather_Indoors == 0 and G.Heather_Scene == 0 and not __main__.IsDead("Heather")):
        #Heather gets to die now
        print "incoming heather"
        heather = Find("Heather")
        relay = Find("heather_scene_unhider")
        relay.Trigger()
        G.Heather_Scene = 1
        if(heather):
            if G.Patch_Plus == 1:  
                heather_dead = Find("heather_dead")
                heather_dead.ScriptUnhide()
                heather_dead.WillTalk(1)
            if(G.Heather_Outfit == 1):
                heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather_goth.mdl")
            elif(G.Heather_Outfit == 2):
                heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather_3.mdl")
            else:
                heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather.mdl")
    else:
        #normal encounter
        print "no heather"
        relay = Find("non_heather_scene_unhider")
        relay.Trigger()

#HALLOBROOK HOTEL 2: Heather screams for the first time
def heatherScream1():
    heather = Find("Heather")
    if heather:
        heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line901_col_e.mp3")

#HALLOBROOK HOTEL 2: Heather screams for the first time, changed by wesp
def heatherCry():
    heather = Find("Heather")
    if heather:
        heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line921_col_e.mp3")

#HALLOBROOK HOTEL 2: Heather screams for the first time
def heatherScream2():
    heather = Find("Heather")
    if heather:
        heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line911_col_e.mp3")

#HALLOBROOK HOTEL 2: Heather screams for the first time
def heatherDie():
    heather = Find("Heather")
    if heather:
        heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line931_col_e.mp3")        

#HALLOBROOK HOTEL 2: This makes me sad, changed by wesp
def initVars():
    G.shadowList = [1, 1, 0, 0, 1]
    G.deadShadowMages = 0
    heather = Find("Heather")
    if G.Heather_Scene == 1:
        if heather: heather.ScriptHide()
    if G.Player_Sabbat == 1:
        G.Player_Sabbat = 2

#HALLOBROOK HOTEL 2: Returns true if the shadow is not occupied
def isUnoccupied(spot):
    L1Spot = Find("Lasombra").GetOrigin()
    if L1Spot:
        if(__main__.distanceSquared(L1Spot, spot) < 100000):
            return 0
    L2Spot = Find("Lasombra_2").GetOrigin()
    if L2Spot:
        if(__main__.distanceSquared(L2Spot, spot) < 100000):
            return 0
    L3Spot = Find("Lasombra_3").GetOrigin()
    if L3Spot:
        if(__main__.distanceSquared(L3Spot, spot) < 100000):
            return 0
    return 1

#HALLOBROOK HOTEL 2: Tries to figure out which Lasombra is in the given shadow
def leaveShadow(number):
    trigger = Find("shadow_trigger_%i" % number)
    trigger.Enable()

#HALLOBROOK HOTEL 2: Tells the game that the given shadow is now free for use
def shadowFree(number):
    G.shadowList[number] = 0
    print "shadowList [%i, %i, %i, %i, %i]" % (G.shadowList[0], G.shadowList[1], G.shadowList[2], G.shadowList[3], G.shadowList[4])
 
#HALLOBROOK HOTEL 2: Tells the game that the given shadow is now occupied by a Lasombra
def shadowOccupied(number):
    G.shadowList[number] = 1
    print "shadowList [%i, %i, %i, %i, %i]" % (G.shadowList[0], G.shadowList[1], G.shadowList[2], G.shadowList[3], G.shadowList[4])
