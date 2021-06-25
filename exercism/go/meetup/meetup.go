package meetup

import (
	"time"
)

// WeekSchedule is the qualifier of which day of the month the meetup is hosted
type WeekSchedule int

const (
	First WeekSchedule = iota
	Second
	Third
	Fourth
	Last
	Teenth
)

// Day converts the description of the meetup date to an actual date
func Day(ws WeekSchedule, day time.Weekday, month time.Month, year int) int {
	curr := time.Date(year, month, 1, 0, 0, 0, 0, time.UTC)
	nextMonth := curr.AddDate(0, 1, 0)
	oneWeek, _ := time.ParseDuration("168h")

	for curr.Before(nextMonth) {
		switch {
		case ws == First && curr.Day() <= 7 && curr.Weekday() == day:
			return curr.Day()
		case ws == Second && curr.Day() >= 8 && curr.Day() <= 14 && curr.Weekday() == day:
			return curr.Day()
		case ws == Third && curr.Day() >= 15 && curr.Day() <= 21 && curr.Weekday() == day:
			return curr.Day()
		case ws == Fourth && curr.Day() >= 22 && curr.Day() <= 28 && curr.Weekday() == day:
			return curr.Day()
		case ws == Teenth && curr.Day() >= 13 && curr.Day() <= 19 && curr.Weekday() == day:
			return curr.Day()
		case ws == Last && nextMonth.Sub(curr) <= oneWeek && curr.Weekday() == day:
			return curr.Day()
		}

		curr = curr.AddDate(0, 0, 1)
	}

	return -1
}
