package prime

// Factors gives the prime factors for a given number
func Factors(n int64) []int64 {
	facts := make([]int64, 0)
	var k int64 = 2

	for n > 1 {
		if n%k == 0 {
			facts = append(facts, k)
			n /= k
		} else {
			k++
		}
	}

	return facts
}
