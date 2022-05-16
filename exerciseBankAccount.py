"""
scrivere un programma che visualizzi il saldo
di un conto bancario dopo il primo, secondo e terzo anno.
Il conto ha un saldo iniziale di 1000$
e vi vengono accreditati interessi annuali al 5%
"""

OpeningBalance = 1000

for year in range(3):
    OpeningBalance = OpeningBalance + round(OpeningBalance * 5 / 100, 2)
    print(OpeningBalance)
