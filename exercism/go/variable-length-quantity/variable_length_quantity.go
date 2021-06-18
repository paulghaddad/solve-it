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

		// encode to base 128 representation
		for val > 0 {
			val, r = val/128, val%128
			encoding = append([]byte{byte(r)}, encoding...)
		}

		// append to output, adding a leading bit unless it's the right-most byte
		for i, val := range encoding {
			if i < len(encoding)-1 {
				val = 0b10000000 | val
			}
			output = append(output, val)
		}
	}

	return output
}

// DecodeVarint decodes the VLQ encoded bytes to integers
func DecodeVarint(input []byte) ([]uint32, error) {
	var output []uint32
	var decodedInt uint32

	// sequence should not end with a leading bit
	if input[len(input)-1]&128 != 0 {
		return nil, errors.New("incomplete sequence")
	}

	for _, val := range input {
		decodedInt = 128*decodedInt + uint32(127&val)

		// right-most byte, write out
		if 128&val == 0 {
			output = append(output, decodedInt)
			decodedInt = 0
		}
	}

	return output, nil
}
