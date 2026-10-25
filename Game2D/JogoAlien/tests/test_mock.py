from __future__ import annotations
from typing import Any
from src.coisa_de_desconto.Desconto import Pedido
from src.game_renderer import GameRenderer


def test_pedido_com_mock_desconto(mocker: Any) -> None:
    mock_desconto = mocker.Mock()
    mock_desconto.calcular.return_value = 10

    pedido = Pedido(mock_desconto)
    resultado = pedido.total(100)

    assert resultado == 90

    mock_desconto.calcular.assert_called()
    mock_desconto.calcular.assert_called_once_with(100)
    assert mock_desconto.calcular.call_count == 1


def test_game_renderer_render_screen_com_mock(mocker: Any) -> None:
    mock_screen = mocker.Mock()
    mock_ship = mocker.Mock()
    mock_aliens = mocker.Mock()
    mock_bullets = mocker.Mock()
    mock_bullet = mocker.Mock()
    mock_bullets.sprites.return_value = [mock_bullet]
    mocker.patch("pygame.display.flip")

    renderer = GameRenderer(
        screen=mock_screen,
        bg_color=(230, 230, 230),
        ship=mock_ship,
        aliens=mock_aliens,
        bullets=mock_bullets,
    )
    renderer._render_screen()

    # Validações de comportamento (Mock):
    mock_screen.fill.assert_called_once_with((230, 230, 230))
    mock_ship.blitme.assert_called_once()
    mock_aliens.draw.assert_called_once_with(mock_screen)
    mock_bullet.draw_bullet.assert_called_once()
