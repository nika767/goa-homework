#1)

#Input - მონაცემის მიღება მომხმარებლისგან
name = input("Enter your name: ")  # ეს არის input

# Output - ინფორმაციის გამოყვანა ეკრანზე
print("Hello,", name)  # ეს არის output

#2)

value = input("Enter any value: ")
print("The type of the input is:", type(value))  # input ყოველთვის აბრუნებს სტრინგს

#3)

# string ტიპის ცვლადები
name = "Nika"        # str
surname = "Zarnadze" # str
city = "Tbilisi"     # str
color = "Blue"       # str
fruit = "Apple"      # str

# integer ტიპის ცვლადები
age = 25             # int
year = 2025          # int
day = 14             # int
score = 100          # int
count = 3            # int

# float ტიპის ცვლადები
height = 1.75        # float
weight = 65.5        # float
price = 19.99        # float
distance = 12.3      # float
temperature = 36.6   # float


#4)

a = "hello"      # str
b = 10           # int
c = 3.14         # float

print(type(a))   # ბეჭდავს str ტიპს
print(type(b))   # ბეჭდავს int ტიპს
print(type(c))   # ბეჭდავს float ტიპს


#5)

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
result =( word1 + word2)
print("Combined result:", result)


#6)

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))


num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))

average = (num1 + num2 + num3 + num4 + num5) 
print("The average is:", average)


#7)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
height = input("Enter your height (in meters): ")
weight = input("Enter your weight (in kg): ")

print("My name is {first_name} {last_name}, I am {age} years old, my height is {height} meters and my weight is {weight} kg.")
