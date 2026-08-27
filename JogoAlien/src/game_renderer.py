import pygame

class GameRenderer:
    """responsável por renderizar os elementos do jogo na tela."""
    def __init__(self, screen, bg_color, ship, aliens, bullets) -> None:
        self.screen = screen
        self.bg_color = bg_color
        self.ship = ship
        self.aliens = aliens
        self.bullets = bullets

    def _render_screen(self) -> None:
        """Redesenha a tela a cada passagem pelo laço"""
        self.screen.fill(self.bg_color)  # Preenche a tela com a cor de fundo
        self.ship.blitme()  # Redesenha a nave em sua posição atual
        self.aliens.draw(self.screen)  # Desenha os alienígenas presentes no grupo de alienígenas na tela
        self._draw_bullets()  # Desenha os projéteis na tela
        pygame.display.flip()  # Atualiza a tela com as mudanças

    def _draw_bullets(self) -> None:
        """Desenha os projéteis na tela"""
        for bullet in self.bullets.sprites():  # Atualiza a posição de cada projétil no grupo de projéteis
            bullet.draw_bullet()  # Desenha cada projétil na tela
