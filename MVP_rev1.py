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
    def __init__(self, note, disp)
    self.note = note
    self.disp = False
    pass

class Controller(object):
    def __init__(self, mode):
        self.model = model

    def input_event(self,event):
        if event.type == #keyboard input:
            for shape in model:
                if shape.note == "a4"

                    CHUNK = 1024
                    if len('a4.wav') < 2:
                        sys.exit(-1)
                    wf = wave.open(a4.wav[1], 'rb')

        elif event.type == #keyboard input:
            for shape in model:
                if shape.note == "b4":
                    CHUNK = 1024
                    if len('b4.wav') < 2:
                        sys.exit(-1)
                    wf = wave.open(b4.wav[1], 'rb')

        #this will play the note selected by the if statement
        # instantiate PyAudio
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

        shape.disp = True

class View(object):
    def __init__(self, model):
        self.model = model

    def shape():
        if shape.disp = True:
        #draw that specific shape



if __name__ ==  "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # window size, as a tuple
    pygame.display.set_caption('Maggie and Aurora')

    shape1 = Shape("a4")
    shape2 = Shape("b4")

    model = [shape1,shape2]


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type ==

        screen.fill((0,0,0)) # RGB tuple for black
        pygame.display.update()

    pygame.quit()
