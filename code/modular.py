from Euclid import solve_linear_diophantine;

def mod(n, b, e = 1): # return a^b(mod n)
    """Return b**e(mod n)."""
    if e < 0:
        b, e = multiplicative_inverse(n, b), -e;
    # Account for negative power

    result, square = 1, b%n;
    while e:
        if e & 1:
            result = (result*square) % n;
        square = (square**2) % n;
        e >>= 1;
    return result;

def multiplicative_inverse(n, a):
    """Return the multiplicative inverse of a mod n"""
    (_, b) = solve_linear_diophantine(n, a);
    return b%n;
