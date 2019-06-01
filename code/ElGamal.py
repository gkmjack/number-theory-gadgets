from modular import mod, multiplicative_inverse;
from primality import generate_large_prime;
from random import randint;

class ElGamal_protocol:
    """ElGamal encryption/decryption algorithm"""
    @classmethod
    def generate_keys(cls, digit):
        p = generate_large_prime(digit);
        g = randint(1, p-1); # This needs update
        a = randint(1, p-1);
        A = mod(p, g, a);
        # Give the sender hints
        return (ElGamal_public_key(p, g, A), ElGamal_private_key(p, g, a));

    @classmethod
    def encrypt(cls, message, public_key):
        b = randint(1, public_key.p-1);
        s = mod(public_key.p, public_key.A, b);
        # Generate the random secret
        c = mod(public_key.p, message*s);
        B = mod(public_key.p, public_key.g, b);
        # Give the receiver hints
        return ElGamal_cipher(c, B);

    @classmethod
    def decrypt(cls, cipher, private_key):
        s = mod(private_key.p, cipher.B, private_key.a);
        # Derive the shared secret
        inverse = multiplicative_inverse(private_key.p, s);
        return mod(private_key.p, cipher.c*inverse);


class ElGamal_public_key:
    """Used for encryption"""
    def __init__(self, p, g, A):
        self.p = p;
        self.g = g;
        self.A = A;

class ElGamal_private_key:
    """Used for decryption"""
    def __init__(self, p, g, a):
        self.p = p;
        self.g = g;
        self.a = a;

class ElGamal_cipher:
    """Represents a message transmitted in encoded fashion"""
    def __init__(self, c, B):
        self.c = c;
        self.B = B;
