package allergies

var allergenVals = [8]string{
	"eggs",
	"peanuts",
	"shellfish",
	"strawberries",
	"tomatoes",
	"chocolate",
	"pollen",
	"cats",
}

// Allergies returns the list of allergens for a allergy score
func Allergies(score uint) []string {
	var allergens []string

	for i, all := range allergenVals {
		val := uint(1 << i)
		if score&val > 0 {
			allergens = append(allergens, all)
		}
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
