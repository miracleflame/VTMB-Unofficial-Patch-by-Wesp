print "loading warrens level script"
#function's comments indicate what map they are called on
import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#SEWERS: unlocks drain controls if key present
def checkForPasskey():
    pc = __main__.FindPlayer()
    control = Find("control")
    if ( pc.HasItem("item_g_warrens4_passkey") ):
        control.Unlock()
    #changed by dan_upright 04/12/04 and by wesp
    elif ( pc.CalcFeat("inspection") < 5 ):
        sparklies = __main__.CreateEntityNoSpawn("inspection_node", 0, (0, 0, 0))
        sparklies.SetParent("PassKey")
        __main__.CallEntitySpawn(sparklies)

#WARRENS: Checks if mitnicks quest is active
def mitnicksCheckQuest():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Mitnick")
    if (state > 0):
        mitnicks = Find("Mitnick")
        if mitnicks: mitnicks.ScriptHide()

#WARRENS: Checks if imalias quest is active
def imaliaCheckQuest():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Imalia")
    #changed by dan_upright 09/12/04
    if ( state == 3 and G.Tawni_Dead == 0 and G.Tawni_Boy_Dead == 0 and G.Tawni_Spotted == 0 ):
    #changes end
        newspaper = Find("Imalias_Newspaper")
        if newspaper: newspaper.ScriptUnhide()
    #changed by dan_upright 07/12/04
        highlight = Find("Imalias_Newspaper_Inspect")
        highlight.ScriptUnhide()
    else:
        highlight = Find("Imalias_Newspaper_Inspect")
        if highlight: highlight.ScriptHide()
    #changes end

#WARRENS: Fires the relay that unlocks the door in Gary's room
def garyInteractionEnd():
    relay = Find("Relay_Gary_Interaction_End")
    relay.Trigger()

#WARRENS: Gary Scripts
def garyAppear():
    relay = Find( "Gary_Appear" )
    relay.Trigger()

def garyDisappear():
    relay = Find( "Gary_Disappear" )
    relay.Trigger()
    G.Prince_Gary = G.Prince_Gary + 1

#WARRENS: Gary camera scripts
def talkGaryLeft():
    gary = Find("Gary")
    gary.SetSoundOverrideEnt("gary_left")
    cam = Find("cam_gary_left")
    cam.StartShot()

def talkGaryRight():
    gary = Find("Gary")
    gary.SetSoundOverrideEnt("gary_right")
    cam = Find("cam_gary_right")
    cam.StartShot()

def talkGaryUp():
    gary = Find("Gary")
    gary.SetSoundOverrideEnt("gary_up")
    cam = Find("cam_gary_up")
    cam.StartShot()

def talkGaryMiddle():
    gary = Find("Gary")
    gary.SetSoundOverrideEnt("gary_middle")
    cam = Find("cam_gary_middle")
    cam.StartShot()

def talkGaryBack():
    gary = Find("Gary")
    gary.SetSoundOverrideEnt("gary_back")
    cam = Find("cam_gary_back")
    cam.StartShot()

#WARRENS: Imalia and Mitnick need to turn around in dialog
def ImaliaTurn():
    turn = Find("imalia_turn")
    turn.BeginSequence()

def MitnickTurn():
    turn = Find("mitnick_turn")
    turn.BeginSequence()

#def testflow(x, y, z):
#    print ( "Time, Flow, Steps" )
#    G.W_Time = x
#    G.W_FlowMax = y
#    G.W_FlowSteps = z
#    G.Flow_Ran = 0
#
#def flowUp():
#    ctrlmdl = Find( "Water_Control_MDL" )
#    flow_ent = Find( "Flow_Push" )
#    flow_ent.SetSpeed(G.flow_amt)
#    if ( G.flow_amt == ( G.flow_amt /5 ) ):
#         ctrlmdl.Skin(1)
#def flowDwn():
#    ctrlmdl = Find( "Water_Control_MDL" )
#    flow_ent = Find( "Flow_Push" )
#    flow_ent.SetSpeed(G.flow_amt)
#    if ( G.flow_amt == ( G.flow_amt /5 ) ):
#         ctrlmdl.Skin(1)
#
#def masterFlow(direction):
#    if ( G.Flow_Ran == 1 ):
#        G.flow_amt =( G.W_FlowMax / G.W_FlowSteps )
#        G.time_inc = G.W_Time / G.W_FlowSteps
#    G.Flow_Ran = 1
#    fanmdl = Find( "Flow_fan_blade" )
#    sndon = Find( "Sound_Flow_ON" )
#    sndoff = Find( "Sound_Flow_OFF" )
#    triggers = Find( "FloodRoom_Triggers" )
#
#    if (direction == UP):
#        G.WarrensPump = 1
#        triggers.ScriptUnhide()
#        fanmdl.Start()
#        sndon.PlaySound()
#        sndoff.StopSound()
#        while ( G.flow_amt < G.W_FlowMax ):
#            __main__.ScheduleTask( G.time_inc, "flowUp()" )
#            G.flow_amt = G.flow_amt + G.flow_amt
#
#    if (direction == DOWN):
#        G.WarrensPump = 0
#        triggers.ScriptHide()
#        fanmdl.Stop()
#        sndoff.PlaySound()
#        sndon.StopSound()
#        while ( G.flow_amt > 0 ):
#            __main__.ScheduleTask( G.time_inc, "flowDwn()" )
#            G.flow_amt = G.flow_amt - G.flow_amt

print "levelscript loaded"