import pygame
from tablero import Tablero

# Colores básicos
BLACK = (0, 0, 0)

# Tamaño de la ventana
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Mejorado")
        self.clock = pygame.time.Clock()

        self.tablero = Tablero(WIDTH, HEIGHT, CELL_SIZE)

        self.running = True
        self.score = 0

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # definir algun movimiento
                    pass
                elif event.key == pygame.K_DOWN:
                    # definir algun movimiento
                    pass
                elif event.key == pygame.K_LEFT:
                    # definir algun movimiento
                    pass
                elif event.key == pygame.K_RIGHT:
                    # definir algun movimiento
                    pass

    def game_loop(self):

        while self.running:
            self.handle_input()

            self.screen.fill(BLACK)
            self.tablero.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(10)  # 10 FPS

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.game_loop()
