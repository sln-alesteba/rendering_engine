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
        self.mesh_1 = Mesh(geometry, material)

        geometry_2 = BoxGeometry(0.5, 0.5, 0.5)
        material_2 = SurfaceBasicMaterial({'baseColor': [0.5, 0.5, 1.0]})
        self.mesh_2 = Mesh(geometry_2, material_2)
        self.mesh_2.setPosition(1.0, 1.0, 1.0)

        self.mesh_1.add(self.mesh_2)

        self.scene.add(self.mesh_1)

    def update(self):

        #self.mesh.rotateX(0.0337)
        self.mesh_1.rotateY(0.0514)
        # self.mesh.rotateZ(0.0337)
        
        self.rig.update(self.input, 1/60 )

        self.renderer.render(self.scene, self.camera)

#instantie and run
Test().run()