# view matrix -> inverse of the camera transformation matrix
# every scene object gets affected by the camera transformation
# each caera transformation affects sence objects in the opposite way;
# mathematically: define view matrix as invers of camera transform matrix

from core.object3D import Object3D
from core.matrix import Matrix
from numpy.linalg import inv

class Camera(Object3D):

    def __init__(self, angleOfView=60, aspectRatio=1, near=0.1, far=100):

        super().__init__()

        self.projectionMatrix = Matrix.makePerspective(angleOfView, aspectRatio, near, far)
        
        self.viewMatrix = Matrix.makeIdentity()

    def updateViewMatrix(self):
        # we use the computed world matrix
        self.viewMatrix = inv( self.getWorldMatrix() )


