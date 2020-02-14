print "****************** loading warehouse level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName


def hateSabbat():
    sabbat = Find( "Sabbat1" )
    if (sabbat):
        sabbat.SetRelationship( "Office_Thugs_JDA D_HT 5" )
        sabbat.SetRelationship( "thug_s_office_2 D_HT 5" )
        sabbat.SetRelationship( "thug_s_office_1 D_HT 5" )
        sabbat.SetRelationship( "spawns1 D_HT 5" )
        sabbat.SetRelationship( "spawns2 D_HT 5" )

    print ( "********* Setting Hate **********" )

#WAREHOUSE: called when the beckett cutscene starts
def beckettSceneStart():
    FindByClass = __main__.FindEntitiesByClass
    thugs = FindByClass("npc_VHumanCombatant")
    for thug in thugs:
        thug.Kill()

#WAREHOUSE: sends the player to santa monica after talking to Beckett at the warehouse
def toSantaMonica():
    __main__.ChangeMap(2.5, "warehouselandmark", "santamonicateleport")

#WAREHOUSE: XP bonus for not killing anyone
def warehouseBonusPoints():
    if (G.Warehouse_Kills == 0):
        playerevents = Find("controller")
        playerevents.AwardExp("Explosive04")

#WAREHOUSE: called when warehouse blows up
def finishWarehouseQuest():
    __main__.FindPlayer().SetQuest("Warehouse", 4)

#Set all interior Thugs to flee and die
def fearThugs():
    thugs = Finds( "Thugs_Door_JDA" )
    for thug in thugs:
        if (thug):
            thug.FleeAndDie()
    thug = Find( "door_thug_2jda" )
    if (thug):
        thug.FleeAndDie()
    thugs = Finds( "Thugs_Inside_JDA" )
    for thug in thugs:
        if (thug):
            thug.FleeAndDie()
    thugs = Finds( "Heavy_Freight_Thugs" )
    for thug in thugs:
        if (thug):
            thug.FleeAndDie()
    thug = Find( "thug_second_wave_patrol" )
    if (thug):
        thug.FleeAndDie()
    thug = Find( "thug_interior_2" )
    if (thug):
        thug.FleeAndDie()
    thug = Find( "thug_interior_1" )
    if (thug):
        thug.FleeAndDie()
    thug = Find( "thug_outback" )
    if (thug):
        thug.FleeAndDie()
    thugs = Finds( "Office_Thugs_JDA" )
    for thug in thugs:
        if (thug):
            thug.FleeAndDie()
    thug = Find( "thug_s_office_2" )
    if ( thug ):
        thug.FleeAndDie()
    thug = Find( "thug_s_office_1" )
    if (thug):
        thug.FleeAndDie()
    thug = Find( "spawns1" )
    if (thug):
        thug.FleeAndDie()
    thug = Find( "spawns2" )
    if (thug):
        thug.FleeAndDie()

    print ( "*********** Fearing all Interior Thugs ************" )

# Remove all outside thugs
def removeOutsideThugs():
    thug = Find( "Truckyard_Guard_2" )
    if (thug):
        thug.Kill()
    thug = Find( "Truckyard_Guard_1" )
    if (thug):
        thug.Kill()
    thug = Find( "jump_guard" )
    if (thug):
        thug.ScriptUnhide()
        thug.Kill()
    thug = Find( "player_1" )
    if (thug):
        thug.Kill()
    thug = Find( "player_2" )
    if (thug):
        thug.Kill()
    thugs = Finds( "thug_row1_lounger" )
    for thug in thugs:
        if (thug):
            thug.Kill()
    thug = Find( "thug_row2_patrol" )
    if (thug):
        thug.Kill()
    thug = Find( "engine_guard" )
    if (thug):
        thug.Kill()
    thug = Find( "thug_parking_lot_patrol" )
    if (thug):
        thug.Kill()
    thug = Find( "thug_station_bathroom" )
    if (thug):
        thug.Kill()
    thug = Find( "maker front" )
    if (thug):
        thug.Kill()
    thug = Find( "maker back" )
    if (thug):
        thug.Kill()
    print ( "*********** Removing all outside Thugs ************" )



# Bring on the Sabbat
def bringOnSabbat():
    sabbat = Find( "NPC_Sabbat1" )
    print ( "*********** Unhiding Sabbat1 ************" )
    sabbat.ScriptUnhide()
    print ( "*********** Unhiding Sabbat2 ************" )
    sabbat = Find( "NPC_Sabbat2" )
    sabbat.ScriptUnhide()
    removeOutsideThugs()
    hateSabbat()
    block = Find( "Exit_Block" )
    block.ScriptUnhide()
    
def testtrigg():
    print ( "******** Triggered **********" )

def explodeBoxes():
    print ( "******************** explodeing boxes **********************" )
    box = Find( "truckyard_crush_boxes" )
    box.Break()

def boxExplosion():
    print ( "******************** timeing explodeing boxes **********************" )
    __main__.ScheduleTask( 3.7, "explodeBoxes()" )

print "*************levelscript loaded"
