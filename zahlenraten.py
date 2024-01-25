from random import randint

print("Computer wählt eine Zahl zwischen 1 und 100...")
random = randint(1,100)
print("Die Zufallszahl des Computers lautet: ",random)

count = 0
while True:
    count +=1
    i = int(input("Welche Zahl denkst du hat der Computer gewählt? \n"))
    if random == i:
        print("Korrekt!")
        print("Du hast",count,"Versuche gebraucht um die Zahl zu erraten.")
        print()
        exit = input("Möchtest du das Spiel beenden? [y/n]: ")
        if exit == "y":
            print("Sie haben das Spiel beendet!")
            break
        elif exit == "n":
            print("Neue Runde... Computer wählt eine Zahl zwischen 1 und 100...")
            random = randint(1,100)
            count = 0
            continue
    elif i < random:
        print("Deine Zahl ist zu niedrig...")
    elif i > random:
        print("Deine Zahl ist zu hoch...")