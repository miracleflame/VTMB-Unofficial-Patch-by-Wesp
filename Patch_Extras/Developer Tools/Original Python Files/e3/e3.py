print "loading demo level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName


#########################################################################################
# DIALOG STARTING CONDITIONS
#########################################################################################

def CalDlg():
    from __main__ import *
    if ( G.Cal_quits == 1):
        return 151
    elif (G.Cal_permission == 1):
        return 141
    elif (IsClan(pc,"Nosferatu")):
        return 131
    elif (G.Cal_known ==0 and IsMale(pc)):
        return 1
    else:
        return 71


def CalDlg_Malkavian():
    from __main__ import *
    if ( G.Cal_quits == 1):
        return 151
    elif (G.Cal_permission == 1):
        return 141
    elif (G.Cal_known ==0 and IsMale(pc)):
        return 1
    elif (G.Cal_known ==0 and not IsMale(pc)):
        return 21

def JeanetteDlg():
    from __main__ import *
    if (npc.times_talked == 1):
        return 1
    elif (G.Jeanette_Pissed == 1):
        return 251
    elif (G.Jeanette_Quest == 2):
        return 181
    elif (G.Jeanette_Quest == 4):
        return 261
    else:
	return 251

def Chunk_GuardDlg():
    from __main__ import *
    if (npc.times_talked == 1):
        return 1
    elif (npc.times_talked > 1):
        return 111


    

  
#########################################################################################
# EVENT SCRIPTS
#########################################################################################


def PlayAnimation(szAnimName):
    from __main__ import *
    EntList = FindList("char_prop")
    for Ent in EntList:
        Ent.SetAnimation(szAnimName)


def TestNewEntity():
    from __main__ import *
    Origin = FindPlayer().Center()
    Angles = FindPlayer().Angles()
    NewEnt = CreateEntityNoSpawn("prop_physics", Origin, Angles )
    NewEnt.SetModel("models/scenery/PHYSICS/barbell/100lbs.mdl")
    CallEntitySpawn( NewEnt )
 
