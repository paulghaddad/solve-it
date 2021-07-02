package series

// All returns all substrings in s of length n
func All(n int, s string) []string {
	out := make([]string, len(s)-n+1)

	for i := 0; i+n <= len(s); i++ {
		out[i] = s[i : i+n]
	}

	return out
}

// UnsafeFirst returns the first substring with length n
func UnsafeFirst(n int, s string) string {
	return s[:n]
}

// First returns the first substring with length n, making sure it is possible
// to do so
func First(n int, s string) (string, bool) {
	if n > len(s) {
		return "", false
	}

	return s[:n], true
}
