# Prosty kalkulator
# Funkcja dodaje dwie liczby
def add(x, y):
   return x + y
# Funkcja odejmuje dwie liczby
def subtract(x, y):
   return x - y
# Funkcja mnoży dwie liczby
def multiply(x, y):
   return x * y
# Funkcja dzieli dwie liczby
def divide(x, y):
   return x / y
print("Wybierz działanie.")
print("1.Dodaj")
print("2.Odejmij")
print("3.Pomnóż")
print("4.Podziel")
# Użytkownik wybiera jedną z opcji
choice = input("Wybierz opcję (1/2/3/4): ")
num1 = float(input("Wprowadź pierwszą liczbę: "))
num2 = float(input("Wprowadź druga liczbę: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")