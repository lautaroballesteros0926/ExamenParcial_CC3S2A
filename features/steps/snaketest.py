from src.game import Game
import pygame
from behave import given,when,then
import re
pygame.init()   

game=Game()



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

    game.check_collisions()
    game.obstaculos.obstacles.pop()
    game.snake.body.pop()
    assert not game.colision,"Se esperaba el jugador y el obstaculo colisionen"



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

