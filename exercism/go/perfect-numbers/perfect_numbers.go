package perfect

import (
	"errors"
)

// Classification of the type of natural number
type Classification uint8

// ClassificationPerfect is for perfect natural numbers
const (
	ClassificationInvalid Classification = iota
	ClassificationPerfect
	ClassificationAbundant
	ClassificationDeficient
)

// ErrOnlyPositive indicates a non-positive number was given as input
var ErrOnlyPositive error = errors.New("the input number must be positive")

// Classify determines whether a number is perfect, abundant, or deficient
func Classify(num int64) (Classification, error) {
	var factors []int64
	var sum int64

	if num <= 0 {
		return ClassificationInvalid, ErrOnlyPositive
	}

	for i := int64(1); i <= num/2; i++ {
		if num%i == 0 {
			sum += i
			factors = append(factors, i)
		}
	}

	switch {
	case sum > num:
		return ClassificationAbundant, nil
	case sum < num:
		return ClassificationDeficient, nil
	default:
		return ClassificationPerfect, nil
	}
}
