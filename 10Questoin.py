Values=[1,2,3,4,1,5,1,6,7]
Store=[]
Start=0
End=0
'works out all the length of all the patterns reqiuired and stores it in the array "Store"
for i in range(1,len(Values)):
  if Values[i]>Values[i-1]:
    End=End+1
  else:
    Store.append(End-Start+1)
    Start=i+1
    End=Start
  if i==len(Values)-1:
    Store.append(End-Start+1)
    Start=i+1
    End=Start

print(Store)


