class Scale:
    CHROMATIC_SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    CHROMATIC_FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    DIATONIC_SHARPS = ('A', 'a', 'C', 'G', 'f#')

    INTERVAL_DISTANCES = ('m', 'M', 'A')


    def __init__(self, tonic):
        self.tonic = tonic
        self.scale = self._get_scale_by_tonic()
        self.index = self.scale.index(self.tonic.capitalize())

    def chromatic(self):
        return self.scale[self.index:] + self.scale[:self.index]

    def interval(self, intervals):
        chromatic = self.chromatic()

        i = 0
        scale = []
        for interval in intervals:
            scale.append(chromatic[i])
            i += self.INTERVAL_DISTANCES.index(interval)+1

        return scale

    def _get_scale_by_tonic(self):
        if self.tonic in self.DIATONIC_SHARPS:
            return self.CHROMATIC_SHARPS
        else:
            return self.CHROMATIC_FLATS
