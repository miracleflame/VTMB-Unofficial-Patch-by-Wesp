print "loading chinatown level script"
#function's comments indicate what map they are called on
import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

# RandomLine update, added by Hasimir
# When the game is launched and a save game loaded there is no
# RandomLine in __main__ so we have to check for that:
try:
    RandomLine = __main__.RandomLine
except:
    from vamputil import RandomLine

#Vamputil.py not loaded fix, added by Hasimir, changed by wesp
if __main__.IsClan or FindPlayer.IsClan or IsClan or __main__.IsIdling or FindPlayer.IsIdling or IsIdling is null:
    from vamputil import *

#F.U. SYNDICATE: Check gamestate and open doors accordingly, changed by wesp
def startTest():
    if (G.Barrabus_Exit != 0):
        barabus = Find("barabus")
        if barabus: barabus.Kill()
    if (G.Mandarin_Fu > 0):
        confDoor1 = Find("lobbydoor1")
        confDoor2 = Find("lobbydoor2")
        liftDoor1 = Find("liftdoor1")
        liftDoor2 = Find("liftdoor2")
#        world = Find("world")
#        world.SetSafeArea(0)
        confDoor1.Unlock()
        confDoor2.Unlock()
        confDoor1.Open()
        confDoor2.Open()
        if (G.Mandarin_Enter == 1) and (G.Mandarin_Ride == 0):
            liftDoor1.Open()
            liftDoor2.Open()

#F.U. SYNDICATE: Spawns bertram's key after mandarin dies.
def spawnBarabusKey():
    mandarin = Find("Mandarin")
    center = mandarin.GetCenter()
    point = (center[0], center[1], center[2] + 20)
    key = __main__.CreateEntityNoSpawn("item_k_fu_cell_key", point, (0,0,0) )
    key.SetName("fu_key")
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
    sparklies.SetParent("fu_key")
    __main__.CallEntitySpawn(key)
    __main__.CallEntitySpawn(sparklies)

#F.U. SYNDICATE: Spawns office key from guard.
def spawnOfficeKey():
    guard = Find("guard_1")
    center = guard.GetCenter()
    point = (center[0], center[1], center[2] + 20)
    key = __main__.CreateEntityNoSpawn("item_k_fu_office_key", point, (0,0,0) )
    key.SetName("office_key")
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
    sparklies.SetParent("office_key")
    __main__.CallEntitySpawn(key)
    __main__.CallEntitySpawn(sparklies)

#F.U. SYNDICATE: Starts and restarts the lasers (thanks to stealing Jocelyn code and modifying it), fixed by RobinHood70
class LaserRoomBeams :
    def __init__(self):
        self.reinit()

    def reinit(self):
        print "initializing beams"
        self.track = []
        self.beam = []
        self.beamOn = [0, 0, 0, 0, 0, 0, 0]
        self.beamsStarted = 0
        self.numBeams = 7
        self.beamsFlicker = 1
        self.beamsEnabled = 1

        self.FindTracks()
        self.FindBeams()

        self.SetBeamWidth(1)

        # added by RobinHood70
        for i in range(self.numBeams):
            __main__.ScheduleTask(0.10, "mb.ToggleBeam(%i)" % i)
            __main__.ScheduleTask(0.20, "mb.ToggleBeam(%i)" % i)

    # get beams started
    def StartBeams(self):
        print "beams started"
        if self.beamsStarted == 0:
            for i in range( len(self.track) ):
                self.track[i].Open()
                self.beamOn[i] = 1

            self.beamsStarted = 1

    # make beam[i] go other direction when it hits the end of its track
    # toggle beam[i] on/off when open/close if power shot out
    # RobinHood70:  Note that the FU beams do not seem to suffer from the same problem the museum beams do, so no Try/Except is necessary here.
    def ToggleBeam(self, i):
        if i >= self.numBeams:
            return
        elif self.beamOn[i] == 1:
            self.beamOn[i] = 0
            self.track[i].Close()
        else:
            self.track[i].Open()
            self.beamOn[i] = 1

        if self.beamsFlicker == 1 and self.beamsEnabled == 1:
#            self.beam[i].Toggle()
#            uncommenting following lines will cause game to crash after a minute or so.
            __main__.ScheduleTask(0.10, "__main__.FindEntityByName(\"beam_%d\").Toggle()" %(i+1))
#            __main__.ScheduleTask(0.20, "__main__.FindEntityByName(\"beam_%d\").Toggle()" %(i+1))
#            __main__.ScheduleTask(0.20, "__main__.FindEntityByName(\"beam_trig_%d\").Toggle()" %(i+1))

    def FindTracks(self):
        self.track = []

        for i in range(self.numBeams):
            t = Find("track_%i" % (i+1))
            self.track.append(t)

    def FindBeams(self):
        self.beam = []

        for i in range(self.numBeams):
            b = Find("beam_%i" % (i+1))
            self.beam.append(b)

    def SetBeamWidth(self, width):
        for b in self.beam:
            b.Width(width)

mb = LaserRoomBeams()

#F.U. SYNDICATE: Controls the moving blades, changed by wesp
class BladeMover:
    def bladeInit(self):
        self.track = []
        self.numTracks = 3
        self.baseOn = [0, 0, 0]
        self.bladesStarted =  0
        self.bladeStates = [1,1,1]

        self.FindTracks()

    # populate the track array
    def FindTracks(self):
        self.track = []

        for i in range(self.numTracks):
            t = Find("base_%i" % (i+1))
            self.track.append(t)

    # start moving the blade bases
    def StartBlades(self):
        print "blades started"
        if self.bladesStarted == 0:
            for i in range( len(self.track) ):
                self.track[i].Open()
                self.baseOn[i] = 1

            self.bladesStarted = 1

    # switch direction once the base has reached the end
    def ToggleMove(self, i):
        if i > self.numTracks:
            return
        elif (self.bladeStates[i] == 0):
            return
        elif self.baseOn[i] == 1:
            self.track[i].ToggleMovement()
            self.baseOn[i] = 0
        else:
            self.track[i].ToggleMovement()
            self.baseOn[i] = 1

    # disable blades after power has been pulled
    def Disable(self, i):
        if(i > self.numTracks):
            return
        else:
            self.bladeStates[i] = 0

bm = BladeMover()

#F.U. SYNDICATE: Begin Barabus' haxxor fest, changed by wesp
def barabusHaxxor():
    haxxor = Find("barabus_hack_1")
    if (G.Barabus_Hack == 1 and G.Barrabus_Exit != 1):
        print "barabus needs to hack"
        haxxor.BeginSequence()

#F.U. SYNDICATE: Sset "Invitation" state to 2
def surviveTest():
    __main__.FindPlayer().SetQuest("Mandarin", 2)

#F.U. SYNDICATE: Set "Invitation" state to 3, changed by wesp
def killedMandarin():
    if __main__.FindPlayer().GetQuestState("Mandarin") < 3:
        __main__.FindPlayer().SetQuest("Mandarin", 3)

#F.U. SYNDICATE: Set "Barabus" state to 2
def barabusQuestUpdate():
    __main__.FindPlayer().SetQuest("Barabus", 2)

#F.U. SYNDICATE: Play correct float for Mandarin, changed by wesp
def UVFloat():
    world = Find("world")
    world.SetSafeArea(0)
    Mandarin = Find("Mandarin")
    if(__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
        if(__main__.FindPlayer().IsMale()):
            Mandarin.PlayDialogFile("Character/dlg/Chinatown/mandarin/line181_col_e.mp3")
        else:
            Mandarin.PlayDialogFile("Character/dlg/Chinatown/mandarin/line181_col_f.mp3")
    else:
        if(__main__.FindPlayer().IsMale()):
            Mandarin.PlayDialogFile("Character/dlg/Chinatown/mandarin/line171_col_e.mp3")
        else:
            Mandarin.PlayDialogFile("Character/dlg/Chinatown/mandarin/line171_col_f.mp3")

def MandarinFloat(x):
    Mandarin = Find("Mandarin")
    Mandarin.PlayDialogFile("Character/dlg/Chinatown/mandarin/line" + x + "_col_e.mp3")

print "levelscript loaded"
