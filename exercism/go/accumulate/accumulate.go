package accumulate

// Accumulate processes a collection with an operation and produces a new
// collection with the operation applied to each element
func Accumulate(collection []string, converter func(string) string) []string {
	output := make([]string, len(collection))

	for i, el := range collection {
		output[i] = converter(el)
	}

	return output
}
