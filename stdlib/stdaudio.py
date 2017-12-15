"""
stdaudio.py

The stdaudio module defines functions related to audio.
"""

#-----------------------------------------------------------------------

import sys
import numpy
import pygame

#-----------------------------------------------------------------------

_SAMPLES_PER_SECOND = 44100
_SAMPLE_SIZE = -16           # Each sample is a signed 16-bit int
_CHANNEL_COUNT = 1           # 1 => mono, 2 => stereo
_AUDIO_BUFFER_SIZE = 1024    # In number of samples
_CHECK_RATE = 44100          # How often to check the queue

_myBuffer = []
_MY_BUFFER_MAX_LENGTH = 4096 # Determined experimentally.

def wait():
    """
    Wait for the sound queue to become empty.  Informally, wait for the
    currently playing sound to finish.
    """

    # Can have at most one sound in the queue.  So must wait for the
    # queue to become empty before adding a new sound to the queue.

    global _channel
    clock = pygame.time.Clock()
    while _channel.get_queue() is not None:
    #while pygame.mixer.get_busy():
        clock.tick(_CHECK_RATE)

def playSample(s):
    """
    Play sound sample s.
    """
    global _myBuffer
    global _channel
    _myBuffer.append(s)
    if len(_myBuffer) > _MY_BUFFER_MAX_LENGTH:
        temp = []
        for sample in _myBuffer:
            temp.append(numpy.int16(sample * float(0x7fff)))
        samples = numpy.array(temp, numpy.int16)
        sound = pygame.sndarray.make_sound(samples)
        wait()
        _channel.queue(sound)
        _myBuffer = []

def playSamples(a):
    """
    Play all sound samples in array a.
    """
    for sample in a:
        playSample(sample)

def playArray(a):
    """
    This function is deprecated. It has the same behavior as
    stdaudio.playSamples(). Please call stdaudio.playSamples() instead.
    """
    playSamples(a)

def playFile(f):
    """
    Play all sound samples in the file whose name is f.wav.
    """
    a = read(f)
    playSamples(a)
    #sound = pygame.mixer.Sound(fileName)
    #samples = pygame.sndarray.samples(sound)
    #wait()
    #sound.play()

def save(f, a):
    """
    Save all samples in array a to the WAVE file whose name is f.wav.
    """

    # Saving to a WAV file isn't handled by PyGame, so use the
    # standard "wave" module instead.

    import wave
    fileName = f + '.wav'
    temp = []
    for sample in a:
        temp.append(int(sample * float(0x7fff)))
    samples = numpy.array(temp, numpy.int16)
    file = wave.open(fileName, 'w')
    file.setnchannels(_CHANNEL_COUNT)
    file.setsampwidth(2)  # 2 bytes
    file.setframerate(_SAMPLES_PER_SECOND)
    file.setnframes(len(samples))
    file.setcomptype('NONE', 'descrip')  # No compression
    file.writeframes(samples.tostring())
    file.close()

def read(f):
    """
    Read all samples from the WAVE file whose names is f.wav.
    Store the samples in an array, and return the array.
    """
    fileName = f + '.wav'
    sound = pygame.mixer.Sound(fileName)
    samples = pygame.sndarray.samples(sound)
    temp = []
    for i in range(len(samples)):
        temp.append(float(samples[i]) / float(0x7fff))
    return temp

# Initialize PyGame to handle audio.
try:
    pygame.mixer.init(_SAMPLES_PER_SECOND, _SAMPLE_SIZE,
        _CHANNEL_COUNT, _AUDIO_BUFFER_SIZE)
    _channel = pygame.mixer.Channel(0)
except pygame.error:
    stdio.writeln('Could not initialize PyGame')
    sys.exit(1)

#-----------------------------------------------------------------------

def _createTextAudioFile():
    """
    For testing. Create a text audio file.
    """
    notes = [
        7, .270,
        5, .090,
        3, .180,
        5, .180,
        7, .180,
        6, .180,
        7, .180,
        3, .180,
        5, .180,
        5, .180,
        5, .180,
        5, .900,

        5, .325,
        3, .125,
        2, .180,
        3, .180,
        5, .180,
        4, .180,
        5, .180,
        2, .180,
        3, .180,
        3, .180,
        3, .180,
        3, .900,
        ]

    import outstream
    outStream = outstream.OutStream('looney.txt')
    for note in notes:
        outStream.writeln(note)

def _main():
    """
    For testing.
    """
    import os
    import math
    import stdio
    import instream

    _createTextAudioFile()

    stdio.writeln('Creating and playing in small chunks...')
    sps = _SAMPLES_PER_SECOND
    inStream = instream.InStream('looney.txt')
    while not inStream.isEmpty():
        pitch = inStream.readInt()
        duration = inStream.readFloat()
        hz = 440 * math.pow(2, pitch / 12.0)
        N = int(sps * duration)
        notes = []
        for i in range(N+1):
            notes.append(math.sin(2*math.pi * i * hz / sps))
        playSamples(notes)
    wait()

    stdio.writeln('Creating and playing in one large chunk...')
    sps = _SAMPLES_PER_SECOND
    notes = []
    inStream = instream.InStream('looney.txt')
    while not inStream.isEmpty():
        pitch = inStream.readInt()
        duration = inStream.readFloat()
        hz = 440 * math.pow(2, pitch / 12.0)
        N = int(sps * duration)
        for i in range(N+1):
            notes.append(math.sin(2*math.pi * i * hz / sps))
    playSamples(notes)
    wait()

    stdio.writeln('Saving...')
    save('looney', notes)

    stdio.writeln('Reading...')
    notes = read('looney')

    stdio.writeln('Playing an array...')
    playSamples(notes)
    wait()

    stdio.writeln('Playing a file...')
    playFile('looney')
    wait()

    os.remove('looney.wav')
    os.remove('looney.txt')

if __name__ == '__main__':
    _main()
