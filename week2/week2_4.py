
s=int(input("Enter your seconds: "))
h=s//3600 #floor divide
s = s % 3600 #deduct hours, left seconds
m= s//60 
s = s % 60  
print(f"{h} hours {m} minutes {s} seconds")
