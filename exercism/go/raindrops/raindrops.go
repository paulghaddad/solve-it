package raindrops

import "strconv"

// Convert a numbers factors into raindrop sounds
func Convert(num int) string {
	factorSounds := map[int]string{
		3: "Pling",
		5: "Plang",
		7: "Plong",
	}

	raindropSounds := ""
	for factor, sound := range factorSounds {
		if num%factor == 0 {
			raindropSounds += sound
		}
	}

	if raindropSounds == "" {
		return strconv.Itoa(num)
	}

	return raindropSounds
}
