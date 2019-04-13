from basic import *
from primality import *

if __name__ == "__main__":
    digit = 256;
    for i in range(10):
        print(i);
        p = generate_large_prime(digit, False);
        q = generate_large_prime(digit, False);
        n = p * q;
        period = (p-1) * (q-1);
        while(True):
            e = randint(1, n-1);
            if gcd(period, e) == 1:
                break;
        # e has to be invertible
        d = multiplicative_inverse(period, e);
        print((d*e)%period);
