#Getting Pi using Leibniz


answer=0
n=1

for i in range (999999):
    answer=((-1)**n)/(2*n+1)
    n=n+2

answer=answer*4
answer=format(answer, '.50f')
print ("My aproximation to Pi is", answer)

print("Press enter to close")
a=input("")

#Correct
#3.14159265358979323846264338327950288419716939937510

#Closes aprox. I have gotten by increasing the range
#3.14159265308807666983170747698750346899032592773438




