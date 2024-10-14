from src.game import Game
import pygame
from behave import given,when,then
import re
pygame.init()   

game=Game()


######################################################

@given('que la serpiente se encuentra en la posicion {posicion}')
def check_posicion(context,posicion):
    pattern=re.compile(r'(\d+),(\d+)')
    match=pattern.match(posicion.lower())
    if match:
        head_x=int(match.group(0))
        head_y=int(match.group(1))
        game.snake.body[0] = head_x , head_y
        print(f'La posicion es:{posicion}')
    else:
        raise ValueError(f"No se pudo interpretar la posicion de la serpiente: {posicion}")
    
@when('el obstaculo se encuentra en la posicion {posicion}')
def check_posicionobstacle(context,posicion):
    pattern=re.compile(r'(\d+),(\d+)')
    match=pattern.match(posicion.lower())
    if match:
        obs_x=match.group(0)
        obs_y=match.group(1)
        game.obstaculos.generar_obstaculos(1)
        game.obstaculos[0]=obs_x,obs_y
    else:
        raise ValueError(f"No se pudo interpretar la posicion del obstaculo: {posicion}")
    
@then('el juego termina')
def end_game(context):
    assert not game.snake.is_life