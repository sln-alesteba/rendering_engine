from materials.basicMaterial import BasicMaterial
from OpenGL.GL import *

# estamos simplemente encapsulando la funcionalid de los shader
# en diferentes tipos de materiales.

class LineBasicMaterial(BasicMaterial):

    def __init__(self, properties={}):
        super().__init__()

        # esto es lo que necesito
        # varias formas de renderizar puntos como lineas

        # render vertices as continuos by default
        self.settings["drawStyle"] = GL_LINE_STRIP
        # line type: "connected" | "loop" | "segments"
        self.settings["lineType"] = "connected"
        # line thickness
        self.settings["lineWidth"] = 4

        self.setProperties(properties)


    def updateRenderSettings(self):
        
        glLineWidth( self.settings["lineWidth"] )

        if self.settings["lineType"] == "connected":
            self.settings["drawStyle"] = GL_LINE_STRIP
        elif self.settings["lineType"] == "loop":
            self.settings["drawStyle"] = GL_LINE_LOOP
        elif self.settings["lineType"] == "segments":
            self.settings["drawStyle"] = GL_LINES
        else:
            raise Exception("Unknown line style:" +self.settings["lineType"])
