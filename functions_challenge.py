#define the function
# the result should be ANANAB 

uppercase_and_reverse = "banana" [::-1]   
print(uppercase_and_reverse.upper())
#above is how I did it 

def uppercase_and_reverse(text):
    return text.upper()[::-1]

print(uppercase_and_reverse("banana"))



