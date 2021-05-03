package lsproduct

import "fmt"

/*
 Time: O(n)
 Space: O(1)
*/

func LargestSeriesProduct(digits string, span int) (int, error) {
	switch {
	case len(digits) < span:
		return -1, fmt.Errorf("span must be smaller than string length")
	case len(digits) == 0:
		return 1, nil
	case span == 0:
		return 1, nil
	case span < 0:
		return -1, fmt.Errorf("span must be greater than zero")
	}

	var product, largestProduct, window int

	for i := range digits {
		digit := int(digits[i] - '0')
		if digit < 0 || digit > 9 {
			return -1, fmt.Errorf("digits input must only contain digits")
		}

		if digit == 0 {
			product, window = 0, 0
			continue
		}

		if window < span {
			if product == 0 {
				product = 1
			}
			product *= digit
			window++
		} else {
			digitToRemove := int(digits[i-span] - '0')
			product /= digitToRemove
			product *= digit
		}

		if window == span && product > largestProduct {
			largestProduct = product
		}
	}

	return largestProduct, nil
}
