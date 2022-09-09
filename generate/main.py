from bs_map import BS_MAP
import os

levels = os.listdir("input/")
# print()
# for index, level in enumerate(levels):
#     print(str(index) + ": " + level)
# choices = input("Please choose songs to generate map(separate by ' '): \n")
# if choices.strip() == '*':
choice_path = os.path.join('./input', 'song.egg')
song_map = BS_MAP()