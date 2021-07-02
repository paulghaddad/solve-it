package brackets

var complements = map[rune]rune{
	'[': ']',
	'{': '}',
	'(': ')',
}

// Bracket determines if the complements of the string properly match
func Bracket(s string) bool {
	var stack []rune

	for _, r := range s {
		if r == '[' || r == '{' || r == '(' {
			stack = append(stack, r)
		}

		if r == ']' || r == '}' || r == ')' {
			if len(stack) == 0 {
				return false
			}

			expectedPair := stack[len(stack)-1]
			if complements[expectedPair] != r {
				return false
			}

			stack = stack[:len(stack)-1]
		}

	}

	return len(stack) == 0
}
