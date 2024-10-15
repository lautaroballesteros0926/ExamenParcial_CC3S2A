import pygame
import random

BLUE = (0, 0, 255)
CELL_SIZE = 40

class PowerUps:
    def __init__(self, tablero):
        self.tablero = tablero
        self.position = None  # Posición del power-up

    def generar_power_up(self):
        x = random.randint(0, self.tablero.columns - 1)
        y = random.randint(0, self.tablero.rows - 1)
        self.position = (x, y)

    def draw(self, screen):
        if self.position:
            rect = pygame.Rect(self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLUE,rect)