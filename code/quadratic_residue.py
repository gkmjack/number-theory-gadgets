from modular import mod;
from primality import is_prime, factorize, miller_rabin_test;

def legendre_symbol(a, p, recursive = False):
    """Compute the Legendre symbol (a/p) where p is an odd prime.
    When 'recursive' option is set, use the law of quadratic reciprocity;
    otherwise, use Euler's criterion."""
    if (p == 1) or (p%2 == 0) or (miller_rabin_test(p) == 0):
        raise Exception("Invalid Legendre symbol");
    # Check that p is indeed an odd prime
    a %= p;
    if recursive:
        if (a == 0 or a == 1):
            return a;
        if a == 2:
            return legendre_symbol(a, p, False);
        if is_prime(a):
            if (a%4==3 and p%4==3):
                return -legendre_symbol(p, a, True);
            else:
                return legendre_symbol(p, a, True);
        factors = factorize(a);
        result = 1;
        for i in factors:
            if factors[i]%2:
                result *= legendre_symbol(i, p, True);
    else:
        result = mod(p, a, (p-1)>>1);
        if result == (p-1):
            result = -1;
    return result;
