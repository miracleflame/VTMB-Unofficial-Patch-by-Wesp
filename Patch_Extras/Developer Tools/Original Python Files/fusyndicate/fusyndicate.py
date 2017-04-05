print "loading chinatown level script"
#function's comments indicate what map they are called on
import __main__

from __main__ import G 

__main__.Level = __name__

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

RandomLine = __main__.RandomLine

#F.U. SYNDICATE: check gamestate and open doors accordingly
def startTest():
    confDoor1 = Find("lobbydoor1")
    confDoor2 = Find("lobbydoor2")    
    world = Find("world")
    if (G.Mandarin_Fu > 0):
        world.SetSafeArea(0)
        confDoor1.Unlock()
        confDoor2.Unlock() 
        confDoor1.Open()
        confDoor2.Open()

#F.U. SYNDICATE:  spawns bertram's key after mandarin dies.
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
    

#F.U. SYNDICATE:  spawns office key from guard.
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
    
#F.U. SYNDICATE:  starts and restarts the lasers (thanks to stealing Jocelyn code and modifying
#                 it).    
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

    ## get beams started
    def StartBeams(self):
        print "beams started"
        if self.beamsStarted == 0:
            for i in range( len(self.track) ):
                self.track[i].Open()
                self.beamOn[i] = 1

            self.beamsStarted = 1


    ## make beam[i] go other direction when it hits the end of its track
    ## toggle beam[i] on/off when open/close if power shot out
    def ToggleBeam(self, i):
        if i > self.numBeams:
            return
        elif self.beamOn[i] == 1:
            self.track[i].Close()
            self.beamOn[i] = 0
        else:
            self.track[i].Open()
            self.beamOn[i] = 1

        if self.beamsFlicker == 1 and self.beamsEnabled == 1:
##            self.beam[i].Toggle()
##            uncommenting following lines will cause game to crash after a minute or so.
            __main__.ScheduleTask(0.10, "__main__.FindEntityByName(\"beam_%d\").Toggle()" %(i+1))
##            __main__.ScheduleTask(0.20, "__main__.FindEntityByName(\"beam_%d\").Toggle()" %(i+1))
##            __main__.ScheduleTask(0.20, "__main__.FindEntityByName(\"beam_trig_%d\").Toggle()" %(i+1))


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

#F.U. SYNDICATE:  controls the moving blades
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
            self.track[i].Close()
            self.baseOn[i] = 0
        else:
            self.track[i].Open()
            self.baseOn[i] = 1

    # disable blades after power has been pulled
    def Disable(self, i):
        if(i > self.numTracks):
            return
        else:
            self.bladeStates[i] = 0
    

bm = BladeMover()

#F.U. SYNDICATE:  begin Barabus' haxxor fest
def barabusHaxxor():
    haxxor = Find("barabus_hack_1")
    if (G.Barabus_Hack == 1 and G.Barabus_Exit != 1):
        print "barabus needs to hack"
        haxxor.BeginSequence()

#F.U. SYNDICATE:  set "Invitation" state to 2
def surviveTest():
    __main__.FindPlayer().SetQuest("Mandarin", 2)

#F.U. SYNDICATE:  set "Invitation" state to 3
def killedMandarin():
    __main__.FindPlayer().SetQuest("Mandarin", 3)

#F.U. SYNDICATE:  set "Barabus" state to 2
def barabusQuestUpdate():
    __main__.FindPlayer().SetQuest("Barabus", 2)

#F.U. SYNDICATE: play correct float for Mandarin
def UVFloat():
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
