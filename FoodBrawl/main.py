import pygame
import os
from game.screen import Screen
from game.draw import Draw
from game.character import Character
from game.loop import Loop
from scraping.scrape_food_stats import get_food_stats

if __name__ == "__main__":
    # get food stats
    omena_id = "28942"
    banaani_id = "11049"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    url = "https://fineli.fi/fineli/api/v1/foods/"
    food_stats = get_food_stats(headers, url)
    # Apple stats
    omena_energy = food_stats.get_stat(omena_id, "energy")
    omena_carbs = food_stats.get_stat(omena_id, "carbs")
    omena_protein = food_stats.get_stat(omena_id, "protein")
    omena_fat = food_stats.get_stat(omena_id, "fat")
    # Banana stats
    banaani_energy = food_stats.get_stat(banaani_id, "energy")
    banaani_carbs = food_stats.get_stat(banaani_id, "carbs")
    banaani_protein = food_stats.get_stat(banaani_id, "protein")
    banaani_fat = food_stats.get_stat(banaani_id, "fat")
    # PyGame related stuff
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    screen = Screen(1920,1080, "game/images/Colosseum_Arena.jpg", "game/images/FoodBrawl.png", "game/images/Start.PNG", "game/images/Quit.PNG", "game/images/NewGame.PNG", "game/images/Menu.PNG", "game/sounds/WhosAfreidOf.mp3", "game/sounds/CrimsonSunset.mp3", pygame)
    draw = Draw(screen, pygame)
    banaani = Character("Banaani", "game/images/BananaTransparent.png", "game/images/GunFire.png", "game/sounds/GunShootSoundEffect.mp3",banaani_energy, banaani_carbs, banaani_protein, banaani_fat, screen, pygame)
    omena = Character("Omena", "game/images/AppleWithGun.png", "game/images/Laser.png", "game/sounds/LaserGunSoundEffect.mp3", omena_energy, omena_carbs, omena_protein, omena_fat, screen, pygame)
    game_loop = Loop(60, draw, omena, banaani, screen, pygame)
    game_loop.loop()
