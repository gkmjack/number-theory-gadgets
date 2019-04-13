from basic import mod, gcd, multiplicative_inverse;
from primality import generate_large_prime;
from random import randint;

class RSA_protocol:
    """RSA encryption/decryption algorithm"""

    @classmethod
    def generate_keys(cls, digit):
        """Generate public and private keys.
        The length of each number is roughly twice the value of 'digit'"""
        p = generate_large_prime(digit);
        q = generate_large_prime(digit);
        n = p * q;
        period = (p-1) * (q-1);
        while(True):
            e = randint(1, n-1);
            if gcd(period, e) == 1:
                break;
        # e has to be invertible
        d = multiplicative_inverse(period, e);

        public_key = RSA_public_key(n, e);
        private_key = RSA_private_key(n, d);
        return (public_key, private_key);

    @classmethod
    def encrypt(cls, message, public_key):
        """Encode plain text into cipher text"""
        if isinstance(public_key, RSA_public_key):
            return RSA_cipher(mod(public_key.n, message, public_key.e));
        else:
            raise Exception("Argument type mismatch");

    @classmethod
    def decrypt(cls, cipher, private_key):
        """Decode cipher text into plain text"""
        if isinstance(cipher, RSA_cipher) \
        and isinstance(private_key, RSA_private_key):
            return mod(private_key.n, cipher.c, private_key.d);
        else:
            raise Exception("Argument type mismatch");

class RSA_public_key:
    """Used for encryption"""
    def __init__(self, n, e):
        self.n = n;
        self.e = e;

class RSA_private_key:
    """Used for decryption"""
    def __init__(self, n, d):
        self.n = n;
        self.d = d;

class RSA_cipher:
    """Represents a message transmitted in encoded fashion"""
    def __init__(self, c):
        self.c = c;
