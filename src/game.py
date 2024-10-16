import pygame
from src.tablero import Tablero
from src.powerup import Food, Inmunidad, Double_Points
from src.obstaculos import Obstaculos
from src.snake import Snake
from src.menu import Menu


# Colores básicos
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tamaño de la ventana
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40

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
        self.controlador_nivel=0

        self.running = True
        self.score = 0
        self.controller = 1 
        self.menu = Menu()
    def check_collisions(self):
        # Colisión con los bordes del tablero
        head_x, head_y = self.snake.body[0]
        if not (0 <= head_x < self.tablero.columns and 0 <= head_y < self.tablero.rows):
            self.snake.life=self.snake.life-1
            if self.snake.life==0:
                self.running = False        
            else:
                self.running = True   
                self.snake.body=[(10, 10)]
                pygame.time.delay(400)

        # Colisión con el prfoodio cuerpo
        if len(self.snake.body) != len(set(self.snake.body)):
            self.snake.life=self.snake.life-1
            if self.snake.life==0:
                self.running = False        
            else:
                self.running = True   
                self.snake.body=[(10, 10)]
                pygame.time.delay(400)

    
        # Colisión con Double_point
        if self.double_points.position == (head_x, head_y):
            self.snake.grow()
            while True:
                self.double_points.generar_power_up()
                if self.food.position not in self.obstaculos.obstacles:
                    print("ok")
                    break
                else:
                    print("not ok")

            self.score += 20  # Aumentar puntuación
            self.controlador_nivel+=20

	    #Colision con obstaculos
        if (head_x,head_y) in self.obstaculos.obstacles:
            self.snake.life=self.snake.life-1
            if self.snake.life==0:
                self.running = False        
            else:
                self.running = True  
                self.colision = False
                self.snake.body=[(10, 10)]
                pygame.time.delay(400)
                
        # Colisión con food
        if self.food.position == (head_x, head_y):
            self.snake.grow()
            while True:
                self.food.generar_power_up()
                if self.food.position not in self.obstaculos.obstacles:
                    print("ok")
                    break
                else:
                    print("not ok")

            self.score += 10  # Aumentar puntuación
            self.controlador_nivel+=10



            
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.set_direction(0, -1)
                    break
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction(0, 1)
                    break
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction(-1, 0)
                    break
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction(1, 0)
                    break
    


    def game_loop(self):
        self.obstaculos.generar_obstaculos(3)  # Generar obstáculos
        self.double_points.generar_power_up()
        #######################################
        #Se asegura que la comida no aparezca en la misma posicion que los obstaculos
        while True:
            self.food.generar_power_up()
            if self.food.position not in self.obstaculos.obstacles:
                print("ok")
                break
            else:
                print("not ok")
            self.double_points.generar_power_up()
            if self.double_points.position not in self.obstaculos.obstacles:
                print("ok")
                break
            else:
                print("not ok")

        ###########################    


        while self.running:
            if(self.controller == 1): # Menu principal 
                action = self.menu.handle_input()
                if action == 'start':
                    self.controller = 2  # Entrar al juego
                    self.tablero.draw_nivel(self.screen,1)   
                elif action == 'quit':
                    self.running = False 
                self.menu.draw(self)
            if (self.controller == 2):  # Directamente entrar al Juego   
                self.handle_input()
                self.snake.move()
                self.check_collisions()
                self.screen.fill(BLACK)
                self.snake.draw(self.screen)
                self.obstaculos.draw(self.screen)
                self.food.draw(self.screen)
                self.double_points.draw(self.screen)
                self.tablero.draw_score(self.screen,self.score)
                self.tablero.draw_life(self.screen,self.snake.life)
                if self.controlador_nivel>=50:
                    nivel=self.obstaculos.nivel
                    self.obstaculos.nivel=nivel+1
                    self.obstaculos.niveles(nivel)
                    self.snake.body=[(10, 10)]
                    self.controlador_nivel=0
                    self.tablero.draw_nivel(self.screen,self.obstaculos.nivel)   
                    self.snake.growing=False
            pygame.display.flip()
            self.clock.tick(10)  # 10 FPS

        pygame.quit()
       
      
