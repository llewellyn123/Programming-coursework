n=input("pick a number")
n=int(n)


def Prime(n,a):
  if a==0 or a==1:
    print ("Not Prime")
    return
  if a%n==0:
    print("Not Prime")
    return
  else:
    if n==2:
      print("Prime")
      return
    else:
      Prime(n-1,a)

    
Prime(n-1,n)
