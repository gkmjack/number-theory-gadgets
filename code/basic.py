def mod(m, b, e = 1): # return a^b(mod n)
    """Return b**e(mod n)."""
    binary = bin(e);
    binary.reverse();
    # Ger the binary representation of the e
    result, square = 1, b%m;
    for i in range(len(binary)):
        if binary[i]:
            result = (square*result) % m;
        square = (square**2) % m;
    return result;

def gcd(a, b):
    """Return the greatest common divisor of a and b"""
    if (a < b):
        a, b = b, a; # Make sure a is always bigger
    while (b != 0):
        a, b = b, a%b;
    return a;

def lcm(a, b):
    """Return the least common multiple of a and b"""
    return int(a*b/gcd(a,b));

def bin(n):
    """Return the binary expansion of a positive integer"""
    result = [];
    while n != 0:
        result = [1 & n] + result;
        n = n >> 1;
    return result;
