from core.object3D import Object3D
from OpenGL.GL import *

class Mesh(Object3D):

    def __init__(self, geometry, material):
        super().__init__()

        self.geometry = geometry
        self.material = material

        #should this object be rendered
        self.visible = True

        # set up asociations bewtween
        #   attributes in geometry and shader variables in material
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        for variableName, attributeObject in geometry.attributes.items():
            attributeObject.associateVaraible(material.programRef, variableName)
        #unbind the vertex array object
        glBindVertexArray(0)