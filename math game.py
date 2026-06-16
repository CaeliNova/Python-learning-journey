
Setnumber = [8,9,5,6,11,30,5,8,10]
life = 3
i = 0
print ("Welcome to the life game")
while life > 0:
    if i<len(Setnumber):
        answer = int(input (f"what is {Setnumber[i]} * {i}"))
        p = Setnumber[i]* i
        if answer == p:
            print ("Pass")
        else:
            print ("Fail")
            life = life - 1
            print(f"Remaining life: {life}")

        i = i + 1
    else:
        print("congratulations! You finished all the questions!")
        break
if life ==0:
    print("Game Over")