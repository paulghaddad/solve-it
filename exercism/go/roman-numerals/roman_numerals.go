package romannumerals

import "fmt"

// ToRomanNumeral converts an arabic number to a roman one
func ToRomanNumeral(arabic int) (string, error) {
	if arabic <= 0 || arabic > 3000 {
		err := fmt.Errorf("The arabic numeral %d cannot be converted to a roman numeral", arabic)
		return "", err

	}

	roman := ""
	for arabic > 0 {
		switch {
		case arabic >= 1000 && arabic%1000 >= 0:
			roman += "M"
			arabic -= 1000
		case arabic >= 900 && arabic%900 >= 0:
			roman += "CM"
			arabic -= 900
		case arabic >= 500 && arabic%500 >= 0:
			roman += "D"
			arabic -= 500
		case arabic >= 400 && arabic%400 >= 0:
			roman += "CD"
			arabic -= 400
		case arabic >= 100 && arabic%100 >= 0:
			roman += "C"
			arabic -= 100
		case arabic >= 90 && arabic%90 >= 0:
			roman += "XC"
			arabic -= 90
		case arabic >= 50 && arabic%50 >= 0:
			roman += "L"
			arabic -= 50
		case arabic >= 40 && arabic%40 >= 0:
			roman += "XL"
			arabic -= 40
		case arabic >= 10 && arabic%10 >= 0:
			roman += "X"
			arabic -= 10
		case arabic >= 9 && arabic%9 >= 0:
			roman += "IX"
			arabic -= 9
		case arabic >= 5 && arabic%5 >= 0:
			roman += "V"
			arabic -= 5
		case arabic >= 4 && arabic%4 == 0:
			roman += "IV"
			arabic -= 4
		default:
			roman += "I"
			arabic--
		}
	}

	return roman, nil
}
