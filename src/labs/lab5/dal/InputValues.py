import pygame

class InputManager:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.figure_x = 350
        self.figure_y = 350
        self.K2 = 400
        self.hue = 0
        self.multicolor = False
        self.paused = False
        self.show_2d = False

    def handle_events(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        focused = pygame.mouse.get_focused()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                if event.key == pygame.K_p:  # Save image when 'P' is pressed
                    return "SAVE"
                if event.key == pygame.K_2:  # Toggle 2D mode when '2' is pressed
                    self.show_2d = not self.show_2d

        if keys[pygame.K_UP]:
            self.A -= 0.05
        if keys[pygame.K_DOWN]:
            self.A += 0.05
        if keys[pygame.K_LEFT]:
            self.B -= 0.05
        if keys[pygame.K_RIGHT]:
            self.B += 0.05
        if keys[pygame.K_c]:
            self.hue += 0.01
            if self.hue > 1:
                self.hue = 0
        if focused and mouse[0]:
            mouse_motion = pygame.mouse.get_rel()
            self.A -= mouse_motion[0] * 0.005
            self.B -= mouse_motion[1] * 0.005

        return True