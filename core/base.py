import pygame
import sys
import os

from core.input import Input

# https://stackoverflow.com/questions/15933493/pygame-error-no-available-video-device
# es muy importante tener en cuenta que wsl parece no traer ningún pequete de interefaz gráfica.

# other links mesa & graphics server windows:
# https://www.youtube.com/watch?v=E0pEcv9Ncmc
# https://seanthegeek.net/234/graphical-linux-applications-bash-ubuntu-windows/amp/
# https://gist.github.com/Mluckydwyer/8df7782b1a6a040e5d01305222149f3c

class Base(object):

    def __init__(self):

        # initializa all pygame modules
        # pygame.init()

        os.environ["SDL_VIDEODRIVER"]="x11"
        # os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        # # pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF)
        # pygame.display.set_mode((1,1))

        # width and height of window
        screensize = (640, 480)

        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)

        # indicate rendering options
        displayFlags = pygame.HWSURFACE|pygame.OPENGL|pygame.DOUBLEBUF

        # error just in linux->Ubuntu
        pygame.display.init()

        # initialize buffers to perform antialiasing
        # pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        # pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)

        # use a core OpenGL progile for cros-platform compatibility
        #   requires pygame >= 2.0.0
        # pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK,
        #                                 pygame.GL_CONTEXT_PROFILE_CORE)

        # create and display the window
        self.screen = pygame.display.set_mode(screensize, displayFlags)

        # set the text that appears in title bar of window
        pygame.display.set_caption("Graphics window")

        # determines if main loop is active
        self.running = True

        # manage time-related data and operations
        self.clock = pygame.time.Clock()

        # manage user input
        self.input = Input()

    # implement by extending class
    def initialize(self):
        pass

    # implement by extending class
    def update(self):
        pass

    def run(self):
        
        ## startup ##
        self.initialize()

        ## main loop ##

        while self.running:

            ## process input ##
            self.input.update()

            if self.input.quit:
                self.running = False

            ## update ##
            self.update()

            ## render ##
            pygame.display.flip()

            # pause if necessary to achive 60 FPS
            self.clock.tick(60)

        ## shutdown ##
        pygame.quit()
        sys.exit()
