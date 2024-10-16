from src.game import Game
from src.snake import Snake
import pygame
from behave import given,when,then
import re
pygame.init()   
game=Game()
snake=Snake()

# TEST PARA EL MOVIMIENTO DE LA SNAKE 
def movement(move):
    if move=='izquierda' and snake.body == [(9,10)]:
        return True
    elif move=='derecha' and snake.body == [(11,10)]:
        return True
    elif move=='arriba' and snake.body == [(10,11)]:
        return True
    elif move=='abajo' and snake.body == [(10,9)]:
        return True
    else:
        return False

@given('que el usuario quiere mover a la serpiente en la direccion {direccion}')
def check_movimiento(context,direccion):
    pattern=re.compile(r'(izquierda|derecha|abajo|arriba)')
    match=pattern.match(direccion.lower())
    if match:
        print('correcto')
    else:
        raise ValueError(f"No se pudo interpretar el movimiento: {direccion}")


@when('el jugador presiona una tecla de direccion {direccion}')
def do_movement(context,direccion):
    pattern=re.compile(r'(izquierda|derecha|abajo|arriba)')
    match=pattern.match(direccion.lower())
    if match:
        if match.group(1)=='izquierda':
            snake.direction = (-1,0)
            snake.move()
            print(snake.body)
        elif match.group(1)=='derecha':
            snake.direction = (1,0)
            snake.move()
            print(snake.body)
        elif match.group(1)=='abajo':
            snake.direction = (0,-1)
            snake.move()
            print(snake.body)
        elif match.group(1)=='arriba':
            snake.direction = (0,1)
            snake.move()
            print(snake.body)
        else:
            print('No se intrepeto correctamente la tecla presionada')
    else:
        raise ValueError(f"No se pudo interpretar el boton presionado: {direccion}")
    
@then('la serpiente debe cambiar su dirección acorde a la tecla izquierda')
def check_movement(context):
    assert movement('izquierda'),"No se movio correctamente"
    snake.body = [(10,10)]

@then('la serpiente debe cambiar su dirección acorde a la tecla derecha')
def check_movement(context):
    assert movement('derecha'),"No se movio correctamente"
    snake.body = [(10,10)]

@then('la serpiente debe cambiar su dirección acorde a la tecla arriba')
def check_movement(context):
    assert movement('arriba'),"No se movio correctamente"
    snake.body = [(10,10)]

@then('la serpiente debe cambiar su dirección acorde a la tecla abajo')
def check_movement(context):
    assert movement('abajo'),"No se movio correctamente"
    snake.body = [(10,10)]
    
#################################################################################
@given('que la serpiente se encuentra en la posicion {posicion}')
def check_posicionsnake(context,posicion):
    pattern=re.compile(r'(\d+),(\d+)')
    match=pattern.match(posicion.lower())
    print(match.group(0))
    if match:
        head_x=int(match.group(1))
        head_y=int(match.group(2))
        game.snake.body[0] = head_x , head_y
        print(f'La posicion es:{posicion}')
    else:
        raise ValueError(f"No se pudo interpretar la posicion de la serpiente: {posicion}")
    
@when('el obstaculo se encuentra en la posicion {posicion}')
def check_posicionobstacle(context,posicion):
    pattern=re.compile(r'(\d+),(\d+)')
    match=pattern.match(posicion.lower())
    if match:
        obs_x=int(match.group(1))
        obs_y=int(match.group(2))
        game.obstaculos.generar_obstaculos(1)
        print(game.obstaculos.obstacles)
        game.obstaculos.obstacles[0]=obs_x,obs_y
        print(game.obstaculos.obstacles)

    else:
        raise ValueError(f"No se pudo interpretar la posicion del obstaculo: {posicion}")
    
@then('ocurre una colision')
def end_game(context):
    print(game.obstaculos.obstacles)
    print(game.snake.body[0])
    print(game.colision)
    print(game.tablero.rows)
    print(game.tablero.columns)
    print(game.snake.life)
    game.check_collisions()
    print(game.snake.life)
    
    print(game.colision)
    game.obstaculos.obstacles.pop()
    game.snake.body.pop()
    assert game.colision,"Se esperaba el jugador y el obstaculo colisionen"



#############################
@given('un tablero con "{cantidad}"')
def make_tablero(context,cantidad):
    pattern=re.compile(r'(\d+)\s(?:columnas?)\sy\s(\d+)\s(?:filas?)')
    match=pattern.match(cantidad.lower())
    if match:
        game.tablero.rows = int(match.group(2))
        game.tablero.columns = int(match.group(1))
    else:
        raise ValueError(f"No se pudo interpretar las dimensiones de la tabla:{cantidad}")
    
@when('genero {cantidad:d} obstaculos')
def generate_obstacles(context,cantidad):
        game.obstaculos.generar_obstaculos(cantidad)
    

@then('los obstaculos deben estar dentro de los limites')
def limit_obstacles(context):
    for x, y in game.obstaculos.obstacles:
        print((x,y))
        assert  0 <= x <= game.tablero.columns-1, f"Obstáculo en x={x} fuera de los límites"
        assert 0 <= y <= game.tablero.rows-1, f"Obstáculo en y={y} fuera de los límites"


#####################3

@given('que me encuentro en el nivel {nivel:d}')
def nivel(context,nivel):
    game.obstaculos.nivel=nivel

@when('obtengo {puntos:d} puntos')
def puntosnivel(context,puntos):
    game.score=50

@then('debo avanzar al siguiente nivel')
def up_nivel(context):
    nivelinicial=game.obstaculos.nivel
    game.level_up(game.score)
    nivelfinal=game.obstaculos.nivel
    assert (nivelinicial)<nivelfinal,"Debio subir de nivel"