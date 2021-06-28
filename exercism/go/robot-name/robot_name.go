package robotname

import (
	"math/rand"
	"time"
)

// Robot is the struct defining a robot
type Robot struct {
	name string
}

// Name creates a name for a robot
func (r *Robot) Name() (string, error) {
	if r.name == "" {
		rand.Seed(time.Now().UnixNano())
		b := make([]byte, 5)

		for i := 0; i < 2; i++ {
			b[i] = byte(rand.Intn(26) + 'A')
		}

		for i := 2; i < 5; i++ {
			b[i] = byte(rand.Intn(10) + '0')
		}

		r.name = string(b)
	}

	return r.name, nil
}

// Reset removes the current name, allowing for a new one to be set
func (r *Robot) Reset() {
	r.name = ""
}
