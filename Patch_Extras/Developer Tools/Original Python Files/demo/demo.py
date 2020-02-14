print "loading demo level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass



  
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
    

def despawnBomb():  
    bomb = FindClass("item_g_astrolite")  
    origin = bomb[0].GetOrigin()  
    angles = bomb[0].GetAngles()  
    bomb[0].Kill()  
    bombProp = Find("bomb_prop")  
    bombProp.SetOrigin(origin)  
    bombProp.SetAngles(angles)  
    bombProp.ScriptUnhide()

def SquareTrigger():
    from __main__ import *
    #Player = __main__.FindPlayer()

def TriggerEnable():
    from __main__ import *
    nNumSquares = 64   
    for n in range(1, nNumSquares+1):
        E = Find("trigger_%d"%n)
        E.Enable()

def TriggerDisable():
    from __main__ import *
    nNumSquares = 64   
    for n in range(1, nNumSquares+1):
        E = Find("trigger_%d"%n)
        E.Disable()
        
def SquareTimer():
    from __main__ import *
    nNumSquares = 64
    nNumSkins = 4
    from random import Random
    from time import time
    R = Random( time() )
    for n in range(1, nNumSquares+1):
        E = Find("cube_%d"%n)
        nSkin = (R.random()*100)%nNumSkins
        #print "cube %d being set to skin %d " % (n,  nSkin)
        E.SetSkin( nSkin )
        



def ConfessionCages():
    nNumCages = 12
    from random import Random
    from time import time
    R = Random( time() )
    for n in range(1, nNumCages+1):
        E = Find("cagedancer_%d"%n)
        E.SetAnimation("dance0%d" % R.randint(1,3))
        E = Find("cageimpact_%d"%n)
        fScale = 0.5 + R.random()
        #E.scale(fScale)    #WHY DOES THIS CRASH?
        E.Activate()


    
    

print "levelscript loaded"
