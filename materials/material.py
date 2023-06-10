from random import uniform
from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform

class Material(object):

    def __init__(self, vertexShaderCode, fragmentShaderCode):

        self.programRef = OpenGLUtils.initializeProgram(vertexShaderCode, fragmentShaderCode)

        #store Uniforms objects
        self.uniforms = {}

        # standard Uniform objects (matrices)
        self.uniforms["modelMatrix"] = Uniform("mat4", None)
        self.uniforms["viewMatrix"]  = Uniform("mat4", None)
        self.uniforms["projectionMatrix"]  = Uniform("mat4", None)

        # store OpenGl render settings
        self.settings = {}
        self.settings["drawStyle"] = None


    # initialize all Uniform variable references
    def localteUniforms(self):
        # way of iterate a dictionary
        for variableName, uniformObjecet in self.uniforms.items():
            uniformObjecet.locateVariable(self.programRef, variableName)

    #configure OpenGL render settings
    def updateRenderSettings(self):
        pass

    # convenience method for settings multiple "properties":
    #   uniform and render settings values
    def setProperties(self, properties={}):
        for name, data in properties.items():
            #update uniforms
            if name in self.uniforms.keys():
                self.uniforms[name].data = data
            # update render settings
            elif name in self.settings.keys():
                self.settings[name] = data
            # unknown property
            else:
                raise Exception("material has no property: " + name)