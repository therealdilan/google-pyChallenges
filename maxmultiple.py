import string

nums = []
pos = []
neg = []
val = 1

def solution(x):
    for i in x:
        if i >= 0: # Find if positive and add
            pos.append(i)
        if i <= 0: # Find if negative and add
            neg.append(i)

    if len(neg) % 2 != 0: # If there is an odd number of negatives, remove the smallest
        neg.sort()
        neg.remove(neg[0])

    global nums
    global val

    nums = pos + neg # Combine the two lists

    for product in nums:
        val = val * product # Multiples all numbers together

    print(str(val)) #Convert to string
