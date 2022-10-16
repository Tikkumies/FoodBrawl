class Draw:
    def __init__(self, screen, pygame):
        self.screen = screen
        self.pygame = pygame

    def draw_rect(self, rect, image , x, y):
        rect.x = x
        rect.y = y
        self.screen.screen.blit(image, rect)

    def draw_health_bar(self, character, x, y):
        character.healthbar.x = x
        character.healthbar.y = y
        hp_percentage = character.hp / character.max_hp * 100
        if hp_percentage < 33:
            color = "red"
        elif hp_percentage < 66:
            color = "yellow"
        elif hp_percentage <= 100:
            color = "green"
        self.pygame.draw.rect(self.screen.screen, color, character.healthbar)

    def blit(self, screen, surface_or_image, x, y):
        screen.screen.blit(surface_or_image,(x, y))