"""
stdrandom.py

The stdrandom module defines functions related to pseudo-random
numbers.
"""

#-----------------------------------------------------------------------

import random
import math

#-----------------------------------------------------------------------

def seed(i=None):
    """
    Seed the random number generator as hash(i), where i is an int.
    If i is None, then seed using the current time or, quoting the
    help page for random.seed(), "an operating system specific
    randomness source if available."
    """
    random.seed(i)

#-----------------------------------------------------------------------

def uniformInt(lo, hi):
    """
    Return an integer chosen uniformly from the range [lo, hi).
    """
    return random.randrange(lo, hi)
    
#-----------------------------------------------------------------------

def uniformFloat(lo, hi):
    """
    Return a number chosen uniformly from the range [lo, hi).
    """
    return random.uniform(lo, hi)

#-----------------------------------------------------------------------

def bernoulli(p=0.5):
    """
    Return True with probability p.
    """
    return random.random() < p

#-----------------------------------------------------------------------

def binomial(n, p=0.5):
    """
    Return the number of heads in n coin flips, each of which is
    heads with probability p.
    """
    heads = 0
    for i in range(n):
        if bernoulli(p):
            heads += 1
    return heads
    
#-----------------------------------------------------------------------

def gaussian(mean=0.0, stddev=1.0):
    """
    Return a float according to a standard Gaussian distribution
    with the given mean (mean) and standard deviation (stddev).
    """

    # Approach 1:
    # return random.gauss(mu, sigma)

    # Approach 2: Use the polar form of the Box-Muller transform.
    x = uniformFloat(-1.0, 1.0)
    y = uniformFloat(-1.0, 1.0)
    r = x*x + y*y
    while (r >= 1) or (r == 0):
        x = uniformFloat(-1.0, 1.0)
        y = uniformFloat(-1.0, 1.0)
        r = x*x + y*y
    g = x * math.sqrt(-2 * math.log(r) / r)
    # Remark:  x * math.sqrt(-2 * math.log(r) / r)
    # is an independent random gaussian
    return mean + stddev * g

#-----------------------------------------------------------------------

def discrete(a):
    """
    Return a float from a discrete distribution: i with probability
    a[i].  Precondition: the elements of array a sum to 1.
    """
    r = uniformFloat(0.0, sum(a))
    subtotal = 0.0
    for i in range(len(a)):
        subtotal += a[i]
        if subtotal > r:
            return i
    #return len(a) - 1

#-----------------------------------------------------------------------

def shuffle(a):
    """
    Shuffle array a.
    """
    
    # Approach 1:
    # for i in range(len(a)):
    #     j = i + uniformInt(len(a) - i)
    #     temp = a[i]
    #     a[i] = a[j]
    #     a[j] = temp
    
    # Approach 2:
    random.shuffle(a)

#-----------------------------------------------------------------------

def exp(lambd):
    """
    Return a float from an exponential distribution with rate lambd.
    """
    
    # Approach 1:
    # return random.expovariate(lambd)
    
    # Approach 2:
    return -math.log(1 - random.random()) / lambd
    
#-----------------------------------------------------------------------

def _main():
    """
    For testing.
    """
    import sys
    import stdio
    seed(1)
    n = int(sys.argv[1])
    for i in range(n):
        stdio.writef(' %2d '   , uniformInt(10, 100))
        stdio.writef('%8.5f '  , uniformFloat(10.0, 99.0))
        stdio.writef('%5s '    , bernoulli())
        stdio.writef('%5s '    , binomial(100, .5))
        stdio.writef('%7.5f '  , gaussian(9.0, .2))
        stdio.writef('%2d '    , discrete([.5, .3, .1, .1]))
        stdio.writeln()

if __name__ == '__main__':
    _main()
    
#-----------------------------------------------------------------------

# python stdrandom.py 5
#  27 60.65914 False    41 9.01682  0
#  55 46.88378  True    48 8.90171  0 
#  58 92.96468  True    52 9.12770  0 
#  79 64.41387 False    47 9.49241  0 
#  29 32.30299  True    45 8.77630  1 

