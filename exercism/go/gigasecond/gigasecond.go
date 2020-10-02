// Gigasecond calculates the moment when a gigasecond will occur, given a
// starting moment
package gigasecond

import "time"

// AddGigasecond adds a gigasecond to a given moment
func AddGigasecond(t time.Time) time.Time {
	gigasecond, _ := time.ParseDuration("1000000000s")
	return t.Add(gigasecond)
}
