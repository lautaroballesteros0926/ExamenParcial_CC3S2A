import pygame
import random

RED = (255, 0, 0)
CELL_SIZE = 40

class Obstaculos:
    def __init__(self, tablero):
        self.tablero = tablero
        self.obstacles = []  # Lista de tuplas con las posiciones de los obstáculos

    def generar_obstaculos(self, cantidad):
        for _ in range(cantidad):
            x = random.randint(0, self.tablero.columns - 1)
            y = random.randint(0, self.tablero.rows - 1)
            self.obstacles.append((x, y))

    def draw(self, screen):
        for obstacle in self.obstacles:
            rect = pygame.Rect(obstacle[0] * CELL_SIZE, obstacle[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, RED, rect)