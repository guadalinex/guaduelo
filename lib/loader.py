import pygame
from pygame.locals import *

from os import path

if path.exists('/usr/share/guaduelo'):
    BASE_DIR = '/usr/share/guaduelo/data'
else:
    BASE_DIR = './data'

class Loader(object):
    def __init__(self):
        pass

    def load_sound(self,filename):
        filepath = path.join(BASE_DIR,"snd",filename)
        return pygame.mixer.Sound(filepath)

    def load_image(self,filename,alpha=False):
        filepath = path.join(BASE_DIR,"img",filename)
        img = pygame.image.load(filepath)
        if alpha:
            img = img.convert_alpha()
        else:
            img = img.convert()
        return img        

    def load_font(self,filename,size):
        filepath = path.join(BASE_DIR,"fnt",filename)
        fnt = pygame.font.Font(filepath, size)
        return fnt  
