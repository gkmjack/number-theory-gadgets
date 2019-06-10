from Euclid import solve_linear_diophantine;
from Euclid import lcm;
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
    """Use Chinese Remainder Theorem to combine a system of congruences:
    E.g. x=a mod m, x=b mod n, etc, into a single one."""

    modulo = list(c);
    while(len(modulo)>1):
        (m, n) = (modulo[0], modulo[1]);
        (a, b) = (c[m], c[n]);
        (s, _) = solve_linear_diophantine(m, -n, b-a);
        del modulo[0];
        M = modulo[0] = lcm(m, n);
        c[M] = (s*m+a) % M;

    return (modulo[0], c[modulo[0]]);
