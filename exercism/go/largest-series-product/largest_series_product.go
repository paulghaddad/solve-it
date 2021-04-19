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

	largest := 1
	product := 1
	for i := 0; i <= len(digits)+1-span; i++ {
		digit := int(digits[i] - '0')
		fmt.Println(digit)

		if i < span {
			product *= digit
			largest = product
			continue
		}

		oldDigit := int(digits[i-span] - '0')
		if oldDigit == 0 {
			product = 1
			continue
		}
		product /= oldDigit
		product *= digit

		if product > largest {
			largest = product
		}
	}

	return largest, nil
}
