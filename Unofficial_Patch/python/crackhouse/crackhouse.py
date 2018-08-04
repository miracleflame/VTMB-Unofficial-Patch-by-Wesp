print "loading crackhome level script"

import __main__

from __main__ import G

__main__.Level = __name__

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#CRACKHOUSE: Called on Vick's death, changed by wesp
def bishopVickDeath():
    pc = __main__.FindPlayer()
    if pc.GetQuestState("AllPlague") > 0:
        pc.SetQuest( "AllPlague", 3 )
    if pc.GetQuestState("Regent") > 0 and not pc.GetQuestState("Regent") == 7:
        pc.SetQuest("Regent", 5)
    G.Vick_Dead = 1
    G.Jumbles_Removed = 1
    __main__.ChangeMap(3, "ch_exit_landmark", "trig_ch_exit")

def reenterCheck():
    if G.Jumbles_Removed >= 1:
        __main__.ChangeMap(3, "ch_exit_landmark", "trig_ch_exit")

print "crackhouse levelscript loaded"
