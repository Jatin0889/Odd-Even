# WAP to find the Odd/Even number entered by the user
num = int(input("Enter number :"))
if(num % 2==0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")


#WAP to find the Odd/Even number between 1 to 100 by for loop
num = 100
for i in range(1,num + 1,1):
    if i % 2 == 0:
        print(f"{i} is Even.")
    else:
        print(f"{i} is Odd.")


#WAP to find the Odd/Even number between 1 to 100 by while loop
num = 100 
r = 1
while r < num+1 :
    if r % 2 == 0:
        print(f"{r} is Even.")
    else:
        print(f"{r} is Odd.")
    r = r + 1

    
