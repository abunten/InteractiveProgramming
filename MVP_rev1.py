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

    def input_event(self,event):
        is_audio_event = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                for shape in self.model:
                    if shape.note == "a4":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('a4.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_b:
                for shape in self.model:
                    if shape.note == "b4":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('b4.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_c:
                for shape in self.model:
                    if shape.note == "c4":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('c4.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_d:
                for shape in self.model:
                    if shape.note == "d4":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('d4.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_e:
                for shape in self.model:
                    if shape.note == "e4":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('e4.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_f:
                for shape in self.model:
                    if shape.note == "f4":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('f4.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_g:
                for shape in self.model:
                    if shape.note == "g4":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('g4.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_h:
                for shape in self.model:
                    if shape.note == "a5":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('a5.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_i:
                for shape in self.model:
                    if shape.note == "b5":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('b5.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_j:
                for shape in self.model:
                    if shape.note == "c5":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('c5.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_k:
                for shape in self.model:
                    if shape.note == "d5":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('d5.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_l:
                for shape in self.model:
                    if shape.note == "e5":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('e5.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_m:
                for shape in self.model:
                    if shape.note == "f5":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('f5.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
            elif event.key == pygame.K_n:
                for shape in self.model:
                    if shape.note == "g5":
                        shape.disp = True
                        CHUNK = 1024
                        wf = wave.open('g5.wav', 'rb')
                        is_audio_event = True
                    else:
                        shape.disp = False
        #this will play the note selected by the if statement
        # instantiate PyAudio
        if is_audio_event:
            p = pyaudio.PyAudio()
            # open stream
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            # read data
            data = wf.readframes(CHUNK)
            # play stream (3)
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(CHUNK)
            # stop stream (4)
            stream.stop_stream()
            stream.close()
            # close PyAudio (5)
            p.terminate()

class View(object):
    def __init__(self, model, surface):
        self.model = model
        self.surface = surface

    def draw(self):
        for shape in self.model:
            if shape.note == "a4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,0,0), (100,100), 100)
                    #print("drawing a4")
            elif shape.note == "b4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,0), (100,100), 100)
            elif shape.note == "c4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,0,255), (100,100), 100)
            elif shape.note == "d4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,51,255), (100,100), 100)
            elif shape.note == "e4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (51,255,153), (100,100), 100)
            elif shape.note == "f4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,153,51), (100,100), 100)
            elif shape.note == "g4":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,153,255), (100,100), 100)
            elif shape.note == "a5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (153,255,255), (100,100), 100)
            elif shape.note == "b5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,255,153), (100,100), 100)
            elif shape.note == "c5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,128,0), (100,100), 100)
            elif shape.note == "d5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (0,255,128), (100,100), 100)
            elif shape.note == "e5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (128,0,255), (100,100), 100)
            elif shape.note == "f5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,0,127), (100,100), 100)
            elif shape.note == "g5":
                if shape.disp == True:
                    pygame.draw.circle(self.surface, (255,255,51), (100,100), 100)

if __name__ ==  "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # window size, as a tuple
    pygame.display.set_caption('Maggie and Aurora')


    shape1 = Shape("a4") #"a4" == note
    shape2 = Shape("b4")
    shape3 = Shape("c4")
    shape4 = Shape("d4")
    shape5 = Shape("e4")
    shape6 = Shape("f4")
    shape7 = Shape("g4")
    shape8 = Shape("a5")
    shape9 = Shape("b5")
    shape10 = Shape("c5")
    shape11 = Shape("d5")
    shape12 = Shape("e5")
    shape13 = Shape("f5")
    shape14 = Shape("g5")

    model = [shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9, shape10, shape11, shape12, shape13, shape14]

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
