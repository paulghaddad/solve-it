package raindrops

import "strconv"

// Convert a numbers factors into raindrop sounds
func Convert(num int) string {
	raindropSounds := ""

	if num%3 == 0 {
		raindropSounds += "Pling"
	}
	if num%5 == 0 {
		raindropSounds += "Plang"
	}
	if num%7 == 0 {
		raindropSounds += "Plong"
	}

	if raindropSounds == "" {
		return strconv.Itoa(num)
	}

	return raindropSounds
}
