import pygame
from math import *
from figures.cube import Cube
from camera import Camera
import keyboard_input_handler

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# screen config
(WIDTH, HEIGHT) = (800, 800)
SCREEN_CAPTION = "Camera Simulator"

pygame.init()

# set screen config
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(SCREEN_CAPTION)

# init cubes
cubes = [
    Cube(7, -3, 30, 5, WHITE),
    Cube(5, -3, 40, 5, GREEN),
    Cube(-7, -3, 30, 5, BLUE),
    Cube(-6, -3, 40, 5, RED),
]
camera = Camera(cubes)

is_running = True
clock = pygame.time.Clock()

while is_running:
    for event in pygame.event.get():
        is_running = keyboard_input_handler.handle_keyboard_input(camera, event)

    camera.draw(screen, WIDTH, HEIGHT)
    pygame.display.update()
    screen.fill(BLACK)
    clock.tick(60)
