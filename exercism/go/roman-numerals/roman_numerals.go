package romannumerals

import (
	"fmt"
	"sort"
)

type arabicToRoman struct {
	arabic int
	roman  string
}

var mappings = [13]arabicToRoman{
	arabicToRoman{1000, "M"},
	arabicToRoman{900, "CM"},
	arabicToRoman{500, "D"},
	arabicToRoman{400, "CD"},
	arabicToRoman{100, "C"},
	arabicToRoman{90, "XC"},
	arabicToRoman{50, "L"},
	arabicToRoman{40, "XL"},
	arabicToRoman{10, "X"},
	arabicToRoman{9, "IX"},
	arabicToRoman{5, "V"},
	arabicToRoman{4, "IV"},
	arabicToRoman{1, "I"},
}

// ToRomanNumeral converts an arabic number to a roman one
func ToRomanNumeral(arabic int) (string, error) {
	if arabic <= 0 || arabic > 3000 {
		err := fmt.Errorf("The arabic numeral %d cannot be converted to a roman numeral", arabic)
		return "", err
	}
	numberMappings := len(mappings)

	roman := ""
	for arabic > 0 {
		idx := sort.Search(numberMappings, func(i int) bool {
			return arabic >= mappings[i].arabic
		})

		if idx == numberMappings {
			return "", fmt.Errorf("There was an error processing the arabic digit")

		}

		roman += mappings[idx].roman
		arabic -= mappings[idx].arabic
	}

	return roman, nil
}
