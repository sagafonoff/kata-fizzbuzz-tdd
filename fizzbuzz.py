def fizzbuzz(number):
    # if type(number) != int:
    #     raise TypeError("Incorrect input type, should be integer")
    if number % 15 == 0:
        answer = "FizzBuzz"
    elif number % 3 == 0:
        answer = "Fizz"
    elif number % 5 == 0:
        answer = "Buzz"
    else: answer = number
    
    if type(answer) != int:
        result = answer
    else:
        result = number
    
    return result
    # return msg
