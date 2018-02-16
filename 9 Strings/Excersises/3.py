import string

text = "For long periods the High seem to be securely in power, but sooner or later there always comes a moment when they lose either their belief in themselves or their capacity to govern efficiently, or both. They are then overthrown by the Middle, who enlist the Low on their side by pretending to them that they are fighting for liberty and justice. As soon as they have reached their objective, the Middle thrust the Low back into their old position of servitude, and themselves become the High. Presently a new Middle group splits off from one of the other groups, or from both of them, and the struggle begins over again. Of the three groups, only the Low are never even temporarily successful in achieving their aims. It would be an exaggeration to say that throughout history there has been no progress of a material kind. Even today, in a period of decline, the average human being is physically better off than he was a few centuries ago. But no advance in wealth, no softening of manners, no reform or revolution has ever brought human equality a millimetre nearer. From the point of view of the Low, no historic change has ever meant much more than a change in the name of their masters."

letters=0
e=0

lower = string.ascii_lowercase
upper = string.ascii_uppercase

for char in text:

    if char == 'e':
        e+=1
    
    for char2 in lower:
        if char == char2:
            letters+=1
    for char3 in upper:
        if char == char3:
            letters+=1

percent = (e*100)/letters

print("Your text contains",letters, "letters of which", e, "(" + "%.2f" % percent + "%)" " are the letter 'e'.")
