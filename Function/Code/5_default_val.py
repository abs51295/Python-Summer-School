def describe_pet(pet_name, animal_type="dog"):
    """Display info about a pet"""
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is: " + pet_name.title())


describe_pet("tommy")

# This is same as above
describe_pet(pet_name="tommy")

# Over-riding default value
describe_pet("tommy", "cat")
