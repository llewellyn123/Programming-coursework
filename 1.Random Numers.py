Numbers=[5,3,8,6,1,9,2,7]
'Veribles needed to preform the swap
Value=0
Swap=0

import random

'Cycles through the hole array swapping a random number with the current positons
for i in range (0,len(Numbers)):
  Value=random.randrange(0,len(Numbers))
  Swap=Numbers[i]
  Numbers[i]=Numbers[Value]
  Numbers[Value]=Swap
    
print Numbers

'I decided to do swapping to avoid the possibility of data loss or dublication 
'the big O notaion is N
