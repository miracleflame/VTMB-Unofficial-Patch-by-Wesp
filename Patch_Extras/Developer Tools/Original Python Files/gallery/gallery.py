print "loading gallery level script"
#function's comments indicate what map they are called on
import __main__

from __main__ import G 

__main__.Level = __name__

Find = __main__.FindEntityByName

RandomLine = __main__.RandomLine
#slashedPaintings = [0, 0, 0, 0]


#GALLERY: called when the blood guardian is killed
def bloodGuardianDeath():
    __main__.FindPlayer().SetQuest("Slashterpiece", 2)
    G.Jeanette_Quest = 2

#GALLERY: called when the PC steals the charity money from Gallery Noir
def charityMoneyStolen():
    pc = __main__.FindPlayer()
    pc.MoneyAdd(250)
    if (pc.humanity >= 6):
        pc.HumanityAdd(-1)

#GALLERY: disables security in the Gallery if Chunk allows the player to enter
def disableGallerySecurity():
    if(G.Chunk_Befriend == 3 or G.Chunk_Dominated >= 1):
        switch = Find("camera_switch")
        switch.Deactivate()

#pretty self explanatory really
def enterGallery():
    G.SlashedPaintings = [0, 0, 0, 0]

#the paintings were slashed out of order, and now they will heal themselves
def healPaintings():
    i = 0
    while(i < 4):
        G.SlashedPaintings[i] = 0
        i = i + 1
    healer = Find("painting_healer")
    healer.Trigger()
    __main__.FindPlayer().Bloodloss(1)

#GALLERY: determines if the paintings have been placed in the gallery
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
        monies = Find("charity_monies")
        monies.ScriptUnhide()
    if(G.Jeanette_Refuse > 0 or G.Jeanette_Quest == 2):
        relay = Find("gallery_done_relay")
        relay.Trigger()
        monies = Find("charity_monies")
        monies.Kill()
        
#Gallery: called when a painting gets slashed.  Determines if it stays slashed, or if healing occurs
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
					
#GALLERY: updates the PC when they have slashed the paintings
def paintingsSlashed():
    G.Jeanette_Quest = 2
    __main__.FindPlayer().SetQuest("Slashterpiece", 2)

#GALLERY: Summons the blood creature when all four paintings are slashed.
def summonBloodCreature():
    summoner = Find("summon_relay")
    summoner.Trigger()

print "levelscript loaded"
