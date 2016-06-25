def user_profile(name, **info):
    print("Name is: " + name)
    for key, value in info.items():
        print(key + ": " + value)


user_profile('Einstein', location='princeton', field='physics')
