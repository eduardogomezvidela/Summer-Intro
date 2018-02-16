#even number adder

list = [2,5,65,43,46,70,6,9,10,11,32,6] # 2+46+70+6+10+32+6 == 172

adder = 0

for num in list:
    if num % 2 == 0:
        adder = adder + num

print(adder)
