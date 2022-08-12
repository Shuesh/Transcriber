"""
Get an mp3, convert it to a spectrogram, and transcribe it into sheet music
"""

import os
from tempfile import mktemp
from pydub import AudioSegment      #type: ignore
# from pydub.playback import play
import matplotlib.pyplot as plt     #type: ignore
from scipy.io import wavfile        #type: ignore

#Must have ffmpeg installed
mp3 = "Happy.mp3"
mp3_audio = AudioSegment.from_file(file=mp3, format="mp3") #Read the mp3
mp3_audio = mp3_audio.set_channels(1)
# play(mp3_audio)
wname = mktemp('.wav') #Use a temporary file
mp3_audio.export(wname, format="wav") #Convert to wav format
#Gets the sample frequency (FS) and a data dump. This is a two dimensional array in my case because it has two channels?
FS, data = wavfile.read(wname) #Read the wav file
plt.specgram(data, Fs=FS, NFFT=128, noverlap=0) #Plot
plt.show()
