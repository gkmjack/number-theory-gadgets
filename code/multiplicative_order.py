from basic import gcd, mod;
from primality import factorize;
from arithmetic import euler_totient;

def ord(n, b): # Multiplicative order
    """Return the smallest positive integer e such that b**e=1(mod n)."""
    if gcd(n, b) != 1 or n == 1:
        raise Exception("Multiplicative order is not defined");
    e = 1;
    power = b%n;
    while power != 1:
        power = (power*b)%n;
        e += 1;
    return e;

def count_primitive_roots(n):
    """Count the number of primitive roots mod n"""
    factors = factorize(n);
    # If n is 1, 2, 4, powers of odd prime, or 2*powers of odd prime
    if n == 1 or n == 2 or n ==4 \
    or (2 not in factors and len(factors) == 1) \
    or (2 in factors and factors[2] == 1 and len(factors) == 2):
        return euler_totient(euler_totient(n));
    # Otherwise it doesn't have primitive root
    else:
        return 0;
