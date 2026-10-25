from __future__ import annotations
import pygame
from tests.doubles import StubSemDesconto, StubAlienQueTocouBorda
from src.coisa_de_desconto.Desconto import Pedido
from src.fleet_manager import FleetManager
from src.settings import Settings
from src.ship import Ship


def test_pedido_com_stub() -> None:
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100


def test_fleet_manager_inverte_direcao_com_stub_alien() -> None:
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    settings = Settings()
    ship = Ship(screen, settings)
    fleet_manager = FleetManager(screen, settings, ship)

    stub_alien = StubAlienQueTocouBorda()
    fleet_manager.aliens.add(stub_alien)

    direcao_inicial = settings.fleet_direction
    fleet_manager._check_fleet_edges()

    # O stub forçou a colisão com a borda, logo a direção deve ser invertida
    assert settings.fleet_direction == -direcao_inicial
    # E o alienígena deve ter descido fleet_drop_speed (10 pixels)
    assert stub_alien.rect.y == 110
