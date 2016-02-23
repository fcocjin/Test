#TESTING GIT HUBBBBBB

a = 4047 #Storing first integer
b = 8367 #Storing second integer
answer = 0 #Initializing int answer as 0
for i in range(b-a+1): #iterates through all numbers between a and b
    if (i+a)%2 == 1: #checks to see if the number is odd
        answer += (i+a) #adds the value to answer
print(answer) #Prints answer to the shell
