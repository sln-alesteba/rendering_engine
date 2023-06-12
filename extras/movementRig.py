import math

from core.object3D import Object3D

class MovementRig(Object3D):

    """
    Add moving forwards and backwards, left and right, up and down (all local translations),
    as well as turning left and right, and looking up and down
    """
    
    def __init__(self, units_per_second=1, degrees_per_second=60):

        # Initialize base Object3D.
        # Controls movement and turn left/right.
        super().__init__()
        # Initialize attached Object3D; controls look up/down
        self._look_attachment = Object3D()
        self.children_list = [self._look_attachment]
        self._look_attachment.parent = self
        # Control rate of movement
        self._units_per_second = units_per_second
        self._degrees_per_second = degrees_per_second

        # Customizable key mappings.
        # Defaults: W, A, S, D, R, F (move), Q, E (turn), T, G (look)
        self.KEY_MOVE_FORWARDS = "w"
        self.KEY_MOVE_BACKWARDS = "s"
        self.KEY_MOVE_LEFT = "a"
        self.KEY_MOVE_RIGHT = "d"
        self.KEY_MOVE_UP = "r"
        self.KEY_MOVE_DOWN = "f"
        self.KEY_TURN_LEFT = "q"
        self.KEY_TURN_RIGHT = "e"
        self.KEY_LOOK_UP = "t"
        self.KEY_LOOK_DOWN = "g"

    # Adding and removing objects applies to look attachment.
    # Override functions from the Object3D class.
    def add(self, child):
        self._look_attachment.add(child)

    def remove(self, child):
        self._look_attachment.remove(child)

    def update(self, input_object, delta_time):

        move_amount = self._units_per_second * delta_time
        rotate_amount = self._degrees_per_second * (math.pi / 180) * delta_time

        # translation
        if input_object.isKeyPressed(self.KEY_MOVE_FORWARDS):
            self.translate(0, 0, -move_amount)
        if input_object.isKeyPressed(self.KEY_MOVE_BACKWARDS):
            self.translate(0, 0, move_amount)
        if input_object.isKeyPressed(self.KEY_MOVE_LEFT):
            self.translate(-move_amount, 0, 0)
        if input_object.isKeyPressed(self.KEY_MOVE_RIGHT):
            self.translate(move_amount, 0, 0)
        if input_object.isKeyPressed(self.KEY_MOVE_UP):
            self.translate(0, move_amount, 0)
        if input_object.isKeyPressed(self.KEY_MOVE_DOWN):
            self.translate(0, -move_amount, 0)

        # rotation:
        if input_object.isKeyPressed(self.KEY_TURN_RIGHT):
            self.rotateY(-rotate_amount)
        if input_object.isKeyPressed(self.KEY_TURN_LEFT):
            self.rotateY(rotate_amount)
        if input_object.isKeyPressed(self.KEY_LOOK_UP):
            self._look_attachment.rotateX(rotate_amount)
        if input_object.isKeyPressed(self.KEY_LOOK_DOWN):
            self._look_attachment.rotateX(-rotate_amount)