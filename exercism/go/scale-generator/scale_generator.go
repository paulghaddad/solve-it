package scale

import "strings"

var (
	sharps          = []string{"C", "G", "f#", "a", "A"}
	intervals       = map[rune]int{'m': 1, 'M': 2, 'A': 3}
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
	for j, space := range interval {
		diatonic[j] = chromatic[i%len(chromatic)]
		i += intervals[space]
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
