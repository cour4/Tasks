import decimal
def lista(skok=decimal.Decimal(0.5),start = decimal.Decimal(2),end = decimal.Decimal(5.5),listx=[decimal.Decimal(2),decimal.Decimal(5.5)]):
	x = start
	while start != end:
		x = x + skok
		listx.append(x)
		start = start + skok
	print(sorted(listx))
lista()


		