class Scale:
    CHROMATIC_WITH_SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    CHROMATIC_WITH_FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']


    def __init__(self, tonic):
        self.tonic = tonic

    def chromatic(self):
        if self.tonic in ('A', 'a', 'C', 'G', 'f#'):
            tonic = self.tonic[0].upper() + self.tonic[1:]
            index = Scale.CHROMATIC_WITH_SHARPS.index(tonic)
            return Scale.CHROMATIC_WITH_SHARPS[index:] + Scale.CHROMATIC_WITH_SHARPS [:index]
        else:
            tonic = self.tonic[0].upper() + self.tonic[1:]
            index = Scale.CHROMATIC_WITH_FLATS.index(tonic)
            return Scale.CHROMATIC_WITH_FLATS[index:] + Scale.CHROMATIC_WITH_FLATS [:index]

    def interval(self, intervals):
        chromatic = self.chromatic()
        scale = []

        i = 0
        for interval in intervals:
            scale.append(chromatic[i])
            if interval == 'M':
                i += 2
            elif interval == 'A':
                i += 3
            else:
                i += 1

        return scale
