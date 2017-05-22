
def razdelitev_na_k_delov(s,m):
    if len(s)==m:
        return [[[i] for i in s]]
    if m == 1:
        return [[s]]
    else:
        razdelitve = []
        for i in range (1,len(s)-m+2):
            for j in razdelitev_na_k_delov(s[i:],m-1):
                temp = j[::-1]+[s[:i]]
                razdelitve = razdelitve + [temp[::-1]]
        return razdelitve


def je_postena(delitev, znaki):
	presteto = dict()
	for i in znaki:
		presteto[i] = [0,0] 
	for i in range(len(delitev)):
		for j in delitev[i]:
			if i%2 == 0:
				presteto[j][0] += 1
			else:
				presteto[j][1] += 1
	for i in presteto:
		if presteto[i][0] != presteto[i][1]:
			return False
		
	return True


def postena_delitev(s):
	postene=[]
	znaki = set()
	for i in s:
		znaki.add(i)
	k = len(znaki)
	for delitev in razdelitev_na_k_delov(s,k+1):
		if je_postena(delitev, znaki):
			#return delitev
			postene.append(delitev)
	return postene

for i in postena_delitev(['red', 'blue', 'blue', 'green', 'green', 'red']):
	print(i)

