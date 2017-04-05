print "loading silly test level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName


def TripDlg():
    from __main__ import *
    if (npc.times_talked == 1):
        return 1
    elif (G.Trip_Dominated == 1):
        return 201
    elif (G.Trip_Trust == 1):
        return 231
    elif (G.Trip_Trust < 1):
        return 251

def PlayAnimation(szAnimName):
    from __main__ import *
    EntList = FindList("char_prop")
    for Ent in EntList:
        Ent.SetAnimation(szAnimName)

print "levelscript loaded"
