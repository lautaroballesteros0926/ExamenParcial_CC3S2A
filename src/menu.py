import pygame

# Colores
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Menu:
    def __init__(self):
        self.title_menu = pygame.image.load("sprites/boton_menu.png")
        self.buttom_start = pygame.image.load("sprites/boton_start.png")
        self.background_image = pygame.image.load("sprites/fondo.jpeg")

        # Inicializar el rectángulo del botón "Start"
        self.buttom_rect_start = self.buttom_start.get_rect()
        self.buttom_rect_start.topleft = (320, 420)

        # Movimiento del fondo
        self.background_x = 0
        self.background_speed = 5  # Velocidad de desplazamiento del fondo

        # Cuadro de texto
        self.rect_input = pygame.Rect(330, 270, 200, 40)
        self.color = WHITE
        self.nombre = ""
        self.font = pygame.font.SysFont("Arial", 24)
        self.active = False

        # Mensaje de ingreso de nombre
        self.message_font = pygame.font.SysFont("Arial", 24)

    def update_background(self):
        # Desplazar el fondo hacia la izquierda
        self.background_x -= self.background_speed
        if self.background_x <= -self.background_image.get_width():
            self.background_x = 0

    def draw(self, game):
        pygame.display.set_caption("Menú de Juego")

        # Mover y dibujar el fondo
        self.update_background()
        game.screen.blit(self.background_image, (self.background_x, 0))
        game.screen.blit(self.background_image, (self.background_x + self.background_image.get_width(), 0))

        # Dibujar el texto del menú y el botón "Start"
        game.screen.blit(self.title_menu, (280, 100))
        game.screen.blit(self.buttom_start, self.buttom_rect_start.topleft)

        # Dibujar el mensaje para ingresar el nombre
        message_surface = self.message_font.render("Por favor, ingresa tu nombre:", True, WHITE)
        game.screen.blit(message_surface, (280, self.rect_input.y - 40))

        # Renderizar el texto dentro del cuadro de texto
        txt_surface = self.font.render(self.nombre, True, BLACK)
        # Ajustar el ancho del cuadro de texto si el texto es muy largo
        width = max(200, txt_surface.get_width() + 10)
        self.rect_input.w = width
        # Dibujar el cuadro de texto
        pygame.draw.rect(game.screen, self.color, self.rect_input, 2)
        # Dibujar el texto dentro del cuadro de texto
        game.screen.blit(txt_surface, (self.rect_input.x + 5, self.rect_input.y + 5))

    def handle_input(self):
        # Manejar eventos relacionados con el menú
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 es el botón izquierdo del ratón
                    mouse_pos = pygame.mouse.get_pos()
                    if self.buttom_rect_start.collidepoint(mouse_pos):
                        if self.nombre.strip() != "":  # Solo permitir avanzar si hay un nombre
                            return 'start'
                        else:
                            print("Debe ingresar un nombre para comenzar el juego")
                    elif self.rect_input.collidepoint(mouse_pos):
                        # Si el usuario hace clic dentro del cuadro de texto, activarlo 
                        self.active = True
                    else:
                        self.active = False
                    self.color = WHITE if self.active else GRAY
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        if self.nombre.strip() != "":
                            print(f"Nombre ingresado: {self.nombre}")
                        else:
                            print("Debe ingresar un nombre")
                    elif event.key == pygame.K_BACKSPACE:
                        # Eliminar el último carácter del texto
                        self.nombre = self.nombre[:-1]
                    else:
                        # Agregar el carácter al texto
                        self.nombre += event.unicode
        return None
