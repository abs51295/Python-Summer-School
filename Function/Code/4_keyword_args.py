def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is: " + pet_name.title())


describe_pet(animal_type="dog", pet_name="tommy")

# This is equivalent to the above call unlike positional args.
describe_pet(pet_name="tommy", animal_type="dog")
