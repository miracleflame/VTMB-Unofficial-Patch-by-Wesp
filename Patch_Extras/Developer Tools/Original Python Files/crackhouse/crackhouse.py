print "loading crackhome level script"

import __main__


import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

def bishopVickDeath():
    pc = __main__.FindPlayer()
    if pc.GetQuestState("AllPlague") > 0:
        pc.SetQuest( "AllPlague", 3 )

    if pc.GetQuestState("Regent") > 0:
        pc.SetQuest("Regent", 5)
        
    G.Jumbles_Removed = 1
    __main__.ChangeMap(3, "ch_exit_landmark", "trig_ch_exit")



print "crackhouse levelscript loaded"
