package encode

import (
	"bytes"
	"strconv"
	"unicode"
	"unicode/utf8"
)

// RunLengthEncode encodes a string to its RLE equivalent
func RunLengthEncode(str string) string {
	var encoded bytes.Buffer
	strLen := utf8.RuneCountInString(str)

	for i := 0; i < strLen; {
		j := i
		for j < len(str) && str[i] == str[j] {
			j++
		}

		if j-i > 1 {
			encoded.WriteString(strconv.Itoa(j - i))
		}
		encoded.WriteByte(str[i])

		i = j
	}

	return encoded.String()
}

// RunLengthDecode decodes a RLE string to its full value
func RunLengthDecode(encoded string) string {
	var decoded bytes.Buffer
	encodedLen := utf8.RuneCountInString(encoded)

	for i := 0; i < encodedLen; i++ {
		j := i

		for unicode.IsDigit(rune(encoded[j])) {
			j++
		}

		times := 1
		if j > i {
			times, _ = strconv.Atoi(encoded[i:j])
			i = j
		}

		for times > 0 {
			decoded.WriteByte(encoded[i])
			times--
		}
	}

	return decoded.String()
}
