#negative number adder

list = [5,-5,2,14,-20,8,98,-30,-6,5,-5] #-5-20-30-6-5 == -66

answer= 0

for num in list:
    if num < 0:
        answer = answer + num

print(answer)
