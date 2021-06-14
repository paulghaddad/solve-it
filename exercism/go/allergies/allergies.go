package allergies

// Allergies returns the list of allergens for a allergy score
func Allergies(score uint) []string {
	var allergens []string

	if score&1 == 1 {
		allergens = append(allergens, "eggs")
	}
	if score&2 == 2 {
		allergens = append(allergens, "peanuts")
	}
	if score&4 == 4 {
		allergens = append(allergens, "shellfish")
	}
	if score&8 == 8 {
		allergens = append(allergens, "strawberries")
	}
	if score&16 == 16 {
		allergens = append(allergens, "tomatoes")
	}
	if score&32 == 32 {
		allergens = append(allergens, "chocolate")
	}
	if score&64 == 64 {
		allergens = append(allergens, "pollen")
	}
	if score&128 == 128 {
		allergens = append(allergens, "cats")
	}

	return allergens
}

// AllergicTo returns whether a person is allergic to a set of allergens
func AllergicTo(score uint, substance string) bool {
	allergens := Allergies(score)

	for _, all := range allergens {
		if all == substance {
			return true
		}
	}

	return false
}
