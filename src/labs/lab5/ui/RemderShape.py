import pygame
import colorsys


class Utils:
    @staticmethod
    def hsv2rgb(h, s, v):
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

class Renderer:
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont('Arial', 20, bold=True)
        self.pixel_width = 20
        self.pixel_height = 20

    def draw_text(self, char, x, y, color):
        text = self.font.render(str(char), True, color)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)

    def render_shape(self, shape, input_manager):
        self.screen.fill((0, 0, 0))

        theta_spacing = 10
        phi_spacing = 3

        output = [' '] * ((self.WIDTH // self.pixel_width) * (self.HEIGHT // self.pixel_height))
        zbuffer = [0] * len(output)

        for theta in range(0, 628, theta_spacing):
            for phi in range(0, 628, phi_spacing):
                coords = shape.calculate_coordinates(input_manager.A, input_manager.B, theta, phi)

                if coords is None:
                    continue

                xp, yp, ooz = coords

                xp = int(input_manager.figure_x / self.pixel_width + xp)
                yp = int(input_manager.figure_y / self.pixel_height - yp)

                if 0 <= xp < self.WIDTH // self.pixel_width and 0 <= yp < self.HEIGHT // self.pixel_height:
                    position = xp + (self.WIDTH // self.pixel_width) * yp

                    if ooz > zbuffer[position]:
                        zbuffer[position] = ooz
                        hue = (theta / 628) % 1 if input_manager.multicolor else input_manager.hue
                        luminance = max(0, min(1, ooz * 8))
                        luminance_index = int(luminance * 11)
                        output[position] = (".,-~:;=!*#$@"[luminance_index], hue)

        for y in range(self.HEIGHT // self.pixel_height):
            for x in range(self.WIDTH // self.pixel_width):
                char, hue = output[x + y * (self.WIDTH // self.pixel_width)] if isinstance(output[x + y * (self.WIDTH // self.pixel_width)], tuple) else (' ', input_manager.hue)
                self.draw_text(char, x * self.pixel_width, y * self.pixel_height, Utils.hsv2rgb(hue, 1, 1))

    def render_2d_projection(self, shape, input_manager):
        self.screen.fill((0, 0, 0))
        color = Utils.hsv2rgb(input_manager.hue, 1, 1)

        for theta in range(0, 628, 10):
            for phi in range(0, 628, 10):
                coords = shape.calculate_coordinates(0, 0, theta, phi)
                if coords is None:
                    continue

                xp, yp, _ = coords
                xp = int(input_manager.figure_x / self.pixel_width + xp)
                yp = int(input_manager.figure_y / self.pixel_height - yp)

                if 0 <= xp < self.WIDTH // self.pixel_width and 0 <= yp < self.HEIGHT // self.pixel_height:
                    pygame.draw.circle(self.screen, color, (xp * self.pixel_width, yp * self.pixel_height), 2)