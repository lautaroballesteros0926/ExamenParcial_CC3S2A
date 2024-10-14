# features/movimiento_snake.feature
# language: es

Característica: Movimiento y lógica básica del Snake

  Escenario: El Snake sale del borde de la pantalla por la derecha
    Dado que el snake está cerca del borde derecho
    Cuando el snake se mueve hacia la derecha
    Entonces el juego termina

  Escenario: El Snake sale del borde de la pantalla por la izquierda
    Dado que el snake está cerca del borde izquierdo
    Cuando el snake se mueve hacia la izquierda
    Entonces el juego termina

  Escenario: El Snake sale del borde de la pantalla por arriba
    Dado que el snake está cerca del borde superior
    Cuando el snake se mueve hacia arriba
    Entonces el juego termina

  Escenario: El Snake sale del borde de la pantalla por abajo
    Dado que el snake está cerca del borde inferior
    Cuando el snake se mueve hacia abajo
    Entonces el juego termina

  Escenario: El Snake se choca a sí mismo
    Dado que el snake es suficientemente largo
    Cuando el snake se mueve hacia su propio cuerpo
    Entonces el juego termina

  Escenario: El Snake se choca con algún obstáculo
    Dado que hay un obstáculo en el tablero
    Cuando el snake se mueve hacia el obstáculo
    Entonces el juego termina

  Escenario: El Snake se mueve a la izquierda si se presiona la tecla Left
    Dado que el jugador está jugando el snake
    Cuando se presiona la tecla Left
    Entonces el snake se mueve hacia la izquierda

  Escenario: Movimiento inválido hacia la derecha o izquierda
    Dado que el snake se está moviendo a la derecha
    Cuando el jugador presiona la tecla Left
    Entonces el snake no admite ese movimiento

  Escenario: Movimiento inválido hacia arriba o abajo
    Dado que el snake se está moviendo hacia arriba
    Cuando el jugador presiona la tecla Down
    Entonces el snake no admite ese movimiento
