# So you decided to see the source of this magic. Well then, nothing can stop you. Just be careful!

# Following line is to unlock the tool

LockStatus = 0 # 0 is locked, 1 is unlocked

while LockStatus == 0:
    key = input("Please say the magical words that can break the \"lock spell\": ")
    if key == "claim the magic tool":
        LockStatus += 1
    else:
        print("Looks like you are not the chosen one... Try again, maybe?")

# Actual tool here

def reverser(FirstForm):

    ingredients = ""

    for x in FirstForm:
        ingredients += x
        
    return ingredients[::-1]

FirstForm = input("What word should be reversed with the indefinite powers of this magical tool?: ")
print(reverser(FirstForm))
