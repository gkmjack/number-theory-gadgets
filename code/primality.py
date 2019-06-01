from random import randint;
from Euclid import gcd;
from modular import mod;

DEFAULT_TRIALS = 50;

def is_prime(n):
    """Decides whether a positive integer 'n'(>=2) is prime."""
    for i in range(2,n):
        if ((n%i) == 0):
            return 0;
    return 1;

def factorize(n):
    """Factor a (small) number into products of primes"""
    factors = {};
    # Create a dictionary (key: prime factors, value: its exponent)
    for i in range(2,n+1):
        if (n%i == 0 and is_prime(i)):
            factors[i] = 0;

    while n != 1:
        for i in factors:
            if ((n%i) == 0):
                factors[i] += 1;
                n /= i;
    return factors;


def fermat_test(n, trials = DEFAULT_TRIALS, show_witness = False):
    """Using Fermet test, to check (with certain confidence) whether a
    positive integer 'n'(>=3) is prime.
    Carmichael numbers, which are composites satisfying the korselt criterion,
    can fool this algorithm."""
    for i in range(trials):
        while True:
            witness = randint(2, n-1);
            if gcd(n, witness) == 1:
                break;
        if (mod(n, witness, n-1) != 1):
            if show_witness:
                print("Witness:", witness);
            return 0;
    return 1;

def miller_rabin_test(n, trials = DEFAULT_TRIALS, show_witness = False):
    """Using Miller-Rabin test, to check (with very high confidence)
    whether a positive odd integer 'n'(>=3) is prime."""
    if (n%2 == 0):
        return 0;
    s = 0;
    while (n-1) % 2**(s+1) == 0:
        s += 1;
    t = (n-1) >> s;
    # Finding the biggest 's' such that 2**s divides n

    for i in range(trials):
        witness = randint(2, n-2);
        temp = mod(n, witness, t);
        if (temp%n) == 1:
            continue;
        possibly_prime = 0;
        for j in range(s):
            if (temp%n) == (n-1):
                possibly_prime = 1;
                break;
            temp = (temp**2)%n;

        if not possibly_prime:
            if show_witness:
                print("Witness:", witness);
            return 0;
    return 1;


def lucas_lehmer_test(base):
    """Determines whether (2**base)-1 is Mersenne prime"""
    modular = (2**base)-1;
    for i in range(1,base):
        if (i == 1):
            residue = 4;
        else:
            residue = mod(modular, (residue**2)-2);

    if (residue == 0):
        return 1;
    else:
        return 0;

def generate_large_prime(digit = 256, trials = DEFAULT_TRIALS):
    """Use Miller Rabin test to generate a large number that's likely prime.
    'digit' specifies the length of the number.
    'trials' decides how many Miller Rabin tests to perform."""
    while(True):
        n = randint(10**(digit-1)+1, 10**digit);
        if(miller_rabin_test(n, trials)):
            return n;

def korselt_criterion(n):
    """Determines whether an integer 'n'(>=4) is a carmichael number."""
    if (is_prime(n)):
        return 0;

    prime_divisors = factorize(n);

    for p in prime_divisors:
        if (n%(p**2)==0) or ((n-1)%(p-1)!=0):
            return 0;
    return 1;
