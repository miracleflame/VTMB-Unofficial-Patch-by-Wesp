# --------------------------------------------------------------------------
# Illusoft Collada 1.4 plugin for Blender version 0.3.146
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

import Blender
import collada
from Blender.Mathutils import *

class Armature(object):	
	# static vars
	# A list of all created armatures
	_armatures = dict()
	
	def __init__(self, armatureBObject, daeNode):
		self.armatureBObject = armatureBObject
		self.blenderArmature = armatureBObject.data
		self.boneInfos = dict()
		self.rootBoneInfos = dict()
		# The real blender name of this armature
		self.realName = None
		self.deaNode = daeNode

	def GetBlenderObject(self):
		return self.armatureBObject

	def GetBlenderArmature(self):
		return self.blenderArmature
	
	def HasBone(self, boneName):
		return boneName in self.boneInfos
	
	def AddNewBone(self, boneName, parentBoneName, daeNode):
		# Create a new Editbone.
		editBone = Blender.Armature.Editbone()
		# Add the bone to the armature
		self.blenderArmature.bones[boneName] = editBone
		# Get the boneInfo for the parent of this bone. (if it exists)
		parentBoneInfo = None
		if not parentBoneName is None and parentBoneName in self.boneInfos:
			parentBoneInfo = self.boneInfos[parentBoneName]
		# Create a new boneInfo object
		boneInfo = BoneInfo(boneName, parentBoneInfo, self, daeNode)
		# Store the boneInfo object in the boneInfos collection of this armature.
		self.boneInfos[boneName] = boneInfo
		
		# If this bone has a parent, set it.
		if not parentBoneName is None and parentBoneName in self.boneInfos:			
			parentBoneInfo = self.boneInfos[parentBoneName]
			parentBoneInfo.childs[boneName] = boneInfo
			editBone.parent = self.GetBone(parentBoneName)
			##boneInfo.SetConnected()
		else:
			self.rootBoneInfos[boneName] = boneInfo
		
		return boneInfo
	
	def MakeEditable(self,makeEditable):
		if makeEditable:
			self.GetBlenderArmature().makeEditable()
		else:
			self.GetBlenderArmature().update()
	
	def GetBone(self, boneName):
		if boneName is None or not (boneName in self.blenderArmature.bones.keys()):
			return None
		else:
			return self.blenderArmature.bones[boneName]

	# Get the location of the armature (VECTOR)
	def GetLocation(self):
		return Vector(self.armatureBObject.loc).resize4D()
	
	def GetTransformation(self):
		return self.armatureBObject.matrix

	def GetBoneInfo(self, boneName):
		if boneName is None:
			return None
		else:
			return self.boneInfos[boneName]
		
	def GetBoneInfoFromJoint(self, jointName):
		for boneInfo in self.boneInfos:
			if boneInfo.jointName == jointName:
				return boneInfo
		return None

	def GetJointList(self):
		result = dict()
		for boneInfo in self.boneInfos.values():
			result[boneInfo.GetJointName()] = boneInfo
		return result

	#---CLASSMETHODS
	
	# Factory method
	def CreateArmature(cls,objectName,armatureName, realArmatureName, daeNode):		
		armatureBObject = Blender.Object.New('Armature',objectName)
		armatureBObject.data.name = str(realArmatureName)
		armature = Armature(armatureBObject, daeNode)		
		armature.name = armatureName
		cls._armatures[armatureName] = armature
		
		return armature
	CreateArmature = classmethod(CreateArmature)
	
	def GetArmature(cls, armatureName):
		return cls._armatures.setdefault(armatureName)
	GetArmature = classmethod(GetArmature)
	
	def FindArmatureWithJoint(cls, jointName):
		for armature in cls._armatures.values():
			jointList = armature.GetJointList()
			if jointName in jointList:
				return armature
		return None
	FindArmatureWithJoint = classmethod(FindArmatureWithJoint)
	
class BoneInfo(object):
	
	def __init__(self, boneName, parentBoneInfo, armature, daeNode):
		self.name = boneName
		self.parent = parentBoneInfo
		self.armature = armature
		self.childs = dict()
		self.daeNode = daeNode
		
		self.headTransformMatrix = None
		self.tailTransformMatrix = None
		
		self.localTransformMatrix = Matrix()
		self.worldTransformMatrix = Matrix()
	
	def GetBone(self):
		return self.armature.GetBone(self.name)

	def SetTail(self, tailLocVector):
		if len(tailLocVector) == 4:
			tailLocVector.resize3D()
		self.GetBone().tail = tailLocVector
	
	def GetTail(self):
		return self.GetBone().tail

	def SetHead(self, headLocVector):
		if len(headLocVector) == 4:
			headLocVector.resize3D()
		self.GetBone().head = headLocVector
	
	def GetHead(self):
		return self.GetBone().head

	def SetConnected(self):		
		self.GetBone().options = Blender.Armature.CONNECTED
		
	def IsEnd(self):
		return len(self.childs) == 0

	def IsRoot(self):
		return self.parent is None

	def GetTailName(self):
		return self.daeNode.name

	def GetJointName(self):
		return self.name
##		if not self.parent is None:
##			return self.parent.name
##		else:
##			return self.armature.name

class AnimationInfo(object):
	_animations = dict()
	
	def __init__(self, nodeId):
		self.nodeId = nodeId
		self.times = dict()
	
	def GetTypes(self, daeNode):
		types = []
		if len(self.times) > 0:
			for target in self.times.values()[0]:
				ta = self.GetType(daeNode, target)
				if ta[0] == collada.DaeSyntax.TRANSLATE and not Blender.Object.Pose.LOC in types:
					types.append(Blender.Object.Pose.LOC)
				elif ta[0] == collada.DaeSyntax.ROTATE and not Blender.Object.Pose.ROT in types:
					types.append(Blender.Object.Pose.ROT)						
		return types			
	
	def GetType(self, daeNode, target):
		ta = target.split('.', 1)
		for t in daeNode.transforms:
			if t[2] == ta[0]:
				return [t[0], ta]
				
	
	def CreateAnimations(cls, animationsLibrary, fps, axiss):
		for daeAnimation in animationsLibrary.daeLibrary.items:
			for channel in daeAnimation.channels:
				# Get the id of the node
				targetArray = channel.target.split("/", 1)
				nodeId = targetArray[0]
				targetId = targetArray[1]
				# Get the animationInfo object for this node (or create a new one)
				animation = cls._animations.setdefault(nodeId, AnimationInfo(nodeId))
				
				# loop trough all samplers
				sampler = None
				for s in daeAnimation.samplers:
					if s.id == channel.source[1:]:
						sampler = s
				
				# Get the values for all the inputs
				if not sampler is None:
					input = sampler.GetInput("INPUT")
					inputSource = daeAnimation.GetSource(input.source)
					if inputSource.techniqueCommon.accessor.HasParam("TIME") and len(inputSource.techniqueCommon.accessor.params) == 1:
						output = sampler.GetInput("OUTPUT")
						outputSource = daeAnimation.GetSource(output.source)
						outputAccessor = outputSource.techniqueCommon.accessor
						accessorCount = outputAccessor.count
						accessorStride = outputAccessor.stride
						times = [x*fps for x in inputSource.source.data]
						
						for timeIndex in range(len(times)):
							time = animation.times.setdefault(times[timeIndex], dict())
							target = time.setdefault(targetId, dict())
							for j in range(accessorStride):
								target[outputAccessor.params[j]] = outputSource.source.data[timeIndex*accessorStride + j]

	CreateAnimations = classmethod(CreateAnimations)
	
	
		
	def GetAnimationInfo(cls, nodeId):
		for animation in cls._animations.values():
			if animation.nodeId == nodeId:
				return animation
		return None
	GetAnimationInfo = classmethod(GetAnimationInfo)

	