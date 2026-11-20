import pygame
import sys
from settings import Settings


class BlueSky:
    """Класс для управления русурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Blue Sky")

    def run_game(self):
        """Запускает основной цикл игры."""
        while True:
            # Обрабатывает нажатия клавиш и события мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Перерисовывает экран во время каждого прохода.
            self.screen.fill(self.settings.bg_color)

            # Сделать последний отрисованный экран видимым.
            pygame.display.flip()
            self.clock.tick(60)

# Создает экземпляр игры и запускает игру.
if __name__ == "__main__":
    bs = BlueSky()
    bs.run_game()
