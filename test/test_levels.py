import os
from utils import get_data, get_file_with_postfix

levels_path = "./levels"
def test_levels_exists():
    assert os.path.isdir(levels_path)
    assert len(os.listdir(levels_path))

def test_songs_map():
    songs = os.listdir(levels_path)
    for song in songs:
        assert check_one_song(os.path.join(levels_path, song))

'''
{
    "_time": 9,
    "_lineIndex": 2,
    "_lineLayer": 0,
    "_type": 1,
    "_cutDirection": 1
}
'''
def check_one_song(song_path):
    files = os.listdir(song_path)
    info_file = get_file_with_postfix(files, "nfo.dat")
    info = get_data(os.path.join(song_path, info_file))
    difficulties = info["_difficultyBeatmapSets"][0]["_difficultyBeatmaps"]
    map_file = difficulties[0]["_beatmapFilename"]
    song_map = get_data(os.path.join(song_path, map_file))
    notes = song_map["_notes"]
    for note in notes:
        t = int(note.get("_time")) >= 0
        x = 0 <= int(note.get("_lineIndex")) <= 3
        y = 0 <= int(note.get("_lineLayer")) <= 2
        p = int(note.get("_type")) in [0, 1, 3]
        d = 0 <= int(note.get("_cutDirection")) <= 8
        if not all([t, x, y, p, d]):
            return False
    return True
