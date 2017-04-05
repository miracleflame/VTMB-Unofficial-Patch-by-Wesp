#!BPY
##--------------------------------------------------------------------------------------
## File:		ImportSceneX.py
## Description:	Blender Direct X Import Script For Packfile Explorer.
## Author:		Dave Gaunt
## Platform:	PC
##
## Copyright (c) 2008 Dave Gaunt.
##--------------------------------------------------------------------------------------
## History:
##	09-Aug-2008		DMG		Initial Revision.
##--------------------------------------------------------------------------------------

""" Registration info for Blender menus:
Name: 'NEW_IMPORT(*.x *.scene)...'
Blender: 246
Group: 'Import'
Tip: 'Import from DirectX text file format.'
"""

__bpydoc__ = """\
This script NEW_IMPORT
"""

import Blender, string
from Blender import NMesh, Object, Material, Texture, Image, Draw, Window
from Blender.Window import DrawProgressBar

##--------------------------------------------------------------------------------------
## Description:	
##--------------------------------------------------------------------------------------
class xImport:

	def __init__( self, szFileName ):
		self.szDirectoryName = Blender.sys.dirname( szFileName )
		self.file = open( szFileName, "r" )
		self.m_aLines = self.file.read().splitlines()
		self.file.close()

	##--------------------------------------------------------------------------------------
	## Description:	Tokenise Line
	##--------------------------------------------------------------------------------------
	def TokeniseLine( self ):

		while self.m_uLineIndex < self.m_uLineCount:
			szNoSemiColons = self.m_aLines[ self.m_uLineIndex ].replace( ';', ' ' )
			szNoCommas = szNoSemiColons.replace( ',', ' ' )
			aLineTokens = szNoCommas.strip().split( ' ' )
			self.m_uLineIndex += 1

			if len( aLineTokens[ 0 ]):
				return aLineTokens

	##--------------------------------------------------------------------------------------
	## Description:	Find Next Character
	##--------------------------------------------------------------------------------------
	def FindNextCharacter( self, cCharacter ):

		while self.m_uLineIndex < self.m_uLineCount:
			szCurrentLine = self.m_aLines[ self.m_uLineIndex ]
			self.m_uLineIndex += 1

			if -1 != string.find( szCurrentLine, cCharacter ):
				return 1

		return 0

	##--------------------------------------------------------------------------------------
	## Description:	Find Brace Pair
	##--------------------------------------------------------------------------------------
	def FindBracePair( self ):
		nHierarchyLevel = 0

		while self.m_uLineIndex < self.m_uLineCount:
			szCurrentLine = self.m_aLines[ self.m_uLineIndex ]
			self.m_uLineIndex += 1

			if -1 != string.find( szCurrentLine, '{' ):
				nHierarchyLevel += 1

			elif -1 != string.find( szCurrentLine, '}' ):

				if nHierarchyLevel > 1:
					nHierarchyLevel -= 1
				else:
					if 0 == nHierarchyLevel:
						print "Error - Closing Brace Before Open!"

					return

	##--------------------------------------------------------------------------------------
	## Description:	Tokenise Numbers
	##--------------------------------------------------------------------------------------
	def TokeniseNumbers( self ):

		while self.m_uLineIndex < self.m_uLineCount:
			szNoSemiColons = self.m_aLines[ self.m_uLineIndex ].replace( ';', ',' )
			szNoDoubleCommas = szNoSemiColons.replace( ',,', '' )
			szNoWhiteSpace = szNoDoubleCommas.replace( ' ', '' ).strip()
			self.m_uLineIndex += 1

			if ',' == szNoWhiteSpace[ -1 ]:
				aLineTokens = szNoWhiteSpace[ :-1 ].split( ',' )
			else:
				aLineTokens = szNoWhiteSpace.split( ',' )

			if len( aLineTokens[ 0 ]):
				return aLineTokens

		print "Error - Unexpected End Of File In TokeniseNumbers!"

	##--------------------------------------------------------------------------------------
	## Description:	Parse Float Array
	##--------------------------------------------------------------------------------------
	def ParseFloatArray( self, uFloatCount ):
		aFloatBuffer = []

		while self.m_uLineIndex < self.m_uLineCount:
			aNewNumbers = self.TokeniseNumbers()
			uNewCount = len( aNewNumbers )
			uNumberIndex = 0

			if len( aFloatBuffer ) + uNewCount > uFloatCount:
				uNewCount = uFloatCount - len( aFloatBuffer )

			while uNumberIndex < uNewCount:
				aFloatBuffer.append( float( aNewNumbers[ uNumberIndex ]))
				uNumberIndex += 1

			if len( aFloatBuffer ) >= uFloatCount:
				return aFloatBuffer

		print "Error - Unexpected End Of File In ParseFloatArray!"

	##--------------------------------------------------------------------------------------
	## Description:	Parse Int Array
	##--------------------------------------------------------------------------------------
	def ParseIntArray( self, uIntCount ):
		aIntBuffer = []

		while self.m_uLineIndex < self.m_uLineCount:
			aNewNumbers = self.TokeniseNumbers()
			uNewCount = len( aNewNumbers )
			uNumberIndex = 0

			if len( aIntBuffer ) + uNewCount > uIntCount:
				uNewCount = uIntCount - len( aIntBuffer )

			while uNumberIndex < uNewCount:
				aIntBuffer.append( int( aNewNumbers[ uNumberIndex ]))
				uNumberIndex += 1

			if len( aIntBuffer ) >= uIntCount:
				return aIntBuffer

		print "Error - Unexpected End Of File In ParseIntArray!"

	##--------------------------------------------------------------------------------------
	## Description:	Parse Vec2 Array
	##--------------------------------------------------------------------------------------
	def ParseVec2Array( self, uVec2Count ):
		aVec2Buffer = []

		while self.m_uLineIndex < self.m_uLineCount:
			aNewVec2 = self.TokeniseNumbers()

			if 2 == len( aNewVec2 ):
				aVec2Buffer.append([ float( aNewVec2[ 0 ]), float( aNewVec2[ 1 ]) ])
			else:
				print "Error - Vec2 Expecting Two Floats!"

			if len( aVec2Buffer ) >= uVec2Count:
				return aVec2Buffer

		print "Error - Unexpected End Of File In ParseVec2Array!"

	##--------------------------------------------------------------------------------------
	## Description:	Parse Vec3 Array
	##--------------------------------------------------------------------------------------
	def ParseVec3Array( self, uVec3Count ):
		aVec3Buffer = []

		while self.m_uLineIndex < self.m_uLineCount:
			aNewVec3 = self.TokeniseNumbers()

			if 3 == len( aNewVec3 ):
				aVec3Buffer.append([ float( aNewVec3[ 0 ]), float( aNewVec3[ 1 ]), float( aNewVec3[ 2 ]) ])
			else:
				print "Error - Vec3 Expecting Three Floats!"

			if len( aVec3Buffer ) >= uVec3Count:
				return aVec3Buffer

		print "Error - Unexpected End Of File In ParseVec3Array!"

	##--------------------------------------------------------------------------------------
	## Description:	Parse Face Array
	##--------------------------------------------------------------------------------------
	def ParseFaceArray( self, uFaceCount ):
		aFaceBuffer = []

		while self.m_uLineIndex < self.m_uLineCount:
			aNewFace = self.TokeniseNumbers()

			if 4 == len( aNewFace ):
				aFaceBuffer.append([ int( aNewFace[ 1 ]), int( aNewFace[ 2 ]), int( aNewFace[ 3 ]) ])
			else:
				print "Error - Only Triangulated Faces Supported!"

			if len( aFaceBuffer ) >= uFaceCount:
				return aFaceBuffer

		print "Error - Unexpected End Of File In ParseFaceArray!"

	##--------------------------------------------------------------------------------------
	## Description:	Parse Material
	##--------------------------------------------------------------------------------------
	def ParseMaterial( self ):
		self.FindNextCharacter( '{' )

		aColourFace = self.TokeniseNumbers()
		aPower = self.TokeniseNumbers()
		aColourSpecular = self.TokeniseNumbers()
		aColourEmissive = self.TokeniseNumbers()

		self.FindNextCharacter( '"' )
		aTextureName = self.m_aLines[ self.m_uLineIndex - 1 ].split( '"' )
		self.FindNextCharacter( '}' )

		material = ( aTextureName[ 1 ], aColourFace )

		print "\tFace Colour =", aColourFace
		print "\tPower =", aPower
		print "\tSpecular Colour =", aColourSpecular
		print "\tEmissive Colour =", aColourEmissive
		print "\tTexture File Name = '", aTextureName[ 1 ], "'"

		self.FindNextCharacter( '}' )
		return material

	##--------------------------------------------------------------------------------------
	## Description:	Parse XSkin Mesh Header
	##--------------------------------------------------------------------------------------
	def ParseXSkinMeshHeader( self ):
		self.FindNextCharacter( '{' )

		aMaxSkinWeightsPerVertex = self.TokeniseNumbers()
		aMaxSkinWeightsPerFace = self.TokeniseNumbers()
		aBoneCount = self.TokeniseNumbers()

		print "\tMax Skin Weights Per Vertex =", int( aMaxSkinWeightsPerVertex[ 0 ])
		print "\tMax Skin Weights Per Face =", int( aMaxSkinWeightsPerFace[ 0 ])
		print "\tBone Count =", int( aBoneCount[ 0 ])

		self.FindNextCharacter( '}' )

	##--------------------------------------------------------------------------------------
	## Description:	Parse XSkin Weights
	##--------------------------------------------------------------------------------------
	def ParseSkinWeights( self ):
		self.FindNextCharacter( '{' )
		aLineTokens = self.TokeniseLine()
		szBoneName = aLineTokens[ 0 ].replace( '"', '' )
		aLineTokens = self.TokeniseLine()
		uVertexCount = int( aLineTokens[ 0 ])

#		print "\tFound Skin With", uVertexCount, "Vertices Weighted To Bone", szBoneName

		aVertices = self.ParseFloatArray( uVertexCount )
		aWeights = self.ParseFloatArray( uVertexCount )
		aMatrix = self.ParseFloatArray( 16 )

#		print "Tokens (", len( aLineTokens ), ") = ", aLineTokens
		self.FindNextCharacter( '}' )

	##--------------------------------------------------------------------------------------
	## Description:	Parse Placed Entity
	##--------------------------------------------------------------------------------------
	def ParsePlacedEntity( self ):
		self.FindNextCharacter( '{' )
		aLineEntity = self.TokeniseLine()
		strEntityToken = aLineEntity[ 0 ].lower()

		if -1 != strEntityToken.find( "entitydynamic" ) or -1 != strEntityToken.find( "entitystatic" ) or -1 != strEntityToken.find( "entityinstance" ):
			aLineFileName = self.TokeniseLine()
			szNoQuotes = aLineFileName[ 0 ].replace( '"', ' ' )
			szFileName = self.szDirectoryName + '\\' + szNoQuotes.strip()

			aMatrix = self.ParseFloatArray( 16 )
			v4Right = Blender.Mathutils.Vector( aMatrix[ 0 ], aMatrix[ 1 ], aMatrix[ 2 ], aMatrix[ 3 ])
			v4Up = Blender.Mathutils.Vector( aMatrix[ 4 ], aMatrix[ 5 ], aMatrix[ 6 ], aMatrix[ 7 ])
			v4At = Blender.Mathutils.Vector( aMatrix[ 8 ], aMatrix[ 9 ], aMatrix[ 10 ], aMatrix[ 11 ])
			v4Position = Blender.Mathutils.Vector( aMatrix[ 12 ], aMatrix[ 13 ], aMatrix[ 14 ], aMatrix[ 15 ])
			matrix = Blender.Mathutils.Matrix( v4Right, v4Up, v4At, v4Position )
			ximport = xImport( szFileName )

			if -1 != strEntityToken.find( "entitydynamic" ):
				ximport.Import( "MeshDynamic" + str( self.uMeshIndex ), matrix * self.matrix )

			elif -1 != strEntityToken.find( "entitystatic" ):
				ximport.Import( "MeshStatic" + str( self.uMeshIndex ), matrix * self.matrix )

			else:
				ximport.Import( "MeshInstance" + str( self.uMeshIndex ), matrix * self.matrix )

			self.FindNextCharacter( '}' )
			self.uMeshIndex += 1

		else:
			print "Unexpected Entity '", strEntityToken, "' on line", self.m_uLineIndex

	##--------------------------------------------------------------------------------------
	## Description:	Parse Mesh
	##--------------------------------------------------------------------------------------
	def ParseMesh( self, szMeshName ):
		print "\tfound Mesh", szMeshName
		self.FindNextCharacter( '{' )
		nHierarchyLevel = 1

		aLineTokens = self.TokeniseLine()
		aVertices = self.ParseVec3Array( int( aLineTokens[ 0 ]))
		aLineTokens = self.TokeniseLine()
		aFaces = self.ParseFaceArray( int( aLineTokens[ 0 ]))
		aMaterialList = []

		while self.m_uLineIndex < self.m_uLineCount:
			uBaseLine = self.m_uLineIndex
			aLineTokens = self.TokeniseLine()
			strToken = aLineTokens[ 0 ].lower()

			if "material" == strToken:
				aMaterialList.append( self.ParseMaterial() )

			elif "meshmateriallist" == strToken:
				nHierarchyLevel += 1
				self.FindNextCharacter( '{' )
				aLineTokens = self.TokeniseLine()
				uMaterialCount = int( aLineTokens[ 0 ])
				aLineTokens = self.TokeniseLine()
				aMaterialFaces = self.ParseIntArray( int( aLineTokens[ 0 ]))

				print "\tMaterial Count =", uMaterialCount, "Material Faces =", len( aMaterialFaces )

			elif "meshnormals" == strToken:
				self.FindBracePair()

#				nHierarchyLevel += 1
#				self.FindNextCharacter( '{' )
#				aLineTokens = self.TokeniseLine()
#				aNormals = self.ParseVec3Array( int( aLineTokens[ 0 ]))
#				aLineTokens = self.TokeniseLine()
#				aNormalFaces = self.ParseFaceArray( int( aLineTokens[ 0 ]))
#				print "\tNormal count =", len( aNormals ), "Normal Faces =", len( aNormalFaces )

			elif "meshtexturecoords" == strToken:
				nHierarchyLevel += 1
				self.FindNextCharacter( '{' )
				aLineTokens = self.TokeniseLine()
				aTexCoords = self.ParseVec2Array( int( aLineTokens[ 0 ]))

			elif "skinweights" == strToken:
				self.ParseSkinWeights()

			elif "xskinmeshheader" == strToken:
				self.ParseXSkinMeshHeader()

			elif -1 != string.find( self.m_aLines[ uBaseLine ], '}' ):
				nHierarchyLevel -= 1

				if 0 == nHierarchyLevel:
					print "End Mesh"
					break
			else:
				print "Unexpected Mesh Token '", strToken, "' on line", self.m_uLineIndex
				break

		print "Vertex count =", len( aVertices ), "Face Count =", len( aFaces ), "Tex Coord count =", len( aTexCoords )
		meshCurrent = NMesh.GetRaw()

		for vertex in aVertices:
			v3Vertex = Blender.Mathutils.Vector( vertex ) * self.matrix
			meshCurrent.verts.append( NMesh.Vert( v3Vertex[ 0 ], v3Vertex[ 2 ], v3Vertex[ 1 ]))

#		aMaterialList = []
#		material = Material.New( "Material_Test" )
#		material.rgbCol = [ float(words[0]), float(words[1]), float(words[2]) ]
#		material.setAlpha( float(words[3]) )
#		aMaterialList.append( material )
#		meshCurrent.setMaterials( aMaterialList )
#		meshCurrent.update()

		aImageList = []
		uFaceIndex = 0

		for material in aMaterialList:
			szFileName = self.szDirectoryName + '\\' + material[ 0 ]
			print "Loading Image " + szFileName
			aImageList.append( Image.Load( szFileName ))

		for face in aFaces:
			faceNew = NMesh.Face()
			faceNew.v.append( meshCurrent.verts[ face[ 0 ]])
			faceNew.uv.append( (aTexCoords[ face[ 0 ]][ 0 ], -aTexCoords[ face[ 0 ]][ 1 ]) )
			faceNew.v.append( meshCurrent.verts[ face[ 2 ]])
			faceNew.uv.append( (aTexCoords[ face[ 2 ]][ 0 ], -aTexCoords[ face[ 2 ]][ 1 ]) )
			faceNew.v.append( meshCurrent.verts[ face[ 1 ]])
			faceNew.uv.append( (aTexCoords[ face[ 1 ]][ 0 ], -aTexCoords[ face[ 1 ]][ 1 ]) )
			faceNew.image = aImageList[ aMaterialFaces[ uFaceIndex ]]
#			faceNew.materialIndex = uMaterialIndex
#			faceNew.smooth = 1
			meshCurrent.faces.append( faceNew )
			uFaceIndex += 1

		NMesh.PutRaw( meshCurrent, self.szModelName + "_" + str( self.uMeshIndex ), 1 )
		self.uMeshIndex += 1
		meshCurrent.update()

	##--------------------------------------------------------------------------------------
	## Description:	Parse Frame
	##--------------------------------------------------------------------------------------
	def ParseFrame( self ):
		self.FindNextCharacter( '{' )
		nHierarchyLevel = 1

		while self.m_uLineIndex < self.m_uLineCount:
			uBaseLine = self.m_uLineIndex
			aLineTokens = self.TokeniseLine()
			strToken = aLineTokens[ 0 ].lower()

			if "frame" == strToken:
				self.m_uLineIndex -= 1
				self.ParseSkeleton()

			elif "mesh" == strToken:
				self.ParseMesh( aLineTokens[ 1 ])

			elif "placedentity" == strToken:
				self.ParsePlacedEntity()

			elif -1 != string.find( self.m_aLines[ uBaseLine ], '}' ):
				nHierarchyLevel -= 1

				if 0 == nHierarchyLevel:
					print "End Frame"
					break
			else:
				print "Unexpected Frame Token '", strToken, "' on line", self.m_uLineIndex
				break

	##--------------------------------------------------------------------------------------
	## Description:	Parse Skeleton
	##--------------------------------------------------------------------------------------
	def ParseSkeleton( self ):
		nHierarchyLevel = 0
		szSpace = "                               " 

### FIXME !!! This Should Be In Parse Frame !!!

		while self.m_uLineIndex < self.m_uLineCount:
			uBaseLine = self.m_uLineIndex
			aLineTokens = self.TokeniseLine()
			strToken = aLineTokens[ 0 ].lower()

			if "frame" == strToken:
#				print szSpace[ : nHierarchyLevel * 2 ], "Found Bone", aLineTokens[ 1 ]
				self.FindNextCharacter( '{' )
				nHierarchyLevel += 1
	
			elif "frametransformmatrix" == strToken:
				self.FindNextCharacter( '{' )
				nHierarchyLevel += 1
				aMatrix = self.ParseFloatArray( 16 )
#				print "Matrix (", len( aMatrix ), ") = ", aMatrix

			elif -1 != string.find( self.m_aLines[ uBaseLine ], '}' ):
				nHierarchyLevel -= 1
#				print szSpace[ : nHierarchyLevel * 2 ], '}'

				if 0 == nHierarchyLevel:
					return
			else:
				print "Unexpected Skeleton Token '", strToken, "' on line", self.m_uLineIndex
				break

	##--------------------------------------------------------------------------------------
	## Description:	Parse Animation Key
	##--------------------------------------------------------------------------------------
	def ParseAnimationKey( self ):
		self.FindNextCharacter( '{' )

		aLineTokens = self.TokeniseLine()
		uKeyType = int( aLineTokens[ 0 ])

		if 4 != uKeyType:
			print "Unsupported Key Frame Type", uKeyType
			return

		aLineTokens = self.TokeniseLine()
		uKeyFrameCount = int( aLineTokens[ 0 ])
#		print "Found Key Of Type", uKeyType, "With", uKeyFrameCount, "Key Frames"

		uKeyFrameIndex = 0

		while uKeyFrameIndex < uKeyFrameCount:
			aLineTokens = self.TokeniseNumbers()
#			print "Tokens (", len( aLineTokens ), ") = ", aLineTokens
			uKeyFrameIndex += 1

		self.FindNextCharacter( '}' )

	##--------------------------------------------------------------------------------------
	## Description:	Parse Animation Set
	##--------------------------------------------------------------------------------------
	def ParseAnimationSet( self ):
		self.FindNextCharacter( '{' )
		nHierarchyLevel = 1

		while self.m_uLineIndex < self.m_uLineCount:
			uBaseLine = self.m_uLineIndex
			aLineTokens = self.TokeniseLine()
			strToken = aLineTokens[ 0 ].lower()

			if "animation" == strToken:
				nHierarchyLevel += 1
				self.FindNextCharacter( '{' )
				# Skip Bone Name
				self.m_uLineIndex += 1

			elif "animationkey" == strToken:
				self.ParseAnimationKey()

			elif -1 != string.find( self.m_aLines[ uBaseLine ], '}' ):
				if 1 == nHierarchyLevel:
#					print "Tokens (", len( aLineTokens ), ") = ", aLineTokens
					return

				nHierarchyLevel -= 1

			else:
				print "Unexpected Animation Token '", strToken, "' on line", self.m_uLineIndex
				break

	##--------------------------------------------------------------------------------------
	## Description:	Import
	##--------------------------------------------------------------------------------------
	def Import( self, szModelName, matrix ):
		self.szModelName = szModelName
		self.matrix = matrix
		self.uMeshIndex = 0
		self.m_uLineCount = len( self.m_aLines )
		self.m_uLineIndex = 0

		while self.m_uLineIndex < self.m_uLineCount:
			aLineTokens = self.TokeniseLine()
			strToken = aLineTokens[ 0 ].lower()

			if "xof" == strToken:
				print "found xof"

			elif "animationset" == strToken:
				self.ParseAnimationSet()

			elif "frame" == strToken:
				print "found Frame", aLineTokens[ 1 ]
				self.ParseFrame()

			elif "template" == strToken:
				print "found template", aLineTokens[ 1 ]
				self.FindBracePair()

			elif "xfileversion" == strToken:
				print "found xFileVersion"
				self.FindBracePair()

			else:
				print "Unexpected Token '", strToken, "' on line", self.m_uLineIndex
				break
				
##--------------------------------------------------------------------------------------
## Description:	
##--------------------------------------------------------------------------------------
def my_callback( szFileName ):

	fScale = 0.1

	print "\n\nImporting Into Blender ...\n"
	DrawProgressBar( 0.0, "Importing Into Blender ..." )
	editmode = Window.EditMode()

	if editmode:
		# Leave Edit Mode Before Getting The Mesh
		Window.EditMode( 0 ) 

#	scene = Blender.Scene.GetCurrent()
	v4Right = Blender.Mathutils.Vector( fScale, 0.0, 0.0, 0.0 )
	v4Up = Blender.Mathutils.Vector( 0.0, fScale, 0.0, 0.0 )
	v4At = Blender.Mathutils.Vector( 0.0, 0.0, fScale, 0.0 )
	v4Position = Blender.Mathutils.Vector( 0.0, 0.0, 0.0, 1.0 )
	matScale = Blender.Mathutils.Matrix( v4Right, v4Up, v4At, v4Position )

	if -1 != szFileName.find( '.scene', -6 ):
		ximport = xImport( szFileName[ :-6 ] + ".x" )
		ximport.Import( "BaseModel", matScale )

		ximport = xImport( szFileName )
		ximport.Import( "Mesh", matScale )
		print "... Complete\n"

	elif -1 != szFileName.find( '.x', -2 ):
		ximport = xImport( szFileName )
		ximport.Import( "Mesh", matScale )
		print "... Complete\n"

	else:
		print "Not A Direct 3d .x File."

	DrawProgressBar( 1.0, "...  Complete" )

	if editmode:
		Window.EditMode( 1 )

#	print dir( Blender.NMesh )

arg = __script__[ 'arg' ]

Blender.Window.FileSelector( my_callback, "Import DirectX" )
