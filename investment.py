"""
    We have 10000 dollars in a bank account where we have 5% more every year
    How many years we need to have double of our capital?
"""

our_money = 10000
year = 0


while True:
    if (our_money<20000):
        our_money = our_money * 1.05
        year += 1
        print(round(our_money, 2))
    else:
        print(year)
        break


 