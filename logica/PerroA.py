import pygame

class PerroA (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_perroA = pygame.image.load("img/PerroA.png")
        self.rect = self.imagen_perroA.get_rect()
        self.rect.centerx = 50
        self.rect.centery= 20
        self.velocidad = 10

    def dibujar(self,superficie):
        superficie.blit(self.imagen_perroA, self.rect)
