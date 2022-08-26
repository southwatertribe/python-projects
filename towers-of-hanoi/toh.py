import pygame
import sys
import time
from pygame.locals import*
import queue
pygame.init()

HEIGHT = 600
WIDTH = 1400
ground = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

disks = 10

steps = 0
source = []
temp = []
dest = []

numDisks = disks


class BlockSprite:
    index = 0
    rect = pygame.Rect(0, 0, 0, 0)
    rect_target = pygame.Rect(0, 0, 0, 0)

    def __init__(self, index, rect):
        self.index = index
        self.rect = rect

    def get_index(self):
        return self.index

    def get_rect(self):
        return self.rect

    def set_rect(self, rect):
        self.rect = rect

    def set_target_rect(self, rect_target):
        self.rect_target = rect_target

    def lerp_rect(self):
        self.rect = self.rect_target

    def on_tick(self):
        self.lerp_rect()


for i in range(disks):
    source.append(BlockSprite(numDisks, pygame.Rect(
        (WIDTH / 4) - (i * 10), ground - (20 * i) - 40, (i * 10) * 2, 20)))
    numDisks -= 1


def redraw_screen():
    screen.fill(WHITE)
    # pegs-
    pygame.draw.rect(screen, BLACK, ((WIDTH/4) - 5, 200, 10, 380))
    pygame.draw.rect(screen, BLACK, ((WIDTH/2) - 5, 200, 10, 380))
    pygame.draw.rect(screen, BLACK, (WIDTH - (WIDTH/4) - 5, 200, 10, 380))
    # redraws disks according to given peg array
    for i, val in enumerate(source):
        pygame.draw.rect(screen, RED, val.get_rect())
    for i, val in enumerate(temp):
        pygame.draw.rect(screen, RED, val.get_rect())
    for i, val in enumerate(dest):
        pygame.draw.rect(screen, RED, val.get_rect())
    pygame.display.update()


def update_target_rect():
    # redraws disks according to given peg array
    for i, val in enumerate(source):
        val.set_target_rect(pygame.Rect((WIDTH / 4) - (val.get_index() * 10),
                            ground - (20 * i) - 40, (val.get_index() * 10) * 2, 20))
    for i, val in enumerate(temp):
        val.set_target_rect(pygame.Rect((WIDTH / 2) - (val.get_index() * 10),
                            ground - (20 * i) - 40, (val.get_index() * 10) * 2, 20))
    for i, val in enumerate(dest):
        val.set_target_rect(pygame.Rect(WIDTH - (WIDTH / 4) - (val.get_index() * 10),
                            ground - (20 * i) - 40, (val.get_index() * 10) * 2, 20))


def on_tick():
    # redraws disks according to given peg array
    for i, val in enumerate(source):
        val.on_tick()
    for i, val in enumerate(temp):
        val.on_tick()
    for i, val in enumerate(dest):
        val.on_tick()
    redraw_screen()


# redraw_screen()
update_target_rect()

# recursive algo


def movestack(n, a, b, c):
    # breaking case
    if n == 1:
        action_queue.put((a, c))
        return
    movestack(n-1, a, c, b)
    movestack(1, a, b, c)
    movestack(n-1, b, a, c)


# construct an infinite instruction set and fill in the game conduct
action_queue = queue.Queue()
movestack(disks, source, dest, temp)

clock = pygame.time.Clock()
frame_counter = 0
# recursion
while not action_queue.empty():
    clock.tick(60)
    frame_counter += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    on_tick()
    if frame_counter >= 60:
        frame_counter = 0
        action = action_queue.get()
        action[1].append(action[0].pop())
        update_target_rect()
        action_queue.task_done()
