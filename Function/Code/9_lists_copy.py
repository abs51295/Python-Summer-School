def greet(users):
    for user in users:
        print("Welcome " + user)
    users.append('Shraddha')


my = ['Aagam', 'Smit']

# Now passing a copy.
greet(my[:])
print(my)