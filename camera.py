from math import sin, cos
from figures.cube import Cube


class Camera:
    def __init__(self, cubes) -> None:
        self.cubes = cubes
        self.move_step = 4
        self.rotate_step = 0.1
        self.scaling_step = 50

        self.focal_length = 800

    def move_forward(self):
        for cube in self.cubes:
            for line in cube.lines:
                line.z1 -= self.move_step
                line.z2 -= self.move_step

    def move_backward(self):
        for cube in self.cubes:
            for line in cube.lines:
                line.z1 += self.move_step
                line.z2 += self.move_step

    def move_left(self):
        for cube in self.cubes:
            for line in cube.lines:
                line.x1 += self.move_step
                line.x2 += self.move_step

    def move_right(self):
        for cube in self.cubes:
            for line in cube.lines:
                line.x1 -= self.move_step
                line.x2 -= self.move_step
        
    def move_up(self):
        for cube in self.cubes:
            for line in cube.lines:
                line.y1 -= self.move_step
                line.y2 -= self.move_step

    def move_down(self):
        for cube in self.cubes:
            for line in cube.lines:
                line.y1 += self.move_step
                line.y2 += self.move_step
        
    def rotate_x(self, sign):
        angle = sign * self.rotate_step
        for cube in self.cubes:
            for line in cube.lines:
                print(line.x1, line.x2)
                line.y1 = line.y1 * cos(angle) - line.z1 * sin(angle)
                line.z1 = line.y1 * sin(angle) + line.z1 * cos(angle)
                line.y2 = line.y2 * cos(angle) - line.z2 * sin(angle)
                line.z2 = line.y2 * sin(angle) + line.z2 * cos(angle)

    def rotate_y(self, sign):
        angle = sign * self.rotate_step
        for cube in self.cubes:
            for line in cube.lines:
                line.x1 = line.x1 * cos(angle) + line.z1 * sin(angle)
                line.z1 = -line.x1 * sin(angle) + line.z1 * cos(angle)
                line.x2 = line.x2 * cos(angle) + line.z2 * sin(angle)
                line.z2 = -line.x2 * sin(angle) + line.z2 * cos(angle)

    def rotate_z(self, sign):
        angle = sign * self.rotate_step
        for cube in self.cubes:
            for line in cube.lines:
                line.x1 = line.x1 * cos(angle) - line.y1 * sin(angle)
                line.y1 = line.x1 * sin(angle) + line.y1 * cos(angle)
                line.x2 = line.x2 * cos(angle) - line.y2 * sin(angle)
                line.y2 = line.x2 * sin(angle) + line.y2 * cos(angle)

    def scale(self, sign):
        if self.focal_length + sign * self.scaling_step > 0:
            self.focal_length += sign * self.scaling_step

    def draw(self, screen, screen_width, screen_height):
        for cube in self.cubes:
            cube: Cube = cube
            # print(self.focal_length / 600.0)
            cube.draw(screen, self.focal_length, screen_width, screen_height)
