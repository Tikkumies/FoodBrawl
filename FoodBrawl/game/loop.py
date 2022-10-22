class Loop:
    def __init__(self, fps, draw, character1, character2, screen, pygame):
        self.pygame = pygame
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.draw = draw
        self.character1 = character1
        self.character2 = character2
        self.screen = screen

    def draw_fight_items(self):
        # Value that right hand side healthbar has to move right after hp loss
        self.character1_hp = (self.screen.width/2 - 100) -((self.character1.hp / self.character1.max_hp) * (self.screen.width/2 -100))
        self.draw.blit(self.screen, self.screen.background, 0, 0)
        self.draw.draw_health_bar(self.character2, self.screen.width - (self.screen.width - 50), 50)
        self.draw.draw_health_bar(self.character1, (self.screen.width / 2 + 50) + self.character1_hp  , 50)
        self.draw.blit(self.screen, self.character2.healthbar_name_text, self.screen.width - (self.screen.width - 50), 100)
        self.draw.blit(self.screen, self.character1.healthbar_name_text, self.screen.width - 170, 100)
        self.draw.blit(self.screen, self.character1.image, 850 , 200)
        self.draw.blit(self.screen, self.character2.image, 50, 400)
        
    def loop(self):
        running = True
        self.clock.tick(self.fps)
        char1_attack_time = self.character1.delay
        char2_attack_time = self.character2.delay
        time = 0
        while running:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:   
                    running = False

            match self.screen.game_screen_selection:
                case "menu":
                    time += 1
                    if time == 1:
                        # Play menu music
                        self.screen.music_menu.play(-1)
                    self.draw.blit(self.screen, self.screen.background, 0, 0)
                    self.draw.blit(self.screen, self.screen.logo, 770, 100)
                    self.draw.draw_rect(self.screen.start_button, self.screen.start_button_image, 770, 500)
                    self.draw.draw_rect(self.screen.exit_button, self.screen.exit_button_image, self.screen.start_button.x, self.screen.start_button.y + self.screen.start_button.h)
                    if self.pygame.mouse.get_pressed()[0] and self.screen.exit_button.collidepoint(self.pygame.mouse.get_pos()):
                        running = False
                    if self.pygame.mouse.get_pressed()[0] and self.screen.start_button.collidepoint(self.pygame.mouse.get_pos()):
                        self.screen.game_screen_selection = "game"
                        self.screen.music_menu.stop()
                        time = 0

                case "game":
                    # Play fight music
                    if time == 1:
                        self.screen.music_fight.play(-1)
                    # Attack delay calculation
                    if char1_attack_time == time - 1:
                        char1_attack_time += self.character1.delay
                    if char2_attack_time == time - 1:
                        char2_attack_time += self.character2.delay
                    # Attack activated
                    if char2_attack_time == time:
                        self.character1.hp_loss(self.character2, self.character1, self.screen)
                    if char1_attack_time == time:
                        self.character2.hp_loss(self.character1, self.character2, self.screen)
                    # Draw fight related stuff
                    self.draw_fight_items()
                    # Attack animations
                    if time == char2_attack_time:
                        self.draw.blit(self.screen, self.character2.image_fire, 390 , 530)
                    if time == char1_attack_time:
                        self.draw.blit(self.screen, self.character1.image_fire, 290 , 470)
                    # Check if characters health is zero or less 
                    if self.character1.hp < 1 or self.character2.hp < 1:
                        self.screen.game_screen_selection = "game over"
                    time += 1

                case "game over":
                    self.draw_fight_items()
                    self.draw.draw_rect(self.screen.new_game_button, self.screen.new_game_image, 770, 500)
                    self.draw.draw_rect(self.screen.menu_button, self.screen.menu_image, self.screen.new_game_button.x, self.screen.new_game_button.y + self.screen.new_game_button.h)
                    # Winner name blitting
                    if self.character1.hp < 1:
                        self.draw.blit(self.screen, self.character2.winner_name_text, 700, self.screen.heigth / 3)
                    elif self.character2.hp < 1:
                        self.draw.blit(self.screen, self.character1.winner_name_text, 670, self.screen.heigth / 3)
                    # Go back to menu
                    if self.pygame.mouse.get_pressed()[0] and self.screen.menu_button.collidepoint(self.pygame.mouse.get_pos()):
                        self.character1.reset_character()
                        self.character2.reset_character()
                        self.screen.game_screen_selection = "menu"
                        self.screen.music_fight.stop()
                        time = 0
                    # Start new game
                    if self.pygame.mouse.get_pressed()[0] and self.screen.new_game_button.collidepoint(self.pygame.mouse.get_pos()):
                        self.character1.reset_character()
                        self.character2.reset_character()
                        self.screen.game_screen_selection = "game"
                        self.screen.music_fight.stop()
                        time = 0

                    char1_attack_time = 0
                    char2_attack_time = 0

            self.pygame.display.update()
            self.pygame.time.wait(100)