import pygame

class PuertaBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_puertaBlock = pygame.image.load("img/PuertaBlock.png")
        self.rect = self.imagen_puertaBlock.get_rect()
        self.rect.centerx = 10
        self.rect.centery= 10
        self.velocidad = 0

    def dibujar(self,superficie):
        superficie.blit(self.imagen_puertaBlock, self.rect)
