class Loop:
    def __init__(self, fps, draw, character1, character2, screen, pygame):
        self.pygame = pygame
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.draw = draw
        self.character1 = character1
        self.character2 = character2
        self.screen = screen
        self.time = 0

    def draw_fight_start(self):
            if self.time < 24:
                self.draw.draw_rect(self.screen.final_round_rect, self.screen.final_round_image, self.screen.width / 2 - self.screen.final_round_rect.width / 2, 300)
            if self.time > 25 and self.time < 35:
                self.draw.draw_rect(self.screen.fight_rect, self.screen.fight_image, self.screen.width / 2 - self.screen.fight_rect.width / 2, 300)

    def sounds_fight_start(self):
        if self.time == 1:
            self.screen.sound_fight.play()

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

    def firing_effects(self):
        # Attack animations and sounds
        if self.time == self.char2_attack_time:
            self.draw.blit(self.screen, self.character2.image_fire, 390 , 530)
            self.character2.gun_sound.play()
            
        if self.time == self.char1_attack_time:
            self.draw.blit(self.screen, self.character1.image_fire, 290 , 470)
            self.character1.gun_sound.play()

    def health_checking(self):
        # Check if characters health is zero or less 
        if self.character1.hp < 1 or self.character2.hp < 1:
            self.screen.game_screen_selection = "game over"

    def attack_calculations(self):
        # Attack delay updater
        if self.char1_attack_time == self.time - 1:
            self.char1_attack_time += self.character1.delay
        if self.char2_attack_time == self.time - 1:
            self.char2_attack_time += self.character2.delay

    def health_width_change(self):
        # health bar width change after hp loss
        if self.char2_attack_time == self.time:
            self.character1.hp_loss(self.character2, self.character1, self.screen)
        if self.char1_attack_time == self.time:
            self.character2.hp_loss(self.character1, self.character2, self.screen)

    def draw_menu_items(self):
        self.draw.blit(self.screen, self.screen.background, 0, 0)
        self.draw.blit(self.screen, self.screen.logo, 770, 100)
        self.draw.draw_rect(self.screen.start_button, self.screen.start_button_image, 770, 500)
        self.draw.draw_rect(self.screen.exit_button, self.screen.exit_button_image, self.screen.start_button.x, self.screen.start_button.y + self.screen.start_button.h)  

    def mouse_press_events_menu(self):
        if self.pygame.mouse.get_pressed()[0] and self.screen.exit_button.collidepoint(self.pygame.mouse.get_pos()):
            self.running = False
        if self.pygame.mouse.get_pressed()[0] and self.screen.start_button.collidepoint(self.pygame.mouse.get_pos()):
            self.screen.game_screen_selection = "fight start"
            self.screen.music_menu.stop()
            self.time = 0

    def mouse_press_events_game_over(self):
        # Go back to menu
        if self.pygame.mouse.get_pressed()[0] and self.screen.menu_button.collidepoint(self.pygame.mouse.get_pos()):
            self.character1.reset_character()
            self.character2.reset_character()
            self.screen.game_screen_selection = "menu"
            self.screen.music_fight.stop()
            self.time = 0
        # Start new game
        if self.pygame.mouse.get_pressed()[0] and self.screen.new_game_button.collidepoint(self.pygame.mouse.get_pos()):
            self.character1.reset_character()
            self.character2.reset_character()
            self.screen.game_screen_selection = "fight start"
            self.screen.music_fight.stop()
            self.time = 0

    def draw_game_over_items(self):
        self.draw.draw_rect(self.screen.new_game_button, self.screen.new_game_image, 770, 500)
        self.draw.draw_rect(self.screen.menu_button, self.screen.menu_image, self.screen.new_game_button.x, self.screen.new_game_button.y + self.screen.new_game_button.h)
        # Winner name blitting
        if self.character1.hp < 1:
            self.draw.blit(self.screen, self.character2.winner_name_text, 700, self.screen.heigth / 3)
        elif self.character2.hp < 1:
            self.draw.blit(self.screen, self.character1.winner_name_text, 670, self.screen.heigth / 3)
    
    # Main game loop
    def loop(self):
        self.running = True
        self.clock.tick(self.fps)
        self.char1_attack_time = self.character1.delay
        self.char2_attack_time = self.character2.delay
        while self.running:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:   
                    self.running = False

            match self.screen.game_screen_selection:
                case "menu":
                    self.time += 1
                    if self.time == 1:
                        # Play menu music
                        self.screen.music_menu.play(-1)
                    self.draw_menu_items()
                    # Check if some button is pressed
                    self.mouse_press_events_menu()

                case "fight start":
                    self.sounds_fight_start()
                    self.draw_fight_items()
                    self.health_width_change()
                    self.draw_fight_start()
                    self.time += 1
                    if self.time > 40:
                        self.screen.game_screen_selection = "game"
                        self.time = 0
         
                case "game":
                    # Play fight music
                    if self.time == 1:
                        self.screen.music_fight.play(-1)
                        # Attack delay calculation
                    self.attack_calculations()
                    self.health_width_change()
                    # Draw fight related stuff
                    self.draw_fight_items()
                    self.firing_effects()
                    # Check character health
                    self.health_checking()
                    self.time += 1

                case "game over":
                    self.draw_fight_items()
                    self.draw_game_over_items()
                    self.mouse_press_events_game_over()
                    self.char1_attack_time = 0
                    self.char2_attack_time = 0

            self.pygame.display.update()
            self.pygame.time.wait(100)