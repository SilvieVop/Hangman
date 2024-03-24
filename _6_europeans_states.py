import os
import pygame
import random
from _3_list_of_categories import categories

pink = (242, 49, 235)

class European_states:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Hangman - European_states")
        self.clock = pygame.time.Clock()

        self.categories = ["European_states"]
        self.word = random.choice(categories["European_states"]).upper()  # Získá náhodné slovo ze seznamu pro kategorii "European_states"
        self.guessed_letters = set()  # Uchovává hádaná písmena
        self.lives = 6 # počet životů

        self.font = pygame.font.Font(None, 36)

        # Generování podrtržítek - zde se vytvoří stejně dlouhý řetězec podtržítek jako slovo
        self.hidden_word = "_" * len(self.word)

      # Seznam s názvy souborů obrázků hangmana
        self.hangman_images = ["hangman_1.png", "hangman_2.png", "hangman_3.png", "hangman_4.png", "hangman_5.png", "hangman_6.png"]
        self.current_hangman_index = 0  # Index aktuálně zobrazeného obrázku hangmana

    def draw(self):
        self.screen.fill(pygame.Color('white'))  # Vyplní okno bílou barvou

        # Načtení obrázku se zvířaty
        script_dir = os.path.dirname(__file__)
        image_folder = os.path.join(script_dir, "pictures")
        background_image = pygame.image.load(os.path.join(image_folder, "european_states.png"))

        # Získání rozměrů okna
        window_width, window_height = self.screen.get_size()

        # Umístění obrázku backgroundve spodní části okna
        self.screen.blit(background_image, ((window_width - 800) // 2, window_height - 250))

        # Načtení obrázku hangmana
        hangman_image = pygame.image.load(os.path.join(image_folder,self.hangman_images[self.current_hangman_index]))

        # Umístění obrázku hangman v horní části okna
        self.screen.blit(hangman_image,((window_width - 600) // 2,window_height - 650))

        # Vykreslení podržítek místo hádaného písmene
        for i, letter in enumerate(self.hidden_word):
            underline = self.font.render(letter, True, pygame.Color(pink))
            self.screen.blit(underline, (100 + i * 50, self.screen.get_height() // 1.85))

        # Vykreslení hádaných písmen ve třetí čtvrtině horní části obrazovky s modrou barvou
        for i, letter in enumerate(self.word):
            if letter.upper() in self.guessed_letters:
                text = self.font.render(letter, True, pygame.Color(pink))
                # Umístění písmena do třetiny výšky obrazovky a posunutí horizontálně
                self.screen.blit(text, (100 + i * 50, self.screen.get_height() // 1.855))

        # Vykreslení počtu zbývajících životů
        lives_text = self.font.render("Lives: {}".format(self.lives), True, pygame.Color('black'))
        self.screen.blit(lives_text, (20, 20))

        # Vykreslení abecedy v pravé části okna - rozděleno do tří sloupců
        for i, letter in enumerate("ABCDEFGHI"):
            text = self.font.render(letter, True, pygame.Color('black'))
            self.screen.blit(text, (600, 50 + i * 30))

        for i, letter in enumerate("JKLMNOPQ"):
            text = self.font.render(letter, True, pygame.Color('black'))
            self.screen.blit(text, (670, 50 + i * 30))

        for i, letter in enumerate("RSTUVWXYZ"):
            text = self.font.render(letter, True, pygame.Color('black'))
            self.screen.blit(text, (740, 50 + i * 30))

        pygame.display.flip()

    def game_over_screen(self): # tohle by mi mělo zajistit při přohře zobrazit game_over a pustit def. pro opakovane spuštění či zrušení
        script_dir = os.path.dirname(__file__)
        image_folder = os.path.join(script_dir,"pictures")
        game_over_image = pygame.image.load(os.path.join(image_folder,"game_over.png"))
        self.screen.blit(game_over_image,(0,0))
        pygame.display.flip()
        self.handle_game_end()

    def win_screen(self): # to same jako vyše ale pří výhře
        script_dir = os.path.dirname(__file__)
        image_folder = os.path.join(script_dir,"pictures")
        win_image = pygame.image.load(os.path.join(image_folder,"win.png"))
        self.screen.blit(win_image,(0,0))
        pygame.display.flip()
        self.handle_game_end()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Kontrola levého tlačítka myši
                        x,y = event.pos
                        if 600 <= x <= 630:  # klikání na první sloupec abecedy
                            column = (y - 50) // 30
                            clicked_letter = chr(65 + column)
                            if clicked_letter not in self.guessed_letters:
                                self.guessed_letters.add(clicked_letter)
                                if clicked_letter not in self.word:
                                    print("Wrong guess!")
                                    self.lives -= 1  # Snížení počtu životů při špatném hádání
                                    self.current_hangman_index += 1  # Zvýšení indexu obrázku hangmana
                                    if self.lives == 0:
                                        self.game_over_screen()
                                        self.handle_game_end()
                                else:
                                    if self.hidden_word.count("_") == 0:
                                        self.win_screen()
                                        self.handle_game_end()

                        elif 670 <= x <= 700:  # Pokud je kliknuto ve druhém sloupci abecedy
                            column = (y - 50) // 30
                            clicked_letter = chr(
                                74 + column)  # nastavení správného počáteční indexu pro druhý sloupec (J-Q)
                            self.handle_letter_guess(clicked_letter)

                        elif 740 <= x <= 770:  # Pokud je kliknuto ve třetím sloupci abecedy
                            column = (y - 50) // 30
                            clicked_letter = chr(
                                82 + column)  # nastavení správný počáteční index pro třetí sloupec (R-Z)
                            self.handle_letter_guess(clicked_letter)

            self.draw()
            self.clock.tick(30)

        pygame.quit()

    def handle_letter_guess(self,clicked_letter):
        if clicked_letter not in self.guessed_letters:
            self.guessed_letters.add(clicked_letter)
            if clicked_letter not in self.word:
                print("Wrong guess!")
                self.lives -= 1  # Snížení počtu životů při špatném hádání
                self.current_hangman_index += 1  # Zvýšení indexu obrázku hangmana
                if self.lives == 0:
                    self.game_over_screen()
                    self.handle_game_end()
            else:
                print("Correct guess!")
                if all(letter in self.guessed_letters for letter in self.word):
                    self.win_screen()
                    self.handle_game_end()

    def reset_game(self):
        self.word = random.choice(categories["European_states"]).upper()
        self.guessed_letters = set()
        self.lives = 6
        self.hidden_word = "_" * len(self.word)
        self.current_hangman_index = 0

    def handle_game_end(self):
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        self.reset_game()  # reset hry
                        waiting_for_input = False
                    elif event.key == pygame.K_n:
                        pygame.quit()
                        waiting_for_input = False


if __name__ == "__main__":
    game = European_states()
    game.run()
