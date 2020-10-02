// Gigasecond calculates the moment when a gigasecond will occur, given a
// starting moment
package gigasecond

import "time"

const gigasecond = 1000000000 * time.Second

// AddGigasecond adds a gigasecond to a given moment
func AddGigasecond(t time.Time) time.Time {
	return t.Add(gigasecond)
}
