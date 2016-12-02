Values= [7,8,9,10,11,12,13,14] 
Place=round(len(Values)/2)
Low=7
High=7
Answer=""

while Answer=="":
  print(Place)
  if Values[Place]<Low:
    Place=Place+round((len(Values)-Place)/2)
  else:
    if Values[Place]>High:
      Answer="True"
    else:
      Answer="False"
      
print(Answer)