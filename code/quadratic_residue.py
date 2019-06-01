from modular import mod;
from primality import miller_rabin_test;

def legendre_symbol(a, p):
    """Compute the Legendre symbol (a/p) where p is an odd prime."""
    if (p == 1) or (p%2 == 0) or (miller_rabin_test(p) == 0):
        raise Exception("Invalid Legendre symbol");
    # Check that p is indeed an odd prime
    result = mod(p, a, (p-1)>>1);
    if result > 1:
        return -1;
    return result;
