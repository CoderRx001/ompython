#states = ['NY', 'PA', 'CA']
#states = ['New York', 'Pensylvania', 'California']
#states = ['New York', 'NY', 'Pensylvania', 'PA', 'California', 'CA' ]

#above are lists, below is a dictionary
#dictionaries use {} and are 'key value pairs', keys have to be a string but the values can be anything

states = {'NY': 'New York', 'PA': 'Pensylvania', 'CA': 'California'}

print(states['NY'])
#the string in the [] shows that its pulling from a dictionary but if it was a number it would be a list 
#print(states["FL"])
# the above key does not exist 


people = ["mattan", "chris"] 
print(people[1])
# the above is a list

print(type(states))
print(type(people))
# shows what type they are in the terminal

print(states.get('FL', 'Not found'))
print(states.get('NY', 'Not found'))
# with get it will reveal none if not found, or 'Not found' which is the defaul value

print(states.keys())
# prints all the keys in the states dictionary
print(states.values())
# prints all the values in the states dictionary

states['FL'] = 'Florida'
# creates the 'FL': 'Florida' key value pair
print(states)

#user = {'Ant', 70, 12, 'brown', 'brown'}
# the above line is a list but we don't have any keys and therefore are unsure about the data
user = {'name': 'Ant', 'height': 70, 'shoes': 12, 'hair': 'brown', 'eyes': 'brown'}

blog_post = {'title': '11 sexy uses for dictionaries', 'body': 'blah blah blah'}

print(user['name'])
print(blog_post['title'])




