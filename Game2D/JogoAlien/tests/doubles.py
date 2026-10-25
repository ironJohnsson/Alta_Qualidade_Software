from __future__ import annotations
import pygame
from src.coisa_de_desconto.Desconto import IDesconto


class StubSemDesconto(IDesconto):
    def calcular(self, valor: float) -> float:
        return 0.0


class StubAlienQueTocouBorda(pygame.sprite.Sprite):
    """Stub de alienígena do jogo que sempre responde que atingiu a borda."""
    def __init__(self) -> None:
        super().__init__()
        self.rect = pygame.Rect(100, 100, 60, 58)

    def check_edges(self) -> bool:
        return True
