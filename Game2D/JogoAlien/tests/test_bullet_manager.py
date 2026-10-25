import pygame
from bullet_manager import BulletManager
from settings import Settings
from ship import Ship


def test_bullet_manager_fire() -> None:
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    settings = Settings()
    ship = Ship(screen, settings)
    bullet_manager = BulletManager(screen, settings, ship)

    # Inicialmente sem projéteis
    assert len(bullet_manager.bullets) == 0

    # Dispara um projétil
    bullet_manager._fire_bullet()

    # Deve conter exatamente 1 projétil
    assert len(bullet_manager.bullets) == 1


def test_bullet_manager_respects_limit() -> None:
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    settings = Settings()
    settings.bullet_allowed = 1
    ship = Ship(screen, settings)
    bullet_manager = BulletManager(screen, settings, ship)

    bullet_manager._fire_bullet()
    bullet_manager._fire_bullet()  # Segunda tentativa deve ser bloqueada pelo limite

    assert len(bullet_manager.bullets) == 1

