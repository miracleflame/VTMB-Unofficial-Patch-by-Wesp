print "loading warrens level script"
#function's comments indicate what map they are called on
import __main__

from __main__ import G 

__main__.Level = __name__

Find = __main__.FindEntityByName

#unlocks drain controls if key present
def checkForPasskey():
    pc = __main__.FindPlayer()
    control = Find("control")
    if ( pc.HasItem("item_g_warrens4_passkey") ):
        control.Unlock()

# Warrens: checks if mitnicks quest is active
def imaliaCheckQuest():
    if (G.Imalia_Quest == 3 ):
        newpaper = Find("Imalias_Newspaper")
        newpaper.ScriptUnhide()

# Set's mitnick's default disposition
def patchMitnick():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Mitnick")
    if ( state < 1 ):
        mitnick = Find( "Mitnick" )
        if ( mitnick ):
            mitnick.SetDisposition( "OperateComputer", 1 )

# Warrens 5: Called each time the map is loaded,
#            used to fix any scripting issues
def hw_warrens_5_patch():
    if ( G.patch_hw_warrens_5 < 1 ):
        #patchMitnick()
        G.patch_hw_warrens_5 = 1

        

#Warrens: checks if mitnicks quest is active
def mitnicksCheckQuest():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Mitnick")
    if (state > 0):
        mitnick = Find("Mitnick")
        mitnick.ScriptHide()


#Warrens: checks if mitnicks quest is active
def imaliaCheckQuest():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Imalia")
    if ( state == 3 ):
        newspaper = Find("Imalias_Newspaper")
        newspaper.ScriptUnhide()
 
#Warrens: Fires the relay that unlocks the door in Gary's room
def garyInteractionEnd():
    relay = Find("Relay_Gary_Interaction_End")
    relay.Trigger()

#Gary Scripts
def garyAppear():
    relay = Find( "Gary_Appear" )
    relay.Trigger()

def garyDisappear():
    relay = Find( "Gary_Disappear" )
    relay.Trigger()
    G.Prince_Gary = G.Prince_Gary + 1


#gary camera scripts
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

#HW_WARRENS_5: Imalia and Mitnick need to turn around in dialog
def ImaliaTurn():
    turn = Find("imalia_turn")
    turn.BeginSequence()

def MitnickTurn():
    turn = Find("mitnick_turn")
    turn.BeginSequence()
    mitnick = Find("Mitnick")
    mitnick.SetDisposition("Neutral",1)


##def testflow(x, y, z):
##    print ( "Time, Flow, Steps" )
##    G.W_Time = x
##    G.W_FlowMax = y
##    G.W_FlowSteps = z
##    G.Flow_Ran = 0
##
##def flowUp():
##    ctrlmdl = Find( "Water_Control_MDL" )
##    flow_ent = Find( "Flow_Push" )
##    flow_ent.SetSpeed(G.flow_amt)
##    if ( G.flow_amt == ( G.flow_amt /5 ) ):
##         ctrlmdl.Skin(1)
##def flowDwn():
##    ctrlmdl = Find( "Water_Control_MDL" )
##    flow_ent = Find( "Flow_Push" )
##    flow_ent.SetSpeed(G.flow_amt)
##    if ( G.flow_amt == ( G.flow_amt /5 ) ):
##         ctrlmdl.Skin(1)
##
##def masterFlow(direction):
##    if ( G.Flow_Ran == 1 ):
##        G.flow_amt =( G.W_FlowMax / G.W_FlowSteps )
##        G.time_inc = G.W_Time / G.W_FlowSteps
##    G.Flow_Ran = 1
##    fanmdl = Find( "Flow_fan_blade" )
##    sndon = Find( "Sound_Flow_ON" )
##    sndoff = Find( "Sound_Flow_OFF" )
##    triggers = Find( "FloodRoom_Triggers" )
##
##    if (direction == UP):
##        G.WarrensPump = 1
##        triggers.ScriptUnhide()
##        fanmdl.Start()
##        sndon.PlaySound()
##        sndoff.StopSound()
##        while ( G.flow_amt < G.W_FlowMax ):
##            __main__.ScheduleTask( G.time_inc, "flowUp()" )
##            G.flow_amt = G.flow_amt + G.flow_amt
##
##    if (direction == DOWN):
##        G.WarrensPump = 0
##        triggers.ScriptHide()
##        fanmdl.Stop()
##        sndoff.PlaySound()
##        sndon.StopSound()
##        while ( G.flow_amt > 0 ):
##            __main__.ScheduleTask( G.time_inc, "flowDwn()" )
##            G.flow_amt = G.flow_amt - G.flow_amt
            
print "levelscript loaded"
