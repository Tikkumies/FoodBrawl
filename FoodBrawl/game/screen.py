class Screen:
    def __init__(self, width, heigth, background, logo, start_image, exit_image, new_game_image, menu_image, pygame):
        self.background = pygame.image.load(background)
        self.logo = pygame.image.load(logo)
        
        self.start_button_image = pygame.image.load(start_image)
        self.start_button = self.start_button_image.get_rect()

        self.exit_button_image = pygame.image.load(exit_image)
        self.exit_button = self.start_button_image.get_rect()

        self.new_game_image = pygame.image.load(new_game_image)
        self.new_game_button = self.new_game_image.get_rect()

        self.menu_image = pygame.image.load(menu_image)
        self.menu_button = self.menu_image.get_rect()

        self.width = width
        self.heigth = heigth
        self.screen = pygame.display.set_mode((self.width,self.heigth))
        pygame.display.set_caption("Food Brawl")
        self.game_screen_selection = "menu"

if __name__ == "__main":
    import pygame
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    screen = Screen(1920,1080, "images/Colosseum_Arena.jpg", "images/FoodBrawl.png", "images/StartButton.png", pygame)
    print(screen.screen)

