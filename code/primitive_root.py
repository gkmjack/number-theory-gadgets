from basic import gcd, mod;

def ord(m, b):
    """Return the smallest positive integer e such that b**e≡1(mod m)."""
    if gcd(m, b) != 1:
        return 0; # order is not defined
    e = 1;
    while mod(m, b, e) != 1:
        e += 1;
    return e;
