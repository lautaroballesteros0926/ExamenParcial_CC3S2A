import pygame

GREEN = (0, 255, 0)
CELL_SIZE = 20
class Snake:
    def __init__(self):
        self.body = [(10, 10)]  # Lista de tuplas representando las posiciones del cuerpo
        self.direction = (1, 0)  # Movimiento inicial hacia la derecha
        self.growing = False
        self.is_life = True

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)
        if not self.growing:
            self.body.pop()
        self.growing = False

    def grow(self):
        self.growing = True

    def draw(self, screen):
        for segment in self.body:
            rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)

    def set_direction(self, dir_x, dir_y):
        if (dir_x, dir_y) != (-self.direction[0], -self.direction[1]):  # Evitar moverse hacia la dirección opuesta
            self.direction = (dir_x, dir_y)