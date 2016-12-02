original=10
Factorial=1
Zero=0

'figures out the factorial (for ease of input not relevent to the question)
for i in range (1,original+1):
	Factorial=Factorial*i
Factorial=str(Factorial)


'counts how many zeros are in the factorial given by the user
for i in range (0,len(Factorial)):
	if Factorial[i]=="0":
		Zero=Zero+1
print Zero

'the big O notation is N

