class Scale:
    CHROMATIC_WITH_SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    CHROMATIC_WITH_FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    DIATONIC_SHARPS = ('A', 'a', 'C', 'G', 'f#')


    def __init__(self, tonic):
        self.tonic = tonic

    def chromatic(self):
        if self.tonic in self.DIATONIC_SHARPS:
            tonic = self.tonic[0].upper() + self.tonic[1:]
            index = Scale.CHROMATIC_WITH_SHARPS.index(tonic)
            return Scale.CHROMATIC_WITH_SHARPS[index:] + Scale.CHROMATIC_WITH_SHARPS [:index]
        else:
            tonic = self.tonic[0].upper() + self.tonic[1:]
            index = Scale.CHROMATIC_WITH_FLATS.index(tonic)
            return Scale.CHROMATIC_WITH_FLATS[index:] + Scale.CHROMATIC_WITH_FLATS [:index]

    def interval(self, intervals):
        chromatic = self.chromatic()

        i = 0
        scale = []
        for interval in intervals:
            scale.append(chromatic[i])
            if interval == 'm':
                i += 1
            elif interval == 'M':
                i += 2
            elif interval == 'A':
                i += 3

        return scale
