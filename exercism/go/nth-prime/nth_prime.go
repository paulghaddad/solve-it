package prime

import "math"

// Nth returns the nth prime number
func Nth(n int) (int, bool) {
	if n == 0 {
		return 0, false
	}

	primeCount := 0
	i := 2
	for {
		if isPrime(i) {
			primeCount++
		}

		if primeCount == n {
			break
		}

		i++
	}

	return i, true
}

// using primality test that max factor for a number is its square root
func isPrime(n int) bool {
	if n == 2 {
		return true
	}

	if n%2 == 0 {
		return false
	}

	i := int(math.Floor(math.Sqrt(float64(n))))
	for ; i > 1; i-- {
		if n%i == 0 {
			return false
		}
	}

	return true
}
