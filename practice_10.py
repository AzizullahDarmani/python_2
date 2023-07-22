# task 1: 
# n = input("enter text: ")
# with open('file.txt','w') as f:
#     f.write(n ) 
# print('Ok, it has been written in the file named: file.txt ') 



# task 2: 
# n = int(input("add your number: "))  
# with open('file1.txt', 'r') as f:
#     lines = f.readlines() 
# print(lines[n-1]) 


#task 3:
print('hello, welcome to the character creator.')
n1 = input("enter the name of your character :  ")
n2 = int(input("enter the age of you character: "))
n3 = input("Enter the superpower of your character: ")
n4 = input("Enter the weakness of your character:")
with open('files.txt', 'w') as f:
    f.write(n1 + "\n")
    f.write(f"{n2} \n")
    f.write(n3 + "\n")
    f.write(n4 + "\n")