Feature: COLISION CON LOS POWERUPS

    Scenario: Consumir un power-up food
        Given un power-up food aparece en el mapa
        When la serpiente recolecta food
        Then el score de la serpiente incrementa en 10

    Scenario: Consumir un power-up double_points
        Given un power-up double_points aparece en el mapa
        When la serpiente recolecta double_points
        Then el score de la serpiente incrementa en 20
