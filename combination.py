def P(n,k):
	p = []
	for i in range(n+1):
		l = []
		for j in range(k+1):
			l.append(0)
		p.append(l)
	for i in range(n+1):
		p[i][0] = 1
	for i in range(1,k+1):
		p[0][i] = 0
	for i in range(1,n+1):
		for j in range(1,k+1):
			p[i][j] = p[i-1][j] + j*p[i-1][j-1]
	return 	p[n][k]
	
def func(a,b,level):
	if level<6:
		i = a*(9-level+1)
		j = 0
	else:
		j = 8*P(3,3)*P(6,level-3)
		i = a*(9-level+1)
		i = i - j
	return i,j
	
preva = 9
prevb = 0

print(str(1) + " " + str(preva)+" "+str(prevb))

for i in range(1,9):
	k,j = func(preva,prevb,i+1)
	print(str(i+1) + " " + str(k)+" "+str(j))
	preva,prevb = k,j
	