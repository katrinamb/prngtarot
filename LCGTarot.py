"""
Name: LCGTarot.py
Purpose: Using the Linear Congruential Generator (LCG) to generate a prng to pick a tarot card
Last Updated: 14 Dec 2023
"""
import datetime

today = datetime.datetime.now()
now = today.microsecond

# LCG formula: x(i+1) = (a * x(i) + c) mod m
# xi = seed number (now is xi)
# a = multiplier
# c = increment
# m = modulus

# source: https://dl.acm.org/doi/pdf/10.5555/2955239.2955463
m = 22873
a = 6943
c = 5593

def LCG_tarot(seed):
    # time is the seed number
    random_num = (a * seed + c)%m
    return random_num 

# mod by 44 because there are 22 major arcana tarot cards but also they can all be reversed, totaling to 44
if __name__ == "__main__":
    for i in range (50):
        now = LCG_tarot(now)
        print (now%44)