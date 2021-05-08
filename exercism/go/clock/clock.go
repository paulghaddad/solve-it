package clock

import "fmt"

const (
	minPerHour = 60
	minPerDay  = 1440
)

// Clock represents the minutes of time
type Clock struct {
	minutes int
}

// New constructs a new Clock type
func New(hour, minute int) Clock {
	totalMinutes := hour*minPerHour + minute
	totalMinutes24HourClock := (totalMinutes%minPerDay + minPerDay) % minPerDay

	return Clock{totalMinutes24HourClock}
}

func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c.minutes/minPerHour, c.minutes%minPerHour)
}

// Add adds time to an existing clock
func (c Clock) Add(min int) Clock {
	return New(c.minutes/minPerHour, c.minutes%minPerHour+min)
}

// Subtract subtracts time from an existing clock
func (c Clock) Subtract(min int) Clock {
	return New(c.minutes/minPerHour, c.minutes%minPerHour-min)
}
