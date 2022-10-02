from forex_python.converter import CurrencyRates
c=CurrencyRates()
exc=c.get_rate('USD','EUR')
d=float(input("Enter your dollars amount: "))
e=d*exc
print(round(e,2))
