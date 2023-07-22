#task 1:
# list =['apple','banana']
# print(list) 
# b= str(input("what do you want to add?"))
# list.append(b)
# print("here is the list: ", list )  

#task 2: 
# list0 =[]
# for i in range(1,21,1):
#     list0.append(i)
# print(list0)
# for i in range(len(list0)):
#     if (list0[i]%2==0):
#         print(list0[i],end=" ")  
        
#task 3: 
# list0 = [54, 6, 23, 1, 5, 98] 
# total=0
# print("the list is: ", list0)
# for i in range (len(list0)):
#     total+= list0[i]
# print(total) 


#task 4:
# list0 = [54, 6, 23, 1, 5, 98]
# list0.sort()
# print("the list is: ", list0)


#task 5: 
done = ['kiwi','apple']
choice = 1
while choice != 0:
    print("here is the list: ")
    for i in done:
        print('\t',i)
    choice = int(input("do you want to add sth(enter 1)/nor remove something (enter 2) ore exit (enter 0)")) 
    if choice ==1:
        item = input("enter what you want: ")
        done.append(item) 
    elif choice ==2:
        item= input("what do you want to remover: ")
        done.remove(item)
    elif choice ==0:
        for i in done:
            print('\t-',i)  
print("good bye") 



        


