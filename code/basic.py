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

def gcd(*n):
    """Return the greatest common divisor of several positive integers"""
    n = list(n); # Convert tuple into list
    while(len(n) > 1):
        a = n[0];
        b = n[1];
        if (a < b):
            a, b = b, a; # Make sure a is always bigger
        while b:
            a, b = b, a%b;
        del n[0];
        n[0] = a;
    return n[0];


def lcm(*n):
    """Return the least common multiple of several positive integers"""
    n = list(n);
    while(len(n) > 1):
        a = n[0];
        b = n[1];
        g = gcd(a,b);
        del n[0];
        n[0] = (a*b)//g;
    return n[0];


def multiplicative_inverse(n, a):
    """Return the multiplicative inverse of a mod n"""
    (_, b) = solve_linear_diophantine(n, a);
    return b%n;


def solve_linear_diophantine(a, b, c = 1):
    """Return a pair of integer solutions (x,y) to ax+by=c"""
    g = gcd(a, b);
    if c%g != 0:
        raise Exception("No solutions exist");
    a, b, c = a//g, b//g, c//g;
    # Divide the equation by gcd(a,b)

    flipped = False;
    if (a < b):
        a, b = b, a;
        flipped = True;
    # Perform extended Euclidean algorithm
    w = {a:(1,0), b:(0,1)};
    while b != 1:
        q, r = a//b, a%b;
        # Ensure that precision overflow doesn't happen
        w[r] = (w[a][0]-w[b][0]*q, w[a][1]-w[b][1]*q);
        a, b = b, r;
    # Flip the result back
    if flipped:
        return (c*w[1][1], c*w[1][0]);
    else:
        return (c*w[1][0], c*w[1][1]);
