package letter

// FreqMap records the frequency of each rune in a given text.
type FreqMap map[rune]int

// Frequency counts the frequency of each rune in a given text and returns this
// data as a FreqMap.
func Frequency(s string) FreqMap {
	m := FreqMap{}
	for _, r := range s {
		m[r]++
	}
	return m
}

// ConcurrentFrequency is the same as FreqMap but counts the frequency of each
// text concurrently
func ConcurrentFrequency(s []string) FreqMap {
	numMaps := len(s)

	ch := make(chan FreqMap, numMaps)

	for _, s := range s {
		go func(s string) {
			ch <- Frequency(s)
		}(s)
	}

	m := FreqMap{}
	for range s {
		fm := <-ch
		for r, val := range fm {
			m[r] += val
		}
	}

	return m
}
