# otro ejemplo para el shader:

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

    def initialize(self):

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(far=1000)

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)

        self.rig.setPosition(0,0,10)

        geometry = BoxGeometry( )
        material = SurfaceBasicMaterial({'baseColor': [1.0, 0.5, 1.0]})
        self.mesh = Mesh(geometry, material)

        self.scene.add(self.mesh)

    def update(self):

        #self.mesh.rotateX(0.0337)
        self.mesh.rotateY(0.0514)
        # self.mesh.rotateZ(0.0337)
        
        self.rig.update(self.input, 1/60 )

        self.renderer.render(self.scene, self.camera)

#instantie and run
Test().run()