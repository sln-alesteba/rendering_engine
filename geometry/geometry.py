class Geometry(object):

    def __init__(self):

        # dicctionary to store attribute objects
        self.attributes = {}

        # number of vertices:
        self.vertexCount = None

    def countVertices(self):
        # the number of vertices the length of any 
        # Attributes object's array of data
        attrib = list ( self.attributes.values() )[0]
        self.vertexCount = len( attrib.data )