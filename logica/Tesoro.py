import pygame

class Tesoro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_tesoro = pygame.image.load("img/Tesoro.png")
        self.rect = self.imagen_tesoro.get_rect()
        self.rect.centerx = 100
        self.rect.centery= 150
        self.velocidad = 0

    def dibujar(self,superficie):
        superficie.blit(self.imagen_tesoro, self.rect)
