from Euclid import solve_linear_diophantine;
from primality import miller_rabin_test;
from primality import factorize;

def split(n, x):
    """Split a congruence into equivalent ones with relatively prime modulo."""
    factors = factorize(n);
    c = {};
    for p in factors:
        m = p**factors[p];
        c[m] = x%m;
    return c;

def merge(c):
    """Use Chinese Remainder Theorem to combine a system of congruences.
    E.g. x=a mod p, x=b mod q, etc, where p, q are primes."""
    for p in c:
        if not miller_rabin_test(p):
            raise Exception("Non-prime modulo given.");
        c[p] %= p;

    m = list(c);
    while(len(m)>1):
        (p, q) = (m[0], m[1]);
        (s, t) = solve_linear_diophantine(p, q);
        del m[0];
        m[0] = p*q;
        c[p*q] = (s*p*c[q]+t*q*c[p]) % (p*q);

    return (m[0], c[m[0]]);
