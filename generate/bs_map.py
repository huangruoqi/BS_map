'''
{
    "_time": 9,
    "_lineIndex": 2,
    "_lineLayer": 0,
    "_type": 1,
    "_cutDirection": 1
}
'''
class BS_MAP:
    def __init__(self, data):
        self.data = data
        sorted_data = sorted(data)
        self.high_amplitude_bound = sorted_data[len(data)//10 * 9]
        self.low_amplitude_bound = sorted_data[len(data)//10]
        self.notes = []

        # consistency for similar parts
        self.abs_sums = [0 for i in data] 
        self.threshold = 1000 # margin of sums
        self.interval = 20 # beats
        # self.obstacles = []
        # self.sliders = []

    def insert(self, t, x, y, p, d):
        self.notes.append({
            "_time": t,
            "_lineIndex": x,
            "_lineLayer": y,
            "_type": p,
            "_cutDirection": d
        })

    def generate(self):
        print(self.notes)

    def build(self):
        index = 0
        last = len(self.data)
        while index < last:
            index+=1
