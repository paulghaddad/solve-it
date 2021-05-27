package cipher

import (
	"bytes"
)

const caesarShiftAmt = 3

// ShiftCipher is an object for performing Caesar Cipher encoding/decoding
type ShiftCipher struct {
	shift int
}

// KeyCipher contains the key for encode/decode operations
type KeyCipher struct {
	key string
}

// NewCaesar is a factory function returning a ShiftCipher
func NewCaesar() Cipher {
	return ShiftCipher{caesarShiftAmt}
}

// NewShift is a factory function returning a ShiftCipher with a shift amount
func NewShift(amt int) Cipher {
	if amt == 0 || amt > 25 || amt < -25 {
		return nil
	}

	var sc Cipher
	sc = ShiftCipher{amt}
	return sc
}

// Encode returns the caeser cipher encoded string
func (c ShiftCipher) Encode(str string) string {
	var b bytes.Buffer

	for _, ch := range str {

		ch |= 0b0100000
		if ch >= 'a' && ch <= 'z' {
			b.WriteByte(byte(mod((int(ch)-'a'+c.shift), 26) + 'a'))
		}
	}

	return b.String()
}

// Decode returns the plain string from the encoded text
func (c ShiftCipher) Decode(str string) string {
	var b bytes.Buffer

	for _, ch := range str {
		b.WriteByte(byte(mod((int(ch)-'a'-c.shift), 26) + 'a'))
	}

	return b.String()
}

// NewVigenere is a factory function returning a KeyCipher
func NewVigenere(key string) Cipher {
	if key == "" {
		return nil
	}

	allAs := true
	invalidChar := false
	for _, ch := range key {
		if ch == 32 || ch < 'a' || ch > 'z' {
			invalidChar = true
		}

		if ch != 'a' {
			allAs = false
		}
	}

	if allAs || invalidChar {
		return nil
	}

	var vs Cipher
	vs = KeyCipher{key}
	return vs
}

// Encode returns the encoded string from the plain text for key ciphers
func (k KeyCipher) Encode(str string) string {
	var b bytes.Buffer
	var i int

	for _, ch := range str {
		ch |= 0b0100000

		if ch >= 'a' && ch <= 'z' {
			amt := int(k.key[i%len(k.key)] - 'a')
			b.WriteByte(byte(mod((int(ch)-'a'+amt), 26) + 'a'))
			i++
		}
	}

	return b.String()
}

// Decode returns the plain text string from the encoded text for key ciphers
func (k KeyCipher) Decode(str string) string {
	var b bytes.Buffer

	for i, ch := range str {
		amt := int(k.key[i%len(k.key)] - 'a')
		b.WriteByte(byte(mod((int(ch)-'a'-amt), 26) + 'a'))
	}

	return b.String()
}
