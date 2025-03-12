import random
num_random = random.randint(0, 20)
contador = 1
print("You got 3 chances!")
num_choosen = int(input("Choose a number between 0 and 20:"))
while contador <3:
    if num_choosen != num_random:
        print("Ble! Try it again")
        contador += 1
    else:
        break
    num_choosen = int(input("Choose a number between 0 and 20:"))

if num_choosen == num_random:
    print("You got it right!")
else:
    print("You lost!")

print("The drawn number was:", num_random)
