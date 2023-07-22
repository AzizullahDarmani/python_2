#task 1:
# def welcome ():
#     a = input("hello, what is your name: " ) 
#     print("welcome to my game ",a,". Take a seat") 
#     print("-"*10)
# welcome()
# welcome()



#task 2:

# def factorial(a):
#     fact = 1
#     # a= int(input("number: ")) 
#     for i in range(a,1,-1):
#         fact*=i
#     print("the factorial of ",a," is ",fact)
# factorial(6) 


#task 3:
# def sum_of_number(end, start = 0, step = 1):
#     total = 0
#     for i in range(start, end ,step):
#         total+=i
#     print(total) 
    
# sum_of_number(10,5)  
# sum_of_number(10, 5, 3)
# sum_of_number(10) #default value for start = 0, step = 1
# sum_of_number(10, 0, 1)





#task 4:
def perfect(n):
  s = 0
  for i in range(1, n):
    if n%i == 0:
      s = s+ i
  return s == n

ans = perfect(6)
print(ans)
ans = perfect(8)
print(ans)
