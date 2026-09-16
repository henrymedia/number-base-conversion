base = int(input("Enter a base (2-9): "))
number = input("Enter a number in that base: ")

total = 0
for digit in number:
    total = total * base + int(digit)

print("My answer:", total)

print("Built-in answer:", int(number, base))