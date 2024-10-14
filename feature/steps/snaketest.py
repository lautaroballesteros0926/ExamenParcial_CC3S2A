# features/steps/steps.py
from behave import given, when, then
from src.snake import Snake
from src.game import Game

# Crear instancias del juego y la serpiente
@given('el snake está cerca del borde {borde}')
def step_snake_near_edge(context, borde):
    context.game = Game()  # Crear el juego
    context.snake = context.game.snake  # Obtener la serpiente

    # Colocar la cabeza del snake cerca del borde especificado
    if borde == 'derecho':
        context.snake.body = [(context.game.tablero.columns - 1, 10)]  # Borde derecho
    elif borde == 'izquierdo':
        context.snake.body = [(0, 10)]  # Borde izquierdo
    elif borde == 'superior':
        context.snake.body = [(10, 0)]  # Borde superior
    elif borde == 'inferior':
        context.snake.body = [(10, context.game.tablero.rows - 1)]  # Borde inferior

@given('el snake es suficientemente largo')
def step_snake_is_long(context):
    context.snake.body = [(10, 10), (11, 10), (12, 10), (13, 10)]  # Snake largo

@given('hay un obstáculo en el tablero')
def step_obstacle_on_board(context):
    context.game.obstaculos.obstacles = [(15, 10)]  # Colocar un obstáculo en la posición (15, 10)

@when('el snake se mueve hacia la {direccion}')
def step_snake_moves(context, direccion):
    if direccion == 'derecha':
        context.snake.set_direction(1, 0)  # Mover derecha
    elif direccion == 'izquierda':
        context.snake.set_direction(-1, 0)  # Mover izquierda
    elif direccion == 'arriba':
        context.snake.set_direction(0, -1)  # Mover arriba
    elif direccion == 'abajo':
        context.snake.set_direction(0, 1)  # Mover abajo
    context.snake.move()

@when('se presiona la tecla {tecla}')
def step_key_pressed(context, tecla):
    if tecla == 'Left':
        context.snake.set_direction(-1, 0)  # Mover izquierda
    elif tecla == 'Right':
        context.snake.set_direction(1, 0)  # Mover derecha
    elif tecla == 'Up':
        context.snake.set_direction(0, -1)  # Mover arriba
    elif tecla == 'Down':
        context.snake.set_direction(0, 1)  # Mover abajo
    context.snake.move()

@then('el juego termina')
def step_game_ends(context):
    context.game.check_collisions()
    assert context.game.running is False, "El juego no terminó como se esperaba"

@then('el snake se mueve hacia la izquierda')
def step_snake_moves_left(context):
    context.snake.move()
    assert context.snake.direction == (-1, 0), "El snake no se movió hacia la izquierda"

@then('el snake no admite ese movimiento')
def step_invalid_move(context):
    context.snake.move()
    head_x, head_y = context.snake.body[0]
    assert head_x != context.snake.body[0][0], "El movimiento no fue inválido como se esperaba"
