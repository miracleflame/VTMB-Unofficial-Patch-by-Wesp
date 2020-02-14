print "loading downtown level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

import random
random.seed()

#ABANDONED BUILDING: Called to enable the murder scene in the abandoned building
def abandonedBuildingMurder():
    if(G.Killer_Message):
        relay = Find("murder_scene_unhider")
        relay.Trigger()

#ABANDONED BUILDING: Called to determine results of talking with the bum
def bumDialog():
    if(G.Bum_Leave):
        script = Find("bum_flee_relay")
        script.Trigger()

#CONFESSION:  Makes the cages move
def ConfessionCages():
    nNumCages = 12
    from random import Random
    from time import time
    R = Random( time() )
    for n in range(1, nNumCages+1):
        E = Find("cagedancer_%d"%n)
        if(G.Confession_Crime == 0):
            E.SetAnimation("dance0%d" % R.randint(1,3))
        elif(1):
            cowerNumber = R.randint(1,3)
            if(cowerNumber == 1):
                E.SetAnimation("cower_idle")
            elif(1):
                E.SetAnimation("cower%d_idle" % cowerNumber)
        #COMMENTED OUT BECAUSE THE DANCERS DON'T ANIMATE RIGHT IF THE CAGES SWING
        #E = Find("cageimpact_%d"%n)
        #fScale = 0.5 + R.random()
        #E.scale(fScale)    #WHY DOES THIS CRASH?
       # E.Activate()
        
#CONFESSION: Called after talking to Venus
def venusDialog():
    if(G.Venus_Office):
        camera = Find("venus_camera")
        camera.StartShot()
        script = Find("venus_to_office")
        script.BeginSequence()
        #MAY CAUSE PROBLEMS LATER
        G.Venus_Office = 0

#CONFESSION: Called to determine if Patty is still there or not
def pattyGone():
    patty = Find("Patty")
    if(G.Patty_Alley or G.Patty_SD or G.Patty_Pisha):
        patty.Kill()

#E3 HUB: Sets the quest for E3
def setQuest():
    __main__.FindPlayer().SetQuest("Venus", 1)
    __main__.FindPlayer().SetQuest("LaCroix", 1)


#E3 HUB: Called when the player hacks Venus' computer
def hackcomplete():
    __main__.FindPlayer().SetQuest("LaCroix", 5)

#EMPIRE: Called afer dialog with Boris
def borisDialog():
    if(G.Boris_Hostile == 1):
        __main__.ScheduleTask(10.0, "__main__.FindEntityByName(\"Dema\").SetRelationship(\"player D_HT 5\")")
    elif(G.Boris_Hostile == 2):
        __main__.ScheduleTask(0.5, "__main__.FindEntityByName(\"Dema\").SetRelationship(\"player D_HT 5\")")
    elif(G.Dema_Go == 0):
        dema = Find("Dema")
        #NEED DIALOG CHANGE TO MAKE THIS COOLER
        dema.ScriptHide()
    elif(G.Boris_Dementated):
        boris = Find("Boris")
        boris.SetRelationship("Dema D_HT 5")
        dema = Find("Dema")
        __main__.ScheduleTask(2.0, "__main__.FindEntityByName(\"Dema\").SetRelationship(\"Boris D_HT 5\")")
        

#EMPIRE: Called when opening Boris' office door to see if anyone gets mad
def borisDoorOpen():
    if(__main__.IsDead("Dema")):
        #print "DEMA IS DEAD"
        boris = Find("Boris")
        boris.StartPlayerDialog()
    elif((G.Dema_Go != 1) and (G.Dema_Dominated != 1) and (G.Dema_Dementated != 1)):
       #print "DEMA IS ALIVE"
        dema = Find("Dema")
        dema.SetRelationship("player D_HT 5")
        boris = Find("Boris")
        boris.SetRelationship("player D_HT 5")

#EMPIRE: Called upon talking to Dema, Boris' guard
def demaDialog():
    if(G.Dema_Go == 1):
        script = Find("dema_escort_player")
        script.BeginSequence()
        pc = Find("dema_controller")
        pc.CreateControllerNPC()
        script = Find("player_move")
        script.BeginSequence()
    elif(G.Dema_Go == 2):
        __main__.ScheduleTask(10.0, "__main__.FindEntityByName(\"Dema\").SetRelationship(\"player D_HT 5\")")
    elif(G.Dema_Dominated == 1 or G.Dema_Dementated == 1):
        script = Find("dema_dominated")
        script.BeginSequence()
    elif(G.Dema_Hostile):
        boris = Find("Boris")
        boris.SetRelationship("player D_HT 5")

#EXHAUST PIPE:  Called as the player approaches Skelter/Damsel
def approachSkelter():
    skelter = Find("Skelter")
    damsel = Find("Damsel")
    if(G.Story_State < 20 and G.Skelter_Know == 0):
        skelter.StartPlayerDialog()

#EXHAUST PIPE:  Called to determine if any of the various Anarchs are missing from the bar
def populateBar():
    if(G.Story_State >= 20 and G.Story_State <= 90):
        nines = Find("Nines")
        nines.ScriptHide()

#HOSPITAL: Called to determine if Milligan is scared
def milliganDialog():
    script = Find("milligan_cower")
    script.BeginSequence()
   # milligan = Find("Milligan")
    #milligan.SetDisposition("Fear", 3)

#HOSPITAL: enacts the effects of talking to Pisha
def pishaDialog():
    if(G.Pisha_Attack):
        trigger = Find("pisha_fight_relay")
        trigger.Trigger()

#SKYLINE: Called after talking to Hannah
def hannahDialog():
    if(G.Hannah_Dead):
        hannah = Find("Hannah")
        hannah.WillTalk(0)
        hannah.SetDisposition("Dead", 1)

#SKYLINE: Populates the various skyline apartments if their residents are in
def residentCheck():
    #on plaguebearer quest
    if(G.Damsel_Quest):
        hannah = Find("Hannah")
        hannah.ScriptUnhide()
        paul = Find("paul")
        paul.ScriptUnhide()
        door = Find("paul_door")
        door.Unlock()
        answering_machine = Find("paul_answering_machine")
        answering_machine.ScriptUnhide()
    #serial killer victim #2, do we need this check here?
    if(G.SK_Downtown):
        answering_machine = Find("victim_answering_machine")
        answering_machine.ScriptUnhide()
    #Milligan
    if(G.Mill_Loose):
        milligan = Find("Milligan")
        milligan.ScriptUnhide()
        script = Find("milligan_scared")
        script.BeginSequence()

#SKYLINE: Called to switch which camera is active in the Skyline security room
def skylineCameraSwitch():
    G.Skyline_Camera = G.Skyline_Camera + 1
    if(G.Skyline_Camera > 10):
        G.Skyline_Camera = 1
    monitor = Find("security_monitor")
    monitor.SetCamera("camera_%i" % (G.Skyline_Camera))
        
#SKYLINE: Called to place the appropriate type of bloodpacks in the player's new haven.
def stockTheFridge():
    fridge = Find("fridge")
    bloodpacks = 3
    while(bloodpacks > 0):
        if(__main__.IsClan(__main__.FindPlayer(), "Ventrue")):
            fridge.SpawnItemInContainer("item_g_bluebloodpack")
        elif(1):
            fridge.SpawnItemInContainer("item_g_bloodpack")
        bloodpacks = bloodpacks - 1


#DOWNTOWN: set gangs to hate each other
def gangWarfare():
    sharks = ["shark_1", "shark_2"]
    jets = ["jet_1", "jet_2", "jet_3", "jet_4"]

    for i in range(0, len(sharks)):
        shark = Find(sharks[i])
        for j in range(0, len(jets)):
            shark.SetRelationship("%s D_HT 10" %jets[j])

    for j in range(0, len(jets)):
        jet = Find(jets[j])
        for i in range(0, len(sharks)):
            jet.SetRelationship("%s D_HT 10" %sharks[i])
        

#DOWNTOWN: set bums to stop talking if one has talked
def SetBumsTalk():
    if G.TinCanBill_Know:
        bums = FindList("Bum_disease_male") + FindList("Bum_disease_female")
        for bum in bums:
            bum.WillTalk(0)
##    elif G.TinCanBill_Heard:

#DOWNTOWN: unhide Tin Can Bill
def SetTinCanBill():
    if G.TinCanBill_Heard == 1 or G.TinCanBill_Know == 1:
        bill = Find("Tin_Can_Bill")
        if bill: bill.ScriptUnhide()

        trig = Find("trig_tincanbill")
        trig.Kill()


#DOWNTOWN: unhide Igor
def SetIgor():
    if G.Venus_Quest == 1:
        igor = Find("Igor")
        if igor: igor.ScriptUnhide()
        igorbuddy = Find("igor_buddy")
        if igorbuddy: igorbuddy.ScriptUnhide()

#DOWNTOWN: set igorbuddy to hate if igor hates
def IgorEndDialog():
    if (not G.Igor_Dominated and not G.Igor_Dementated):
        ## hope dialog doesn't change and assume igor then hates player.
        igorbuddy = Find("igor_buddy")
        if igorbuddy: igorbuddy.SetRelationship("player D_HT 5")


#DOWNTOWN: set Patty in alley by Confession
def SetPatty():
    if G.Patty_Alley:
        patty = Find("Patty")
        patty.ScriptUnhide()
        trig = Find("trig_patty_alley")
        trig.Enable()


#DOWNTOWN: random sound effect (dogs/cats fight)
def Alley1():
    if not random.randrange(3):
        a = Find("logic_alley1")
        a.Trigger()

#DOWNTOWN: random sound effect (parking garage)
def Alley2():
    if not random.randrange(4):
        a = Find("logic_alley2")
        a.Trigger()


print "levelscript loaded"
