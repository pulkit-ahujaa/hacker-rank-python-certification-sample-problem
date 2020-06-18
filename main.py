for x in list(range(n)):
    output = ""
    if(x % 3 == 0):
        output += 'Fizz'
    if(x % 5 == 0):
        output += 'Buzz'
    if(output == ""):
        output += str(x)

    print(output)