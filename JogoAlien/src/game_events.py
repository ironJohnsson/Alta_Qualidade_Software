import sys
import pygame



class GameEventHandler:
    def __init__(self, ship, bullet_manager) -> None:
        self.ship = ship
        self.bullet_manager = bullet_manager

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
            self.bullet_manager._fire_bullet()  # Dispara um projétil
    
    def _handle_keyup(self, event: pygame.event.Event) -> None:
        """Responde a eventos de liberação de teclas."""
        if event.key == pygame.K_RIGHT:  # Verifica se a tecla liberada é a seta para a direita
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:  # Verifica se a tecla liberada é a seta para a esquerda
            self.ship.moving_left = False
