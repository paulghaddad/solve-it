package lsproduct

import "fmt"

/*
 Time: O(n)
 Space: O(1)
*/

func LargestSeriesProduct(digits string, span int) (int, error) {
	if len(digits) < span {
		return -1, fmt.Errorf("span must be smaller than string length")
	}

	if len(digits) == 0 {
		return 1, nil
	}

	if span < 0 {
		return -1, fmt.Errorf("span must be greater than zero")
	}

	if span == 0 {
		return 1, nil
	}

	var i, product, largestProduct int
	needProduct := true

MAIN:
	for i < len(digits) {
		digit, err := getDigit(digits, i)
		if err != nil {
			return -1, err
		}

		// skip over 0s and reset product
		if digit == 0 {
			needProduct = true
			product = 0
			i++
			continue
		}

		if needProduct == true {
			// find the product of three non-zero digits
			for j := 0; j < span && i-j+span-1 < len(digits); j++ {
				digit, err := getDigit(digits, i)
				if err != nil {
					return -1, err
				}

				if digit == 0 {
					product = 0
					i++
					goto MAIN
				}

				if product == 0 {
					product = 1
				}

				product *= digit
				i++
			}

			if product > largestProduct {
				largestProduct = product
			}
			needProduct = false
			continue
		}

		digitToRemove, err := getDigit(digits, i-span)
		if err != nil {
			return -1, err
		}
		// calculate current product of span
		product /= digitToRemove
		product *= digit

		if product > largestProduct {
			largestProduct = product
		}

		i++
	}

	return largestProduct, nil
}

func getDigit(digits string, i int) (int, error) {
	digit := int(digits[i] - '0')
	if digit < 0 || digit > 9 {
		return -1, fmt.Errorf("digits input must only contain digits")
	}

	return digit, nil
}
