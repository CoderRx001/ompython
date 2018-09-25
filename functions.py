
#print is a function
def greet(name):
# above is a fuction I created. def= define, greet is the name, name is the argument inside the ()
    return f"Hey {name}!"
#functions are a way of saving code for later to run whenever you need them

print(greet("Ant"))
print(greet("Viri"))
# I can greet any name I want

def concatenate(word_one, word_two):
    return word_one + word_two

print(concatenate('Ant', 'Viri'))

def age_in_dog_years(age):
    return age * 7
#    return result
# always make sure there is a return for the fuction OR else you get none
# anything after return will do nothing 
# could return a list or dictionary 
#fuctions are usually defined up top

print(age_in_dog_years(30))

