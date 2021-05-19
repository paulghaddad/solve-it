package atbash

import "strings"

// Atbash encodes a string using the Atbash cipher
func Atbash(in string) string {
	var out strings.Builder
	var i int

	for _, ch := range in {
		lower := ch | 0b0100000

		switch {
		case lower < 'a' || lower > 'z':
			continue
		case lower > '0' && lower < '9':
			out.WriteByte(byte(lower))
		default:
			if i > 0 && i%5 == 0 {
				out.WriteByte(' ')
			}

			out.WriteByte(byte('z'-lower) + 'a')
		}

		i++
	}

	return out.String()
}
