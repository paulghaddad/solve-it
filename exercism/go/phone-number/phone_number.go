package phonenumber

import (
	"errors"
	"fmt"
	"regexp"
)

// Number returns the digits in a phone number
func Number(s string) (string, error) {
	re := regexp.MustCompile(`[^0-9]`)

	out := re.ReplaceAllString(s, "")

	if len(out) < 10 || len(out) > 11 {
		return "", errors.New("not correct number of digits")
	}

	if len(out) == 11 && out[0] != '1' {
		return "", errors.New("11 digit numbers must begin with 1")
	}

	if len(out) == 11 {
		out = out[1:]
	}

	if out[0] < '2' {
		return "", errors.New("area code cannot start with 0 or 1")
	}

	if out[3] < '2' {
		return "", errors.New("exchange code cannot start with 0 or 1")
	}

	return out, nil
}

// AreaCode returns the area code
func AreaCode(s string) (string, error) {
	num, err := Number(s)
	if err != nil {
		return "", err
	}

	return num[0:3], nil
}

// Format returns the area code and number formatted
func Format(s string) (string, error) {
	num, err := Number(s)
	if err != nil {
		return "", err
	}

	return fmt.Sprintf("(%s) %s-%s", num[0:3], num[3:6], num[6:10]), nil
}
