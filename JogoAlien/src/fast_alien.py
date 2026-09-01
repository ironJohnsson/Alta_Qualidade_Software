from alien import Alien

class FastAlien(Alien):
    """Representa um alienígena rápido que se move mais rapidamente do que os alienígenas normais."""

    def update(self) -> None:
        self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction  # Move o alienígena para a direita ou esquerda com base na direção da frota, mas mais rápido
        self.rect.x = self.x  # Atualiza a posição do rect do alienígena com base na nova coordenada x