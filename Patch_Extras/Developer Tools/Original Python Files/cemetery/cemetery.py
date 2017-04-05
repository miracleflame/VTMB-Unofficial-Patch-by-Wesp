print "loading cemetery level script..."

import __main__

from __main__ import G 

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

#CEMETERY: removes all zombies and disables spawners
def destroyAllZombies():
    print ( "***********  All Zombies removed and disabled   ***********" )
    relay = Find( "Relay_Waves_End" )
    relay.Trigger()
    zombies = Finds( "zombie" )
    for zombie in zombies:
        zombie.Kill()

#CEMETERY:  Setup cemetery quest on map Load
def checkCemeteryQuest():
    print ( "************** Running Check CemeteryQuest *****************" )
    destroyAllZombies()
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Romero")
    if (state > 1):
        print ( "***********  General Setup For Map Post Romero Quest *************" )
        relaygates = Find("Relay_Gates_Post_Quest")
        relaygates.Trigger()
    if (state == 3):
        print ( "***********  Map in Boched State  *************" )
        timerrelay = Find("timer_logic_start")
        timerrelay.Kill()
        doorblocks = Finds("Door_Blocks")
        for doorblock in doorblocks:
                doorblock.ScriptUnhide()
        remero = Find("romero")
        remero.ScriptHide()
    if (state == 2 or state == 1):
        print ( "***********  Map in Success State *************" )
        sequence = Find("romero_seq1")
        sequence.BeginSequence()
    if (state < 1):
        print ( "***********  Map in Default State *************" )
        sequence = Find("romero_seq1")
        if (sequence):
            print ("Found Couch Sequence")
            sequence.BeginSequence()

#CEMETERY:  Checks on entering Romero Shack
def runRomeroSeq():
    if ( G.CemeteryBoched == 1 ):
        romeroseq1 = Find("romero_seq1")
        romeroseq1.CancelSequence()
        return
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Romero")
    if (((state < 1) and (G.Romero_Offer == 0)) or (G.Romero_Whore == 2)):
        print ( "***********  Romoro Init Dialogue *************" )
        control = Find ("Player_control")
        control.CreateControllerNPC()
        playerseq = Find("player_control_seq")
        playerseq.BeginSequence()
        romeroseq1 = Find("romero_seq1")
        romeroseq1.CancelSequence()
        romeroseq2 = Find("romero_seq_stand")
        romeroseq2.BeginSequence()

#CEMETERY:  fade the player back to HW after failing zombies.
def leaveCemetery():
    __main__.ChangeMap(2.5, "hollywood", "cem_hollywood")

#CEMETERY:  End of Romero dlg set up
def setCemQuest():
    print ("running setCemQuest")
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Romero")
    stateho = pc.GetQuestState("Loser")
    if (G.Romero_Hate == 1):
        print ( "Romero Hates You")
        romero = Find("Romero")
        romero.SetRelationship("player D_HT 5")
        return
    if (stateho == 5):
        print ( "Delivered the Goods" )
        prostitute = Find( "ProstituteCem" )
        prostitute.Kill()
        relay = Find( "Relay_Prostitute_Event" )
        relay.Trigger()
    if (state == 3):
        print ( "Boched Reaction")
        bochedlevel = Find("Relay_Zombie_Kill_Sequence")
        bochedlevel.Trigger()
    elif (state == 2):
        if (G.FinishedCemetery == 0):
            print ( "Success Teleport back to HW")
            G.FinishedCemetery = 1
            __main__.ScheduleTask( 7.5, "leaveCemetery()" )
        else:
            print ( "Just exit dialogue" )
    elif (state == 1):
        print ( "Been given the quest")
        eventStart = Find("quest_accepted")
        eventStart.Trigger()
    elif (state == 0):
        print ( "Denied to do the quest")
        romeroseq1 = Find("romero_seq1")
        romeroseq1.BeginSequence()

#CEMETERY:  trigger Romero sequence if you fail.
def failureCheck():
    failureRelay = Find("Relay_Zombie_Kill_Sequence")
    failureRelay.Trigger()

#CEMETERY:  Botch Remote
def checkBotch():
    print ( "*********** Is PC chickening out on Romero ***********" )
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Romero")
    if (state == 1):
        botch = Find("Relay_Chicken_Botch")
        botch.Trigger()

#CEMETERY:  Fill Romero's container
def ammoRefill():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Romero")
    if  (state == 1):
        container = __main__.Find("romero_container")
        player = __main__.FindPlayer() 
        if (container):
            container.DeleteItems()
            if ( player.HasItem("item_w_thirtyeight") ):
                container.SpawnItemInContainer("item_w_thirtyeight")
                container.SpawnItemInContainer("item_w_thirtyeight")
            if ( player.HasItem("item_w_glock_17c") ):
                container.SpawnItemInContainer("item_w_glock_17c")
                container.SpawnItemInContainer("item_w_glock_17c")
            if ( player.HasItem("item_w_ithaca_m_37") ):
                container.SpawnItemInContainer("item_w_ithaca_m_37")
                container.SpawnItemInContainer("item_w_ithaca_m_37")


#Masqurad Violation: Triggered when gates break
def masquradeViolation():
    pc = __main__.FindPlayer()
    pc.ChangeMasqueradeLevel( 1 )

#CEMETERY: puts tape in Ginger Swan's crypt
def SetGingerSwanTape():
    if __main__.FindPlayer().GetQuestState("Courier") == 4:
        door = Find("swan_door_container")
        door.ScriptUnhide()
        node = Find("swan_inspect")
        node.ScriptUnhide()
        G.Ginger_Swan = 2

#CEMETERY: set quest on tape retrieval
def SetGingerSwanTapeQuestState():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Courier")
    if (state > 2 and state < 5):
        pc.SetQuest("Courier", 5)

## CEMETERY: Romero Prostitute disband follower, fade and teleport (from romero dlg)
def endRomero():
    print ( "*************** Cleaning up Loser Quest ***************" )

## CEMETERY: 
def startProstituteDlg():
    prostitute = Find("ProstituteCem")
    if ( prostitute ):
        prostitute.StartPlayerDialog(0)
        
## CEMETERY: Prostitute inits dialogue in cemetery (on trigger in cemetery)
def prostituteInitCemetery():
    prostitute = Find("ProstituteCem")
    print ( "**************** Looking for Romero Prostitute ********************" )
    if ( G.Whore_Follower == 1 and G.In_Cemetery == 0 and G.Romero_Whore == 2 ):
        print ( "************** Have Prostitute for Romero ********************" )
        G.In_Cemetery = 1
        if ( G.Blondie == 1 ):
            prostitute.SetModel( "models/character/npc/common/prostitute/prostitute_1/prostitute_1.mdl" )
            print ( "************** Is Blondie ********************" )
        if (prostitute):
            print ( "***************** Unhide Prostitute ******************" )
            prostitute.ScriptUnhide()
        sequence = Find( "Seq_SetupProstitute" )
        sequence.BeginSequence()
        prostitute.SetFollowerBoss( "!Player" )
        trigger = Find( "Trigger_Pimp" )
        trigger.Kill()
        if (G.Whore_Orphans == 1):
            print ( "*************** Whore_Orphans == 1, Should Talk ****************" )
            __main__.ScheduleTask( 2.0, "startProstituteDlg()" )
    else:
        print ( "**************** No Prostitute ********************" )
        

## CEMETERY: Fail Loser Quest when Romero dies
def failLoser():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Loser")
    if (state > 1):
       pc.SetQuest("Loser", 4)

def cemeteryFail():
    pc = __main__.FindPlayer()
    pc.SetQuest("Romero", 3)
        
print "...cemetery levelscript loaded"
