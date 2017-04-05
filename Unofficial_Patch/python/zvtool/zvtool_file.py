# ZVTOOL
# ===================================================================
# zvtool_file.py
# map and general file reading/writing/processing functions
# ===================================================================

# standard imports
import __main__
from struct import *
from types import *
Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

# zvtool imports
from zvtool_util import *
import zvtool_globals
gz = zvtool_globals
del zvtool_globals

# mods support imports
import sys
try: sys.moddir
except AttributeError:
	 sys.moddir = "vampire"
from sys import moddir

# -------------------------------------------------------------------
# manually reinitialize global data structures for current map
# -------------------------------------------------------------------
class zinitmapClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		# TODO: add marker removal
		initMapChanged()
# instantiate class
zinitmap = zinitmapClass()

# -------------------------------------------------------------------
# save changes
# -------------------------------------------------------------------
class zsaveClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		zdumpchanges()
		print ""
		zupdatemap()
# instantiate class
zsave = zsaveClass()

# -------------------------------------------------------------------
# dump contents of G
# -------------------------------------------------------------------
class zdumpgClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		G = __main__.G
		dumpfile = "zvtool_g_dump.txt"
		f = open(dumpfile, "w")
		f.write("Dump of __main__.G global persistent database.\n")
		f.write("Generated from within map \"" + getMapName() + "\", at Story State " + str(G.Story_State) +".\n\n")
		keyList = G.keys()
		keyList.sort()
		for k in keyList:
			f.write(k + " = " + str(G[k]) + "\n")
		# prettyprint morgue dictionary
		f.write("\nG.morgue:\n")
		f.write("========================================\n")
		morgueKeys = G.morgue.keys()
		morgueKeys.sort()
		for k in morgueKeys:
			f.write("   " + k + "\n")
		f.write("\nDUMP COMPLETE\n")
		f.close()
		print "DUMP COMPLETE"
		print "Written to \"" + dumpfile + "\"",
# instantiate class
zdumpg = zdumpgClass()

# -------------------------------------------------------------------
# dump entity data from BSP file for current map
# -------------------------------------------------------------------
class zdumpmapClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		lump_raw = getDynEntLump(getMapName())
		if lump_raw == -1: return
		dumpname = moddir + "/maps/" + getMapName("txt")
		dump = open(dumpname, "w")
		dump.write(lump_raw)
		dump.close()
		print "MAP DUMP COMPLETE"
		print "Written to \"" + dumpname + "\"",
# instantiate class
zdumpmap = zdumpmapClass()

# -------------------------------------------------------------------
# dump changed entity data from BSP file for current map
# -------------------------------------------------------------------
class zdumpchangesClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		checkMapChanged()
		dumpname = moddir + "/maps/" + getMapName("txt")
		dump = open(dumpname, "w")
		c = 0
		for bspEnt in gz.BspDynEnts:
			if bspEnt[1] == 1:
				c += 1
				ent = bspEnt[0]
				# TODO: add support for deleting entities
				#setBspDynProp(bspEnt, "name", ent.GetName())
				setBspDynProp(bspEnt, "angles", ent.GetAngles())
				setBspDynProp(bspEnt, "origin", ent.GetOrigin())
				setBspDynProp(bspEnt, "model", ent.GetModelName())
				setBspDynChangeComment(bspEnt)
			dump.write(bspEnt[2])
		dump.close()
		print "MAP DUMP COMPLETE"
		print "Written to \"" + dumpname + "\""
		print str(c) + " entities changed.",
# instantiate class
zdumpchanges = zdumpchangesClass()

# -------------------------------------------------------------------
#  dump a readable list of the current dynamic entities
# -------------------------------------------------------------------
class zdumpentsClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		entList = FindClass("*")
		dumpname = moddir + "/maps/entity_dump_" + getMapName("txt")
		dump = open(dumpname, "w")
		dump.write("Name, ModelName, Origin\n")
		for ent in entList:
			entName = ent.GetName()
			entMdl = ent.GetModelName()
			entOrig = ent.GetOrigin()
			if (entName == ""): entName = "[no targetname]"
			if (entMdl == ""): entMdl = "[no model]"
			dump.write(entName + ", " + entMdl + ", " + str(entOrig) + "\n")
		dump.close()
		print "ENTITY DUMP COMPLETE"
		print "Written to \"" + dumpname + "\"",
# instantiate class
zdumpents = zdumpentsClass()

# -------------------------------------------------------------------
# update entity data for current map
# -------------------------------------------------------------------
class zupdatemapClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		# constants
		magic_word = "QnDbTm"
		linefeed = chr(10)
		null_terminator = chr(0)
	
		# structs
		header_struct = "4sl"
		lump_struct = "ll"
		mod_offset_struct = "l"
	
		# open input file
		mapname = moddir + "/maps/" + getMapName()
		dumpname = moddir + "/maps/" + getMapName("txt")
		try:
			dump = open(dumpname, "rb")
		except:
			print "zERR: Could not open input file \"" + dumpname + "\".",
			return
	
		# grab input data
		dump_raw = dump.read()
		dump.close()
		line_end = determineTerminator(dump_raw)
		if line_end == "":
			print "zERR: No valid data found in input file.",
			return
		dump_lines = dump_raw.split(line_end)
		# clean up trailing newline
		if dump_lines[-1] == "":
			dump_lines.pop()
	
		# open BSP file
		bsp = open(mapname, "rb+")
	
		# grab header
		bsp_data = bsp.read(calcsize(header_struct))
		bsp_ident, bsp_ver = unpack(header_struct, bsp_data)
		if (bsp_ident != "VBSP"):
			print "zERR: Not a Source engine BSP file."
		else:
			# check if map previously modified
			bsp.seek(-len(magic_word), 2)
			bsp_data = bsp.read(len(magic_word))
			if bsp_data == magic_word:
				print "Found previous modding information. Replacing."
				# grab previous offset
				bsp.seek(-10, 2)
				bsp_data = bsp.read(calcsize(mod_offset_struct))
				mod_offset = unpack(mod_offset_struct, bsp_data)[0]
				# remove old mod info
				bsp.seek(mod_offset)
				bsp.truncate()
			# write new mod info
			brace_depth = 0
			line_num = 0
			bsp.seek(0, 2)
			mod_offset = bsp.tell()
			for line in dump_lines:
				line_num += 1
				bsp.write(line.rstrip() + linefeed)
				# sanity check braces
				if line[0:1] == "{":
					brace_depth += 1
				elif line[-1:1] == "}":
					brace_depth -= 1
				if brace_depth < 0:
					print "zERR: Unexpected closing brace at line #" + str(line_num) + "."
					brace_depth = 0
				elif brace_depth > 1:
					print "zERR: Unexpected opening brace at line #" + str(line_num) + "."
					brace_depth = 1
			# cap off mod info
			bsp.write(null_terminator + pack(mod_offset_struct, mod_offset) + magic_word)
			# write new lump header
			mod_size = bsp.tell() - mod_offset
			bsp.seek(8)
			bsp_data = pack(lump_struct, mod_offset, mod_size)
			bsp.write(bsp_data)		
		bsp.close()
		print "MAP UPDATE COMPLETE"
		print "Updated \"" + mapname + "\"",
# instantiate class
zupdatemap = zupdatemapClass()

# -------------------------------------------------------------------
# correlate BSP dynamic entities with live dynamic entities
# -------------------------------------------------------------------
def matchDynEnts():
	G = __main__.G
	parseDynEntLump()
	# these classes are not enumerated by FindClass()
	nonEnumList = [
		"ai_script_conditions",
		"events_player",
		"events_world",
		"info_hint",
		"info_node",
		"info_node_air",
		"info_node_air_hint",
		"info_node_bach_run_1",
		"info_node_bach_run_2",
		"info_node_bach_teleport_1",
		"info_node_bach_teleport_2",
		"info_node_bach_teleport_3",
		"info_node_bach_teleport_4",
		"info_node_chang_column",
		"info_node_chang_jumpbase",
		"info_node_chang_ledge",
		"info_node_chang_teleport",
		"info_node_climb",
		"info_node_cover_corner",
		"info_node_cover_low",
		"info_node_cover_med",
		"info_node_crosswalk",
		"info_node_hint",
		"info_node_kick_at",
		"info_node_kick_over",
		"info_node_link",
		"info_node_manbat_fly_to_point",
		"info_node_patrol_point",
		"info_node_sabbat_arch",
		"info_node_sabbat_bottom",
		"info_node_sabbat_dive",
		"info_node_sabbat_hide",
		"info_node_sabbat_nojump",
		"info_node_sabbat_top",
		"info_node_shoot_at",
		"info_node_tzimisce",
		"info_node_tzimisce_claw_left",
		"info_node_tzimisce_claw_right",
		"info_node_werewolf",
		"info_node_werewolf_hint",
		"light_environment",
		"trigger_autosave"
	]
	# these classes are blacklisted (intangible or not to be messed with)
	blacklistList = [
		"logic_auto",
		"light",
		"light_spot",
		"light_dynamic",
		"worldspawn",
		"z"
	]
	# skip these classes if unnamed; they're either invisible to FindClass() if no
	# targetname assigned or prone to disappearing
	mustBeNamedList = [
		"ambient_location",
		"ambient_soundscheme",
		"ent_angl",
		"info_player_start",
		"infodecal",
		"inspection_node",
		"trigger_once"
	]
	# classes with model in items directory
	itemClassList = ["item_g", "item_k", "item_m", "item_p"]

	# FIRST PASS
	# iterate through entity list, matching each uniquely-named live entity
	# with its corresponding BSP entity; this guarantees that unique named
	# entities will always be matched

	# build temporary list of map entity indexes for faster lookup
	n = -1
	entListIndexCache = {}
	entList = FindClass("*")
	for e in entList:
		n += 1
		entListIndexCache[e] = n

	# build temporary list of BSP dynamic entity names for faster lookup
	bspNameCache = []
	for d in gz.BspDynEnts:
		bspNameCache.append(getBspDynProp(d, "targetname"))

	# iterate in-game entity list
	for ent in entList:
		entName = ent.GetName()
		# targetname must exist and be unique
		if (entName == "") or (entName == "BigNet") or (len(FindList(entName)) != 1):
			continue
		elif bspNameCache.count(entName) == 1:
			gz.BspDynEnts[bspNameCache.index(entName)][0] = ent
	del bspNameCache

	# SECOND PASS
	# iterate through raw BSP data, attempting to match each dynamic entity
	# with its corresponding live in-game entity; this is, sadly, way more
	# complicated than it should be
	e = -1 # entity block index
	for d in gz.BspDynEnts:
		# fetch BSP entity data
		dEntName = getBspDynProp(d, "targetname")
		dEntMdl = getBspDynProp(d, "model")
		dEntClass = getBspDynProp(d, "classname")
		# skip already-matched entities
		if d[0] != 0:
			e =  entListIndexCache[d[0]] # skip e ahead to known good index
			continue
		# skip enumerable but blacklisted classes
		if dEntClass in blacklistList:
			continue
		# skip non-enumerable classes
		if dEntClass in nonEnumList:
			continue
		# skip classes that get filtered from the in-game entity list (unless given a targetname)
		if (dEntName == "") and (dEntClass in mustBeNamedList):
			continue
		# this class doesn't ennumerate in-game without a "message" property
		if (dEntClass == "ambient_generic") and (getBspDynProp(d, "message") == ""):
			continue
		# skip named entities that no longer exist
		if (dEntName != "") and (len(FindList(dEntName)) == 0):
			continue
		# this class reports its model as null if not specified
		if (dEntClass.startswith("npc_V")) and (dEntMdl == ""):
			dEntMdl = "models/null.mdl"
		# this class reports its "shootmodel" property as its model name
		if dEntClass == "env_shooter":
			dEntMdl = getBspDynProp(d, "shootmodel")
		# find matching game entity
		found = 0
		strikes = 0
		eResume = e
		eMax = len(entList) - 1
		entName = ""
		entMdl = ""
		while (e < eMax) and (found == 0):
			e += 1
			ent = entList[e]
			lastEntName = entName
			lastEntMdl = entMdl
			entName = ent.GetName()
			entMdl = ent.GetModelName()
			# general case allowing for blank names or models
			if (dEntName == entName) and (dEntMdl == entMdl):
				found = 1
			# allow matching just targetname if non-blank
			elif (dEntName == entName) and (dEntName != ""):
				found = 1
			# allow matching items (model name not supplied in BSP)
			elif (dEntClass[:6] in itemClassList) and (entMdl.startswith("models/items/")):
				found = 1
			# allow matching weapon items
			elif (dEntClass.startswith("item_w")) and (entMdl.startswith("models/weapons/")):
				found = 1
			# this particular class reports the model of its "target" entity as its model,
			# which isn't always unique, but is always a func_brush
			elif (dEntClass == "func_areaportalwindow") and (entMdl.startswith("*")):
				found = 1
			# only allow skipping so many valid and non-identical entities before bailing
			elif ((entName != "") or (entMdl != "")) and ((entName != lastEntName) or (entMdl != lastEntMdl)):
				strikes += 1
				if strikes == 10:
					break
		if found:
			d[0] = ent # stash entity in master list
		else:
			e = eResume # failed to find entity; reset to where we started

# -------------------------------------------------------------------
# populate gz.BspDynEnts from current map's BSP
# -------------------------------------------------------------------
def parseDynEntLump():
	lump_raw = getDynEntLump(getMapName())
	if lump_raw == -1: return
	# build entity list
	lump_raw = lump_raw.split("}")
	lump_raw.pop() # last item just a linefeed
	gz.BspDynEnts[:] = []
	i = -1
	for ent in lump_raw:
		i += 1
		gz.BspDynEnts.append([0, 0, ent.strip() + "\n}\n", i])
	#print str(i) + " dynamic entities loaded from " + getMapName()

# -------------------------------------------------------------------
# retrieve dynamic entity lump from the requested BSP file
# -------------------------------------------------------------------
def getDynEntLump(mapname):
	# structs
	header_struct = "4sl"
	lump_struct = "ll"
	# filename stuff
	mapname = moddir + "/maps/" + mapname
	bsp = open(mapname, "rb")
	# grab header
	bsp_data = bsp.read(calcsize(header_struct))
	bsp_ident, bsp_ver = unpack(header_struct, bsp_data)
	if (bsp_ident != "VBSP"):
		print "zERR: Not a Source engine BSP file."
		bsp.close()
		return -1
	# grab Dynamic Entities lump (lump zero)
	bsp_data = bsp.read(calcsize(lump_struct))
	lump_offset, lump_len = unpack(lump_struct, bsp_data)
	bsp.seek(lump_offset)
	lump_data = bsp.read(lump_len - 1)
	bsp.close()
	return lump_data

# -------------------------------------------------------------------
# retrieve static entity lump from the requested BSP file
# -------------------------------------------------------------------
def getStatEntLump(mapname):
	# filename stuff
	mapname = moddir + "/maps/" + mapname
	bsp = open(mapname, "rb")
	# grab header
	bsp_data = bsp.read(calcsize(header_struct))
	bsp_ident, bsp_ver = unpack(header_struct, bsp_data)
	if (bsp_ident != "VBSP"):
		print "zERR: Not a Source engine BSP file."
		bsp.close()
		return -1
	# TODO: actual functionality
	return
