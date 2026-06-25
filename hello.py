# print('Hello, World!')
# print('Mi nombre es')

# # this is a string example
# learner = 'Senor Awesome'
# print(learner)

# # this is an integer example
# ideal_number_of_pets = 3
# print(ideal_number_of_pets)

# # this is a float example
# pi = 3.14159
# print(pi)

# # this is an example of a boolean
# is_learning_learning_important = True
# print(is_learning_learning_important)

# print(type(learner))
# print(type(ideal_number_of_pets))
# print(type(pi))
# print(type(is_learning_learning_important))

# print(9 + 9)
# print(9 - 9)
# print(9 * 9)
# print(9 / 9)
# # example of modulus operator
# print(10 % 3)
# print(10 / 3)
# print(10 / 5)

# # example of exponent operator
# print(2**5)
# print(2**2)
# print(32**73)

# # find the area of a rectangle
# length = 3
# width = 4
# area = length * width
# print(area)

# # find tax amount
# price = 10
# tax_rate = 0.08
# tax = price * tax_rate
# print(tax)

# # find the average
# avg = (10 + 20 + 30) / 3
# print(avg)

# #  ask the user their favorite color
# fav_color = input('What is your favorite color? ')
# print(f'Your favorite color is {fav_color}.')

#  test multiple inputs
# print('This', 'is', 'a', 'test', 'of', 'multiple', 'inputs.')
# print(12, 24, -2, sep='**')
# print('but', 'not', 'including', sep='')

# Create a receipt,
# print('Receipt')
# print('--------------------------')
# customerName = input("Enter customer's name: ")
# itemPrice = float(input('what is the cost of the item '))
# quantity = int(input('Enter quantity '))
# totalCost = itemPrice * quantity
# roundedCost = round(totalCost, 2)

# 1. Collect all inputs first
customer_name = input("Enter customer's name: ")
item_price = float(input("What is the cost of the item? "))
quantity = int(input("Enter quantity: "))

# 2. Perform calculations
total_cost = item_price * quantity
# Using f-string formatting to ensure 2 decimal places
formatted_total = f"{total_cost:.2f}"

# 3. Print the formatted receipt
print("\nReceipt")
print("--------------------------")
print(f"Customer: {customer_name}")
print(f"Item price: ${item_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total cost: ${formatted_total}")

name = input('What is your name? ')
age = input('What is your age? ')

print("Hello, " + name + "!")
print("You are " + age + " years old.")

