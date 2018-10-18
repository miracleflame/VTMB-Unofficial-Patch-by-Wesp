# ZVTOOL
# ===================================================================
# zvtool_pc.py
# player character functions
# ===================================================================

# standard imports
import __main__
from types import *
Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

# zvtool imports
from zvtool_util import strH

# -------------------------------------------------------------------
# set humanity level
# -------------------------------------------------------------------
class zhumClass:
	def __repr__(self):
		return "zERR: This function accepts one numeric argument in the range 0-10."
	def __call__(*args):
		errMsg = "zERR: This function accepts one numeric argument in the range 0-10."
		if len(args) != 2:
			print errMsg,
			return
		newH = args[1]
		if (type(newH) != IntType) or newH < 0 or newH > 10:
			print errMsg,
			return
		pc = __main__.FindPlayer()
		# there's no reliable way to read current humanity level,
		# so max it out and then subtract as needed
		pc.HumanityAdd(10)
		pc.HumanityAdd(newH - 10)
		print "HUMANITY LEVEL SET",
# instantiate class
zhum = zhumClass()

# -------------------------------------------------------------------
# set masquerade violations
# -------------------------------------------------------------------
class zmasClass:
	def __repr__(self):
		return "zERR: This function accepts one numeric argument in the range 0-5."
	def __call__(*args):
		errMsg = "zERR: This function accepts one numeric argument in the range 0-5."
		if len(args) != 2:
			print errMsg,
			return
		newM = args[1]
		if (type(newM) != IntType) or newM < 0 or newM > 5:
			print errMsg,
			return
		pc = __main__.FindPlayer()
		oldM = pc.GetMasqueradeLevel()
		if oldM == newM:
			print "MASQUERADE VIOLATIONS UNCHANGED",
		else:
			pc.ChangeMasqueradeLevel(newM - oldM)
			print "MASQUERADE VIOLATIONS SET",
# instantiate class
zmas = zmasClass()

# -------------------------------------------------------------------
# max out character stats, disciplines, armor, keys, and weapons
# -------------------------------------------------------------------
class zbuffClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		pc = __main__.FindPlayer()
		pc.ChangeMasqueradeLevel(-10)
		pc.HumanityAdd(10)
		pc.MoneyAdd(1000000)
	
		# max all character stats
		statList = (
			"strength",
			"dexterity",
			"stamina",
			"charisma",
			"manipulation",
			"appearance",
			"perception",
			"intelligence",
			"wits",
			"brawl",
			"dodge",
			"intimidation",
			"subterfuge",
			"firearms",
			"melee",
			"security",
			"stealth",
			"computer",
			"finance",
			"investigation",
			"academics"
		)
		for stat in statList:
			pc.BumpStat(stat, 10)
	
		# max character disciplines
		# (only maximizes disciplines that character already has)
		discList = (
			"animalism",
			"auspex",
			"celerity",
			"dementation",
			"dominate",
			"fortitude",
			"obfuscate",
			"potence",
			"presence",
			"protean",
			"thaumaturgy"
		)
		for disc in discList:
			if getattr(pc, disc) != -1:
				pc.BumpStat(disc, 10)
	
		# give all useful items
		itemList = (
			"item_a_hvy_cloth",
			"item_a_lt_leather",
			"item_a_hvy_leather",
			"item_a_body_armor",
			"item_g_lockpick",
			"item_g_bloodpack",
			"item_g_bluebloodpack",
			"item_g_eldervitaepack",
			"item_k_ash_cell_key",
			"item_k_carson_apartment_key",
			"item_k_chinese_theatre_key",
			"item_k_clinic_cs_key",
			"item_k_clinic_maintenance_key",
			"item_k_clinic_stairs_key",
			"item_k_edane_key",
			"item_k_empire_jezebel_key",
			"item_k_empire_mafia_key",
			"item_k_fu_cell_key",
			"item_k_fu_office_key",
			"item_k_gallery_noir_key",
			"item_k_gimble_key",
			"item_k_hannahs_safe_key",
			"item_k_kiki_key",
			"item_k_leopold_int_key",
			"item_k_lilly_key",
			"item_k_lucky_star_murder_key",
			"item_k_malcolm_office_key",
			"item_k_malkavian_refrigerator_key",
			"item_k_murietta_key",
			"item_k_museum_basement_key",
			"item_k_museum_office_key",
			"item_k_museum_storage_key",
			"item_k_museum_storeroom_key",
			"item_k_netcafe_office_key",
			"item_k_oceanhouse_basement_key",
			"item_k_oceanhouse_sewer_key",
			"item_k_oceanhouse_upstairs_key",
			"item_k_oh_front_key",
			"item_k_shrekhub_four_key",
			"item_k_shrekhub_one_key",
			"item_k_shrekhub_three_key",
			"item_k_skyline_haven_key",
			"item_k_tatoo_parlor_key",
			"item_k_tawni_apartment_key",
			"item_k_tutorial_chopshop_stairs_key",
			"item_w_baton",
			"item_w_torch",
			"item_w_fireaxe",
			"item_w_sledgehammer",
			"item_w_bush_hook",
			"item_w_occultblade",
			"item_w_deserteagle",
			"item_w_crossbow_flaming",
			"item_w_flamethrower",
			"item_w_ithaca_m_37",
			"item_w_steyr_aug",
			"item_w_supershotgun",
			"item_w_uzi"
		)
		for item in itemList:
			pc.GiveItem(item)
		zammo()
		print ""
		print "PLAYER STATS AND INVENTORY MAXED",
# instantiate class
zbuff = zbuffClass()

# -------------------------------------------------------------------
# give player some ammo
# -------------------------------------------------------------------
class zammoClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		pc = __main__.FindPlayer()
		gunList = (
			"item_w_colt_anaconda",
			"item_w_crossbow",
			"item_w_crossbow_flaming",
			"item_w_deserteagle",
			"item_w_flamethrower",
			"item_w_glock_17c",
			"item_w_ithaca_m_37",
			"item_w_mac_10",
			"item_w_steyr_aug",
			"item_w_supershotgun",
			"item_w_thirtyeight",
			"item_w_uzi"
		)
		for gun in gunList:
			pc.GiveAmmo(gun, 10000)
		print "PLAYER AMMO FILLED",
# instantiate class
zammo = zammoClass()

# -------------------------------------------------------------------
# display the player's current angle and position
# -------------------------------------------------------------------
class zposClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		pc = __main__.FindPlayer()
		pcCent = pc.GetCenter()
		pcOrig = pc.GetOrigin()
		pcAng = pc.GetAngles()
		print "PLAYER CENTER = " + strH(pcCent[0]) +", " + strH(pcCent[1]) + ", " + strH(pcCent[2])
		print "PLAYER ORIGIN = " + strH(pcOrig[0]) +", " + strH(pcOrig[1]) + ", " + strH(pcOrig[2])
		print "PLAYER ANGLES = " + strH(pcAng[0]) +", " + strH(pcAng[1]) + ", " + strH(pcAng[2]),
# instantiate class
zpos = zposClass()

# -------------------------------------------------------------------
# open all taxi destinations
# -------------------------------------------------------------------
class ztaxiClass:
	def __repr__(self):
		self()
		return ""
	def __call__(self):
		G = __main__.G
		flagList = (
			"Chinatown_Open",
			"Downtown_Open",
			"Giovanni_Open",
			"Hollywood_Open",
			"Kingsway_Open",
			"Mansion_Open",
			"Museum_Open",
			"Society_Open"
		)
		for flag in flagList:
			G[flag] = 1
		print "ALL TAXI DESTINATIONS OPEN"
		print "Now you just need to find a taxi.",
		#__main__.FindPlayer().SewerMap(G.WorldMap_State)
# instantiate class
ztaxi = ztaxiClass()
