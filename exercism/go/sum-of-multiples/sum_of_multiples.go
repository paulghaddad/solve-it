package summultiples

// SumMultiples returns the sum of all the multiples of the division up to the
// limit
func SumMultiples(limit int, divisors ...int) int {
	sum := 0

	for num := 0; num < limit; num++ {
		for _, divisor := range divisors {
			if divisor == 0 {
				continue
			}

			if isMultiple(num, divisor) {
				sum += num
				break
			}
		}
	}

	return sum
}

func isMultiple(num, divisor int) bool {
	return num >= divisor && num%divisor == 0
}
