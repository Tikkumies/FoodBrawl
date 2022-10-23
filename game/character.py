class Character:
    def __init__ (self, name, image, image_fire, gun_sound, hp, attack, defence, fatness, screen, pygame):
        self.name = name
        self.hp = hp + fatness
        self.max_hp = hp + fatness
        self.attack = attack
        self.defence = defence
        self.fatness = fatness
        self.delay = (attack + defence + fatness)
        self.delay_at_start = self.delay

        self.image = pygame.image.load(image)
        self.char = self.image.get_rect()
        
        self.image_fire = pygame.image.load(image_fire).convert_alpha()
        self.healthbar = pygame.Rect(50, 50, screen.width/2 - 100, 50)
        self.healthbar_name_font = pygame.font.Font('freesansbold.ttf', 32)
        self.healthbar_name_text = self.healthbar_name_font.render(name, False, "red" )
        self.winner_font = pygame.font.Font('freesansbold.ttf', 72)
        self.winner_name_text = self.winner_font.render(name.upper() + " WINS!", False, "red", (10,19,22) )
        self.gun_sound = pygame.mixer.Sound(gun_sound)
    
    def reset_character(self):
        self.hp = self.max_hp
        self.delay = self.delay_at_start
        
    def hp_loss(self, attacker, defender, screen):
        defender.hp -= attacker.attack
        defender.healthbar.width = (defender.hp / defender.max_hp) * (screen.width/2 -100)
        