'''''
Interactive Programming: Visual Sound Rev 1

author@ Maggie Rosner & Aurora Bunten

03/01/17
'''''

import pygame
import pyaudio
import wave
import sys

class Shape(object):
    def __init__(self, note):
        self.note = note
        self.disp = False


class Controller(object):
    def __init__(self, model):
        self.model = model
        self.octive = 4
    def input_event(self,event):
        is_audio_event = False

        #keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_5:#next octive starts her
                self.octive = 5
            elif event.key == pygame.K_4:
                self.octive = 4

            if self.octive == 4:
                if event.key == pygame.K_a and (event.mod & pygame.KMOD_CTRL):
                    print('aaaaaaaaaaaaaaaa')
                    for shape in self.model:
                        if shape.note == "ab4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('ab4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_a and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "a#4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('a#4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_a:
                    print('gooo')
                    for shape in self.model:
                        if shape.note == "a4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('a4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_s and (event.mod & pygame.KMOD_CTRL): #working here
                    for shape in self.model:
                        if shape.note == "bb4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('bb4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_s and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "b#4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('b#4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_s:
                    for shape in self.model:
                        if shape.note == "b4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('b4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_d and (event.mod & pygame.KMOD_CTRL):
                    print('aaaaaaaaaaaaaaaa')
                    for shape in self.model:
                        if shape.note == "cb4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('cb4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_d and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "c#4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('c#4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_d:
                    for shape in self.model:
                        if shape.note == "c4":
                            shape.disp = True
                            CHUNK = 1024
                            effect = pygame.mixer.Sound('c4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_f and (event.mod & pygame.KMOD_CTRL):
                    print('aaaaaaaaaaaaaaaa')
                    for shape in self.model:
                        if shape.note == "db4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('db4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_f and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "d#4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('d#4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_f:
                    for shape in self.model:
                        if shape.note == "d4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('d4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_g and (event.mod & pygame.KMOD_CTRL):
                    print('aaaaaaaaaaaaaaaa')
                    for shape in self.model:
                        if shape.note == "eb4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('eb4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_g and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "e#4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('e#4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_g:
                    for shape in self.model:
                        if shape.note == "e4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('e4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_h and (event.mod & pygame.KMOD_CTRL):
                    print('aaaaaaaaaaaaaaaa')
                    for shape in self.model:
                        if shape.note == "fb4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('fb4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_h and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "f#4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('f#4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_h:
                    for shape in self.model:
                        if shape.note == "f4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('f4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_j and (event.mod & pygame.KMOD_CTRL):
                    print('aaaaaaaaaaaaaaaa')
                    for shape in self.model:
                        if shape.note == "gb4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('gb4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_j and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "g#4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('g#4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_j:
                    for shape in self.model:
                        if shape.note == "g4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('g4.wav')
                            effect.play()
                        else:
                            shape.disp = False
#second octive starts here
            elif self.octive == 5:
                if event.key == pygame.K_a and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "a#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('a#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_a and (event.mod & pygame.KMOD_CTRL):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "ab5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('ab5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_a:
                    for shape in self.model:
                        if shape.note == "a5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('a5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_s and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "b#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('b#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_s and (event.mod & pygame.KMOD_CTRL):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "bb5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('bb5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_s:
                    for shape in self.model:
                        if shape.note == "b5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('b5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_d and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "c#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('c#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_d and (event.mod & pygame.KMOD_CTRL):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "cb5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('cb5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_d:
                    for shape in self.model:
                        if shape.note == "c5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('c5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_f and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "d#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('d#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_f and (event.mod & pygame.KMOD_CTRL):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "db5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('db5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_f:
                    for shape in self.model:
                        if shape.note == "d5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('d5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_g and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "e#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('e#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_g and (event.mod & pygame.KMOD_CTRL):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "eb5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('eb5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_g:
                    for shape in self.model:
                        if shape.note == "e5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('e5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_h and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "f#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('f#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_h and (event.mod & pygame.KMOD_CTRL):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "fb5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('fb5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_h:
                    for shape in self.model:
                        if shape.note == "f5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('f5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_j and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "g#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('g#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_j and (event.mod & pygame.KMOD_SHIFT):
                    print('aa####$$$')
                    for shape in self.model:
                        if shape.note == "gb5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('gb5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_j:
                    for shape in self.model:
                        if shape.note == "g5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('g5.wav')
                            effect.play()
                        else:
                            shape.disp = False
        #this will play the note selected by the if statement
        # instantiate PyAudio

class View(object):
    def __init__(self, model, surface):
        self.model = model
        self.surface = surface

    def draw(self):
        for shape in self.model:
            if shape.note == "a4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,0,0), (100,100), 100)
            elif shape.note == "a#4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,3,0), (100,100), 100)
            elif shape.note == "ab4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,3,0), (100,100), 100)
            elif shape.note == "b4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "bb4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "b#4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "c4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,0,255), (100,100), 100)
            elif shape.note == "cb4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "c#4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "d4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,51,255), (100,100), 100)
            elif shape.note == "db4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "d#4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "e4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (51,255,153), (100,100), 100)
            elif shape.note == "eb4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "e#4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "f4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "fb4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,153,51), (100,100), 100)
            elif shape.note == "f#4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "g4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "gb4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,153,255), (100,100), 100)
            elif shape.note == "g#4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "a5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "ab5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "a#5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "b5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,255,153), (100,100), 100)
            elif shape.note == "bb5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "b#5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "c5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,128,0), (100,100), 100)
            elif shape.note == "cb5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "c#5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "d5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,128), (100,100), 100)
            elif shape.note == "db5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "d#5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "eb5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "e#5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "e5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (128,0,255), (100,100), 100)
            elif shape.note == "f5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,0,127), (100,100), 100)
            elif shape.note == "fb5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "f#5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "g5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,255,51), (100,100), 100)
            elif shape.note == "gb5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "g#5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)

if __name__ ==  "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # window size, as a tuple
    pygame.display.set_caption('Maggie and Aurora')


    shape1 = Shape("a4")
    shape1s = Shape("a#4")
    shape1b = Shape("ab4")
    shape2 = Shape("b4")
    shape2s = Shape("b#4")
    shape2b = Shape("bb4")
    shape3 = Shape("c4")
    shape3s = Shape("c#4")
    shape3b = Shape("cb4")
    shape4 = Shape("d4")
    shape4s = Shape("d#4")
    shape4b = Shape("db4")
    shape5 = Shape("e4")
    shape5s = Shape("e#4")
    shape5b = Shape("eb4")
    shape6 = Shape("f4")
    shape6s = Shape("f#4")
    shape6b = Shape("fb4")
    shape7 = Shape("g4")
    shape7s = Shape("g#4")
    shape7b = Shape("gb4")
    shape8 = Shape("a5")
    shape8b = Shape("ab5")
    shape8s = Shape("a#5")
    shape9 = Shape("b5")
    shape9b = Shape("bb5")
    shape9s = Shape("b#5")
    shape10 = Shape("c5")
    shape10b = Shape("cb5")
    shape10s = Shape("c#5")
    shape11 = Shape("d5")
    shape11b = Shape("db5")
    shape11s = Shape("d#5")
    shape12 = Shape("e5")
    shape12b = Shape("eb5")
    shape12s = Shape("e#5")
    shape13 = Shape("f5")
    shape13b = Shape("fb5")
    shape13s = Shape("f#5")
    shape14 = Shape("g5")
    shape14b = Shape("gb5")
    shape14s = Shape("g#5")

    model = [shape1, shape1b, shape1s, shape2, shape2b, shape2s, shape3, shape3b, shape3s, shape4, shape4b, shape4s, shape5, shape5b, shape5s, shape6, shape6b, shape6s, shape7, shape7b, shape7s, shape8, shape8b, shape8s, shape9, shape9b, shape9s, shape10, shape10b, shape10s, shape11, shape11b, shape11s, shape12, shape12b, shape12s, shape13, shape13b, shape13s, shape14, shape14b, shape14s]

    my_controller = Controller(model)
    my_screen = View(model, screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                my_controller.input_event(event)
        screen.fill((0,0,0)) # RGB tuple for black
        my_screen.draw()
        pygame.display.update()

    pygame.quit()
