from core.matrix import Matrix

class Object3D(object):

    def __init__(self):
        self.transform = Matrix.makeIdentity()
        self.parent = None
        self.children = []

    def add(self, child):
        self.children.append(child)
        child.parent = self

    def remove(self, child):
        self.children.remove(child)
        child.parent = None

    # calculate transformation of this Object3D relative
    #   to the root Object3D of the scene graph -> recursive
    def getWorldMatrix(self):
        if self.parent == None:
            return self.transform
        else:
            return self.parent.getWorldMatrix() @ self.transform

    # return a single list containing all descendents -> tree traversal
    def getDescendentList(self):
        # master list of all descendant nodes
        descendants = []
        # nodes to be added to descendant list,
        #   whose children will be added to this list
        nodesToProcess = [self]
        # continue processing nodes while any left in the list
        while len(nodesToProcess) > 0:
            # remove first node from list
            node = nodesToProcess.pop(0)
            # add node to descendant list
            descendants.append(node)
            # children of this node must also be processed
            nodesToProcess = node.children + nodesToProcess

        return descendants

    ### TRANSFORMATIONS ###

    # apply geometric transformations
    def applyMatrix(self, matrix, localCoord=True):
        if localCoord:
            self.transform = self.transform @ matrix
        else:
            self.transform = matrix @ self.transform

    def translate(self, x,y,z, localCoord=True):
        m = Matrix.makeTranslation(x,y,z)
        self.applyMatrix(m, localCoord)

    def rotateX(self, angle, localCoord=True):
        m = Matrix.makeRotationX(angle)
        self.applyMatrix(m, localCoord)

    def rotateY(self, angle, localCoord=True):
        m = Matrix.makeRotationY(angle)
        self.applyMatrix(m, localCoord)

    def rotateZ(self, angle, localCoord=True):
        m = Matrix.makeRotationZ(angle)
        self.applyMatrix(m, localCoord)

    def scale(self, s, localCoord=True):
        m = Matrix.makeScale(s)
        self.applyMatrix(m, localCoord)

    # get/set position components of transform 
    def getPosition(self):
        return [self.transform.item((0,3)),
                self.transform.item((1,3)),
                self.transform.item((2,3))]

    def setPosition(self, x,y,z):
        self.transform.itemset((0,3), x)
        self.transform.itemset((1,3), y)
        self.transform.itemset((2,3), z)

    
