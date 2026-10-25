import pygame
from settings import Settings
from ship import Ship


def test_ship_move_esquerda() -> None:
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    settings = Settings()

    ship = Ship(screen, settings)

    x_inicial = ship.x

    # ação
    ship.moving_left = True
    ship.update()

    # verificação
    assert ship.x < x_inicial

