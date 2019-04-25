#!BPY

"""
Name: 'COLLADA 1.4(.dae) ...'
Blender: 241
Group: 'Export'
Tooltip: 'Export scene from Blender to COLLADA 1.4 format (.dae)'
"""

__author__ = "Illusoft - Pieter Visser"
__url__ = ("Project homepage, http://colladablender.illusoft.com")
__version__ = "0.2.65"
__email__ = "colladablender@illusoft.com"
__bpydoc__ = """\

Description: Exports a Blender scene into a COLLADA 1.4 file.

Usage: Run the script from the menu or inside Blender. 
"""

# --------------------------------------------------------------------------
# Illusoft Collada 1.4 plugin for Blender version 0.2.65
# --------------------------------------------------------------------------
# ***** BEGIN GPL LICENSE BLOCK *****
#
# Copyright (C) 2006: Illusoft - colladablender@illusoft.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****
# --------------------------------------------------------------------------

import sys
##import os
import Blender

error = False

######################## SET PATH TO FOLDER consisting 'colladaImEx' here (if necessary)
	
# Example:
   
# scriptsDir = "C:/Temp/"
   
scriptsDir = ""
#############################################################################

try:
	import colladaImEx.cstartup
	if Blender.Get('scriptsdir') is None:
		if scriptsDir == '' or scriptsDir is None:
			Blender.Draw.PupMenu("Cannot find folder %t | Please set path in file 'colladaImport14.py'")
			error = True
		else:
			loc = scriptsDir
	else:
		loc = ""
except ImportError:
	# Check if full version of python is installed:
	try:
		import os
		pythonFull = True
	except ImportError:
		pythonFull = False
	
	if not pythonFull:
		from sys import version_info
		version = '%s.%s' % version_info[0:2]
		print """
This script requires the xml module that is part of a
default standalone Python install.

To run the collada importer and exporter you need to have
Python version %s installed in your system. It can be downloaded from:

http://www.python.org

Notes:
- The minor (third) version number doesn't matter, you can have either
Python %s.1 or %s.2 or higher.
- If you do have Python %s installed and still can't run the scripts, then
make sure Blender's Python interpreter is finding the standalone modules
(run 'System Information' from Blender's Help -> System menu).
""" % (version, version, version, version)
		Blender.Draw.PupMenu("Please install full version of python %t | Check the console for more info")
		error = True
	else:	
		if scriptsDir == "":
			Blender.Draw.PupMenu("Cannot find folder %t | Please set path in file 'colladaImport14.py'")
			error = True
		else:
			if scriptsDir not in sys.path:
				sys.path.append(scriptsDir)
			try:
				import colladaImEx.cstartup
				loc = scriptsDir
			except:
				Blender.Draw.PupMenu("Cannot find colladaImEx files %t | Please make sure the path is correct in file 'colladaImport14.py'")
				error = True
except StandardError:
	error = True
			
if not error:		 
	try:
		reload(colladaImEx.cstartup)
		colladaImEx.cstartup.Main(False, loc)
	except StandardError:
		pass
