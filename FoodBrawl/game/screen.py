class Screen:
    def __init__(self, width, heigth, background, logo, start_image, exit_image, new_game_image, menu_image, final_round_image, fight_image, music_menu, music_fight, sound_start_fight, pygame):
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

        self.final_round_image = pygame.image.load(final_round_image)
        self.final_round_rect = self.final_round_image.get_rect()

        self.fight_image = pygame.image.load(fight_image)
        self.fight_rect = self.fight_image.get_rect()

        self.music_menu = pygame.mixer.Sound(music_menu)
        
        self.music_fight = pygame.mixer.Sound(music_fight)

        self.sound_fight = pygame.mixer.Sound(sound_start_fight)

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

