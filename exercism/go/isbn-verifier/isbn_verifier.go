package isbn

// IsValidISBN returns whether the given ISBN number is valid
func IsValidISBN(isbn string) bool {
	var total, n int = 0, 10

	for _, num := range isbn {
		switch {
		case num >= '0' && num <= '9':
			total += int(num-'0') * n
			n--
		case n == 1 && num == 'X':
			total += 10
			n--
		}
	}

	return total%11 == 0 && n == 0
}
