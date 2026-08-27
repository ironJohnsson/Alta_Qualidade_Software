import pygame
from bullet import Bullet

class BulletManager:
    """responsável por gerenciar os projéteis disparados pela nave."""
    def __init__(self, screen, settings, ship) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets = pygame.sprite.Group()  # Cria um grupo para armazenar os projéteis disparados pela nave

    def _fire_bullet(self) ->None:
        """Dispara um projétil se o limite de projéteis na tela não for excedido."""
        if len(self.bullets) <self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)  # Cria um novo projétil
            self.bullets.add(new_bullet)  # Adiciona o novo projétil ao grupo de projéteis

    def _update_bullets(self,aliens) -> None:
        self.bullets.update()  # Atualiza a posição de cada projétil no grupo de projéteis
        self._remove_offscreen_bullets()  # Remove projéteis que saíram da tela
        self._check_bullet_alien_collisions(aliens)  # Verifica colisões entre projéteis e alienígenas

    def _remove_offscreen_bullets(self) -> None:
        """Remove projéteis que saíram da tela."""
        for bullet in self.bullets.copy():  # Verifica se algum projétil saiu da tela
            if bullet.rect.bottom <= 0:  # Se o projétil saiu da tela (parte inferior do retângulo do projétil é menor ou igual a 0)
                self.bullets.remove(bullet)  # Remove o projétil do grupo de projéteis

    def _check_bullet_alien_collisions(self, aliens) -> None:
        """Verifica colisões entre projéteis e alienígenas"""
        pygame.sprite.groupcollide(self.bullets, aliens, True, True)
