package cryptosquare

import (
	"unicode"
)

// Encode returns the crypto square encoding of the input text
func Encode(s string) string {
	var normS, encrypted []byte

	for _, ch := range s {
		lower := unicode.ToLower(ch)

		if lower >= 'a' && lower <= 'z' || lower >= '0' && lower <= '9' {
			normS = append(normS, byte(lower))
		}
	}

	// Determine c and r
	var c, r int
	for c = 1; c <= len(normS); c++ {
		if c*(c-1) >= len(normS) {
			r = c - 1
			break
		}

		if c*c >= len(normS) {
			r = c
			break
		}
	}

	// Add padding if necessary
	spacesNeeded := c*r - len(normS)
	for i := 0; i < spacesNeeded; i++ {
		normS = append(normS, ' ')
	}

	for i := 0; i < c; i++ {
		for j := 0; j < r; j++ {
			encrypted = append(encrypted, normS[c*j+i])
		}

		if i < c-1 {
			encrypted = append(encrypted, ' ')
		}
	}

	return string(encrypted)
}
