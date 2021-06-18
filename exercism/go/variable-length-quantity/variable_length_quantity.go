package variablelengthquantity

import "errors"

// EncodeVarint encodes the input according to the VLQ algorithm
func EncodeVarint(input []uint32) []byte {
	var output []byte
	var r uint32

	for _, val := range input {
		var encoding []byte

		if val == 0 {
			output = append(output, byte(0))
		}

		for val > 0 {
			val, r = val/128, val%128
			encoding = append([]byte{byte(r)}, encoding...)
		}

		for i := 0; i < len(encoding)-1; i++ {
			encoding[i] = 0b10000000 | encoding[i]
		}

		for _, val := range encoding {
			output = append(output, val)
		}
	}

	return output
}

// DecodeVarint decodes the VLQ encoded bytes to integers
func DecodeVarint(input []byte) ([]uint32, error) {
	var output []uint32
	var decodedInt uint32
	var bitOn bool

	for _, val := range input {
		if 0b10000000&val > 0 {
			bitOn = true
		} else {
			bitOn = false
		}

		val = 0b01111111 & val
		decodedInt = 128*decodedInt + uint32(val)

		if !bitOn {
			output = append(output, decodedInt)
			decodedInt = 0
		}
	}

	if bitOn {
		return []uint32{}, errors.New("incomplete sequence")
	}

	return output, nil
}
