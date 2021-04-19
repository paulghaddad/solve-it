package lsproduct

import "fmt"

// LargestSeriesProduct returns the largest product for a continguous series of
// digits
func LargestSeriesProduct(digits string, span int) (int, error) {
	if span > len(digits) {
		return 0, fmt.Errorf("span must be smaller than string length")
	}

	if span < 0 {
		return 0, fmt.Errorf("span must be greater than zero")
	}

	largest := 0
	for i := 0; i < len(digits)+1-span; i++ {
		product := 1
		for j := 0; j < span; j++ {
			digit := digits[i+j] - '0'
			if digit < 0 || digit > 9 {
				return 0, fmt.Errorf("digits input must only contain digits")
			}

			product *= int(digit)
		}

		if product > largest {
			largest = product
		}
	}

	return largest, nil
}
