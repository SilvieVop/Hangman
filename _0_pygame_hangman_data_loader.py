# TODO list - vytvořit další soubor s listem, kde budou zvířata - více zvířat :D
#  + vytvoření dalších skupin a rozšíření hry o vybrání hádané skupiny jako třeba zvíčřata, ovoce/zelenina, země, atd.
# TODO list - přidej zvuky
# TODO list -

import os

import pygame

# Inicializace hry
pygame.init()

# Velikost okna
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH)) # tohle je vloženo jako tuple
pygame.display.set_caption("Hangman with animals")

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY43 = (110, 110, 110)

# Načtení obrázků
script_dir = os.path.dirname(__file__)
image_folder = os.path.join(script_dir, "pictures")

background_image = pygame.image.load(os.path.join(image_folder, "welcome.png"))
menu_image = pygame.image.load(os.path.join(image_folder, "menu.png"))

# Font pro textový výstup
font = pygame.font.Font(None, 24)

# Proměnná pro aktuální stav hry
game_state = "welcome"

# Hlavní smyčka hry
running = True

while running: # všecchny kliknutí se nazývají event (klik nahoru, dolu, pohyb myši,atd)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:  # Přidá kontrola quit a escape
                running = False
            elif event.key == pygame.K_SPACE:
                if game_state == "welcome":
                    game_state = "menu"
                elif game_state == "menu":
                    game_state = "welcome"

    if game_state == "welcome": # úvodní welcome okno
        screen.blit(background_image, (0, 0))
        terminal_height = 100  # Výška terminálu
        pygame.draw.rect(screen, BLACK, (0, WINDOW_HEIGHT - terminal_height, WINDOW_WIDTH, terminal_height))
        text_surface = font.render("Press SPACE to switch between Welcome and Menu or Q for Quit.. ", True, WHITE)
        screen.blit(text_surface, (20, WINDOW_HEIGHT - terminal_height - 30))


    elif game_state == "menu":  # toto se má vykreslit po stisknutí mezerníku
        screen.blit(menu_image, (0, 0))
        #terminal_height = 130  # Výška terminálu
        #pygame.draw.rect(screen, BLACK, (0, WINDOW_HEIGHT - terminal_height, WINDOW_WIDTH, terminal_height))
        text_surface = font.render("Select category, which you wanna to guess...  ", True, BLACK)
        screen.blit(text_surface, (20, WINDOW_HEIGHT - terminal_height - 400))

        # TODO List - Zde bych mohla vykreslit další prvky menu - obdelníčky s výběrem hádané kategorie
        # Takze nejdriv obdelnicky
        category_rect1 = pygame.Rect(100, 150, 150, 50)
        category_rect2 = pygame.Rect(100, 250, 150, 50)
        category_rect3 = pygame.Rect(100, 350, 150, 50)

        pygame.draw.rect(screen,GREY43,category_rect1)
        pygame.draw.rect(screen,GREY43,category_rect2)
        pygame.draw.rect(screen,GREY43,category_rect3)

        # Text v obdelníčcích.. tak ale ted už budeš muset vytvořit další soubor jako knihovnu s listy..
        font = pygame.font.Font(None,24)

        text1 = font.render("Animals",True,WHITE)
        text2 = font.render("Fruit/Vegetable",True,WHITE)
        text3 = font.render("European states",True,WHITE)

        screen.blit(text1,(category_rect1.x + 10,category_rect1.y + 15))
        screen.blit(text2,(category_rect2.x + 10,category_rect2.y + 15))
        screen.blit(text3,(category_rect3.x + 10,category_rect3.y + 15))


    pygame.display.update()

# Ukončení
pygame.quit()
