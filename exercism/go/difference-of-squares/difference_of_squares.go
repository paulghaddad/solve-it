package diffsquares

// SquareOfSum returns the square of the sum from 1 to n
func SquareOfSum(n int) int {
	sum := n * (1 + n) / 2
	return sum * sum
}

// SumOfSquares returns the sum of the squares from 1 to n
func SumOfSquares(n int) int {
	return n * (n + 1) * (2*n + 1) / 6
}

// Difference returns the difference between the square of sums and the sum of
// squares
func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
