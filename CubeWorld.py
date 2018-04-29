#CubeWorld
import sys, pygame, math, time

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
CENTER = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)
FPS = 40
BASIC_FONT_SIZE = 20

ZOOM = 5
THICKNESS = 5

BLACK = (0,0,0)
WHITE = (255,255,255)

class Cube:
    def __init__(self):
        self.points = [(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),
                       (-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]
        self.edges = [(0,1),(1,2),(2,3),(3,0),
                      (4,5),(5,6),(6,7),(7,4),
                      (0,4),(1,5),(2,6),(3,7),]
class Camera:
    def __init__(self):
        self.position = [0,0,5]
        self.rotation = [0,0]
    def update(self, KEYS):
        MOVE=0.1
        if KEYS[pygame.K_w]:
            self.position[2]-=MOVE
        if KEYS[pygame.K_s]:
            self.position[2]+=MOVE
        if KEYS[pygame.K_a]:
            self.position[0]+=MOVE
        if KEYS[pygame.K_d]:
            self.position[0]-=MOVE

def main():
    global DISPLAY, BASIC_FONT,FPS_CLOCK
    
    pygame.init()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("CubeWorld")
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE)
    FPS_CLOCK = pygame.time.Clock()
    
    CUBE = Cube()
    CAMERA = Camera()

    while True:
        DISPLAY.fill(BLACK)
        
        '''
        for x,y,z in CUBE.points:
            x-=CAMERA.position[0]
            y-=CAMERA.position[1]
            z-=CAMERA.position[2]
            scale = WINDOW_HEIGHT/z
            x,y = CENTER[0]+int(x*scale), CENTER[1]+int(y*scale)
            pygame.draw.circle(DISPLAY,WHITE,(x,y),THICKNESS)
        '''
        
        for p0,p1 in CUBE.edges:
            x,y,z = CUBE.points[p0]
            x-=CAMERA.position[0]
            y-=CAMERA.position[1]
            z-=CAMERA.position[2]
            scale = WINDOW_HEIGHT/z
            #print(x,y,z)
            a,b = CENTER[0]+(x*scale), CENTER[1]+(y*scale)
            x,y,z = CUBE.points[p1]
            x-=CAMERA.position[0]
            y-=CAMERA.position[1]
            z-=CAMERA.position[2]
            scale = WINDOW_HEIGHT/z
            #print(x,y,z)
            c,d = CENTER[0]+(x*scale), CENTER[1]+(y*scale)
            print(a,b,c,d)
            pygame.draw.line(DISPLAY,WHITE,(a,b),(c,d),THICKNESS)
        
        pygame.display.update()
        FPS_CLOCK.tick(FPS)
        print("Koniec blyat")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        KEYS = pygame.key.get_pressed()
        CAMERA.update(KEYS)
                
            
    
if __name__ == '__main__':
    main()
