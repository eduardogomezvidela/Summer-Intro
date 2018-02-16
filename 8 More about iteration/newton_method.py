#Newton Method 
#better =  1/2 * (old + n/old)

old = input("Number: ")
old=int(old)
n=old
better=1

while (old!=better):
        old=better
        
        if(better==1):
            alpedo=1
        else:
            print(better)

        better=1/2*(old+n/old)
