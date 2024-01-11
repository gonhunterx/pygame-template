import pygame, os 
from states.state import State

class Chest():
    def __init__(self, color:int, game, x:int, y:int):
        State.__init__(self, game)
        self.game = game
        self.img = pygame.Surface((40, 40))
        self.img.fill(color)
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = x, y
        
    def render(self):
        self.game.screen(self.img, (self.rect.x, self.rect.y))
        