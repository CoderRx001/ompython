
#dictionaries and lists can be inside of each other

animal_sounds = {
    "cat": ['meow', 'pur'],
    "dog": ['bark', 'woof'],
    "fox": []
}
# above is a dictionary of lists

ant = {'name': 'Ant', 'height': 70, 'shoes': 12, 'hair': 'brown', 'eyes': 'brown'}
oscar = {'name': 'Oscar', 'height': 68, 'shoes': 11, 'hair': 'brown', 'eyes': 'brown'}
viri = {'name': 'Viri', 'height': 60, 'shoes': 7, 'hair': 'brown', 'eyes': 'brown'}
#the above lines are variables which are dictionaries

people = [ant, oscar, viri]
# above is a list of dictionaries
print(people)

for person in people: 
    print(person['height'])
# this prints the heights of every person from the people list

for person in people: 
    print(person.get('height', 'not found'))
# this 2nd block is the safer 'version' block of code to make the print to the console 
# including the 'not found' default value in case some do not have a height key
