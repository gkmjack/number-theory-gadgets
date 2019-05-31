def mod(n, b, e = 1): # return a^b(mod n)
    """Return b**e(mod n)."""
    if e < 0:
        b, e = multiplicative_inverse(n, b), -e;
    # Account for negative power

    binary = bin(e);
    binary.reverse();
    # Ger the binary representation of the e

    result, square = 1, b%n;
    for i in range(len(binary)):
        if binary[i]:
            result = (square*result) % n;
        square = (square**2) % n;
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
        (l,_) = large_integer_division(a*b, g);
        del n[0];
        n[0] = l;
    return n[0];


def multiplicative_inverse(n, a):
    """Return the multiplicative inverse of a mod n"""
    (_, b) = solve_linear_diophantine(n, a);
    return b%n;


def solve_linear_diophantine(a, b):
    """Return a pair of integer solutions (x,y) to ax+by=1"""
    if gcd(a,b)!=1:
        raise Exception("No solutions exist");
    flipped = False;
    if (a < b):
        a, b = b, a;
        flipped = True;
    # Perform extended Euclidean algorithm
    w = {a:(1,0), b:(0,1)};
    while b != 1:
        (q, r) = large_integer_division(a, b);
        # Ensure that precision overflow doesn't happen
        w[r] = (w[a][0]-w[b][0]*q, w[a][1]-w[b][1]*q);
        a, b = b, r;
    # Flip the result back
    if flipped:
        return (w[1][1], w[1][0]);
    else:
        return w[1];


def bin(n):
    """Return the binary expansion of a positive integer"""
    result = [];
    while n != 0:
        result = [1 & n] + result;
        n = n >> 1;
    return result;

def large_integer_division(dividend, divisor):
    """Return the quotient and remainder after huge integer division.
    Both return values are INTEGERS. This avoids precision overflow."""
    shift_amount = 0;
    # Find the maximum distance to shift without exceeding dividend
    while dividend >= (divisor<<(shift_amount+1)):
        shift_amount += 1;

    # Binary division
    quotient = 0;
    while shift_amount >= 0:
        if dividend >= (divisor<<shift_amount):
            new_bit = 1;
            dividend -= (divisor<<shift_amount);
        else:
            new_bit = 0;
        # Compute the value on each bit
        quotient = (quotient << 1) + new_bit;
        shift_amount -= 1;

    # Left-ver will be remainder
    remainder = dividend;
    return (quotient, remainder);
