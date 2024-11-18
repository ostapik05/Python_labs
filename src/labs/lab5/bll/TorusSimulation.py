import os
import pygame
from labs.lab5.dal.InputValues import InputManager
from labs.lab5.ui.RemderShape import Renderer
from labs.lab5.bll.Torus import Torus

class TorusSimulation:
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.clock = pygame.time.Clock()

        self.input_manager = InputManager()
        self.renderer = Renderer(700, 700)
        self.shape = Torus(R1=10, R2=40, K1=100, K2=400)

    def get_user_input(self):
        print("Set torus parameters:")
        R1 = int(input("Enter inner radius (R1): "))
        R2 = int(input("Enter outer radius (R2): "))

        print("Choose base color:")
        print("1 - Red")
        print("2 - Blue")
        print("3 - Yellow")
        color_choice = int(input("Enter your choice (1-3): "))

        if color_choice == 1:
            self.input_manager.hue = 0
        elif color_choice == 2:
            self.input_manager.hue = 0.66
        elif color_choice == 3:
            self.input_manager.hue = 0.17
        else:
            print("Invalid choice, defaulting to Red.")
            self.input_manager.hue = 0

        multicolor_choice = input("Do you want multicolor mode? (yes/no): ").strip().lower()
        self.input_manager.multicolor = multicolor_choice == 'yes'

        self.shape.set_parameters(R1, R2)

        print("Press '2' during simulation to toggle 2D projection mode.")

    def save_image(self, filename="torus_image.png"):
        assets_path = os.path.join(os.getcwd(), 'assets')  # Corrected path to avoid nesting within src/labs/lab5
        os.makedirs(assets_path, exist_ok=True)
        filepath = os.path.join(assets_path, filename)
        pygame.image.save(self.renderer.screen, filepath)
        print(f"Image saved as {filepath}")

    def run(self):
        running = True

        while running:
            self.clock.tick(60)
            event_status = self.input_manager.handle_events()
            if event_status == "SAVE":
                self.save_image()
            elif not event_status:
                running = False

            if not self.input_manager.paused:
                if self.input_manager.show_2d:
                    self.renderer.render_2d_projection(self.shape, self.input_manager)
                else:
                    self.renderer.render_shape(self.shape, self.input_manager)
                pygame.display.update()

        pygame.quit()