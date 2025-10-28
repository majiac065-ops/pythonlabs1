year1=int(input("Enter start year "))
year2=int(input("Enter last year "))
print ("List of leap years:")
for i in range(year1, year2):
    if(i%4==0 and i%100!=0) or (i%400==0):
        print(i)
