import pygame
import numpy as np


class Line:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1, self.y1, self.z1 = x1, y1, z1
        self.x2, self.y2, self.z2 = x2, y2, z2

    def project_3d_to_2d(self, focal_length):
        x1, x2, y1, y2, z1, z2 = 0.0, 0.0, 0.0, 0.0, self.z1, self.z2

        if (self.z1 <= 0):
            z1 = 0.0001
        if (self.z2 <= 0):
            z2 = 0.0001

        # projection
        coefficient1 = np.float64(focal_length) / np.float64(z1)
        coefficient2 = np.float64(focal_length) / np.float64(z2)

        x1 = np.float64(self.x1) * coefficient1
        y1 = np.float64(self.y1) * coefficient1
        x2 = np.float64(self.x2) * coefficient2
        y2 = np.float64(self.y2) * coefficient2

        return (x1, y1, x2, y2)

    def draw(self, screen, colour, focal_length, screen_width, screen_height):
        x_middle = np.float64(screen_width) / 2.0
        y_middle = np.float64(screen_height) / 2.0

        line_projected_to_2d = self.project_3d_to_2d(focal_length)
        pygame.draw.line(screen,
                         colour,
                         (line_projected_to_2d[0] + x_middle,
                          -line_projected_to_2d[1] + y_middle),
                         (line_projected_to_2d[2] + x_middle, -line_projected_to_2d[3] + y_middle))
