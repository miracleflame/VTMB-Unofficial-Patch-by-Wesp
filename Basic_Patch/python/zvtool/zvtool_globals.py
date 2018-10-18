# ZVTOOL
# ===================================================================
# zvtool_globals.py
# package globals
# ===================================================================

# current map BSP filename
# used to detect when a different map has been loaded
MapName = ""

# list of inspection node entities added by zmark
Markers = {}

# player info stored by zbe
PlayerTransformed = 0
OldPlayerModel = ""
OldPlayerOrg = ()
OldPlayerAng = ()
ZnintLastWarned = 0
SavedModel = ""

# currently grabbed entity
#   0: EntRef: entity reference
#   1: Int:    record index number
Grabbed = []

# current znear() list
#   0: EntRef: entity reference
#   1: Int:    record index number
EntList = []

# big list of BSP file dynamic entities
#   0: EntRef: entity reference
#   1: Int:    modified flag
#   2: String: plaintext definition
#   3: Int:    record index number
BspDynEnts = []
