#Fight simulation

import random


hp = 100
hp = int(hp)
enemy = 100
enemy = int(enemy)

energy = 100

######
#Punch, 6-12 damage, 75% accuracy, -10 energy

def punch(target):
    print("You strike at your foe!")
    if (random.randrange(1,101) <=75):
        damage = random.randrange(6,12)
        print("Your punch connects for", damage, "damage!")
        print("--------------------")
        target = target - damage
        return target

    else:
        print("You miss!")
        print("--------------------")
        return target

def e_punch(target):
    print("Your foe attacks!")
    if (random.randrange(1,101) <=75):
        damage = random.randrange(6,12)
        print("You take", damage, "damage!")
        print("--------------------")
        target = target - damage
        return target

    else:
        print("Your foe misses!")
        print("--------------------")
        return target

def blocked_e_punch(target):
    print("Your foe attacks!")
    if (random.randrange(1,101) <=75):
        damage = random.randrange(6,12) / 2
        print("You take", damage, "damage!")
        print("--------------------")
        target = target - damage
        return target

    else:
        print("Your foe misses!")
        print("--------------------")
        return target

######
#Kick, 9-18 damage, 50% accuracy, -25 energy

def kick(target):
    print("You strike at your foe!")
    if (random.randrange(1,11) <=5):
        damage = random.randrange(9,18)
        print("Your kick  connects for", damage, "damage!")
        print("--------------------")
        target = target - damage
        return target

    else:
        print("You miss!")
        print("--------------------")
        return target

######
#Block, 60% accuracy, recovers 15 energy
def block(hp):
    if(random.randrange(1,11) <=6):
        print("You block the attack!")
        print("--------------------")
        return True
    else:
        print("You fail to block the attack!")
        print("--------------------")
        return False

########## PROGRAM START##########

while (hp >= 1 and enemy >= 1):
    print("HP:", hp, "  Energy:", energy)                            #Update on HP
    print("Enemy HP:", enemy)

    print("--------------------")

##### PLAYER TURN#####

    print("1. Punch")
    print("2. Kick")
    print("3. Block")

    action = input("Action: ")      #Get user's action for the turn#
    print("################################")

#####CHEATS######
    if(action == "lose"):
        hp = 1
##################

    if (action == "1" and energy  >=10):                                    #Punch
        result = punch(enemy)
        enemy= result
        energy = energy-10
        
    elif (action == "2" and energy >=25):                                #Kick
        result = kick(enemy)
        enemy= result
        energy = energy-25
        
    elif (action == "3"):                                                                   #Block
        blocked = block(hp)
        energy = energy+15
        
    elif (action != "3" and energy < 25):                                   #Too tired
        print("You're too tired for that.")

    if (energy > 100):
        energy = 100
    if (hp > 100):
        hp = 100

    if (enemy < 1):
        print("Exhausted, your foe collapses. You win.")


#####ENEMY TURN#####

    #Select attack

    if(enemy >= 1):                                                                         #If enemy is dead it can't attack on this turn

        attack_type = random.randrange(1,11)

        if (attack_type >= 1 and attack_type < 7):                  #Chooses enemy action
        
            if (action == "3" and blocked == True):                     #Block, halves enemy damage
                result = blocked_e_punch(hp)
                hp = result

            else:                                                                                       #Regular punch
                result = e_punch(hp)
                hp = result

        
    if(hp < 1):
        print("You stumble, you can't keep on fighting. You lose.")
