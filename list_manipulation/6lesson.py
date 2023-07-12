print("#1")
for value in range (1,5):
  print(value)
print("\n")

print("#2")
numbers = list(range(6))
print(numbers)
print("\n")

print("#3")
even_numbers = list(range(2,11,2))
print(even_numbers)
print("\n")

print("#4")
squares = []
for value in range(1,11):
  square = value**2
  squares.append(square)
print(squares)
print("\n")

print("#4.1")
squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares)
print("\n")

print("#5")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
print("\n")

print("#4.2")
squares = [value**2 for value in range(1,11)]
print(squares)
print("\n")