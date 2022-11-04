# TypeError "Разные типы склаживать нельзя"
# ValueError "
try:
   a = input ("Ввведите число1 ")
   b = input ("Ввведите число2 ")
except ValueError:
    print("Результат", int(a) / int(b))
finally:
    print ("Все хорошо!")
    try:
c = "c" + 1
    except TypeError:
    print ("Разные типы слаживать нельзя")
