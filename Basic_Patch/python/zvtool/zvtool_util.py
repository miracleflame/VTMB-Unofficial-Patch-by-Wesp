# ZVTOOL
# ===================================================================
# zvtool_util.py
# shared utility functions
# ===================================================================

# standard imports
import __main__
from types import *
from time import strftime
Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

# zvtool imports
import zvtool_file
import zvtool_globals
gz = zvtool_globals
del zvtool_globals

# -------------------------------------------------------------------
# get a BSP dynamic entity property
# "ent" may be an int or a reference to a gz.BspDynEnts record
# -------------------------------------------------------------------
def getBspDynProp(ent, prop):
	if type(ent) == IntType:
		entProps = gz.BspDynEnts[ent][2]
	else:
		entProps = ent[2]
	propString = "\"" + prop + "\" \""
	propStart = entProps.find(propString)
	if propStart == -1:
		return ""
	propStart += len(propString)
	propEnd = entProps.find("\"", propStart)
	return entProps[propStart:propEnd]

# -------------------------------------------------------------------
# set a BSP dynamic entity property
# "ent" may be an int or a reference to a gz.BspDynEnts record
# -------------------------------------------------------------------
def setBspDynProp(ent, prop, val):
	if type(ent) == IntType:
		entProps = gz.BspDynEnts[ent][2]
	else:
		entProps = ent[2]
		ent = ent[3]
	# pre-process value
	if (type(val) == TupleType) or (type(val) == ListType):
		val = str(val[0]) + " " + str(val[1]) + " " + str(val[2])
	else:
		val = str(val)
	# search for property name
	propString = "\"" + prop + "\" \""
	propStart = entProps.find(propString)
	if propStart != -1:
		propStart += len(propString)
		propEnd = entProps.find("\"", propStart)
		gz.BspDynEnts[ent][2] = entProps[:propStart] + val + entProps[propEnd:]

# -------------------------------------------------------------------
# set a BSP dynamic entity change time comment
# "ent" may be an int or a reference to a gz.BspDynEnts record
# -------------------------------------------------------------------
def setBspDynChangeComment(ent):
	if type(ent) == IntType:
		entProps = gz.BspDynEnts[ent][2]
	else:
		entProps = ent[2]
		ent = ent[3]
	cPrefix = "// Changed on "
	cFullComment = cPrefix + strftime("%d %b %Y %H:%M") + "\n"
	# search for previous comment
	propStart = entProps.find(cPrefix)
	if propStart != -1:
		propEnd = entProps.find("\n", propStart) + 1
	else:
		# insert new comment before first attribute definition
		propStart = entProps.find("\n\"") + 1
		propEnd = propStart
	entProps = entProps[:propStart] + cFullComment + entProps[propEnd:]
	gz.BspDynEnts[ent][2] = entProps

# -------------------------------------------------------------------
# check if map has changed lately, and act accordingly
# -------------------------------------------------------------------
def checkMapChanged():
	if gz.MapName != getMapName():
		initMapChanged()
		return
	if gz.Grabbed != []:
		# check for valid grabee
		try:
			ent = gz.Grabbed[0]
			temp = ent.GetName()
		except:
			initMapChanged()
			return
	if gz.BspDynEnts != []:
		# check for valid entity references
		maxScan = 25
		valid = 0
		for entRec in gz.BspDynEnts:
			ent = entRec[0]
			if ent == 0:
				continue
			entCent = ent.GetCenter()
			if type(entCent) == NoneType:
				pass
			elif entCent == (0, 0, 0):
				pass
			else:
				valid += 1
			maxScan -= 1
			if maxScan == 0:
				break
		if valid == 0:
			initMapChanged()

# -------------------------------------------------------------------
# reinitialize global data structures for new map
# -------------------------------------------------------------------
def initMapChanged():
	# reinitialize globals
	gz.MapName = getMapName()
	gz.Grabbed[:] = []
	gz.EntList[:] = []
	gz.BspDynEnts[:] = []
	gz.Markers.clear()
	gz.PlayerTransformed = 0
	gz.ZnintLastWarned = 0
	gz.SavedModel = ""
	# scan map
	zvtool_file.matchDynEnts()
	print "MAP INITIALIZED"

# -------------------------------------------------------------------
# return current map name
# accepts optional alternate file extension to return
# -------------------------------------------------------------------
def getMapName(*args):
	map = FindClass("worldspawn")[0]
	m = map.GetModelName()
	mapname = m[m.index("/")+1:m.index(".bsp")]
	if len(args) == 1:
		ext = args[0]
		if ext != "":
			mapname += "." + ext
	else:
		mapname += ".bsp"
	return mapname

# -------------------------------------------------------------------
# return the distance squared between two 3D points
# -------------------------------------------------------------------
def distanceSquared(p1, p2):
    xDistance = (p1[0] - p2[0]) * (p1[0] - p2[0])
    yDistance = (p1[1] - p2[1]) * (p1[1] - p2[1])
    zDistance = (p1[2] - p2[2]) * (p1[2] - p2[2])
    return (xDistance + yDistance + zDistance)

# -------------------------------------------------------------------
# determine line terminator
# -------------------------------------------------------------------
def determineTerminator(txt):
	lf = chr(10)
	cr = chr(13)
	if txt.find(cr + lf) > -1: return cr + lf
	if txt.find(lf) > -1: return lf
	if txt.find(cr) > -1: return cr
	return ""

# -------------------------------------------------------------------
# convert float to rounded string
# -------------------------------------------------------------------
def strH(n):
	return str(round(n, 3))

# -------------------------------------------------------------------
# convert BSP origin/angles to numeric tuple
# -------------------------------------------------------------------
def toTuple(s):
	# check if property is numeric triplet
	if s.count(" ") == 2:
		nums = s.split(" ")
		try:
			for n in nums:
				float(n)
		except:
			isNumeric = 0
		else:
			isNumeric = 1
		if isNumeric:
			# convert to tuple
			# WARNING! This will introduce minor precision errors
			bspTuple = (float(nums[0]), float(nums[1]), float(nums[2]))
	else:
		bspTuple = (0, 0, 0)
	return bspTuple

# -------------------------------------------------------------------
# display all zvtool commands
# -------------------------------------------------------------------
class zhelpClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		print "ZVTOOL HELP"
		print "znear - List entities near player; zn for short"
		print "zlist - Repeat last znear() list; zl for short"
		print "zgrab() - Grab entity by znear number, or targetname; zg() for short"
		print "zhere/zthere - Center grabee on player, and vice-versa"
		print "zbe - Become/Unbecome grabee"
		print "zorg(x, y, z), zx(n), zy(n), zz(n) - Set X/Y/Z origin"
		print "zix(n), ziy(n), ziz(n) - Increment X/Y/Z origin"
		print "zang(p, w, r), zp(n), zw(n), zr(n) - Set Pitch/yaW/Roll angle"
		print "zip(n), ziw(n), zir(n) - Increment Pitch/yaW/Roll angle"
		print "zhide, zunhide - Hide/Unhide grabee"
		print "zmark, zunmark - Mark/Unmark grabee"
		print "zinfo - Grabee info; zi for short"
		print "zpos - Player position & angle"
		print "zammo/zbuff - Max ammo/Max everything"
		print "zhum(n)/zmas(n) - Set Humanity level/Masquerade violations"
		print "zhate/zlove/zkill - Make all NPCs hate you, love you, and dead, respectively"
		print "ztaxi - Open all taxi destinations"
		print "zsave - Save changes to the current map"
		print "zdumpmap, zupdatemap - Replicates VPKTool map functionality"
		print "zdumpg - Dump G to text file",
# instantiate class
zhelp = zhelpClass()
