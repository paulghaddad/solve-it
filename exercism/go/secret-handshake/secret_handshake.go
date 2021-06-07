package secret

// Handshake returns the sequence of events for a secret handshake
func Handshake(code uint) []string {
	events := []string{}

	if 1&code == 1 {
		events = append(events, "wink")
	}

	if 2&code == 2 {
		events = append(events, "double blink")
	}

	if 4&code == 4 {
		events = append(events, "close your eyes")
	}

	if 8&code == 8 {
		events = append(events, "jump")
	}

	if 16&code == 16 {
		numEvents := len(events)
		for i := 0; i < numEvents/2; i++ {
			events[i], events[numEvents-1-i] = events[numEvents-1-i], events[i]
		}
	}

	return events
}
