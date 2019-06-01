from Euclid import lcm;
from primality import factorize, is_prime;

def euler_totient(n): # phi
    """Count how many smaller positive integers are relatively prime to n"""
    factors = factorize(n);
    for i in factors:
        n = n*(i-1)/i;
    return int(n);

def carmichael_function(n): # lambda
    """Return the smallest positive integer i such that, for every integer 'a'
    relatively prime to n, mod(n, a, i)==1"""
    factors = factorize(n);
    result = 1;
    for i in factors:
        if i == 2 and factors[i]>2:
            result = lcm(result, euler_totient(i**factors[i])>>1);
        else:
            result = lcm(result, euler_totient(i**factors[i]));
    return result;

def count_prime_factors(n, distinct=True): # omega
    """Return the number of (distinct) prime factors to integer 'n'
    When 'distinct'=True, multiplicity is not counted"""
    factors = factorize(n);
    if distinct:
        return len(factors);
    else:
        return sum(factors[i] for i in factors);

def liouville_function(n): # lambda
    """Return (-1)**(Omega(n)) where Omega counts the number of prime factors,
    with multiplicity, of 'n'"""
    if count_prime_factors(n, False)%2:
        return -1;
    else:
        return 1;

def mobius_function(n): # mu
    """Check the prime factorization of n.
    Return 0 if n is not square-free (has no square divisors)
    Return 1 if n is square free and have even number of prime divisors
    Return -1 if n is square free and have odd number of prime divisors"""
    factors = factorize(n);
    for i in factors:
        if factors[i] > 1:
            return 0;
    if len(factors)%2 == 0:
        return 1;
    if len(factors)%2 == 1:
        return -1;

def prime_counting_function(n): # pi
    """Count the number of primes not exceeding n"""
    result = 0;
    for i in range(2,n+1):
        if (is_prime(i)):
            result += 1;
    return result;
