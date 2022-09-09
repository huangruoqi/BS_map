import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from pydub import AudioSegment

def convert_ogg_to_wav(ogg_path):
    song = AudioSegment.from_ogg(ogg_path)
    song.export("analysis/test.wav", format="wav")
    
levels = os.listdir("levels/")
print()
for index, level in enumerate(levels):
    print(str(index) + ": " + level)
choice = levels[int(input("Please choose one song to analyze: "))]
choice_path = os.path.join("levels/", choice)
files = os.listdir(choice_path)
song_file = list(filter(lambda n: n[len(n)-2:]=="gg", files))[0]
convert_ogg_to_wav(os.path.join(choice_path, song_file))


