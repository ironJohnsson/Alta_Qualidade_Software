from __future__ import annotations
import sys

import pygame
from alien import Alien
from pygame.surface import Surface
from settings import Settings
from ship import Ship


class FleetManager:
    """responsável por gerenciar a frota de alienígenas."""
    def __init__(self, screen: Surface, settings: Settings, ship: Ship, alien_class: type[Alien] = Alien) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.alien_class = alien_class
        self.aliens: pygame.sprite.Group[Alien] = pygame.sprite.Group()  # Cria um grupo para armazenar os alienígenas presentes no jogo

    def _create_alien(self, alien_number: int, row_number: int, alien_width: int, alien_height: int) -> None:
        """Cria um alienígena e o posiciona na linha."""
        alien = self.alien_class(self.screen, self.settings)  # Cria uma instância da classe Alien
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = int(alien.x)
        alien_height = alien.rect.height
        alien.y = float(alien_height + 2 * alien_height * row_number)
        alien.rect.y = int(alien.y)
        self.aliens.add(alien)  # Adiciona o alienígena ao grupo de alienígenas

    def create_fleet(self) -> None:
        """Cria uma frota de alienígenas."""
        alien = self.alien_class(self.screen, self.settings)  # Cria uma instância da classe Alien
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number, alien_width, alien_height)

    def _update_aliens(self) -> None:
        """Verifica se a frota de alienígenas está em uma borda da tela e atualiza suas posições."""
        self._check_fleet_edges()  # Verifica se algum alienígena atingiu a borda da tela
        self.aliens.update()  # Atualiza a posição de cada alienígena no grupo de alienígenas
        self._check_fleet_bottom()  # Encerra o jogo se algum alienígena tocar o fundo da tela
        self._check_ship_collision()  # Verifica se a nave colidiu com algum alienígena

    def _check_fleet_edges(self) -> None:
        """Responde apropriadamente se algum alienígena atingiu a borda da tela."""
        for alien in self.aliens.sprites():
            if alien.check_edges():  # Verifica se algum alienígena atingiu a borda da tela
                self._change_fleet_direction()  # Altera a direção da frota de alienígenas
                break  # Sai do loop após encontrar o primeiro alienígena que atingiu a borda da tela

    def _change_fleet_direction(self) -> None:
        """Desce a frota e muda sua direção"""
        for alien in self.aliens.sprites():  # Atualiza a posição de cada alienígena no grupo de alienígenas
            alien.rect.y += self.settings.fleet_drop_speed  # Move cada alienígena para baixo com base na velocidade de descida da frota
        self.settings.fleet_direction *= -1  # Inverte a direção da frota para que os alienígenas se movam para o lado oposto na próxima atualização

    def _check_fleet_bottom(self) -> None:
        """Encerra o jogo se algum alienígena tocar o fundo da tela."""
        for alien in self.aliens.sprites():
            if alien.check_bottom():
                print("Os alienígenas chegaram ao fundo!")
                sys.exit()

    def _check_ship_collision(self) -> None:
        """Verifica se a nava colidiu com algum alienigena"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):  # Verifica se a nave colidiu com algum alienígena
            print("A nave foi atingida!")  # Imprime uma mensagem no console indicando que a nave foi atingida
            sys.exit()  # Encerra o jogo
