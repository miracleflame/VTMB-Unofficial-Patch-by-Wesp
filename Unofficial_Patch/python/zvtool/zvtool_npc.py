# ZVTOOL
# ===================================================================
# zvtool_npc.py
# NPC manipulation functions
# ===================================================================

# standard imports
import __main__
from types import *
Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

# -------------------------------------------------------------------
# kill all NPCs
# -------------------------------------------------------------------
class zkillClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		npcList = FindClass("npc*")
		for npc in npcList:
			if npc.GetName() != "cabbie":
				npc.Kill()
		print "ALL NPCS KILLED",
# instantiate class
zkill = zkillClass()

# -------------------------------------------------------------------
# make all NPCs hate you
# -------------------------------------------------------------------
class zhateClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		npcList = FindClass("npc*")
		for npc in npcList:
			if npc.GetName() != "cabbie":
				npc.SetRelationship("player D_HT 10")
		print "ALL NPCS HATE YOU",
# instantiate class
zhate = zhateClass()

# -------------------------------------------------------------------
# make all NPCs love you
# -------------------------------------------------------------------
class zloveClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		npcList = FindClass("npc*")
		for npc in npcList:
			if npc.GetName() != "cabbie":
				npc.SetRelationship("player D_LI 10")
		print "ALL NPCS LOVE YOU",
# instantiate class
zlove = zloveClass()
