import pygame
import os
from game.screen import Screen
from game.draw import Draw
from game.character import Character
from game.loop import Loop

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pygame.init()
    screen = Screen(1920,1080, "game/images/Colosseum_Arena.jpg", "game/images/FoodBrawl.png", "game/images/StartButton.png", pygame)
    draw = Draw(screen, pygame)
    banaani = Character("banaani", "game/images/BananaTransparent.png", "game/images/GunFire.png", 100, 30, 80, 20, screen, pygame)
    omena = Character("omena", "game/images/AppleWithGun.png", "game/images/GunFire.png", 100, 0, 80, 160, screen, pygame)
    game_loop = Loop(60, draw, pygame)
    game_loop.loop(omena, banaani, screen)