package rotationalcipher

// RotationalCipher performs a rotation of each letter by the key amount to
// encrypt the plain text
func RotationalCipher(plain string, shift int) string {
	encypted := make([]rune, len(plain))

	for i, ch := range plain {
		var rot rune

		switch {
		case ch >= 'a' && ch <= 'z':
			rot = (ch-'a'+rune(shift))%26 + 'a'
		case ch >= 'A' && ch <= 'Z':
			rot = (ch-'A'+rune(shift))%26 + 'A'
		default:
			rot = ch
		}

		encypted[i] = rot
	}

	return string(encypted)
}
