
def greet(name):
    return f"Hey {name}!"

def concatenate(word_one, word_two):
    return word_one + word_two

def age_in_dog_years(age):
    result = age * 7
    return result

print(greet("Ant"))
print(greet("Viri"))

print(concatenate('Ant', 'Viri'))

print(age_in_dog_years(30))
# - - - - - - - - - - - - - - - - - - - - - - -

#print(greet('Ant', 'this one argument too many'))
# above the greet function can only handle one argument above

#print(greet())
# above the greet function doesn't have a name argument to run the greet function on

#print(concatenate('Ant'))
# above the concatenate function needs another argument to work on

#print(concatenate(word_two='Ant', word_one='Viri'))
# above is only going to work this way on this function

name = "Oscar"

def print_different_name():
    name = 'Rox'
    print(name)
#above function is a world of its own called 'scoping'. print_different_name function prints Rox and not Oscar 

print(name)
print_different_name()
print(name)

