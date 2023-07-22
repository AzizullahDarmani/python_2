# #task 1:
a=int(input("Enter your age:"))
if a>=18:
    print("You are an adult")
else:
    print("You are a child")

# #task 2: 

a= input("Enter a number (0 or 1):")
if a=='0' or a=='1':
    print("Thanks!")
else:
    print("I said 0 or 1!") 

    
# #task 3: 
a=int(input("Enter a number: "))
b= int(input("Enter a number: "))
if a%b==0:
    print("yes,",a,"is a multiple of",b,"because", b,"*",a/b,"=", a/b*b)
else:
    print("No", a, "is not a multiple of",b) 
    
#task 4: 
a=int(input("Enter a year: "))
if  a%400 and a%4==0:
    print("This is a leap year.")
elif a%100==0:
    print("This is not a leap year.")
else:
    print("This is not a leap year.")
    
