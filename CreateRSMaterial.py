# import maya.cmds as cmds
import glob
import os
from PIL import Image as img
from collections import defaultdict

# shader = cmds.shadingNode("RedshiftMaterial", asShader=True, name='OwnMaterial1')

"""

	first all files needs to be found in alls subfolders of a given folder.
	Each subfolder containing files is a shader. The shader setup is defined by the files found in the subfolder(e.g. diffuse albedo glossines)
	A node ist created for each file needed to create the shader and connected to the shader
	special nodes like bump, displacement or reverse are created and connected to the file after the file node is created. After that the node is connected to the shader.

"""

# get all textures from subfolder
# define shadertype by texturetypes found
# create shading group
# create material
# create texture nodes
# create additional nodes(displacement, normal/bump)
# connect nodes(Texture and Shader)
# create .ma file for this material

target_dir = 'J:\\00_textures lib\\Gametextures\\**\\*.tif'


class FileAndFolderHandling() :

	folders_and_files = defaultdict(list)


	def __init__(self) :
		self.getSubfolderAndImageFileNames()


	def getSubfolderAndImageFileNames(self) :

		subfolder = ""
		# files_in_subfolder = 

		for filename in glob.iglob('J:\\00_textures lib\\Gametextures\\textures\\Asphalt\\**\\*.tif', recursive=True) :
			subfolder = os.path.dirname(filename) # new subfolder
			self.folders_and_files[subfolder].append(os.path.basename(filename))






# contains an object with all files in the given folder
class TextureFiles() :


	def defineFileTypeByMetaTags(self, file) :
		pass



class CreateShader() :

	def defineShaderTypeByFileType(self, file) :
		pass

	def createShader(self, file) :
		pass



class CreateShaderGroup() :

	def createShaderGroup(self) :
		pass

	def connectShadersToGroup(self) :
		pass



folder_content = FileAndFolderHandling()



print(folder_content.folders_and_files)
