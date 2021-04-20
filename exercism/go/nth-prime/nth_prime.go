package prime

// Nth returns the nth prime number
func Nth(n int) (int, bool) {
	if n == 0 {
		return 0, false
	}

	primes := []int{}
	num := 2

	for primeCount := 0; primeCount < n; num++ {
		// is num divisible by any preceding prime?
		if isPrime(primes, num) == true {
			primes = append(primes, num)
			primeCount++
		}
	}

	return num - 1, true
}

func isPrime(primes []int, num int) bool {
	if num == 2 {
		return true
	}

	for _, prime := range primes {
		if num%prime == 0 {
			return false
		}
	}

	return true
}
