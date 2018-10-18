# ZVTOOL
# ===================================================================
# zvtool_grabee.py
# grabee manipulation functions
# ===================================================================

# standard imports
import __main__
from types import *
Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

# zvtool imports
from zvtool_util import *
import zvtool_globals
gz = zvtool_globals
del zvtool_globals

# ===================================================================
# entity discovery functions
# ===================================================================

# -------------------------------------------------------------------
# calculate and display entities near the player, sorted by distance
# -------------------------------------------------------------------
class znearClass:
	def __repr__(self):
		self()
		return ""
	def __call__(*args):
		checkMapChanged()
		pc = __main__.FindPlayer()
		pcCent = pc.GetOrigin()
		maxItems = 15 # max items to list
		entList = []
		dist = 0
		gz.ZnintLastWarned = 0
		# player passed class override?
		entClassPrefix = ""
		entClassWildcard = 0
		if len(args) == 2:
			entClassPrefix = args[1]
			if entClassPrefix[-1:] == "*":
				entClassWildcard = 1
				entClassPrefix = entClassPrefix[:-1]
		for entRec in gz.BspDynEnts:
			ent = entRec[0]
			if ent == 0:
				continue
			entCent = ent.GetCenter()
			# cull objects that have disappeared since list was generated
			if type(entCent) == NoneType:
				entRec[0] = 0
				entRec[1] = 0
				continue
			# skip objects that don't match class prefix
			if entClassPrefix != "":
				entClass = getBspDynProp(entRec, "classname")
				if entClassWildcard:
					if not entClass.startswith(entClassPrefix):
						continue
				else:
					if not entClass == entClassPrefix:
						continue
			# skip object in player inventory
			dist = distanceSquared(pcCent, entCent)
			if dist == 0:
				continue
			entList.append((ent, dist, entRec[3]))
		# sort by distance from player
		entList.sort(lambda a, b: _znint(a[1] - b[1], a[2], b[2]))
		# generate list
		i = 1
		gz.EntList[:] = [] # clear out previous persistent list
		for entRec in entList:
			ent = entRec[0]
			bspEnt = entRec[2]
			# store entity reference and BSP reference
			gz.EntList.append([ent, bspEnt])
			# max items?
			i = i + 1
			if i > maxItems:
				break
		del entList
		print "ENTITIES NEAR PLAYER"
		if gz.EntList == []:
			print "No entities found."
		else:
			_zlist_util()
# instantiate class
znear = znearClass()
zn = znear

# -------------------------------------------------------------------
# znear integer conversion
# accepts a float and two gz.BspDynEnt record numbers
# -------------------------------------------------------------------
def _znint(f, e1, e2):
	gz.ZnintLastWarned = 0
	try:
		i = int(f)
	except OverflowError:
		# just return some huge value
		i = int(2**30.0)
		# figure out which entity is to blame
		ent1 = gz.BspDynEnts[e1][0]
		ent2 = gz.BspDynEnts[e2][0]
		entc1 = ent1.GetCenter()
		entc2 = ent2.GetCenter()
		entc1 = abs(entc1[0] + entc1[1] + entc1[2])
		entc2 = abs(entc2[0] + entc2[1] + entc2[2])
		if entc1 > entc2:
			e = e1
			ent = ent1
		else:
			e = e2
			ent = ent2
		# already warned about this one?
		if e != gz.ZnintLastWarned:
			gz.ZnintLastWarned = e
			# display a nice warning
			entClass = getBspDynProp(e, "classname")
			entName = ent.GetName()
			entMdl = ent.GetModelName()
			if (entName == ""):
				entName = "[no targetname]"
			if (entMdl == ""):
				entMdl = "[no model]"
			else:
				entMdl = entMdl[entMdl.rfind("/") + 1:]
			print "WARNING: An entity may have fallen out of the level (" + entName + "; " + entClass + "; " + entMdl + ")"
	return i

# -------------------------------------------------------------------
# display currently stored nearby list, if any
# -------------------------------------------------------------------
class zlistClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		checkMapChanged()
		print "CURRENT ZNEAR LIST"
		if gz.EntList == []:
			print "Entity list is empty. Use znear() to populate it.",
		else:
			_zlist_util()
# instantiate class
zlist = zlistClass()
zl = zlist

# -------------------------------------------------------------------
# display currently stored nearby list; used by znear and zlist
# -------------------------------------------------------------------
def _zlist_util():
	i = 1
	first = 1
	for entData in gz.EntList:
		ent = entData[0]
		bspEnt = entData[1]
		entClass = getBspDynProp(bspEnt, "classname")
		entName = ent.GetName()
		entCent = ent.GetCenter()
		entMdl = ent.GetModelName()
		if (entName == ""):
			entName = "[no targetname]"
		if (entMdl == ""):
			entMdl = "[no model]"
		else:
			entMdl = entMdl[entMdl.rfind("/") + 1:]
		if first:
			first = 0
		else:
			print "\n",
		print str(i) + ". " + entClass + ", " + entName + ", " + entMdl + ", \"" + strH(entCent[0]) + " " + strH(entCent[1]) + " " + strH(entCent[2]) + "\"",
		i = i + 1
	return


# ===================================================================
# grabee origin-setting functions
# ===================================================================

# -------------------------------------------------------------------
# center grabee on player
# -------------------------------------------------------------------
class zhereClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		if _noGrabee(): return
		_markGrabeeChanged()
		pc = __main__.FindPlayer()
		x, y, z = pc.GetCenter()
		# prevent being false detected as in player inventory
		z -= 0.001
		ent = gz.Grabbed[0]
		ent.SetOrigin((x, y, z))
		ent.SetAngles(pc.GetAngles())
		print "GRABEE CENTERED ON PLAYER ORIGIN"
		print "You may need to 'noclip' just about now.",
# instantiate class
zhere = zhereClass()

# -------------------------------------------------------------------
# center player on grabee
# -------------------------------------------------------------------
class zthereClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		if _noGrabee(): return
		pc = __main__.FindPlayer()
		ent = gz.Grabbed[0]
		x, y, z = ent.GetCenter()
		# prevent being false detected as in player inventory
		z += 0.001
		pc.SetOrigin((x, y, z))
		print "PLAYER CENTERED ON GRABEE ORIGIN"
		print "You may need to 'noclip' just about now.",
# instantiate class
zthere = zthereClass()

# -------------------------------------------------------------------
# pull grabee toward player
# -------------------------------------------------------------------
class zpullClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		if _noGrabee(): return
		_markGrabeeChanged()
		pc = __main__.FindPlayer()
		ent = gz.Grabbed[0]
		x1, y1, z1 = pc.GetOrigin()
		x2, y2, z2 = ent.GetOrigin()
		if type(x2) == NoneType:
			print "zERR: Cannot move grabee.",
		per = 0.5 # percent of distance to move
		x = x2 - ((x2 - x1) * per)
		y = y2 - ((y2 - y1) * per)
		z = z2 - ((z2 - z1) * per)
		ent.SetOrigin((x, y, z))
		print "GRABEE PULLED TOWARD PLAYER",
# instantiate class
zpull = zpullClass()

# -------------------------------------------------------------------
# set grabee origin
# -------------------------------------------------------------------
def zorg(*args):
	if _argsInvalid(args, 3): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	ent.SetOrigin((args[0], args[1], args[2]))
	print "ORIGIN SET"

# -------------------------------------------------------------------
# set grabee X origin
# -------------------------------------------------------------------
def zx(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	x, y, z = ent.GetOrigin()
	x = args[0]
	ent.SetOrigin((x, y, z))
	print "X ORIGIN SET TO " + str(x)

# -------------------------------------------------------------------
# increment grabee X origin
# -------------------------------------------------------------------
def zix(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	x, y, z = ent.GetOrigin()
	x += args[0]
	ent.SetOrigin((x, y, z))
	print "X ORIGIN INCREMENTED TO " + str(x)

# -------------------------------------------------------------------
# set grabee Y origin
# -------------------------------------------------------------------
def zy(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	x, y, z = ent.GetOrigin()
	y = args[0]
	ent.SetOrigin((x, y, z))
	print "Y ORIGIN SET TO " + str(y)

# -------------------------------------------------------------------
# increment grabee Y origin
# -------------------------------------------------------------------
def ziy(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	x, y, z = ent.GetOrigin()
	y += args[0]
	ent.SetOrigin((x, y, z))
	print "Y ORIGIN INCREMENTED TO " + str(y)

# -------------------------------------------------------------------
# set grabee Z origin
# -------------------------------------------------------------------
def zz(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	x, y, z = ent.GetOrigin()
	z = args[0]
	ent.SetOrigin((x, y, z))
	print "Z ORIGIN SET TO " + str(z)

# -------------------------------------------------------------------
# increment grabee Z origin
# -------------------------------------------------------------------
def ziz(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	x, y, z = ent.GetOrigin()
	z += args[0]
	ent.SetOrigin((x, y, z))
	print "Z ORIGIN INCREMENTED TO " + str(z)


# ===================================================================
# grabee angle-setting functions
# ===================================================================

# -------------------------------------------------------------------
# set grabee angles
# -------------------------------------------------------------------
def zang(*args):
	if _argsInvalid(args, 3): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	ent.SetAngles((args[0], args[1], args[2]))
	print "ANGLES SET"

# -------------------------------------------------------------------
# set grabee roll angle
# -------------------------------------------------------------------
def zr(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	r, w, p = ent.GetAngles()
	r = args[0]
	ent.SetAngles((r, w, p))
	print "ROLL ANGLE SET TO " + str(r)

# -------------------------------------------------------------------
# increment grabee roll angle
# -------------------------------------------------------------------
def zir(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	r, w, p = ent.GetAngles()
	newAng = r + args[0]
	if newAng < 0: newAng += 360
	if newAng > 360: newAng -= 360
	ent.SetAngles((newAng, w, p))
	print "ROLL ANGLE INCREMENTED TO " + str(r)

# -------------------------------------------------------------------
# set grabee yaw angle
# -------------------------------------------------------------------
def zw(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	r, w, p = ent.GetAngles()
	w = args[0]
	ent.SetAngles((r, w, p))
	print "YAW ANGLE SET TO " + str(w)

# -------------------------------------------------------------------
# increment grabee yaw angle
# -------------------------------------------------------------------
def ziw(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	r, w, p = ent.GetAngles()
	newAng = w + args[0]
	if newAng < 0: newAng += 360
	if newAng > 360: newAng -= 360
	ent.SetAngles((r, newAng, p))
	print "YAW ANGLE INCREMENTED TO " + str(w)

# -------------------------------------------------------------------
# set grabee pitch angle
# -------------------------------------------------------------------
def zp(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	r, w, p = ent.GetAngles()
	p = args[0]
	ent.SetAngles((r, w, p))
	print "PITCH ANGLE SET TO " + str(p)

# -------------------------------------------------------------------
# increment grabee pitch angle
# -------------------------------------------------------------------
def zip(*args):
	if _argsInvalid(args, 1): return
	_markGrabeeChanged()
	ent = gz.Grabbed[0]
	r, w, p = ent.GetAngles()
	newAng = p + args[0]
	if newAng < 0: newAng += 360
	if newAng > 360: newAng -= 360
	ent.SetAngles((r, w, newAng))
	print "PITCH ANGLE INCREMENTED TO " + str(p)


# ===================================================================
# become/unbecome functions
# ===================================================================

# -------------------------------------------------------------------
# become current grabee (copy model and coordinates to player)
# -------------------------------------------------------------------
class zbeClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		if _noGrabee(): return
		pc = __main__.FindPlayer()
		ent = gz.Grabbed[0]
		entModel = ent.GetModelName()
		entOrg = ent.GetOrigin()
		entAng = ent.GetAngles()
		# decide what to do
		if entOrg == (0, 0, 0):
			print "zERR: Cannot become this entity.",
		elif entModel == "":
			print "zERR: Grabee has no physical model.",
		elif gz.PlayerTransformed:
			# already transformed, switch back
			zunbe()
		else:
			# transform!
			gz.PlayerTransformed = 1
			gz.OldPlayerModel = pc.GetModelName()
			gz.OldPlayerOrg = pc.GetOrigin()
			gz.OldPlayerAng = pc.GetAngles()
			pc.SetModel(entModel)
			pc.SetOrigin(entOrg)
			pc.SetAngles(entAng)
			ent.ScriptHide()
			_markGrabeeChanged()
			print "TRANSFORMED"
			print "Switch into third-person view if you haven't already done so.",
# instantiate class
zbe = zbeClass()

# -------------------------------------------------------------------
# revert transformation
# -------------------------------------------------------------------
class zunbeClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		# sanity checks
		if _noGrabee(): return
		if gz.PlayerTransformed == 0: return
		# swap everything back
		pc = __main__.FindPlayer()
		ent = gz.Grabbed[0]
		gz.PlayerTransformed = 0
		ent.SetOrigin(pc.GetOrigin())
		ent.SetAngles(pc.GetAngles())
		ent.ScriptUnhide()
		pc.SetModel(gz.OldPlayerModel)
		pc.SetOrigin(gz.OldPlayerOrg)
		pc.SetAngles(gz.OldPlayerAng)
		print "UN-TRANSFORMED",
# instantiate class
zunbe = zunbeClass()


# ===================================================================
# visibility functions
# ===================================================================

# -------------------------------------------------------------------
# hide grabee
# -------------------------------------------------------------------
class zhideClass:
	def __repr__(self):
		self()
		return ""
	def __call__(*args):
		if len(args) == 2:
			checkMapChanged()
			# hide all class members
			entList = FindClass(args[1])
			for ent in entList:
				ent.ScriptHide()
		else:
			# hide grabee
			if _noGrabee(): return
			gz.Grabbed[0].ScriptHide()
		print "ENTITY HIDDEN",
# instantiate class
zhide = zhideClass()

# -------------------------------------------------------------------
# unhide grabee
# -------------------------------------------------------------------
class zunhideClass:
	def __repr__(self):
		self()
		return ""
	def __call__(*args):
		if len(args) == 2:
			checkMapChanged()
			# hide all class members
			entList = FindClass(args[1])
			for ent in entList:
				ent.ScriptUnhide()
		else:
			# hide grabee
			if _noGrabee(): return
			gz.Grabbed[0].ScriptUnhide()
		print "ENTITY UNHIDDEN",
# instantiate class
zunhide = zunhideClass()

# -------------------------------------------------------------------
# mark things with inspection nodes
# -------------------------------------------------------------------
class zmarkClass:
	def __repr__(self):
		self()
		return ""
	def __call__(*args):
		if len(args) == 2:
			checkMapChanged()
			c = 0
			# mark all class members
			entList = FindClass(args[1])
			for ent in entList:
				if _zmark_util(ent):
					c += 1
			print str(c) + " ENTITIES OF CLASS \"" + args[1] + "\" MARKED",
		else:
			# mark grabee
			if _noGrabee(): return
			ent = gz.Grabbed[0]
			if _zmark_util(ent):
				print "ENTITY MARKED",
			else:
				print "ENTITY ALREADY MARKED",
# instantiate class
zmark = zmarkClass()
	
# -------------------------------------------------------------------
# utility function for zmark
# -------------------------------------------------------------------
def _zmark_util(ent):
	pc = __main__.FindPlayer()
	if pc.GetOrigin() == ent.GetOrigin():
		# inventory entity
		return 0
	if not gz.Markers.has_key(ent):
		entName = ent.GetName()
		tmpName = "_zvtool_tempname"
		# must assign temporary unique targetname in case of entities with no name,
		# or multiple entities with same name
		ent.SetName(tmpName)
		marker = __main__.CreateEntityNoSpawn("inspection_node", ent.GetCenter(), (0, 0, 0))
		marker.SetParent(tmpName)
		__main__.CallEntitySpawn(marker)
		# restore original name
		ent.SetName(entName)
		# add inspection entity pointer to persistent list, so we don't have to
		# screw around with temporary targetnames when removing them
		gz.Markers[ent] = marker
		return 1
	else:
		return 0

# -------------------------------------------------------------------
# remove inspection nodes used to mark things
# -------------------------------------------------------------------
class zunmarkClass:
	def __repr__(self):
		self()
		return ""
	def __call__(*args):
		if len(args) == 2:
			checkMapChanged()
			c = 0
			# unmark all class members
			entList = FindClass(args[1])
			for ent in entList:
				if _zunmark_util(ent):
					c += 1
			print str(c) + " ENTITIES OF CLASS \"" + args[1] + "\" UNMARKED",
		else:		
			# unmark grabee
			if _noGrabee(): return
			ent = gz.Grabbed[0]
			if _zunmark_util(ent):
				print "ENTITY UNMARKED",
			else:
				print "ENTITY NOT MARKED",
# instantiate class
zunmark = zunmarkClass()

# -------------------------------------------------------------------
# utility function for zunmark
# -------------------------------------------------------------------
def _zunmark_util(ent):
	if not gz.Markers.has_key(ent):
		return 0
	else:
		marker = gz.Markers[ent]
		marker.Kill()
		del gz.Markers[ent]
		return 1

# ===================================================================
# other grabee functions
# ===================================================================

# -------------------------------------------------------------------
# let user flag grabee as changed
# -------------------------------------------------------------------
class zchaClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		if _noGrabee(): return
		_markGrabeeChanged()
		print "ENTITY FLAGGED AS CHANGED",
# instantiate class
zcha = zchaClass()

# -------------------------------------------------------------------
# revert all changes
# -------------------------------------------------------------------
class zundoClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		if _noGrabee(): return
		_markGrabeeNotChanged()
		ent = gz.Grabbed[0]
		bspEnt = gz.Grabbed[1]
		bspOrigin = toTuple(getBspDynProp(bspEnt, "origin"))
		bspAngles = toTuple(getBspDynProp(bspEnt, "angles"))
		bspModel = getBspDynProp(bspEnt, "model")
		bspName = getBspDynProp(bspEnt, "targetname")
		if bspOrigin != (0, 0, 0):
			ent.SetOrigin(bspOrigin)
		if bspAngles != (0, 0, 0):
			ent.SetAngles(bspAngles)
		if bspModel != "":
			ent.SetModel(bspModel)
		if bspName != "":
			ent.SetName(bspName)
		print "ENTITY STATE RESTORED FROM BSP",
# instantiate class
zundo = zundoClass()

# -------------------------------------------------------------------
# grab entity
# -------------------------------------------------------------------
class zgrabClass:
	def __repr__(self):
		self()
		return ""
	def __call__(*args):
		checkMapChanged()
		if len(args) == 1:
			if gz.Grabbed == []:
				print "zERR: No entity currently grabbed. zgrab() usage is:"
				print "   zgrab - Display currently grabbed entity."
				print "   zgrab(#) - Grab entity by number from znear list."
				print "   zgrab(\"targetname\") - Grab entity by map targetname.",
			else:
				print "Currently grabbed entity is:"
				_entDump(gz.Grabbed[0], gz.Grabbed[1])
		elif type(args[1]) == StringType:
			# grab by targetname
			if gz.Grabbed != [] and gz.PlayerTransformed:
				zunbe()
			entList = FindList(args[1])
			if len(entList) == 0:
				print "zERR: Could not find an entity with that targetname.",
			elif len(entList) > 1:
				print "zERR: Multiple entities with that targetname.",
			else:
				# find entity record in global list
				ent = entList[0]
				recno = -1
				for bspRec in gz.BspDynEnts:
					if bspRec[0] == ent:
						recno = bspRec[3]
						break
				if recno > -1:
					gz.Grabbed = [ent, recno]
					print "ENTITY GRABBED:"
					_entDump(gz.Grabbed[0], gz.Grabbed[1])
				else:
					print "zERR: Could not find this entity in BSP dynamic entity lump.",
		elif type(args[1]) == IntType:
			# grab by entity list index
			if gz.Grabbed != [] and gz.PlayerTransformed:
				zunbe()
			i = args[1] - 1
			if (i < 0) or (i > len(gz.EntList)):
				print "zERR: Not that many entities in znear() list.",
			else:
				gz.Grabbed = [gz.EntList[i][0], gz.EntList[i][1]]
				print "ENTITY GRABBED:"
				_entDump(gz.Grabbed[0], gz.Grabbed[1])
		else:
			# wrong data type passed
			print "zERR: Invalid data type. This function accepts entity list numbers or targetnames (in quotes!) only.",
# instantiate class
zgrab = zgrabClass()
zg = zgrab

# -------------------------------------------------------------------
# display info on currently grabbed entity
# -------------------------------------------------------------------
class zinfoClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		if _noGrabee(): return
		print "GRABBED ENTITY:"
		_entDump(gz.Grabbed[0], gz.Grabbed[1])
# instantiate class
zinfo = zinfoClass()
zinf = zinfo
zi = zinfo

# ===================================================================
# local utility functions
# ===================================================================

# -------------------------------------------------------------------
# display detailed information about entity
# -------------------------------------------------------------------
def _entDump(ent, bspEntRecNum):
	entName = ent.GetName()
	entCent = ent.GetCenter()
	entOrig = ent.GetOrigin()
	entAng = ent.GetAngles()
	entMdl = ent.GetModelName()
	entClass = getBspDynProp(bspEntRecNum, "classname")
	entChanged = gz.BspDynEnts[bspEntRecNum][1]
	if entName == "":
		entName = "[no targetname]"
	if entMdl == "":
		entMdl = "[no model]"
	if entChanged == 0:
		entChanged = "has not"
	else:
		entChanged= "HAS"
	print "   \"classname\" \"" + entClass + "\""
	print "   \"targetname\" \"" + entName + "\""
	print "   \"model\" \"" + entMdl + "\""
	print "   \"origin\" \"" + str(entOrig[0]) + " " + str(entOrig[1]) + " " + str(entOrig[2]) + "\""
	print "   \"angles\" \"" + str(entAng[0]) + " " + str(entAng[1]) + " " + str(entAng[2]) + "\""
	print "   .GetCenter() = (" + str(entCent[0]) + ", " + str(entCent[1]) + ", " + str(entCent[2]) + ")"
	print "   This entity " + str(entChanged) + " been changed.",

# -------------------------------------------------------------------
# checks if passed argument list is invalid for entity
# also checks if anything has been grabbed
# this should only be used by functions that operate on grabbed entities
# -------------------------------------------------------------------
def _argsInvalid(args, n):
	if _noGrabee(): return 1
	if len(args) != n:
		if n == 0:
			print "zERR: This function does not take any arguments.",
		elif n == 1:
			print "zERR: This function takes exactly 1 numeric argument.",
		else:
			print "zERR: This function expects exactly " + str(n) + " numeric arguments, separated by commas.",
		return 1
	else:
		return 0

# -------------------------------------------------------------------
# check if there's a current grabbed entity
# used by entity manipulation functions to immediately exit if nothing grabbed
# -------------------------------------------------------------------
def _noGrabee():
	checkMapChanged()
	if gz.Grabbed == []:
		print "zERR: No entity grabbed. Use zgrab() to grab one.",
		return 1
	else:
		return 0

# -------------------------------------------------------------------
# mark entity as changed
# -------------------------------------------------------------------
def _markGrabeeChanged():
	if gz.Grabbed == []: return
	gz.BspDynEnts[gz.Grabbed[1]][1] = 1

# -------------------------------------------------------------------
# mark entity as NOT changed
# -------------------------------------------------------------------
def _markGrabeeNotChanged():
	if gz.Grabbed == []: return
	gz.BspDynEnts[gz.Grabbed[1]][1] = 0
