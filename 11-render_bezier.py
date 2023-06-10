from core.base      import Base
from core.renderer  import Renderer
from core.scene     import Scene
from core.camera    import Camera
from core.mesh      import Mesh

from geometry.boxGeometry import BoxGeometry
from materials.lineBasicMaterial import LineBasicMaterial
from materials.surfaceBasicMaterial import SurfaceBasicMaterial
from geometry.bezierGeometry import BezierGeometry

class Test(Base):

    def initialize(self):

        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(far=1000)

        geometry = BoxGeometry()
        material = SurfaceBasicMaterial()
        self.mesh = Mesh(geometry, material)

        self.scene.add(self.mesh)

        # pull camera towards viewer
        self.camera.setPosition(0,0,10)

    def update(self):

        #self.mesh.rotateX(0.0337)
        self.mesh.rotateY(0.0514)
        #self.mesh.rotateZ(0.0514)
        #self.mesh.translate(0,0,-0.01)
        self.renderer.render(self.scene, self.camera)

#instantie and run
Test().run()