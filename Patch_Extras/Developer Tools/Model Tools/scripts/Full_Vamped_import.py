#!BPY

""" Registration info for Blender menus:
Name: 'VampEd_242(.x)...'
Blender: 240
Group: 'Import'
Tip: 'Import from DirectX text file format format.'
"""

__author__ = 'Mod by DDLullu'
__version__ = '2.00'
__bpydoc__ = """\
This script IMPORT x file create by VampEd 92.0 and  packfile explorer 3.09



               From VampEd Version 0.92

It is now possible to move the models vertices.

1. Run VampEd and extract the desired model as a .x file.

2. Put this script and "VampEd_out.py" in the script folder of blender. Run Blender, find the import in file menu.

3. Choose VampEd_IMPORT in the menu import and load the model you exported in step 1

4. Move the verts as desired. Don't create or destroy verts, the strips must match the original model!

5. Select the mesh and click the Export Verts button. The name must be the same as the original .x file so it's best to save it in another directory.

6. Drag and drop this new partial .x file into the appropriate directory in VampEd's tree view.

7. A progress bar will be displayed as the verts are modified, Then a .mdl file will be saved in the correct directory to override the .vpk file.

8. Select the model to reload and view your changes in VampEd, or run the game.

"""

########################################################################################
##                                                                                    ##
#####      modified for Vampire Bloodlines Tool: VampEd  by DDLullu              #######
##                                                                                    ##
########################################################################################
#               From VampEd Version 0.92                                               #
########################################################################################
#It is now possible to move the models vertices.                                       #
#1. Run VampEd and extract the desired model as a .x file.                             #
#2. Put this script and "VampEd_out.py" in the script folder of blender.               #
#   Run Blender, find the import in file menu.                                         #
#3. Choose VampEd_IMPORT in the menu import and load the model you exported in step 1  #
#4. Move the verts as desired. Don't create or destroy verts, the strips must          #
#   match the original model!                                                          #
#5. Select the mesh and click the Export Verts button. The name must be the same       #
#   as the original .x file so it's best to save it in another directory.              #
#6. Drag and drop this new partial .x file into the appropriate directory in           #
#   VampEd's tree view.                                                                #
#7. A progress bar will be displayed as the verts are modified, Then a .mdl file       #
#   will be saved in the correct directory to override the .vpk file.                  #
#8. Select the model to reload and view your changes in VampEd, or run the game.       #
#9. For packfile don't move the vertices at 0,0,0 they are the lods vertices.          #
########################################################################################

# DirectXImporter.py version 1.2
# Copyright (C) 2005  Arben OMARI -- omariarben@everyday.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# This script import meshes from DirectX text file format

# Grab the latest version here :www.omariben.too.it

import Blender
from Blender import NMesh,Object,Material,Texture,Image,Draw,Window
from Blender.Window import DrawProgressBar


class xImport:
	def __init__(self, filename):
		global my_path
		self.file = open(filename, "r")
		my_path = Blender.sys.dirname(filename)
		self.lines = self.file.readlines()
		#my_path += '\\'    #ve
		print "my_path:", my_path

	def Import(self):
	        editmode = Window.EditMode()    # are we in edit mode?  If so ...
		if editmode: Window.EditMode(0) # leave edit mode before getting the mesh


		lines = self.lines
		print "importing into Blender ..."
		DrawProgressBar (0.0, "Importing into Blender ...")
		scene  = Blender.Scene.getCurrent()
		mesh = NMesh.GetRaw()
		#Get the line of Texture Coords
		nr_uv_ind = 0
		for line_uv in lines:
			l = line_uv.strip()
			words = line_uv.split()																																																	
			if l and words[0] == "MeshTextureCoords" :
				nr_uv_ind = lines.index(line_uv)+1 #ve
		                #print nr_uv_ind , "texture line"
		
		

		#Get Materials
		idx = 0
		i = -1
		mat_list = []
		tex_list = []
		for line_mat in lines:
			i += 1
			l = line_mat.strip()
			words = line_mat.split()																																																	
			if l and words[0] == "Material" :
				idx += 1	
				self.writeMaterials(i, idx, mat_list, tex_list)
				print "found material"
			

		nr_fac_mat = 0		
		#Assign Materials		
		for line_m in lines:
			l = line_m.strip()
			words = line_m.split()
			if l and words[0] == "MeshMaterialList" :
				nr_fac_mat = lines.index(line_m)	+ 3    #ve
				
		#Create The Mesh
		DrawProgressBar (0.3, "Creating the Mesh ...")
		for line in lines:
			l = line.strip()
			words = line.split()																																																	
			if l and words[0] == "Mesh" :											
				nr_vr_ind = lines.index(line)																		
				self.writeVertices(nr_vr_ind, mesh, nr_uv_ind, nr_fac_mat, tex_list)

				
		NMesh.PutRaw(mesh,"Mesh",1)
		if len(mat_list) < 16:
		        mesh.setMaterials(mat_list)
		mesh.update()
			
		if nr_fac_mat and len(mat_list) < 16:
			DrawProgressBar (0.9, "Writing Mesh Materials...")
			print "writing mat test"
			self.writeMeshMaterials(nr_fac_mat, mesh)
				
		self.file.close()
		DrawProgressBar (1.0, "...  finished")
		if editmode: Window.EditMode(1)  # optional, just being nice
		print "... finished"
		
	#------------------------------------------------------------------------------
	#        CREATE THE MESH
	#------------------------------------------------------------------------------
	def writeVertices(self, nr_vr_ind, mesh, nr_uv, nr_fac_mat, tex_list):
		

		lin = self.lines[nr_vr_ind + 1]
		lin_b = self.CleanLine(lin)              #ve
		lin_c = lin_b.strip()                    #ve
		if lin_c :                               #ve
			nr_vert = int((lin_c.split()[0]))
			v_ind = self.lines.index(lin)
		else :
		        #print nr_vr_ind + 2
			lin = self.lines[nr_vr_ind + 2]
			lin_c = self.CleanLine(lin)
			nr_vert = int((lin_c.split()[0]))
			v_ind = self.lines.index(lin )

                #print v_ind , nr_vert
		vx_array = range(v_ind + 1, (v_ind + nr_vert +1))
		#--------------------------------------------------
                #print vx_array[0],vx_array[-1],"vx_array"
		lin_f = self.lines[v_ind + nr_vert +1]
		lin_ff = self.CleanLine(lin_f)              #ve
		lin_fc= lin_ff.strip()                      #ve
		if lin_fc :                                 #ve
			nr_face = int((lin_fc.split()[0]))
			nr_fac_li = self.lines.index(lin_f)
		else :
			lin_f = self.lines[v_ind + nr_vert +2]
			lin_fc = self.CleanLine(lin_f)
			nr_face = int((lin_fc.split()[0]))
			nr_fac_li = self.lines.index(lin_f )


		fac_array = range(nr_fac_li + 1, (nr_fac_li + nr_face + 1))
		#print fac_array[0],fac_array[-1],"fac_array"
                #Get Coordinates
		i = 0
		for l in vx_array: 
			i += 1
			line_v = self.lines[l]
			lin_v = self.CleanLine(line_v)
			words = lin_v.split()
			if i == 3000:
				DrawProgressBar (0.4, "Creating the Mesh ...")

			if i == 6000:
				DrawProgressBar (0.5, "Creating the Mesh ...")
			if len(words)==3:
				co_vert_x = float(words[0])
				co_vert_z = float(words[1])  #ve
				co_vert_y = float(words[2])  #ve
				v=NMesh.Vert(co_vert_x,co_vert_y,co_vert_z)
				mesh.verts.append(v) 
				#DrawProgressBar ((0.3 * ((i-1)/nr_vert))+0.3, "Creating the Mesh ...")
				#print "test 1", i,nr_vert

																																																									
		#Make Faces
		DrawProgressBar (0.5, "Creating the Faces ...")
		i = 0
		ofs = 0

		name_tex1 = " "   #ve 242
		for f in fac_array:
			i += 1

			line_f = self.lines[f+ofs]
			lin_f = self.CleanLine(line_f)
			words = lin_f.split()

			if i == 2000:
				DrawProgressBar (0.6, "Creating the Faces ...")

			if i == 4000:
				DrawProgressBar (0.7, "Creating the Faces ...")

			if i == 6000:
				DrawProgressBar (0.8, "Creating the Faces ...")

			if not(words):                              #se  pass blank line
                                #uv = []
                        #else :
                                #print words,"else"
				ofs += 1                       # since i only see one
				line_f = self.lines[f+ofs]     # blank i make a check
				lin_f = self.CleanLine(line_f) # for only one. May be
				words = lin_f.split()          # adjust if necessary.
                       # print f
			if len(words) == 5:
				f=NMesh.Face()                        #Get a new face object.
				f.v.append(mesh.verts[int(words[1])])
				f.v.append(mesh.verts[int(words[2])])
				f.v.append(mesh.verts[int(words[3])])
				f.v.append(mesh.verts[int(words[4])])
				mesh.faces.append(f)
				if nr_uv :
					uv = []
					#---------------------------------
					l1_uv = self.lines[nr_uv + 2 + int(words[1])]
					fixed_l1_uv = self.CleanLine(l1_uv)
					w1 = fixed_l1_uv.split()
					uv_1 = (float(w1[0]), -float(w1[1]))
					uv.append(uv_1)
					#---------------------------------
					l2_uv = self.lines[nr_uv + 2 + int(words[2])]
					fixed_l2_uv = self.CleanLine(l2_uv)
					w2 = fixed_l2_uv.split()
					uv_2 = (float(w2[0]), -float(w2[1]))
					uv.append(uv_2)
					#---------------------------------
					l3_uv = self.lines[nr_uv + 2 + int(words[3])]
					fixed_l3_uv = self.CleanLine(l3_uv)
					w3 = fixed_l3_uv.split()
					uv_3 = (float(w3[0]), -float(w3[1]))
					uv.append(uv_3)
					#---------------------------------
					l4_uv = self.lines[nr_uv + 2 + int(words[4])]
					fixed_l4_uv = self.CleanLine(l4_uv)
					w4 = fixed_l4_uv.split()
					uv_4 = (float(w4[0]), -float(w4[1]))
					uv.append(uv_4)
					#---------------------------------
					f.uv = uv
					if nr_fac_mat :
						fac_line = self.lines[nr_fac_mat + i]
						fixed_fac = self.CleanLine(fac_line)
						w_tex = int(fixed_fac.split()[0])
						name_tex = tex_list[w_tex]
						if name_tex :
							name_file = Blender.sys.join(my_path,name_tex)
							try:
								img = Image.Load(name_file)
								f.image = img
								#print "No image " + name_tex + " to load"
							except:
								#Draw.PupMenu("No image to load")
								#print "No image " + name_tex + " to load"
								pass

			elif len(words) == 4:
				f=NMesh.Face()
				f.v.append(mesh.verts[int(words[1])])
				f.v.append(mesh.verts[int(words[3])])  #ve
				f.v.append(mesh.verts[int(words[2])])  #ve
				mesh.faces.append(f)
				if nr_uv :
					uv = []
					#---------------------------------
					l1_uv = self.lines[nr_uv + 2 + int(words[1])]
					fixed_l1_uv = self.CleanLine(l1_uv)
					w1 = fixed_l1_uv.split()
					uv_1 = (float(w1[0]), 1-float(w1[1]))
					uv.append(uv_1)
					#---------------------------------
					l2_uv = self.lines[nr_uv + 2 + int(words[3])] #ve
					fixed_l2_uv = self.CleanLine(l2_uv)
					w2 = fixed_l2_uv.split()
					uv_2 = (float(w2[0]), 1-float(w2[1]))
					uv.append(uv_2)
					#---------------------------------
					l3_uv = self.lines[nr_uv + 2 + int(words[2])] #ve
					fixed_l3_uv = self.CleanLine(l3_uv)
					w3 = fixed_l3_uv.split()
					uv_3 = (float(w3[0]), 1-float(w3[1]))
					uv.append(uv_3)
					#---------------------------------
					f.uv = uv
					if nr_fac_mat :
						fac_line = self.lines[nr_fac_mat + i]
						fixed_fac = self.CleanLine(fac_line)
						w_tex = int(fixed_fac.split()[0])
						name_tex = tex_list[w_tex]
						if name_tex1 == name_tex :   #ve 242
						        f.image = img        #ve 242
						elif name_tex :
							name_file = Blender.sys.join(my_path ,name_tex)
							try:
								img = Image.Load(name_file)
								#f.transp = 2
								#print "alpha ",Alpha
								f.image = img
								name_tex1 = name_tex #ve 242
                                                                #f.transp = ALPHA
								#print "No image " + name_file + " to load"
							except:
								name_tex1 = " "     #ve 242
                                                                #Draw.PupMenu("No image to load")
								#print "No image " + name_file + " to load"
								pass
								
				
	
		
	def CleanLine(self,line):
		fix_line = line.replace(";", " ")
		fix_1_line = fix_line.replace('"', ' ')
		fix_2_line = fix_1_line.replace("{", " ")
		fix_3_line = fix_2_line.replace("}", " ")
		fix_4_line = fix_3_line.replace(",", " ")
		fix_5_line = fix_4_line.replace("'", " ")
		return fix_5_line
	

	#------------------------------------------------------------------
	# CREATE MATERIALS
	#------------------------------------------------------------------
	def writeMaterials(self, nr_mat, idx, mat_list, tex_list):
		name = "Material_" + str(idx)
		mat = Material.New(name)
		line = self.lines[nr_mat + 2]   #ve
		#print line
		fixed_line = self.CleanLine(line)
		words = fixed_line.split()	
		mat.rgbCol = [float(words[0]),float(words[1]),float(words[2])]
		mat.setAlpha(float(words[3]))
		#mat.mode |= Material.Modes.ZTRANSP
		#mat.setMode('ZTransp')
		mat_list.append(mat)
		#mat.setMode('ZTransp')
		l = self.lines[nr_mat + 6]    #ve
		#print l
		fix_3_line = self.CleanLine(l)
		tex_n = fix_3_line.split()
		if not tex_n:				######################################for packfile explorer
			l = self.lines[nr_mat + 7]    #ve
			fix_3_line = self.CleanLine(l)
			tex_n = fix_3_line.split()
			if tex_n and tex_n[0] == "TextureFilename" :

			#print "yes texture?"
				if len(tex_n) > 1:
					tex_list.append(tex_n[1])

				if len(tex_n) <= 1 :

					l_succ = self.lines[nr_mat + 9] #ve
					fix_3_succ = self.CleanLine(l_succ)
					tex_n_succ = fix_3_succ.split()
					tex_list.append(tex_n_succ[0])
			else:
				tex_name = None
				tex_list.append(tex_name)
		else:					#####################################for vamped 92
			if tex_n and tex_n[0] == "TextureFilename" :

			#print "yes texture?"
				if len(tex_n) > 1:
					tex_list.append(tex_n[1])

				if len(tex_n) <= 1 :

					l_succ = self.lines[nr_mat + 7] #ve
					fix_3_succ = self.CleanLine(l_succ)
					tex_n_succ = fix_3_succ.split()
					tex_list.append(tex_n_succ[0])
				#print tex_n_succ[0]
			else :
				tex_name = None
				tex_list.append(tex_name)


		return mat_list, tex_list
	#------------------------------------------------------------------
	# SET MATERIALS
	#------------------------------------------------------------------
	def writeMeshMaterials(self, nr_fc_mat, mesh):
		for face in mesh.faces:
			nr_fc_mat += 1
			line = self.lines[nr_fc_mat]
			fixed_line = self.CleanLine(line)
			wrd = fixed_line.split()
			mat_idx = int(wrd[0])
			face.materialIndex = mat_idx
		mesh.update()	
		

				
#------------------------------------------------------------------
#  MAIN
#------------------------------------------------------------------
def my_callback(filename):
	if not filename.find('.x', -2): print "Not an .x file" 
	ximport = xImport(filename)
	ximport.Import()

arg = __script__['arg']
Blender.Window.FileSelector(my_callback, "Import VampEd.X")	

