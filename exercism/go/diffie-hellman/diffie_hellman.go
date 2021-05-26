package diffiehellman

import (
	"math/big"
	"math/rand"
	"time"
)

// PrivateKey picks a private key that's greater than 0 and less than or equal
// to p, a prime number
func PrivateKey(p *big.Int) *big.Int {
	pk := big.NewInt(0)
	offset := big.NewInt(2)
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	pk.Rand(r, p)
	pk.Rem(pk, p.Sub(p, offset))

	// set p back to its original value
	p.Add(p, offset)

	return pk.Add(pk, offset)
}

// PublicKey calculates the public key give primes p and g and a private key
func PublicKey(a, p *big.Int, g int64) *big.Int {
	pk := big.NewInt(0)

	return pk.Exp(big.NewInt(g), a, p)
}

// SecretKey calculates the secret key shared by the two private keys
func SecretKey(a, B, p *big.Int) *big.Int {
	sk := big.NewInt(0)

	return sk.Exp(B, a, p)
}

// NewPair calculates a private/public key pair given primes p and g
func NewPair(p *big.Int, g int64) (a, A *big.Int) {
	a = PrivateKey(p)
	A = PublicKey(a, p, g)

	return
}
