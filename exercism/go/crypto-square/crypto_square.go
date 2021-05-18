package cryptosquare

import (
	"strings"
	"unicode"
)

// Encode returns the crypto square encoding of the input text
func Encode(s string) string {
	var b, encrypted strings.Builder

	for _, ch := range s {
		lower := unicode.ToLower(ch)

		if lower >= 'a' && lower <= 'z' || lower >= '0' && lower <= '9' {
			b.WriteByte(byte(lower))
		}
	}

	// Determine c and r
	var c, r int

	for c = 1; c <= b.Len(); c++ {
		if c*(c-1) >= b.Len() {
			r = c - 1
			break
		}

		if c*c >= b.Len() {
			r = c
			break
		}
	}

	// Add padding if necessary
	spacesNeeded := c*r - b.Len()
	for i := 0; i < spacesNeeded; i++ {
		b.WriteByte(' ')
	}

	normS := b.String()
	for i := 0; i < c; i++ {
		for j := 0; j < r; j++ {
			encrypted.WriteByte(normS[c*j+i])
		}

		if i < c-1 {
			encrypted.WriteByte(' ')
		}
	}

	return encrypted.String()
}
