package listops

type binFunc func(int, int) int
type predFunc func(int) bool
type unaryFunc func(int) int

// IntList is an integer list
type IntList []int

// Foldr folds the list from the right
func (l IntList) Foldr(fn binFunc, initial int) int {
	acc := initial

	for i := l.Length() - 1; i >= 0; i-- {
		acc = fn(l[i], acc)
	}

	return acc
}

// Foldl folds the list from the right
func (l IntList) Foldl(fn binFunc, initial int) int {
	acc := initial

	for _, el := range l {
		acc = fn(acc, el)
	}

	return acc
}

// Filter keeps values where the predicate function is true
func (l IntList) Filter(fn predFunc) IntList {
	res := IntList{}

	for _, el := range l {
		if fn(el) {
			res = append(res, el)
		}
	}

	return res
}

// Length returns the number of elements in the list
func (l IntList) Length() int {
	return len(l)
}

// Map applies the function to each item in the list
func (l IntList) Map(fn unaryFunc) IntList {
	res := make(IntList, l.Length())

	for i, el := range l {
		res[i] = fn(el)
	}
	return res
}

// Reverse reverses the elements in the list in place
func (l IntList) Reverse() IntList {
	res := make(IntList, l.Length())

	for i, el := range l {
		res[l.Length()-1-i] = el
	}

	return res
}

// Append extends the list with one or more elements
func (l IntList) Append(vals []int) IntList {
	res := make(IntList, l.Length()+len(vals))

	for i, el := range l {
		res[i] = el
	}

	for i, el := range vals {
		res[l.Length()+i] = el
	}

	return res
}

// Concat combines one or more lists into one
func (l IntList) Concat(lists []IntList) IntList {
	res := l

	for _, list := range lists {
		for _, el := range list {
			res = append(res, el)
		}
	}

	return res
}
