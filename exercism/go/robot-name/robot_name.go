package robotname

import (
	"fmt"
	"math/rand"
	"time"
)

// Robot is the struct defining a robot
type Robot struct {
	name string
}

var random = rand.New(rand.NewSource(time.Now().UnixNano()))

var maxNamespace = 26 * 26 * 10 * 10 * 10
var usedNames = make(map[string]bool)

func newName() string {
	var name string

	c1 := random.Intn(26) + 'A'
	c2 := random.Intn(26) + 'A'
	num := random.Intn(1000)
	name = fmt.Sprintf("%c%c%d", c1, c2, num)
	return name
}

// Name creates a name for a robot
func (r *Robot) Name() (string, error) {
	if r.name != "" {
		return r.name, nil
	}

	if len(usedNames) >= maxNamespace {
		return "", fmt.Errorf("namespace is exhausted")
	}

	r.name = newName()
	for usedNames[r.name] {
		r.name = newName()
	}

	usedNames[r.name] = true

	return r.name, nil
}

// Reset removes the current name, allowing for a new one to be set
func (r *Robot) Reset() {
	r.name = ""
}
