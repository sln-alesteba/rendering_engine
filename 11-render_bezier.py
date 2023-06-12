from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from core.mesh      import Mesh

from geometry.boxGeometry import BoxGeometry
from materials.lineBasicMaterial import LineBasicMaterial
from materials.surfaceBasicMaterial import SurfaceBasicMaterial
from geometry.bezierGeometry import BezierGeometry

from extras.movementRig import MovementRig

class Test(Base):

    def r_n_dim_control(dim, elems):
    
        N, R = 5, 5

        import random

        return [random.sample(range((R + 1) * (R + 1)), dim) for _ in range(elems) ]

    def initialize(self):

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(far=1000)

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)

        self.rig.setPosition(10,10,50)

        geometry = BezierGeometry(Test.r_n_dim_control(3, 15))
        material = LineBasicMaterial()
        self.mesh = Mesh(geometry, material)

        self.scene.add(self.mesh)

    def update(self):

        self.mesh.rotateX(0.00337)
        self.mesh.rotateY(0.00514)
        self.mesh.rotateZ(0.00514)
        #self.mesh.translate(0,0,-0.01)
        
        self.rig.update(self.input, 1/20 )

        self.renderer.render(self.scene, self.camera)

#instantie and run
Test().run()