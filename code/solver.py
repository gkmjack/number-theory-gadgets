from Euclid import gcd;
from modular import multiplicative_inverse;

def linear(n, a, b):
    """Give general solution to linear congruence ax=b (mod n)"""
    if a == 0:
        raise Exception("Not a linear congruence.");
    g = gcd(a, n);
    if b % g:
        return [];
    a, b, s = a//g, b//g, n//g;
    x = (multiplicative_inverse(s, a)*b) % n;
    solutions = [];
    for i in range(g):
        solutions.append(x);
        x = (x+s) % n;
    solutions.sort();
    return solutions;
