package letter

import (
	"sync"
)

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
	var wg sync.WaitGroup
	freqMaps := make([]FreqMap, len(s))

	for i := 0; i < len(s); i++ {
		wg.Add(1)

		go func(i int, s string) {
			freqMaps[i] = Frequency(s)
			wg.Done()
		}(i, s[i])
	}

	wg.Wait()

	combined := combineFreqMaps(freqMaps)

	return combined
}

func combineFreqMaps(fm []FreqMap) FreqMap {
	m := FreqMap{}
	for i := 0; i < len(fm); i++ {
		curMap := fm[i]
		for r, val := range curMap {
			m[r] += val
		}
	}

	return m
}
