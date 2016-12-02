Word="This Is Awesome"

# Making a set length array to save time because it isnt the main part of the task
NewWord=["","","","","","","","","","","","","","","",""]
FinalWord=""

#This runs through each letter in the word and puts it in the oposit postinon in an array 
#i used an array because i couldnt get it to work using string index
for i in range (0,len(Word)):
  if i==len(Word):
    NewWord[0]=Word[i]
  else:
  	NewWord[len(Word)-i]=Word[i]

    #turns the array into a word to be displayed
for i in range(1,len(Word)+1):
  FinalWord=FinalWord+NewWord[i]
      
print(Word)
print(FinalWord)