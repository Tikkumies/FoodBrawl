class Loop:
    def __init__(self, fps, draw, pygame):
        self.pygame = pygame
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.draw = draw
        
    def loop(self, character1, character2, screen):
        running = True
        self.clock.tick(self.fps)
        char1_attack_time = character1.delay
        char2_attack_time = character2.delay
        time = 0
        while running:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    running = False

            match screen.game_screen_selection:
                case "menu":
                    self.draw.blit(screen, screen.background, 0, 0)
                    self.draw.blit(screen, screen.logo, 770, 100)
                    self.draw.draw_rect(screen.start_button, screen.start_button_image, 710, 600)
                    if self.pygame.mouse.get_pressed()[0] and screen.start_button.collidepoint(self.pygame.mouse.get_pos()):
                        screen.game_screen_selection = "game"

                case "game":
                    # Attack delay calculation
                    if char1_attack_time == time - 1:
                        char1_attack_time += character1.delay
                    if char2_attack_time == time - 1:
                        char2_attack_time += character2.delay
                    # Attack activated
                    if char2_attack_time == time:
                        character1.hp_loss(character2, character1, screen)
                    if char1_attack_time == time:
                        character2.hp_loss(character1, character2, screen)
                    # Value that right hand side healthbar has to move right after hp loss
                    character1_hp = (screen.width/2 - 100) -((character1.hp / character1.max_hp) * (screen.width/2 -100))
                    
                    self.draw.blit(screen, screen.background, 0, 0)
                    self.draw.draw_health_bar(character2, screen.width - (screen.width - 50), 50)
                    self.draw.draw_health_bar(character1, (screen.width / 2 + 50) + character1_hp , 50)
                    self.draw.blit(screen, character2.healthbar_name_text, screen.width - (screen.width - 50), 100)
                    self.draw.blit(screen, character1.healthbar_name_text, screen.width - 170, 100)
                    self.draw.blit(screen, character1.image, 850 , 200)
                    self.draw.blit(screen, character2.image, 50, 400)
                    time += 1
                    # Check if characters health is zero or less 
                    if character1.hp < 1 or character2.hp < 1:
                        screen.game_screen_selection = "game over"

                case "game over":
                    self.draw.blit(screen, screen.background, 0, 0)
                    self.draw.blit(screen, character1.image, 850 , 200)
                    self.draw.blit(screen, character2.image, 50, 400)
                    self.draw.draw_health_bar(character2, screen.width - (screen.width - 50), 50)
                    self.draw.draw_health_bar(character1, (screen.width / 2 + 50) + character1_hp , 50)
                    if character1.hp < 1:
                        self.draw.blit(screen, character2.winner_name_text, 600, screen.heigth / 3)
                    elif character2.hp < 1:
                        self.draw.blit(screen, character1.winner_name_text, 600, screen.height / 3)

            self.pygame.display.update()
            self.pygame.time.wait(100)