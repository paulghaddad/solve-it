package clock

import "fmt"

// Clock represents the minutes of time
type Clock struct {
	hour, minute int
}

// New constructs a new Clock type
func New(hour, minute int) Clock {
	if minute >= 60 || minute <= -60 {
		hour += minute / 60
		minute = minute % 60
	}

	if minute > -60 && minute < 0 {
		hour = hour - 1
		minute = 60 + minute
	}

	hour = hour % 24

	if hour < 0 {
		hour = 24 + hour
	}

	return Clock{hour, minute}
}

func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c.hour, c.minute)
}

// Add adds time to an existing clock
func (c Clock) Add(min int) Clock {
	return New(c.hour, c.minute+min)
}

// Subtract subtracts time from an existing clock
func (c Clock) Subtract(min int) Clock {
	return New(c.hour, c.minute-min)
}
