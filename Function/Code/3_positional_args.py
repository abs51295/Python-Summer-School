def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is: " + pet_name.title())


describe_pet("dog", "tommy")
describe_pet("tommy","dog")