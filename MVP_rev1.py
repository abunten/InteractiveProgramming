'''''
Interactive Programming: Visualizing Music

author@ Maggie Rosner & Aurora Bunten

03/01/17
'''''

import pygame
import pyaudio
import wave
import sys

class Shape(object):
    '''
    the shaps class creates objects that are defined by the note they represent
    '''
    def __init__(self, note):
        self.note = note
        self.disp = False


class Controller(object):
    '''
    The controller class calls a specific shape object based on the key pressed.
    the shape is associated with a specific note which will change the shape_disp
    to True and play the wave file associated with the note.
    '''
    def __init__(self, model):
        self.model = model
        self.octave = 4     #sets the default octave to the 4th (middle C)
    def input_event(self,event):
        is_audio_event = False  #sets the initial condition for an event (shape display) to False
        '''
        the conditions below set the octave based on certain number keys that are pressed
        '''
        if event.type == pygame.KEYDOWN: #if a key is pressed
            if event.key == pygame.K_5: #if the number 5 key is pressed
                self.octave = 5 #play notes in the 5th octave
            elif event.key == pygame.K_4:   #if the number 4 key is pressed
                self.octave = 4 #play notes in the 4th octave
            elif event.key == pygame.K_3:   #if the number 3 key is pressed
                self.octave = 3 #play notes in the 3rd octave

            if self.octave == 4:
                '''
                If you push down crtl and the key assigned the note played will be flat
                in that octave. If you push down Shift and the key assigned to that note
                the note played will be a sharp in that octave. If you simply push down
                the key assigned to the note it will play the natural note. Each differet
                note has a different wave file assigned to it that will play when the
                correct key/keys are pressed.
                '''
                if event.key == pygame.K_a and (event.mod & pygame.KMOD_CTRL):
                    #print('aaaaaabbbbbbb444')
                    for shape in self.model:
                        if shape.note == "ab4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('ab4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_a and (event.mod & pygame.KMOD_SHIFT):
                    #print('aa####444')
                    for shape in self.model:
                        if shape.note == "a#4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('a#4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_a:
                    #print('gooo')
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
                    for shape in self.model:
                        if shape.note == "cb4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('cb4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_d and (event.mod & pygame.KMOD_SHIFT):
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
                    for shape in self.model:
                        if shape.note == "db4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('db4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_f and (event.mod & pygame.KMOD_SHIFT):
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
                    for shape in self.model:
                        if shape.note == "eb4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('eb4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_g and (event.mod & pygame.KMOD_SHIFT):
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
                    for shape in self.model:
                        if shape.note == "fb4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('fb4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_h and (event.mod & pygame.KMOD_SHIFT):
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
                    for shape in self.model:
                        if shape.note == "gb4":
                            shape.disp = True
                            effect = pygame.mixer.Sound('gb4.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_j and (event.mod & pygame.KMOD_SHIFT):
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
#second octave starts here
            elif self.octave == 5:
                '''
                This code does the same thing as the code above, however it
                now will play notes in the 5th octave (one octave higher).
                '''
                if event.key == pygame.K_a and (event.mod & pygame.KMOD_SHIFT):
                    #print('aa####')
                    for shape in self.model:
                        if shape.note == "a#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('a#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_a and (event.mod & pygame.KMOD_CTRL):
                    #print('aabbbbb')
                    for shape in self.model:
                        if shape.note == "ab5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('ab5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_a:
                    #print('aaaaaaaaaaa')
                    for shape in self.model:
                        if shape.note == "a5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('a5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_s and (event.mod & pygame.KMOD_SHIFT):
                    for shape in self.model:
                        if shape.note == "b#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('b#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_s and (event.mod & pygame.KMOD_CTRL):
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
                    for shape in self.model:
                        if shape.note == "c#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('c#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_d and (event.mod & pygame.KMOD_CTRL):
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
                    for shape in self.model:
                        if shape.note == "d#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('d#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_f and (event.mod & pygame.KMOD_CTRL):
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
                    for shape in self.model:
                        if shape.note == "e#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('e#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_g and (event.mod & pygame.KMOD_CTRL):
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
                    for shape in self.model:
                        if shape.note == "f#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('f#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_h and (event.mod & pygame.KMOD_CTRL):
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
                    for shape in self.model:
                        if shape.note == "g#5":
                            shape.disp = True
                            effect = pygame.mixer.Sound('g#5.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_j and (event.mod & pygame.KMOD_SHIFT):
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
#lower 3rd octave
            elif self.octave == 3:
                '''
                Same code as above, however it now will play notes in the 3rd octive
                (one below middle C).
                '''
                if event.key == pygame.K_a and (event.mod & pygame.KMOD_SHIFT):
                    #print('aa####3333')
                    for shape in self.model:
                        if shape.note == "a#3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('a#3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_a and (event.mod & pygame.KMOD_CTRL):
                    #print('aabbbb333')
                    for shape in self.model:
                        if shape.note == "ab3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('ab3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_a:
                    #print('aaaaaaaa333333')
                    for shape in self.model:
                        if shape.note == "a3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('a3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_s and (event.mod & pygame.KMOD_SHIFT):
                    for shape in self.model:
                        if shape.note == "b#3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('b#3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_s and (event.mod & pygame.KMOD_CTRL):
                    for shape in self.model:
                        if shape.note == "bb3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('bb3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_s:
                    for shape in self.model:
                        if shape.note == "b3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('b3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_d and (event.mod & pygame.KMOD_SHIFT):
                    for shape in self.model:
                        if shape.note == "c#3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('c#3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_d and (event.mod & pygame.KMOD_CTRL):
                    for shape in self.model:
                        if shape.note == "cb3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('cb3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_d:
                    for shape in self.model:
                        if shape.note == "c3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('c3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_f and (event.mod & pygame.KMOD_SHIFT):
                    for shape in self.model:
                        if shape.note == "d#3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('d#3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_f and (event.mod & pygame.KMOD_CTRL):
                    for shape in self.model:
                        if shape.note == "db3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('db3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_f:
                    for shape in self.model:
                        if shape.note == "d3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('d3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_g and (event.mod & pygame.KMOD_SHIFT):
                    for shape in self.model:
                        if shape.note == "e#3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('e#3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_g and (event.mod & pygame.KMOD_CTRL):
                    for shape in self.model:
                        if shape.note == "eb3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('eb3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_g:
                    for shape in self.model:
                        if shape.note == "e3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('e3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_h and (event.mod & pygame.KMOD_SHIFT):
                    for shape in self.model:
                        if shape.note == "f#3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('f#3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_h and (event.mod & pygame.KMOD_CTRL):
                    for shape in self.model:
                        if shape.note == "fb3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('fb3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_h:
                    for shape in self.model:
                        if shape.note == "f3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('f3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_j and (event.mod & pygame.KMOD_SHIFT):
                    for shape in self.model:
                        if shape.note == "g#3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('g#3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_j and (event.mod & pygame.KMOD_SHIFT):
                    for shape in self.model:
                        if shape.note == "gb3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('gb3.wav')
                            effect.play()
                        else:
                            shape.disp = False
                elif event.key == pygame.K_j:
                    for shape in self.model:
                        if shape.note == "g3":
                            shape.disp = True
                            effect = pygame.mixer.Sound('g3.wav')
                            effect.play()
                        else:
                            shape.disp = False

class View(object):
    '''
    The View class hold the different shapes and colors for every different not
    in the three octaves. if the shape specified by a cretai key press is pressed
    the shape assigned to that note will be called and the shape and color assigned
    th the object will be displayed as the sound plays.
    '''
    def __init__(self, model, surface):
        self.model = model
        self.surface = surface

    def draw(self):
        for shape in self.model: #for the specific shape in the model list
            if shape.note == "a4": #if it is a specific note
                if shape.disp == True: #turn the disp (defalting to False) to True
                    pygame.draw.circle(self.surface, (255,0,0), (100,100), 100) #disp shape/color
            elif shape.note == "a#4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,100,0), (100,100), 100)
            elif shape.note == "ab4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,3,100), (100,100), 100)
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
            elif shape.note == "a3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "ab3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "a#3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "b3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,255,153), (100,100), 100)
            elif shape.note == "bb3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "b#3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "c3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,128,0), (100,100), 100)
            elif shape.note == "cb3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "c#3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "d3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,128), (100,100), 100)
            elif shape.note == "db3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "d#3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "eb3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "e#3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "e3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (128,0,255), (100,100), 100)
            elif shape.note == "f3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,0,127), (100,100), 100)
            elif shape.note == "fb3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "f#3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "g3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,255,51), (100,100), 100)
            elif shape.note == "gb3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "g#3":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)

if __name__ ==  "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) #window size, as a tuple
    pygame.display.set_caption('Music Visualization by Maggie and Aurora')


    shape1 = Shape("a4") #each shape is an object that is created to represent each different note
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
    shape15 = Shape("a3")
    shape15s = Shape("a#3")
    shape15b = Shape("ab3")
    shape16 = Shape("b3")
    shape16b = Shape("bb3")
    shape16s = Shape("b#3")
    shape17 = Shape("c3")
    shape17b = Shape("cb3")
    shape17s = Shape("c#3")
    shape18 = Shape("d3")
    shape18s = Shape("d#3")
    shape18b = Shape("db3")
    shape19 = Shape("e3")
    shape19b = Shape("eb3")
    shape19s = Shape("e#3")
    shape20 = Shape("f3")
    shape20b = Shape("fb3")
    shape20s = Shape("f#3")
    shape21 = Shape("g3")
    shape21b = Shape("gb3")
    shape21s = Shape("g#3")

    # model is a list containing every shape object
    model = [shape1, shape1b, shape1s, shape2, shape2b, shape2s, shape3,
    shape3b, shape3s, shape4, shape4b, shape4s, shape5, shape5b, shape5s,
    shape6, shape6b, shape6s, shape7, shape7b, shape7s, shape8, shape8b,
    shape8s, shape9, shape9b, shape9s, shape10, shape10b, shape10s, shape11,
    shape11b, shape11s, shape12, shape12b, shape12s, shape13, shape13b,
    shape13s, shape14, shape14b, shape14s, shape15, shape15s, shape15b,
    shape16, shape16b, shape16s, shape17, shape17s, shape17b, shape18,
    shape18b, shape18s, shape19, shape19s, shape19b, shape20, shape20s,
    shape20b, shape21, shape21s, shape21b]

    my_controller = Controller(model)
    my_screen = View(model, screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                my_controller.input_event(event)
        screen.fill((0,0,0)) #screen will start out black
        my_screen.draw()
        pygame.display.update()

    pygame.quit()
