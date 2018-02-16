

str_time=input("What time is it?)(STANDARD TIME)")                                  
time= int(str_time)


if (time <=12 and time>=0):
    print("so its",time%12,"am")
else :
    print ("so its", time%12," pm" )   


str_alarm=input("In how many hours will the alarm go off?")            #Prompts for when the alarm will go off
alarm=int(str_alarm)

beep= (time+alarm) % 24                                                      #Calculates what time it wil be when the alarm goes off

if(beep==12) :
    print("12pm")

elif (beep==0) :
         print("12am")

elif ((beep < 12) and (beep >= 0)) :
    print(beep%12,"am")

else  :
    print(beep%12,"pm")

print("The alarm will go off at", beep, "hour/s")
