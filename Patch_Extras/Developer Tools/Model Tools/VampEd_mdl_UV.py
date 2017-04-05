#!BPY

""" Registration info for Blender menus:
Name: 'Bloodlines_UVs  (x.mdl)'
Blender: 240
Group: 'Export'
Tooltip: 'Modified the bloodlines model.MDL directly'
"""

__author__ = 'DDLullu'
__version__ = '2.00'
__bpydoc__ = """\


********From VampEd Version 0.92 and DDLullu.*********


A. It is now possible to move the models vertices and move de UV.

1. Run VampEd and extract the desired model as a .x file. Extract the mdl too.

2. Put this script and "Full_VampEd_import.py" in the script folder of blender. Run Blender, find the import in file menu.

3. Choose VampEd_IMPORT in the menu import and load the model you exported in step 1

4. Move the verts as desired. Don't create or destroy verts, the strips must match the original model!

5. Move the UV as desired. Try to move separates chunks,you could use the scale function on those selected chunks.

6. Select the mesh and choose Bloodlines_mod in export menu. The name must be the same as the original .x file import but with .mdl instead, an x will be append to it.

7. Copied the new file in the proper models directory of bloodlines, make it if necessary and delete the x at the end of the file.
   The new .mdl file will overide the .vpk file.

8. Select the model to reload and view your changes in VampEd, or run the game.

"""

##########################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
# This script modified a bloodlines model.mdl
#
##########################################################################

import Blender
from Blender import NMesh,Object,Material,Texture,Image,Draw,Window,sys
from Blender.Window import *

import struct, string
from types import *

class xExport:
	def __init__(self, filename):
		global my_path
		self.file = open(filename, "rb")
		my_path = Blender.sys.dirname(filename)
		#self.lines = self.file.readlines()
		#filename += 'x'
		filename1 = filename[:-4] + 'x.mdl'
		print "filename1: ", filename1
		self.file1 = open(filename1, "wb" )
		#my_path += '\\'	  #ve
		#print "my_path:", my_path

	def Export(self):
		editmode = Window.EditMode()	# are we in edit mode?	If so ...
		if editmode: Window.EditMode(0) # leave edit mode before getting the mesh

		print " "
		print "modifying MDL..."
		object = Blender.Object.GetSelected()[0]
		mesh = object.getData()

		texcoord = []
		dumdum = (float('0.0'),float('0.0'))
		vertice = 0
		for verti in mesh.verts:
		    vertice += 1
		    texcoord.append(dumdum)


	############  seek the offset of vertices number and position  ##################

#		self.file.seek(288)
#		temp_data = self.file.read(4)		#offset for smd
#		data=struct.unpack('<i', temp_data)
#		#print "offset 1: ",data[0]
#		off_vert = data[0]
#		self.file.seek(data[0]+176)		#offset for number and position of the vertices in model
#		temp_data = self.file.read(8)
#		data = struct.unpack('<ii',temp_data)
#		vertice_nbr = data[0]
#		vertice_ofs = data[1] + 44 + off_vert	 #find start of verts in file
#		print "vert mdl:	", vertice_nbr
#		print "vertice:	", vertice
#		print "addr vert: ", vertice_ofs

       ############  seek the offset of vertices number and position  ##################new one!!!

		self.file.seek(324)
		temp_data = self.file.read(4)           #offset for smd
		data=struct.unpack('<i', temp_data)
		#print "offset 1: ",data[0]
		off_vert = data[0]+16
		self.file.seek(off_vert+144)             #offset for number and position of the vertices in model
		temp_data = self.file.read(8)
		data = struct.unpack('<ii',temp_data)
		vertice_nbr = data[0]
		vertice_ofs = data[1] + off_vert    #find start of verts in file ### -12 for bone's weight
		print "vert mdl:  ", vertice_nbr
		print "vertice:   ", vertice
		print "addr vert: ", vertice_ofs
		#print "filename1: ", filename1

	############  check number of vertices against the mdl if no match exit #########

		if vertice_nbr != vertice :
			print "Wrong count of vertice exiting..."
			result=Blender.Draw.PupMenu("Model vertices dont match Blender vertices %t|OK")
		else:

	##########	write list for vertice UV  #########################################
			if mesh.hasFaceUV():

				for face in mesh.faces:
					texcoord[face.v[0].index] = (face.uv[0][0], 1 -face.uv[0][1])
					texcoord[face.v[1].index] = (face.uv[1][0], 1 -face.uv[1][1])
					texcoord[face.v[2].index] = (face.uv[2][0], 1 -face.uv[2][1])

	##########	start writing new mdl file	########################################

			self.file.seek(0) 			     #return pointer to start of file
			self.file1.write(self.file.read(vertice_ofs))  #read and write until first vertex position

			ii = 0
			for vert in mesh.verts:

				temp_data = self.file.read(44)	     #get vertices information, normals, UVs
				data = struct.unpack('<3BB4h3f3f2f',temp_data)

				if texcoord[ii][0] != 0.0:
					if not ((vert.co.x == 0.0) and (vert.co.y == 0.0) and (vert.co.z == 0.0)):
						#temp_data = struct.pack('<3f3f2f12s',vert.co.x,vert.co.y,vert.co.z,data[3],data[4],data[5],texcoord[ii][0],texcoord[ii][1],data[8])
						#temp_data = struct.pack('<3BB4h3f3f2f',data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],vert.co.x,vert.co.y,vert.co.z,vert.no.x,vert.no.y,vert.no.z,texcoord[ii][0],texcoord[ii][1])
						#temp_data = struct.pack('<3BB4h3f3f2f',data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],vert.co.x,vert.co.y,vert.co.z,vert.no.x,vert.no.y,vert.no.z,data[14],data[15])
						temp_data = struct.pack('<3BB4h3f3f2f',data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],texcoord[ii][0],texcoord[ii][1])
				else:
					if not ((vert.co.x == 0.0) and (vert.co.y == 0.0) and (vert.co.z == 0.0)):
						#temp_data = struct.pack('<3f3f2f12s',vert.co.x,vert.co.y,vert.co.z,data[3],data[4],data[5],data[6],data[7],data[8])
						temp_data = struct.pack('<3BB4h3f3f2f',data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15])
				#temp_data = struct.pack('<3BB4h3f3f2f',data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],vert.co.x,vert.co.y,vert.co.z,vert.no.x,vert.no.y,vert.no.z,texcoord[ii][0],texcoord[ii][1])
				self.file1.write(temp_data)	#overwite verts and UV with blender value
				ii += 1

			self.file1.write(self.file.read())	 #finishing writing the mdl
			result=Blender.Draw.PupMenu("The ...x.MDL was created successfully %t|OK")


		self.file.close()
		self.file1.close()
		#DrawProgressBar (1.0, "...  finished")
		if editmode: Window.EditMode(1)  # optional, just being nice

		print "... finished"




#------------------------------------------------------------------
#  MAIN
#------------------------------------------------------------------
def my_callback(filename):
	if not filename.find('.mdl', -4): print "Not an .mdl file"
	xexport = xExport(filename)
	xexport.Export()


arg = __script__['arg']
Blender.Window.FileSelector(my_callback, "Modified Bloodlines MDL")

