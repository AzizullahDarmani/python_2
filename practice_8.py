#tasl1;
# list1= [0, 1, 2,2, 2, 1, 1, 0, 2, 2, 0,1 , 2, 1, 1, 2, 2, 0]
# list2= ['rock','scissors','paper']
# print("here is the first list: ",list1) 
# print("here is the second list: ",list2) 

#task2: 
# list1= [0, 1, 2,2, 2, 1, 1, 0, 2, 2, 0,1 , 2, 1, 1, 2, 2, 0]
# list2= ['rock','scissors','paper']
# for i in list1:
#     print() 
#     if ( i== 0): 
#         print(0,list2[0])  
#     elif ( i == 1):
#         print(1, list2[1])   
#     else:
#         print(2,list2[2])    


# task3:
# list1= [0, 1, 2,2, 2, 1, 1, 0, 2, 2, 0,1 , 2, 1, 1, 2, 2, 0]
# list2= ['rock','scissors','paper']
# for i in list1:
#     text_input= input("enter your coice (rock/scissors or paper): ")   
#     if ( i== 0): 
#         print(0,list2[0],end=" ")   
#     elif ( i == 1):
#         print(1, list2[1],end=" ")   
#     else:
#         print(2,list2[2],end=" ")   



#task4:
# list1= [0, 1, 2,2, 2, 1, 1, 0, 2, 2, 0,1 , 2, 1, 1, 2, 2, 0]
# list2= ['rock','scissors','paper']
# for i in list1:
#     text_input= input("enter your coice (rock/scissors or paper): ")   
#     if ( i== 0): 
#         print(0,list2[0],end=" ")   
#     elif ( i == 1):
#         print(1, list2[1],end=" ")   
#     else:
#         print(2,list2[2],end=" ")  



#the paper, scissors and tock game:
done = ['rock','paper','scissors']
option = [1,2,0,2,1,0,2,1,0,2,1,0]
# print(done.index('rock')) 
# print(done.index('paper')) 
# print(done.index('scissors')) 
for i in option:
    computer = done[i] 
    player = input("what do you want to play(rock,paper,s): ")
    if player == 'scissors' and computer =='paper':
        print('i win the game')
    elif  player == 'paper' and computer == 'rock':
        print("i win the game")
    elif player == 'rock' and computer == 'scissors':
        print(' i win the game')
    elif player == computer:
        print("it is equal")
    else:
        print("i lost the game, computer win the game") 

        


        
        

    