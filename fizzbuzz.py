#write a program that prints the numbers from 1 to 100
#But for multiples of 3 print "Fizz" instead of the number
#And for multiples of 5 print "Buzz" 
#For multiples of both print "FizzBuzz"

#hint % (modulo) tells you what's left over when you divide one number by another 
#i.e. number % 3 = 0 means it is divisible by 3

for number in range(1,101):
    
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number) 

