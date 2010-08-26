import pygame
from pygame.locals import *
import random 

from loader import Loader

class GfxCard(object):
    def __init__(self,pos,card,back,images,snd):
        self.card = card
        self.back = back
        self.images = images
    
        self.pos = pos
        self.rect = pygame.Rect(pos,(90,90))
        self.rect.topleft = self.pos
        self.rect.x += random.randint(-2,2)
        self.rect.y += random.randint(-2,2)        
        self.snd =snd

    def touch_pos(self):
        self.rect.topleft = self.pos
        self.rect.x += random.randint(-2,2)
        self.rect.y += random.randint(-2,2)
        self.snd.play()
        
    def is_clicked(self,pos):
        if self.rect.collidepoint(pos):
            return True
        return False
    
    def draw(self,dest):
        if not self.card.active:
            return
        dest.blit(self.back,self.rect.topleft)
        if self.card.selected:
            dest.blit(self.images[self.card.type],(self.rect.x+5,self.rect.y+5))

class GameBoard(object):
    def __init__(self):
        self.loader = Loader()
        self.desk = self.loader.load_image("back.png")
        self.back = self.desk.copy()

        self.cards1 = self.loader.load_image("cards1.png",True)
        self.cards2 = self.loader.load_image("cards2.png",True)
        
        self.card_back = self.loader.load_image("card.png",True)
        self.card_images = []
        for i in range(18):
            self.card_images.append(self.loader.load_image("img%d.png" % (i+1)))

        self.gfxcards = []
        self.gfxcards_hidden = []
        self.delay = 0

        self.title_fnt = self.loader.load_font("KLEPTOMA.TTF", 60) 
        self.text_fnt = self.loader.load_font("scribble.TTF", 24) 
        self.small_text_fnt = self.loader.load_font("scribble.TTF", 15) 

        self.START_SCREEN = 0
        self.GAME_PLAY = 1
        self.GAME_OVER = 2

        self.card_snd = self.loader.load_sound("card.wav")

        self.goto_start()

    def goto_start(self):
        self.render_start()
        self.state = self.START_SCREEN

    def goto_gameover(self,result):
        self.render_gameover(result)
        self.state = self.GAME_OVER

    def goto_game(self):
        self.state = self.GAME_PLAY
        self.back.blit(self.desk,(0,0))

    def _title(self,text,y,x=400):
        f = self.title_fnt
        
        t = f.render(text, True, (0,0,0))
        r = t.get_rect()
        r.center = (x+4,y+4)
        self.back.blit(t,r.topleft)

        t = f.render(text, True, (255,255,0))
        r = t.get_rect()
        r.center = (x,y)
        self.back.blit(t,r.topleft)

    def _text(self,text,y,x=400):
        f = self.text_fnt        
        t = f.render(text, True, (0,0,0))
        r = t.get_rect()
        r.center = (x+2,y+2)
        self.back.blit(t,r.topleft)
        t = f.render(text, True, (255,255,255))
        r = t.get_rect()
        r.center = (x,y)
        self.back.blit(t,r.topleft)

    def _text2(self,text,y):
        f = self.small_text_fnt        
        t = f.render(text, True, (0,0,0))
        r = t.get_rect()
        r.center = (400+2,y+2)
        self.back.blit(t,r.topleft)
        t = f.render(text, True, (255,255,255))
        r = t.get_rect()
        r.center = (400,y)
        self.back.blit(t,r.topleft)
                
    def render_start(self):
        self.back.blit(self.desk,(0,0))

        r = self.cards1.get_rect()
        r.center = (400,340-10)
        self.back.blit(self.cards1,r.topleft)

        r = self.cards2.get_rect()
        r.bottomleft = (-30,620)
        self.back.blit(self.cards2,r.topleft)
        
        y = 120-10
        self._title("- Guaduelo -",y); y+=50
        self._text("Pincha en cualquier sitio para comenzar",y)
              
        y = 480
        r = 20
        self._text2("Coding and graphics by John Eriksson",y); y+=r
        self._text2("Photos by Jenny Eriksson",y); y+=r
        self._text2("Testing by Jenny and Pelle Eriksson",y); y+=r
        self._text2("Toys from Pelle and Rasmus collections",y); y+=r
        self._text2("Fonts by Simsjeedy and Jakob Fischer",y); y+=r

    def render_gameover(self,result):
        self.back.blit(self.desk,(0,0))
        y = 275 
        x = 300
        t = ["Both win!","You win!","Robot win!"]
        self._title(t[result],y,x); y+=50
        self._text("Click anywhere to play again",y,x)
          
    def set_board(self,cards):
        self.gfxcards = []
        self.gfxcards_hidden = []
        x = 0
        y = 0
        for c in cards:
            xp = 8+x*100
            yp = 5+y*100
            self.gfxcards_hidden.append(GfxCard((xp,yp), c, self.card_back, self.card_images,self.card_snd))
            x+=1
            if x == 6:
                x=0
                y+=1
        self.delay = 0

    def location_to_card(self,pos):
        for gc in self.gfxcards:
            if gc.is_clicked(pos):
                return gc.card
        return None

    def card_to_location(self,card):
        for gc in self.gfxcards:
            if gc.card == card:
                return gc.rect.center
        
    def touch_card(self,card):
        for gc in self.gfxcards:
            if gc.card == card:
                gc.touch_pos()
                
    def is_init_done(self):
        if len(self.gfxcards_hidden) > 0:
            return False
        else:
            return True
        
    def draw(self,dest):
        dest.blit(self.back,(0,0))

        if self.state == self.GAME_PLAY:
            if len(self.gfxcards_hidden):
                if self.delay > 0:
                    self.delay-=1
                else:
                    gx = self.gfxcards_hidden.pop(0)
                    gx.touch_pos()
                    self.gfxcards.append(gx)
                    if len(self.gfxcards_hidden):
                        self.delay=3
            if len(self.gfxcards):
                for gc in self.gfxcards:
                    gc.draw(dest) 
