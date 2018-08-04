print "loading gallery level script"
#function's comments indicate what map they are called on
import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName

#slashedPaintings = [0, 0, 0, 0]

# RandomLine update, added by Hasimir
# When the game is launched and a save game loaded there is no
# RandomLine in __main__ so we have to check for that:
try:
    RandomLine = __main__.RandomLine
except:
    from vamputil import RandomLine

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#GALLERY: Called when the blood guardian is killed, changed by wesp
def bloodGuardianDeath():
    __main__.FindPlayer().SetQuest("Slashterpiece", 2)
    G.Jeanette_Quest = 2
    __main__.ccmd.vamplight=""
    __main__.ccmd.vampexpo=""

#GALLERY: Called when the PC steals the charity money from Gallery Noir, changed by wesp
def charityMoneyStolen():
    pc = __main__.FindPlayer()
    pc.MoneyAdd(250)
    box_spark = Find("box_sparklies")
    box_spark.ScriptHide()
    if (pc.humanity >= 6 and (G.Charity_Know == 0 or G.Patch_Plus == 0)):
        pc.HumanityAdd(-1)

#GALLERY: Disables security in the Gallery if Chunk allows the player to enter, changed by wesp
def disableGallerySecurity():
    if(G.Jeanette_Quest == 1 and (G.Chunk_Befriend >= 2 or G.Chunk_Dominated >= 1 or G.Chunk_Demented == 1)):
        switch = Find("camera_switch")
        switch.Deactivate()

#GALLERY: Pretty self explanatory really
def enterGallery():
    G.SlashedPaintings = [0, 0, 0, 0]

#GALLERY: The paintings were slashed out of order, and now they will heal themselves, changed by wesp
def healPaintings():
    i = 0
    while(i < 4):
        G.SlashedPaintings[i] = 0
        i = i + 1
    healer = Find("painting_healer")
    healer.Trigger()
    __main__.FindPlayer().Bloodloss(1)
    if G.Patch_Plus == 1:
        c  = __main__.ccmd
        c.showBotch=""

#GALLERY: Determines if the paintings have been placed in the gallery, changed by wesp
def paintingsInGallery():
    if(G.Jeanette_Quest == 1 or G.Jeanette_Refuse > 0):
        i = 0
        while(i < 4):
            painting = Find("painting_%i" % i)
            painting.ScriptUnhide()
            i = i + 1
        signs = __main__.FindEntitiesByName("signs")
        for s in signs:
            s.ScriptUnhide()
        if G.Patch_Plus == 1:
            monies = Find("cash_box")
            monies.ScriptUnhide()
            box_spark = Find("box_sparklies")
            box_spark.ScriptUnhide()
        else:
            monies = Find("charity")
            monies.ScriptUnhide()
            box_spark = Find("box_sparklies")
            box_spark.ScriptUnhide()
            switch = Find("charity_monies")
            switch.ScriptUnhide()
        if(not __main__.IsDead("Chunk") and G.Jeanette_Quest == 1 and G.Patch_Plus == 1):
            __main__.FindPlayer().AwardExperience("Slash02")
    if(G.Jeanette_Refuse > 0 or G.Jeanette_Quest == 2):
        relay = Find("gallery_done_relay")
        relay.Trigger()
# removed        monies = Find("charity_monies")
# by wesp        monies.Kill()

#Gallery: Called when a painting gets slashed.  Determines if it stays slashed, or if healing occurs
def paintingSlashed(p):
    outOfOrder = 0
    if(p == 0):
        G.SlashedPaintings[0] = 1
    else:
        i = 0
        while(i < p):
            if(G.SlashedPaintings[i] == 0):
                outOfOrder = 1
                break;
            i = i + 1
        if(outOfOrder == 1):
            healPaintings()
        else:
            G.SlashedPaintings[p] = 1
            if(p == 3):
                summonBloodCreature()

#GALLERY: Updates the PC when they have slashed the paintings
def paintingsSlashed():
    G.Jeanette_Quest = 2
    __main__.FindPlayer().SetQuest("Slashterpiece", 2)

#GALLERY: Summons the blood creature when all four paintings are slashed.
def summonBloodCreature():
    summoner = Find("summon_relay")
    summoner.Trigger()

print "levelscript loaded"
