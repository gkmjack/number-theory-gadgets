from modular import mod;
from primality import is_prime, factorize, miller_rabin_test;
from random import randint;
from modular import multiplicative_inverse;

def legendre_symbol(p, a, recursive = False):
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

def random_residue(p, is_residue = True):
    while True:
        a = randint(1, p-1);
        if is_residue and legendre_symbol(p, a) == 1:
            return a;
        if (not is_residue) and legendre_symbol(p, a) == -1:
            return a;

def sqrt_mod_p(p, a):
    """Give all x, such that x**2=a (mod p), where p is odd prime."""
    if legendre_symbol(p, a) == -1:
        return [];
    if legendre_symbol(p, a) == 0:
        return [0];
    # if legendre_symbol(p, a) == 1:

    s = 0;
    while (p-1) % 2**(s+1) == 0:
        s += 1;
    t = (p-1) >> s; # Finding the biggest 's' such that (2**s) divides p
    n = random_residue(p, False); # Find a quadratic non-residue 'n'
    b = mod(p, n, t); # Find b = n**t (mod p)
    a_inverse = multiplicative_inverse(p, a);
    x = mod(p, a, (t+1)>>1);

    for k in range(1, s):
        c = mod(p, a_inverse*x**2, 1<<(s-k-1));
        if (c == 1):
            j = 0;
        elif (c == p-1):
            j = 1;
        else:
            raise Exception("Unexpected error.");
        x = x*mod(p, b, j<<(k-1));
        x %= p;
    return [x, p-x];
