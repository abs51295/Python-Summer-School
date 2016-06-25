def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# age is an optional parameter 
print(build_person("Aagam", "Shah"))
print(build_person("Aagam", "Shah", 21))
