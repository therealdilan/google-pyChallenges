condition = 0
numsList = []

def solution(number):
    i=1
    while i <= number:
        numsList.append(i)
        i += 1

    
    for index,value in enumerate(numsList):
        condition = 0
        if (int(value) % 3 == 0):
            numsList[index] = "Fizz"
            condition = 1
        if (int(value) % 5 == 0):
            numsList[index] = "Buzz"
            condition = 1
        if (int(value) % 5 == 0) and (int(value) % 3 == 0):
            numsList[index] = "FizzBuzz"
            condition = 1
        if(condition == 0):
            numsList[index] = str(numsList[index])
