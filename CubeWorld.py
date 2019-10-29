# CubeWorld
import sys, pygame, math, time

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
CENTER = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
FPS = 10
BASIC_FONT_SIZE = 20

ZOOM = 5
THICKNESS = 5

END_LIMIT_TOP = 4e17
END_LIMIT_BOTTOM = -4e17
START_LIMIT_TOP = 4.5e+17
START_LIMIT_BOTTOM = -4.5e+17

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Cube:
    def __init__(self, x, y, z):
        self.points = [(-1 + 2 * x, -1 + 2 * y, -1 + 2 * z), (1 + 2 * x, -1 + 2 * y, -1 + 2 * z),
                       (1 + 2 * x, 1 + 2 * y, -1 + 2 * z), (-1 + 2 * x, 1 + 2 * y, -1 + 2 * z),
                       (-1 + 2 * x, -1 + 2 * y, 1 + 2 * z), (1 + 2 * x, -1 + 2 * y, 1 + 2 * z),
                       (1 + 2 * x, 1 + 2 * y, 1 + 2 * z), (-1 + 2 * x, 1 + 2 * y, 1 + 2 * z)]
        self.edges = [(0, 1), (1, 2), (2, 3), (3, 0),
                      (4, 5), (5, 6), (6, 7), (7, 4),
                      (0, 4), (1, 5), (2, 6), (3, 7)]


class Camera:
    def __init__(self):
        self.position = [0, 0, 5]
        self.rotation = [0, 0]

    def update(self, KEYS):
        MOVE = 0.1
        if KEYS[pygame.K_w]:
            self.position[2] -= MOVE
        if KEYS[pygame.K_s]:
            self.position[2] += MOVE
        if KEYS[pygame.K_a]:
            self.position[0] += MOVE
        if KEYS[pygame.K_d]:
            self.position[0] -= MOVE
        if KEYS[pygame.K_q]:
            self.position[1] += MOVE
        if KEYS[pygame.K_e]:
            self.position[1] -= MOVE


def main():
    global DISPLAY, BASIC_FONT, FPS_CLOCK

    pygame.init()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("CubeWorld")
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE)
    FPS_CLOCK = pygame.time.Clock()

    Cubes = [Cube(0, 0, 0)]

    CAMERA = Camera()

    while True:
        DISPLAY.fill(BLACK)
        for CUBE in Cubes:
            for x, y, z in CUBE.points:
                x -= CAMERA.position[0]
                y -= CAMERA.position[1]
                z -= CAMERA.position[2]
                scale = WINDOW_HEIGHT / z
                x, y = CENTER[0] + int(x * scale), CENTER[1] + int(y * scale)
                # pygame.draw.circle(DISPLAY,WHITE,(x,y),THICKNESS)

            for p0, p1 in CUBE.edges:
                x, y, z = CUBE.points[p0]
                x -= CAMERA.position[0]
                y -= CAMERA.position[1]
                if (CAMERA.position[2] - z) != 0:
                    z -= CAMERA.position[2]
                scale = WINDOW_HEIGHT / z
                # print(x,y,z)
                a, b = CENTER[0] + (x * scale), CENTER[1] + (y * scale)
                x, y, z = CUBE.points[p1]
                x -= CAMERA.position[0]
                y -= CAMERA.position[1]
                if (CAMERA.position[2] - z) != 0:
                    z -= CAMERA.position[2]
                scale = WINDOW_HEIGHT / z
                # print(x,y,z)
                c, d = CENTER[0] + (x * scale), CENTER[1] + (y * scale)
                # print(a,b,c,d)
                try:
                    if START_LIMIT_BOTTOM < a < START_LIMIT_TOP:
                        pygame.draw.line(DISPLAY, WHITE, (a, b), (c, d), THICKNESS)
                except:
                    print(a, b, c, d)

        pygame.display.update()
        FPS_CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        KEYS = pygame.key.get_pressed()
        CAMERA.update(KEYS)


if __name__ == '__main__':
    main()
