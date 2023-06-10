import numpy as np
from OpenGL.GL import *

class Attribute(object):

    def __init__(self, dataType, data):

        # type of elements in data array
        #   int | float | vec2 | vec3 | vec4
        self.dataType = dataType

        # array of data to be stored in buffer
        self.data = data

        # reference to available buffer in GPU
        self.bufferRef = glGenBuffers(1)

        # upload data immediately
        self.uploadData()

    # upload this data to a GPU buffer
    def uploadData(self):

        # convert data to numpy array format; convert to floats
        data = np.array(self.data).astype(np.float32)

        # select buffer used to following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # store data in currentely bound buffer
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)


    # associate variable in GPU program with this buffer
    def associateVaraible(self, programRef, variableName):

        # get reference for program varible with given name
        variableRef = glGetAttribLocation(programRef, variableName)

        # if the program does not reference the variable, exit
        if variableRef == -1:
            return

        # select the buffer used by following functions:
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # specify how data will bee read
        #   from the buffer currently bound to GL_ARRAY_BUFFER

        if self.dataType == "int":
            glVertexAttribPointer(variableRef, 1, GL_INT, False, 0, None)
        elif self.dataType == "float":
            glVertexAttribPointer(variableRef, 1, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec2":
            glVertexAttribPointer(variableRef, 2, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec3":
            glVertexAttribPointer(variableRef, 3, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec4":
            glVertexAttribPointer(variableRef, 4, GL_FLOAT, False, 0, None)
        else:
            raise Exception("Unknown Atribute type " + self.dataType)

        # indicate data shoul be streamed to variable from buffer
        glEnableVertexAttribArray( variableRef )