 # language: es

  Característica: Obstaculos

    Escenario: Colision con un obstaculo
      Dado que la serpiente se encuentra en la posicion 20,20
      Cuando el obstaculo se encuentra en la posicion 20,20
      Entonces se termina el juego

    Escenario: Creacion de un obstaculo
      Dado un tablero con "30 columnas y 20 filas"
      Cuando genero 5 obstaculos
      Entonces los obstaculos deben estar dentro de los limites



