import pygame
from src.tablero import Tablero
from src.powerup import Food Inmunidad, Double_Points
from src.obstaculos import Obstaculos
from src.snake import Snake

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
        self.food = Food(self.tablero)
        self.double_points = Double_Points(self.tablero)
        self.snake = Snake()
        self.obstaculos = Obstaculos(self.tablero)

        self.running = True
        self.score = 0

    def check_collisions(self):
        # Colisión con los bordes del tablero
        head_x, head_y = self.snake.body[0]
        if not (0 <= head_x < self.tablero.columns and 0 <= head_y < self.tablero.rows):
            self.running = False

        # Colisión con el prfoodio cuerpo
        if len(self.snake.body) != len(set(self.snake.body)):
            self.running = False

        # Colisión con obstáculos
        if (head_x, head_y) in self.obstaculos.obstacles:
            self.running = False
            
        # Colisión con Food
        if self.food.position == (head_x, head_y):
            self.snake.grow()
            self.food.generar_power_up()
            self.score += 10  # Aumentar puntuación
            print(self.score)
        
        # Colisión con Double_point
        if self.double_points.position == (head_x, head_y):
            self.snake.grow()
            self.double_points.generar_power_up()
            self.score += 20  # Aumentar puntuación
            print(self.score)


            
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.set_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction(1, 0)

    def game_loop(self):
        self.obstaculos.generar_obstaculos(5)  # Generar obstáculos
        self.double_points.generar_power_up()  # Generar primer power-up
        
        while self.running:
            self.handle_input()
            self.snake.move()
            self.check_collisions()
            self.screen.fill(BLACK)
            self.tablero.draw(self.screen)
            self.snake.draw(self.screen)
            self.obstaculos.draw(self.screen)
            self.double_points.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(10)  # 10 FPS

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.game_loop()
