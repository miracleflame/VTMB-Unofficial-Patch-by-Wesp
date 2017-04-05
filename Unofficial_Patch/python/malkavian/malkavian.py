print "loading malkavian level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#MALKAVIAN 1:
def LoadMap12():
    __main__.ChangeMap(1, "malkext", "malkentranceteleport")

#MALKAVIAN 3:
def LoadMap34():
    __main__.ChangeMap(1, "bedroom_landmark", "tobedroom")

#MALKAVIAN 2: Sets up patrol paths, and other entity / flag states loads the FIRST time the map is run...
def malk2_MapLoad():
    npc = Find("ghoul_entrance_s_3")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_a_1 hp_a_2 hp_a_3 hp_a_4 hp_a_5 hp_a_6 hp_a_7 hp_a_5 hp_a_3 hp_a_8")
    npc = Find("ghoul_great_hall_s_5")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_b_1 hp_b_2 hp_b_3 hp_b_1 hp_b_6 hp_b_5 hp_b_4")
    npc = Find("ghoul_dining_hall_s_4")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_c_1 hp_c_2 hp_c_3 hp_c_4 hp_c_5 hp_c_6 hp_c_9 hp_c_8 hp_c_7")
    npc = Find("ghoul_dining_hall_s_5")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_c_8 hp_c_7 hp_c_1 hp_c_9 hp_c_12 hp_c_11 hp_c_10")

    # all the lights / switchs START on....
    G.MalkavianMansion_Library_Lights = [1,1,1,1,1,1]		# changed by vladdmaster

    # change the state of this light so that
    # the puzzle is not solved by the scripted NPC
    libraryLightToggle(2)

    # the lamps upstairs start off....
    libraryLightToggle(4)
    libraryLightToggle(5)
    libraryLightToggle(6)

# Library downstairs lamps
#
# Updated 09-08-04 by TJP
# Skin swapping for bulbs was busted when I started... and my mucking around didn't miraculously fix it.
#
# The 3 wall lamps/levers toggle the lights on and off.
# Facing, left to right: 1 - 2 - 3
# lamp 1 (eye)  toggles lights 2 and 3 simultaneously- tested and confirmed TJP 09-08-04
# lamp 2 (time) toggles 1 and 3 on alternate pulls- tested and confirmed TJP 09-08-04
# lamp 3 (mind) toggles lights randomly - CORRECT - tested and confirmed TJP 09-08-04

#MALKAVIAN 2:
def libraryLightToggle( number ):
    #set flags so we know what state things are in. (lame)
    switch = Find("library_light_switch_%d" % number )
    if ( G.MalkavianMansion_Library_Lights[number-1] == 1):
        G.MalkavianMansion_Library_Lights[number-1] = 0
        switch.skin = 0
    else:
        G.MalkavianMansion_Library_Lights[number-1] = 1
        switch.skin = 1
    # Toggle the lights
    lights = FindList( "library_light_%d" % number )
    for light in lights:
        light.Toggle()

#MALKAVIAN 2:
def libraryLampOne():
        libraryLightToggle(2)
        libraryLightToggle(3)
        libraryLowerLightCheck()

#MALKAVIAN 2:
def libraryLampTwo():
    if ( G.MalkavianMansion_Library_Lamp_Two == 1 ):
        G.MalkavianMansion_Library_Lamp_Two = 0
        libraryLightToggle(3)
    else:
        G.MalkavianMansion_Library_Lamp_Two = 1
        libraryLightToggle(1)
    libraryLowerLightCheck()

#MALKAVIAN 2:
def libraryLampThree():
    from random import Random
    from time import time
    R = Random( time() )
    libraryLightToggle( R.randint(1,3) )
    libraryLowerLightCheck()

#MALKAVIAN 2:
def libraryLowerLightCheck():
    if ( G.MalkavianMansion_Library_Light_Ready and
         G.MalkavianMansion_Library_Lights[0] and
         G.MalkavianMansion_Library_Lights[1] and
         G.MalkavianMansion_Library_Lights[2] ):
        ent = Find("great_hall_door_bar_relay_1")
        ent.Trigger()

# Library upstairs lamps
#
# Updated 09-08-04 by TJP
# Skin swapping for bulbs was busted when I started... and my mucking around didn't miraculously fix it.
#
# The 3 wall lamps/levers toggle the lights on and off.
# facing, left to right- 4 - 5 - 6
# lamp 4 (chaos) toggles lights randomly- tested and confirmed TJP 09-08-04
# lamp 5 (key)   toggles 6 and 4 on alternate pulls- tested and confirmed TJP 09-08-04
# lamp 6 (order) toggles lights 5 and 4 simultaneously- tested and confirmed TJP 09-08-04

#MALKAVIAN 2:
def libraryLampFour():
    from random import Random
    from time import time
    R = Random( time() )
    libraryLightToggle( R.randint(4,6) )
    libraryUpperLightCheck()

#MALKAVIAN 2:
def libraryLampFive():
    if ( G.MalkavianMansion_Library_Lamp_Five == 0 ):
        G.MalkavianMansion_Library_Lamp_Five = 1
        libraryLightToggle(4)
    else:
        G.MalkavianMansion_Library_Lamp_Five = 0
        libraryLightToggle(6)
    libraryUpperLightCheck()

#MALKAVIAN 2:
def libraryLampSix():
    libraryLightToggle(4)
    libraryLightToggle(5)
    libraryUpperLightCheck()

#MALKAVIAN 2:
def libraryUpperLightCheck():
    if ( G.MalkavianMansion_Library_Lights[3] and
         G.MalkavianMansion_Library_Lights[4] and
         G.MalkavianMansion_Library_Lights[5] ):
        ent = Find("library_bookshelf_door")
        ent.Open()
        cam = Find("bookcase_cam")
        if ( cam ):
            tar = Find("bookcase_target")
            pc = Find("playercontroller")
            cam.PlayAsCameraPosition()
            tar.PlayAsCameraTarget()
            pc.ImmobilizePlayer()

#MALKAVIAN 3: Sets up patrol paths, and other entity / flag states loads the FIRST time the map is run..., changed by wesp
def malk3_MapLoad():
    npc = Find("ghoul_lab_s_6")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_d_1 hp_d_2 hp_d_3 hp_d_4 hp_d_5 hp_d_6 hp_d_7")
    npc = Find("ghouls_cells1_s_4")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_e_1 hp_e_2 hp_e_3")
    npc = Find("ghouls_cells2_s_3")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_f_1 hp_f_2 hp_f_3")
    npc = Find("ghouls_pits_s_1")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_g_1 hp_g_2")

#MALKAVIAN: Quest updates
def malk1_JournalSeeMingAsNines():
    __main__.FindPlayer().SetQuest( "Grout" , 4 )

def malk2_JournalEnterMap():
    __main__.FindPlayer().SetQuest( "Grout" , 5 )

def malk2_PuzzleExperience():
    __main__.FindPlayer().AwardExperience("Grout03")

def malk2_SanctumExperience():
    __main__.FindPlayer().AwardExperience("Grout04")

def malk4_JournalSeeGrout():
    __main__.FindPlayer().SetQuest( "Grout" , 2 )

#MALKAVIAN 5: When leaving, if player is nosferatu, return him to sewers else put at taxi_landmark in hub, changed by RobinHood70.
def LeaveMansion():
    pc = __main__.FindPlayer()
    if(pc.HasItem("item_k_malkavian_refrigerator_key")):
        __main__.ScheduleTask(5.00, "__main__.FindPlayer().RemoveItem(\"item_k_malkavian_refrigerator_key\")")
    if __main__.IsClan(__main__.FindPlayer(), "Nosferatu"):
        trig = Find("malk_la")
        trig.ScriptHide()
        trig = Find("malk_la_sewer")
        trig.ScriptUnhide()
    else:
        trig = Find("malk_la_sewer")
        trig.ScriptHide()
        trig = Find("malk_la")
        trig.ScriptUnhide()

print "levelscript loaded"
