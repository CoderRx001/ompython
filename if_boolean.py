answer = input("Do you wnat to hear a joke? ")

affirmitive_response == ["Yes", "yes","Y", "y"]
negative_response == ["No", "no", "N", "n"]

if answer in affirmitive_response:
    print("I'm against picketing but I don't know how to show it.")
elif answer in negative_response:
    print("fine")
else:
    print("I don't understand")
