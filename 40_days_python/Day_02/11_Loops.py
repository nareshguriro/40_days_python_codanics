#while and for Loops
#while loop
#x=0
#while (x<5):
    #print(x)
    #x=x+1

#for loop 
for x in range (4,11):
    print(x)

#Array
days = ["Mon","Tue","Thu","Fri","Sat","Sun"]
for d in days:
    #if (d=="Fri"):break
    if (d=="Fri"):continue
    print(d)