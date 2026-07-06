class Slime:
    def __init__(self,monster,hp,atk):
        self.monster = monster
        self.hp=hp
        self.atk=atk

class Hero:
    def __init__(self,name,hp,atk):
        self.name = name
        self.hp=hp
        self.atk=atk

greenSlime = Slime("green",100,10)
Character =Hero ("Elie",100,50)

print (Character.name + " versus " + greenSlime.monster )
print ("Fight!!")

while greenSlime.hp>0:
    diff = greenSlime.hp - Character.atk
    print (str(Character.atk) + " - " + str(greenSlime.hp) +" = " + str(diff))
    greenSlime.hp = diff
    if greenSlime.hp>0:
        heal = greenSlime.hp + 20
        print("Heal! Greenslime HP" + str(heal ))
        greenSlime.hp=heal
        print("Fight!!")
    else:
        print ("You Won")


