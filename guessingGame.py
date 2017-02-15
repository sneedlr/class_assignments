import random
guess=(1,2,3,4,5,6,7,8,9,0)
rando=(random.choice(guess))
attempt = 0
while attempt != rando:
    attempt = int(input("guess the number: "))
    if attempt >= rando:
        print("lower..")
    else:
        print("higher..")
if attempt == rando:
    print("congratulations, you guessed it")