import os
import numpy as np
import json
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from pydub import AudioSegment


def get_data(data_path):
    with open(data_path) as f:
        return json.load(f)


def get_file_with_postfix(files, p):
    return list(filter(lambda n: n[len(n) - len(p) :] == p, files))[0]


test_path = "analysis/test.wav"


def convert_ogg_to_wav(ogg_path):
    song = AudioSegment.from_ogg(ogg_path)
    song.export(test_path, format="wav")


levels = os.listdir("levels/")
print()
for index, level in enumerate(levels):
    print(str(index) + ": " + level)
choice = levels[int(input("Please choose one song to analyze: "))]
choice_path = os.path.join("levels/", choice)
files = os.listdir(choice_path)
song_file = get_file_with_postfix(files, "gg")
convert_ogg_to_wav(os.path.join(choice_path, song_file))

RATE, data = read(test_path)

info_file = get_file_with_postfix(files, "nfo.dat")
info = get_data(os.path.join(choice_path, info_file))
BPM = int(info["_beatsPerMinute"])
difficulties = info["_difficultyBeatmapSets"][0]["_difficultyBeatmaps"]
# for d in difficulties:
map_file = difficulties[0]["_beatmapFilename"]
song_map = get_data(os.path.join(choice_path, map_file))

notes = song_map["_notes"]
print(len(notes))
points = [note["_time"] * 60 * RATE // BPM for note in notes]


f = plt.figure()
f.set_figwidth(16)
f.set_figheight(6)

# plt.subplot(1, 2, 1) # row 1, col 2 index 1
ratio = 1
plt.plot(data[: len(data), 0])
for point in points[: len(points)]:
    plt.plot(point, 0, "ro")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.title("LEFT")

# plt.subplot(1, 2, 2) # row 1, col 2 index 1
# plt.plot(data[:,1])
# plt.xlabel("Sample Index")
# plt.ylabel("Amplitude")
# plt.title("RIGHT")


plt.show()
