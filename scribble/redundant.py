def bin(n):
    """Return the binary expansion of a positive integer"""
    result = [];
    while n != 0:
        result = [1 & n] + result;
        n = n >> 1;
    return result;

def integer_division(dividend, divisor):
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
