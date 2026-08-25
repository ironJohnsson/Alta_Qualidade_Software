import sys

import pygame

from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self):
        """Construtor da classe que inicializa o jogo e cria os recursos básicos"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Criando uma instância da classe Ship para representar a nave espacial
        self.ship = Ship(self.screen, self.settings)

        # Mudando a cor do plano de fundo em RGB
        self.bg_color = self.settings.bg_color

        self.bullets = (
            pygame.sprite.Group()
        )  # Cria um grupo para armazenar os projéteis disparados pela nave

        self.aliens = (
            pygame.sprite.Group()
        )  # Cria um grupo para armazenar os alienígenas presentes no jogo

    def _check_events(self):
        """Responde a eventos de pressionamento de teclas e mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Detecta quando uma tecla é pressionada
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:  # Detecta quando uma tecla é liberada
                self._handle_keyup(event)

    def _handle_keydown(self, event: pygame.event.Event) ->None:
        """Responde a eventos de pressionamento de teclas."""
        if event.key == pygame.K_RIGHT:  # Verifica se a tecla pressionada é a seta para a direita
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # Verifica se a tecla pressionada é a seta para a esquerda
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:  # Verifica se a tecla pressionada é a barra de espaço
            self._fire_bullet()  # Dispara um projétil

    def _handle_keyup(self, event: pygame.event.Event) -> None:
        """Responde a eventos de liberação de teclas."""
        if event.key == pygame.K_RIGHT:  # Verifica se a tecla liberada é a seta para a direita
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:  # Verifica se a tecla liberada é a seta para a esquerda
            self.ship.moving_left = False

    def _fire_bullet(self) ->None:
        """Dispara um projétil se o limite de projéteis na tela não for excedido."""
        if len(self.bullets) <self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)  # Cria um novo projétil
            self.bullets.add(new_bullet)  # Adiciona o novo projétil ao grupo de projéteis

    def _update_bullets(self) -> None:
        self.bullets.update()  # Atualiza a posição de cada projétil no grupo de projéteis
        self._remove_offscreen_bullets()  # Remove projéteis que saíram da tela
        self._check_bullet_alien_collisions()  # Verifica colisões entre projéteis e alienígenas

    def _remove_offscreen_bullets(self) -> None:
        """Remove projéteis que saíram da tela."""
        for bullet in self.bullets.copy():  # Verifica se algum projétil saiu da tela
            if bullet.rect.bottom <= 0:  # Se o projétil saiu da tela (parte inferior do retângulo do projétil é menor ou igual a 0)
                self.bullets.remove(bullet)  # Remove o projétil do grupo de projéteis

    def _check_bullet_alien_collisions(self) -> None:
        """Verifica colisões entre projéteis e alienígenas"""
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _update_aliens(self) -> None:
        """Verifica se a frota de alienígenas está em uma borda da tela e atualiza suas posições."""
        self._check_fleet_edges()  # Verifica se algum alienígena atingiu a borda da tela
        self.aliens.update()  # Atualiza a posição de cada alienígena no

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

    def _check_ship_collision(self) -> None:
        """Verifica se a nava colidiu com algum alienigena"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):  # Verifica se a nave colidiu com algum alienígena
            print("A nave foi atingida!")  # Imprime uma mensagem no console indicando que a nave foi atingida
            sys.exit()  # Encerra o jogo

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

    def _update_game_state(self) -> None:
        """Atualiza a posição da nave, dos projeteis e dos alienigenas"""
        self.ship.update()  # Atualiza a posição da nave com base na variável de controle
        self._update_bullets()  # Atualiza os projéteis e trata colisões
        self._update_aliens()  # Atualiza os alienígenas e trata as bordas da tela
        self._check_ship_collision()  # Verifica se a nave colidiu com algum alienígena

    def create_fleet(self):
        """Cria uma frota de alienígenas."""
        # Cria um alienígena e calcula o número de alienígenas em uma linha
        # O espaçamento entre os alienígenas é igual a um alienígena
        alien = Alien(self.screen, self.settings)
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
            # Cria a primeira linha de alienígenas
            for alien_number in range(number_aliens_x):
                # Cria um alienígena e o posiciona na linha
                alien = Alien(self.screen, self.settings)
                alien.x = alien_width + 2 * alien_width * alien_number
                alien.rect.x = alien.x
                alien.y = alien_height + 2 * alien_height * row_number
                alien.rect.y = alien.y
                self.aliens.add(alien)

    def run_game(self):
        """Cria um laço de repetição para a tela sempre ficar visível até
        que o usuário decida fechar a janela."""

        self.create_fleet()  # Cria a frota de alienígenas para ser desenhada na tela

        while True:
            self._check_events()  # Verifica eventos de pressionamento de teclas e mouse
            self._update_game_state()  # Atualiza a posição da nave, dos projéteis e dos alienígenas
            self._render_screen()  # Redesenha a tela a cada passagem pelo laço
            

if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
