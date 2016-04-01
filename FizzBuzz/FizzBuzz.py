
print ("The game FizzBuzz")
number = int(raw_input("Vnesi stevilko od 1 do 100: "))


for x in range (1, number):
    print "This is x: " + str(x)

    if x % 3 ==0 and x % 5 == 0:
        print ("FizzBuzz")
    elif x % 3 == 0:
        print ("Fizz")
    elif x % 5 == 0:
        print ("Buzz")
    else:
        print x