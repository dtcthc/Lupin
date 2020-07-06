class Key (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_key = pygame.image.load("img/Key.png")
        self.rect = self.imagen_ladronkey.get_rect()
        self.rect.centerx = 20
        self.rect.centery= 30
        

    def dibujar(self,superficie):
        superficie.blit(self.imagen_key, self.rect)
