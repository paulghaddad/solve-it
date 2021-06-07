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
		for i, j := 0, len(events)-1; i < j; i, j = i+1, j-1 {
			events[i], events[j] = events[j], events[i]
		}
	}

	return events
}
