import random 
import string 
print("Random Password Generator") 
def main():
   length = int(input("Enter a length of password: "))
   lowerD=string.ascii_lowercase
   upperD=string.ascii_uppercase
   digitD =string.digits 
   symbolsD=string.punctuation
   combine = lowerD + upperD + digitD + symbolsD 
   X = random.sample(combine,length)
   Password = "".join(X) 
   print(Password) 
   main()
main()
