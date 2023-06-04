from figures.line import Line


class Cube:
    def __init__(self, start_x, start_y, start_z, distance_between_points, color):
        self.lines = self.__init_lines(
            start_x, start_y, start_z, distance_between_points)
        self.distance_between_points = distance_between_points
        self.color = color

    def __init_lines(self, start_x, start_y, start_z, distance_between_points):
        lines = []

        # front
        lines.append(Line(start_x, start_y, start_z, start_x +
                     distance_between_points, start_y, start_z))
        lines.append(Line(start_x + distance_between_points, start_y, start_z, start_x +
                     distance_between_points, start_y + distance_between_points, start_z))
        lines.append(Line(start_x + distance_between_points, start_y + distance_between_points,
                     start_z, start_x, start_y + distance_between_points, start_z))
        lines.append(Line(start_x, start_y + distance_between_points,
                     start_z, start_x, start_y, start_z))

        # back
        lines.append(Line(start_x, start_y, start_z + distance_between_points, start_x +
                     distance_between_points, start_y, start_z + distance_between_points))
        lines.append(Line(start_x + distance_between_points, start_y, start_z + distance_between_points, start_x +
                     distance_between_points, start_y + distance_between_points, start_z + distance_between_points))
        lines.append(Line(start_x + distance_between_points, start_y + distance_between_points, start_z +
                     distance_between_points, start_x, start_y + distance_between_points, start_z + distance_between_points))
        lines.append(Line(start_x, start_y + distance_between_points, start_z +
                     distance_between_points, start_x, start_y, start_z + distance_between_points))

        # sides
        lines.append(Line(start_x, start_y, start_z, start_x,
                     start_y, start_z + distance_between_points))
        lines.append(Line(start_x + distance_between_points, start_y, start_z, start_x +
                     distance_between_points, start_y, start_z + distance_between_points))
        lines.append(Line(start_x + distance_between_points, start_y + distance_between_points, start_z, start_x +
                     distance_between_points, start_y + distance_between_points, start_z + distance_between_points))
        lines.append(Line(start_x, start_y + distance_between_points, start_z, start_x,
                     start_y + distance_between_points, start_z + distance_between_points))

        return lines

    def draw(self, screen, focal_length, screen_width, screen_height):
        for line in self.lines:
            line: Line = line
            line.draw(screen, self.color, focal_length,
                      screen_width, screen_height)
