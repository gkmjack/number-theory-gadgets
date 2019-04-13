from random import randint;
from basic import *;
from primality import *;
from math import log;

def relative_primality_simulation(cap, runs):
    """Simulate 'runs' times to determine the possibility that two random
    integers smaller than 'cap' are relatively prime."""
    count = 0;
    for i in range(runs):
        a = randint(1, cap);
        b = randint(1, cap);
        if (gcd(a,b) == 1):
            count += 1;
    print("After %d runs, %d pairs are relatively prime."
        % (runs, count));
    print("Probability %.5f" % (count/runs));

def find_carmichael_numbers(cap):
    """Find all carmichael numbers less than 'cap'."""
    carmichael_numbers = [];
    for i in range(4, cap):
        if (korselt_criterion(i)):
            carmichael_numbers.append(i);

    print("Carmichael number less than", cap, "are:");
    print(list(carmichael_numbers));

def hardy_littlewood_conjecture(cap):
    """Approximate the number of twin-prime pairs up to 'cap'."""
    twin_pairs = 0;
    TRIALS = 30;
    # Define the confidence in testing primality
    for i in range(5,cap,2):
        # Only looping over odd integers
        if (miller_rabin_test(i,TRIALS) == 1):
            if(miller_rabin_test(i+2,TRIALS) == 1):
                twin_pairs += 1;

    approx = 2*0.66016*cap/(log(cap)**2);
    print("There are %d twin pairs up to %d." % (twin_pairs, cap));
    print("Approximation gives", approx);
    print("Error of is", abs(approx-twin_pairs)/twin_pairs);
