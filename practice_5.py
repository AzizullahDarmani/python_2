#taks 1
# for i in range(5,51,1):
#     print(i, end=" ") 

#task 2:
# a= int(input("Enter the start: "))
# b= int (input("Enter the end: "))
# c= int (input("Enter the step: "))
# for i in range(a,b,c):
#     print(i, end="-") 

#task 3: 
# a= int(input("Enter the height of the pyramid: "))
# for i in range(a+1):
#     print("*"*i) 

#task 4: 
# a= int (input("Enter the height of the pyramid: "))
# for i in range(1,a*2, 2):
#     print("*"*(i) )

# task 5:
height=int (input("Enter the height of the pyramid: "))
b= height-1
for i in range(1,height*2,2):
    print(' ' * b + "*"*i) 
    b-=1



#task 6:
# num=int(input("Enter your number: "))
# prime=True
# for i in range(2,num,1):
#     if num%i==0:
#         prime=False
#         print("this is not a prime number because",i,"*",num/i,"=",num)
#         break
# if prime:
#     print("this is a prime number")

# furthermore, we can use this method also

num=int(input("enter your number: "))
for i in range(2,num,1):
    if num%i==0:
        print("this is not a prime number because ",i,"*",num/i,"=",num)
        break
else :
    print("this is a prime number")
        