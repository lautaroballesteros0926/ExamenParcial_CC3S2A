 # language: es

  Característica: Obstaculos

    Escenario: Colision con un obstaculo
      Dado que la serpiente se encuentra en la posicion 10,10
      Cuando el obstaculo se encuentra en la posicion 10,10
      Entonces ocurre una colision

    Escenario: Creacion de un obstaculo
      Dado un tablero con "30 columnas y 20 filas"
      Cuando genero 5 obstaculos
      Entonces los obstaculos deben estar dentro de los limites



