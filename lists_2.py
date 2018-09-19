
#we could also build lists
people = []

people.append("Tony")
people.append("Viri")
people.append("Oscar")

#now lets print
print(people)

#and remove someone
people.remove("Oscar")
print(people)

for person in people:
    print("Person is", person)

# number squared challenge
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number, "squared is ", number ** 2)
