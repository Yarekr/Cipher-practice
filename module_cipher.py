
code = {"a": "y", "A": "Y", "E": "I", "e": "i", "I": "O", "i": "o", "O": "A", "o": "a", "Y": "E", "y": "e"}
code2 = {"y": "a", "Y": "A", "I": "E", "i": "e", "O": "I", "o": "i", "A": "O", "a": "o", "E": "Y", "e": "y"}

operation = input ("wybierz operację : szyfrowanie, deszyfrowanie, wyjscie : ")
print('---------------------')

while operation == 'szyfrowanie':
    print('podaj zdanie do zaszyfrowania: ')
    txt = input()
    result = ""
    for letter in txt:
        if letter in code:
            result += code[letter]
        else:
            result += letter

    print("Wynik: "+result)
    print('---------------------')
    operation = input("wybierz operację : szyfrowanie, deszyfrowanie, wyjscie : ")
    print('---------------------')

while operation == 'deszyfrowanie':
    print('podaj zdanie do odszyfrowania: ')
    txt = input()
    result = ""
    for letter in txt:
        if letter in code2:
            result += code2[letter]
        else:
            result += letter
    print("Wynik: "+result)

    operation = input("wybierz operację : szyfrowanie, deszyfrowanie, wyjscie : ")
    print('---------------------')


if operation =='wyjscie':
        print('---------------------')
        print("Do widzenia")

elif operation:

    print("Błędna operacja ")

