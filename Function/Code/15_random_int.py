from random import randint

# i = input()
while True:
    i = str(input())
    i = i.lower()
    if i == "no":
        break
    print(randint(1, 6))
