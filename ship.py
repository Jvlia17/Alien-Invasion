import pygame

# rect -> i statek i ekran są traktowane jako prostokąty.

class Ship:
    """Klasa przeznaczona do sterowania statkiem kosmicznym."""

    def __init__(self, ai_game): # ai_game -> odniesienie do aktualnego egzemplarza klasy AlienInvasion
        """Inicjalizacja statku kosmicznego i jego położenie początkowe."""

        self.screen = ai_game.screen # dostęp do ekranu we wszystkich metodach klasy
        self.screen_rect = ai_game.screen.get_rect() # dostęp do atrybutu rect ekranu i umieszczamy go potem w dobrym miejscu.

        #Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect() # dostęp do atrybutu rect statku i zmiana położenia

        #Każdy nowy statek kosmiczny pojawia się na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom #

    def blitme(self):
        """Wyświetlenie statku kosmicznego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect) # funkcja do wyświetlania obrazu na ekranie