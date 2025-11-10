#   https://www.geeksforgeeks.org/python/create-a-voice-recorder-using-python/

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
freq = 44100
duration = 5 
recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
sd.wait()
write("recording0.wav", freq, recording)
wv.write("recording1.wav", recording, freq, sampwidth=1)