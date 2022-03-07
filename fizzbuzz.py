def fizzbuzz(number):
    if type(number) != int:
        raise TypeError("Incorrect input type, should be integer")
    if number % 15 == 0:
        msg = "FizzBuzz"
    elif number % 3 == 0:
        msg = "Fizz"
    elif number % 5 == 0:
        msg = "Buzz"
    else: msg = number
    
    return msg
