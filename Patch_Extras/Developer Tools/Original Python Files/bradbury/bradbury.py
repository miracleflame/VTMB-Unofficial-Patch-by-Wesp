print "loading bradbury level script"

import __main__

from __main__ import G
from random import Random
from time import time

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass




#fired when andrei found
def andreiFound():
    __main__.FindPlayer().SetQuest("Shangrila", 2)

#fired when andrei dies
def andreiDeath():
    __main__.FindPlayer().SetQuest("Shangrila", 3)

#checks the shadows for inhabitants
def checkShadows():
    i = 0
    while(i < 5):
        trigger = Find("shadow_check_%i" % i)
        trigger.Enable()
        __main__.ScheduleTask(1.0, "__main__.FindEntityByName(\"shadow_check_%i\" % i).Disable()")
        i = i + 1

#chooses a shadow to send this Lasombra to, based upon which are occupied.
def chooseDestinationShadow():
    R = Random( time() )
    Index = R.randint(0, 4)
    shadowFree = 0
    while(shadowFree != 1):
        if(Index == 4):
            Index = 0
        elif(1):
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

#counts the number of dead lasombra, and causes the level to continue
#after they are all dead
def deadLasombra():
    G.deadShadowMages = G.deadShadowMages + 1
    if(G.deadShadowMages == 3):
        relay = Find("Lasombra_dead_relay")
        relay.Trigger()

#Enables the appropriate encounter based upon whether or not the player hast kept Heather as a ghoul
def heatherCheck():
    if(G.Heather_Drank == 1 and G.Heather_Gone == 0):
        #Heather gets to die now
        print "incoming heather"
        relay = Find("heather_scene_unhider")
        relay.Trigger()
    elif(1):
        #normal encounter
        print "no heather"
        relay = Find("non_heather_scene_unhider")
        relay.Trigger()

#Heather screams for the first time
def heatherScream1():
    heather = Find("Heather")
    if(heather):
        heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line901_col_e.mp3")

#Heather screams for the first time
def heatherCry():
    heather = Find("Heather")
    #if(heather):
    #    heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line921_col_e.mp3")

#Heather screams for the first time
def heatherScream2():
    heather = Find("Heather")
    if(heather):
        heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line911_col_e.mp3")

#Heather screams for the first time
def heatherDie():
    heather = Find("Heather")
    if(heather):
        heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line931_col_e.mp3")        

#this makes me sad
def initVars():
    G.shadowList = [1, 1, 0, 0, 1]
    G.deadShadowMages = 0

#returns true if the shadow is not occupied
def isUnoccupied(spot):
    L1Spot = Find("Lasombra").GetOrigin()
    if(__main__.distanceSquared(L1Spot, spot) < 100000):
        return 0
    L2Spot = Find("Lasombra_2").GetOrigin()
    if(__main__.distanceSquared(L2Spot, spot) < 100000):
        return 0
    L3Spot = Find("Lasombra_3").GetOrigin()
    if(__main__.distanceSquared(L3Spot, spot) < 100000):
        return 0
    return 1

#tries to figure out which Lasombra is in the given shadow
def leaveShadow(number):
    trigger = Find("shadow_trigger_%i" % number)
    trigger.Enable()

#tells the game that the given shadow is now free for use
def shadowFree(number):
    G.shadowList[number] = 0
    print "shadowList [%i, %i, %i, %i, %i]" % (G.shadowList[0], G.shadowList[1], G.shadowList[2], G.shadowList[3], G.shadowList[4])
 
#tells the game that the given shadow is now occupied by a Lasombra
def shadowOccupied(number):
    shadowList[number] = 1
    print "shadowList [%i, %i, %i, %i, %i]" % (G.shadowList[0], G.shadowList[1], G.shadowList[2], G.shadowList[3], G.shadowList[4])
