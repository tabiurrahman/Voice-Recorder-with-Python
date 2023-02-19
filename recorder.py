#import all required Libraries

import sounddevice as sound
from scipy.io.wavfile import write
import wavio as wc

freq=44100

#Duration is given in seconds
duration=10

recording=sound.rec(int(duration*freq),samplerate=freq,channels=2)

sound.wait()
write("recording.wav",freq,recording)