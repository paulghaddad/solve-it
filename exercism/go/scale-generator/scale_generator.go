package scale

import "strings"

var (
	sharps          = []string{"A", "B", "C", "D", "E", "G", "F#", "f#", "a", "e", "b", "c#", "g#", "d#"}
	intervals       = " mMA"
	chromaticSharps = []string{"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"}
	chromaticFlats  = []string{"F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"}
)

// Scale returns the diatonic scale for a given tonic and interval
func Scale(tonic, interval string) []string {
	chromatic := chromaticForTonic(tonic)

	if interval == "" {
		return chromatic
	}

	diatonic := make([]string, len(interval))

	i := startPosition(chromatic, strings.Title(tonic))

	lenChromatic := len(chromatic)
	for j, space := range interval {
		diatonic[j] = chromatic[i%lenChromatic]
		i += strings.IndexRune(intervals, space)
	}
	return diatonic
}

func chromaticForTonic(tonic string) []string {
	if contains(sharps, tonic) {
		return chromaticSharps
	}
	return chromaticFlats
}

func startPosition(scale []string, tonic string) int {
	for i, val := range scale {
		if val == tonic {
			return i
		}
	}
	return -1
}

func contains(list []string, item string) bool {
	for _, el := range list {
		if el == item {
			return true
		}
	}
	return false
}
