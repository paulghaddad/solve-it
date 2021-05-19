package atbash

import "strings"

// Atbash encodes a string using the Atbash cipher
func Atbash(in string) string {
	var out strings.Builder
	var i int
	var enc byte

	for _, ch := range in {
		lower := ch | 0b0100000

		switch {
		case lower > '0' && lower < '9':
			enc = byte(lower)
		case lower >= 'a' && lower <= 'z':
			enc = byte('z'-lower) + 'a'
		default:
			continue
		}

		if i > 0 && i%5 == 0 {
			out.WriteByte(' ')
		}

		out.WriteByte(enc)
		i++
	}

	return out.String()
}
