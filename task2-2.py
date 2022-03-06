def list(n=10,listx=[4,9,7,1],val=1):
	for i in range(n):
		if val not in listx:
			listx.append(val)
		val = val + 1
	listx = sorted(listx)
list()