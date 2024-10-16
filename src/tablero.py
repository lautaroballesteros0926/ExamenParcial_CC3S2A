import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Tablero:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.columns = width // cell_size
        self.rows = height // cell_size

    def draw(self, screen):
        screen.fill(BLACK)
        for x in range(0, self.width, self.cell_size):
            for y in range(0, self.height, self.cell_size):
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, BLACK, rect, 1)
    def draw_nivel(self,screen,nivel):
        screen.fill(BLACK)
        # Definir la fuente y el tamaño del texto
        font = pygame.font.Font(None, 74)  # Fuente por defecto, tamaño 74

        # Renderizar el texto "Nivel X"
        text = font.render(f"Nivel {nivel}", True, (255, 255, 255))  # Texto en blanco

        # Obtener las dimensiones de la pantalla y del texto
        screen_width, screen_height = screen.get_size()
        text_width, text_height = text.get_size()

        # Calcular la posición para centrar el texto
        text_x = (screen_width - text_width) // 2
        text_y = (screen_height - text_height) // 2

        # Dibujar el texto en la pantalla
        screen.blit(text, (text_x, text_y))

        # Actualizar la pantalla para mostrar el texto
        pygame.display.flip()

        # Esperar un momento para que el jugador vea el texto (por ejemplo, 2 segundos)
        pygame.time.delay(2000)

    def draw_score(self,screen,score):
        # Definir la fuente y el tamaño del texto
        font = pygame.font.Font(None, 36)  # Fuente por defecto, tamaño 74

        # Renderizar el texto "Nivel X"
        text = font.render(f"Score {score}", True, (255, 255, 255))  # Texto en blanco

        # Obtener las dimensiones de la pantalla y del texto
  
        # Dibujar el texto en la pantalla
        screen.blit(text, (10, 10))

        # Actualizar la pantalla para mostrar el texto

        # Esperar un momento para que el jugador vea el texto (por ejemplo, 2 segundos)

    def draw_life(self,screen,life):
        # Definir la fuente y el tamaño del texto
        font = pygame.font.Font(None, 36)  # Fuente por defecto, tamaño 74

        # Renderizar el texto "Nivel X"
        text = font.render(f"Vidas: {life}", True, (255, 255, 255))  # Texto en blanco

        # Obtener las dimensiones de la pantalla y del texto
  
        # Dibujar el texto en la pantalla
        screen.blit(text, (500, 380))

        # Actualizar la pantalla para mostrar el texto

        # Esperar un momento para que el jugador vea el texto (por ejemplo, 2 segundos)
    




