// The twofer problem
package twofer

import "fmt"

// my twofer solution
func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}

	return fmt.Sprintf("One for %s, one for me.", name)
}
