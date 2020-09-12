package strain

// Ints are slices of integer values
type Ints []int

// Lists are slices of integer slices
type Lists [][]int

// Strings are slices of strings
type Strings []string

// Keep filters integers that meet the predicate
func (ints Ints) Keep(pred func(int) bool) Ints {
	if ints == nil {
		return nil
	}

	filtered := make(Ints, 0)

	for _, val := range ints {
		if pred(val) {
			filtered = append(filtered, val)
		}
	}

	return filtered
}

// Discard filters integers that meet the predicate
func (ints Ints) Discard(pred func(int) bool) Ints {
	if ints == nil {
		return nil
	}

	filtered := make(Ints, 0)

	for _, val := range ints {
		if !pred(val) {
			filtered = append(filtered, val)
		}
	}

	return filtered
}

// Keep filters Lists that meet the predicate
func (lists Lists) Keep(pred func([]int) bool) Lists {
	filtered := make(Lists, 0)

	for _, list := range lists {
		if pred(list) {
			filtered = append(filtered, list)
		}
	}

	return filtered
}

// Keep filters Strings that meet the predicate
func (strings Strings) Keep(pred func(string) bool) Strings {
	filtered := make(Strings, 0)

	for _, val := range strings {
		if pred(val) {
			filtered = append(filtered, val)
		}
	}

	return filtered
}
