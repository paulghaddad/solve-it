package sieve

// Sieve returns a list of primes from 2 to the limit of n
func Sieve(limit int) []int {
	marks := make([]bool, limit+1)
	primes := []int{}

	for num := 2; num <= limit; num++ {
		if marks[num] {
			continue
		}

		primes = append(primes, num)

		for i := 2; num*i <= limit; i++ {
			marks[num*i] = true
		}
	}

	return primes
}
