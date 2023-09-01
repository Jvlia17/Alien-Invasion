import sys #Skorzystamy, gdy wystąpi konieczność zakończenia gry na żądanie gracza.
import pygame #Zawiera funkcjonalność niezbędną do przygotowania gry.

from settings import Settings #Wszystkie ustawienia w jednym miejscu.
from ship import Ship

class AlienInvasion:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init() #Inicjalizuje ustawienie tła

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #Tworzenie okna o wymiarach 1200x800. Okno zostaje przypisane atrybutowi self.screen i będzie dostępne dla wszystkich metod.
        # Self.screen -> inaczej powierzchnia, na której będą wyświetlane elementy gry. W trakcie trwania gry powierzchnia będzie automatycznie odświeżana w trakcie każdej iteracji pętli.

        pygame.display.set_caption("Inwazja obcych")

        self.ship = Ship(self) # Atrybut self odnosi się tutaj do bieżącego egzemplarza AlienInvasion -> zapewnia to dostęp do obiektów takich jak screen

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events() # To są tak zwane metody pomocnicze -> działa w klasie, ale nie jest przeznaczona do wywołania z poziomu egzemplarza.
            self._update_screen()

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""

        # Oczekiwane naciśnięcie klawisza lub przycisku myszy.
        for event in pygame.event.get():  # Wbudowana pętla zdarzeń -> nasłuchuje zdarzeń i podejmuje odpowiednie działania.
            if event.type == pygame.QUIT:  # Jeśli gracz kliknie przycisk zamykający okno gry -> gra zostanie zakończona.
                sys.exit()

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()  # Metoda będzie uaktualniać ekran, odzwierciedlając nowe położenie elementów i ukrywając te niepotrzebne.

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie

    ai = AlienInvasion()
    ai.run_game()