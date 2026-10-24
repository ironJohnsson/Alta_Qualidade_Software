from __future__ import annotations
from typing import Any

import pygame
from alien import Alien
from bullet import Bullet
from pygame.surface import Surface
from settings import Settings
from ship import Ship


class BulletManager:
    """responsável por gerenciar os projéteis disparados pela nave."""
    def __init__(self, screen: Surface, settings: Settings, ship: Ship) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets: pygame.sprite.Group[Any] = pygame.sprite.Group()  # Cria um grupo para armazenar os projéteis disparados pela nave

    def _fire_bullet(self) -> None:
        """Dispara um projétil se o limite de projéteis na tela não for excedido."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)  # Cria um novo projétil
            self.bullets.add(new_bullet)  # Adiciona o novo projétil ao grupo de projéteis

    def _update_bullets(self, aliens: pygame.sprite.Group[Alien]) -> None:
        self.bullets.update()  # Atualiza a posição de cada projétil no grupo de projéteis
        self._remove_offscreen_bullets()  # Remove projéteis que saíram da tela
        self._check_bullet_alien_collisions(aliens)  # Verifica colisões entre projéteis e alienígenas

    def _remove_offscreen_bullets(self) -> None:
        """Remove projéteis que saíram da tela."""
        for bullet in self.bullets.copy():  # Verifica se algum projétil saiu da tela
            if bullet.rect.bottom <= 0:  # Se o projétil saiu da tela
                self.bullets.remove(bullet)  # Remove o projétil do grupo de projéteis

    def _check_bullet_alien_collisions(self, aliens: pygame.sprite.Group[Alien]) -> None:
        """Verifica colisões entre projéteis e alienígenas"""
        pygame.sprite.groupcollide(self.bullets, aliens, True, True)
