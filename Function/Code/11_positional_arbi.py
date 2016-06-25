def pizza(size, *toppings):
    print("Size of pizza is :" + str(size))
    print("Toppings of pizza are: ")
    for top in toppings:
        print("- " + top)


pizza(15, 'mushrooms', 'green pepper', 'extra cheese')
