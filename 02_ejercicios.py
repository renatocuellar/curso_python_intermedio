# Challenges

"""
Fizz Buzz
"""
#Esta es la manera en la que yo lo resolví
numero = 1

while numero <= 100:
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
    
    numero += 1


# Esta es la manera en la que el profesor lo resolvió

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print(index)

fizzbuzz()


#Es un anagrama

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False

    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("Amor", "Roma"))


# Sucesión de Fibonacci

def fibonacci():
    prev = 0
    next = 1
    for index in range(0, 51):
        print(prev)

        fib = prev + next
        prev = next
        next = fib

fibonacci()