str_time=input("What time is it?")                                      #Prompts for time
time= int(str_time)

str_alarm=input("In how many hours will the alarm go off?")            #Prompts for when the alarm will go off
alarm=int(str_alarm)

beep= (time+alarm) % 24                                                      #Calculates what time it wil be when the alarm goes off

print("The alarm will go off at", beep, "hour/s")
