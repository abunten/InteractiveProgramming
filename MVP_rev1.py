'''''
Interactive Programming: Visual Sound Rev 1

author@ Maggie Rosner & Aurora Bunten

03/01/17
'''''

import pygame
import pyaudio
import wave
import sys

class Controller(object):
    def __init__(self,model):
        self.model = model
    def input_event(self,event):
        if event.type == #keyboard input:
            for model in self.models:
                if model.contains_pt(     ):#whatever the keyboard input above was
                    model.reset()
                    break
        elif event.type == #another Keyboard input
        #same thing


class View(object):
    def __init__(self,model):
        self.model = model

    def notes():

        if key == a:

            CHUNK = 1024
            if len('a4.wav') < 2:
                sys.exit(-1)
            wf = wave.open(a4.wav[1], 'rb')
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

        elif key == b:

                CHUNK = 1024
                if len('b4.wav') < 2:
                    sys.exit(-1)
                wf = wave.open(b4.wav[1], 'rb')
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
                p.terminate
        elif key == c:
                CHUNK = 1024
                if len('c4.wav') < 2:
                    sys.exit(-1)
                wf = wave.open(c4.wav[1], 'rb')
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
                p.terminate
        elif key == d:
                CHUNK = 1024
                if len('d4.wav') < 2:
                    sys.exit(-1)
                wf = wave.open(d4.wav[1], 'rb')
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
                p.terminate
        elif key == e:
                CHUNK = 1024
                if len('e4.wav') < 2:
                    sys.exit(-1)
                wf = wave.open(e4.wav[1], 'rb')
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
                p.terminate
        elif key == f:
                CHUNK = 1024
                if len('f4.wav') < 2:
                    sys.exit(-1)
                wf = wave.open(f4.wav[1], 'rb')
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
                p.terminate
        elif key == g:
                CHUNK = 1024
                if len('g4.wav') < 2:
                    sys.exit(-1)
                wf = wave.open(g4.wav[1], 'rb')
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
                p.terminate
        else:
            return False



if __name__ ==  "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # window size, as a tuple
    pygame.display.set_caption('Maggie and Aurora')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type ==

        screen.fill((0,0,0)) # RGB tuple for black
        pygame.display.update()

    pygame.quit()
