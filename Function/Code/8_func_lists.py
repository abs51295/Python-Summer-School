def greet(users):
    for user in users:
        print("Welcome " + user)
        print(users.index(user))
    users.append('Shraddha')


my = ['Aagam', 'Smit']
greet(my)
print(my)
