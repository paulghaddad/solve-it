package series

// All returns all substrings in s of length n
func All(n int, s string) []string {
	var out []string

	for i, j := 0, n; j <= len(s); i, j = i+1, j+1 {
		out = append(out, s[i:j])
	}

	return out
}

// UnsafeFirst returns the first substring with length n
func UnsafeFirst(n int, s string) string {
	return s[0:n]
}
