
Feature: MOVIMIENTO BASICO DEL SNAKE

    Scenario: Movimiento para arriba para la snake
    Given que el usuario quiere mover a la serpiente en la direccion arriba
    When el jugador presiona una tecla de direccion arriba
    Then la serpiente debe cambiar su dirección acorde a la tecla arriba

    Scenario: Movimiento para abajo para la snake
    Given que el usuario quiere mover a la serpiente en la direccion abajo
    When el jugador presiona una tecla de direccion abajo
    Then la serpiente debe cambiar su dirección acorde a la tecla abajo

    Scenario: Movimiento para derecha para la snake
    Given que el usuario quiere mover a la serpiente en la direccion derecha
    When el jugador presiona una tecla de direccion derecha
    Then la serpiente debe cambiar su dirección acorde a la tecla derecha

    Scenario: Movimiento para izquierda para la snake
    Given que el usuario quiere mover a la serpiente en la direccion izquierda
    When el jugador presiona una tecla de direccion izquierda
    Then la serpiente debe cambiar su dirección acorde a la tecla izquierda

