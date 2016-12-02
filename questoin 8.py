Original=["b", "e", "a", "u", "t" , "i" ,"f", "u", "l"]
Final=""

def Remove(n,Word,Final):
  if n==len(Word):
    print(Final)
  else:
    if Word[n]=="a"or Word[n]=="e" or Word[n]=="i" or Word[n]=="o" or Word[n]=="u":
      Word[n]=" "
    else:
      Final=Final+Word[n]
    Remove(n+1,Word,Final)

Remove(0,Original,Final)
