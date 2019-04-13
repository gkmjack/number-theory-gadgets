from basic import *
from primality import *
from RSA import RSA_protocol
from ElGamal import ElGamal_protocol

if __name__ == "__main__":
    digit = 256;
    message = 1997101312344132;
    (k1,k2) = ElGamal_protocol.generate_keys(digit);
    cipher = ElGamal_protocol.encrypt(message, k1);
    recover = ElGamal_protocol.decrypt(cipher, k2);

    print(recover);
