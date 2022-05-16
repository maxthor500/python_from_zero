"""
scrivere un programma che visualizzi il saldo
di un conto bancario dopo il primo, secondo e terzo anno.
Il conto ha un saldo iniziale di 1000$
e vi vengono accreditati interessi annuali al 5%
"""


def bank_interests(OpeningBalance, year_interests_percentage, year_requested = 3):
    """
    Calculate the bank interests 
    and print every year how much
    your balance increments
    """
    for year in range(year_requested):
        OpeningBalance = OpeningBalance + OpeningBalance * year_interests_percentage / 100
        message = "After " + str(
            year+1) + " years, your balance is: " + str(round(OpeningBalance, 2))
        print(message)


bank_interests(1000, 5, 20)
