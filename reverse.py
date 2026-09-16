def convert(number, base):
    if number < base:
        return str(number)
    return convert(number // base, base) + str(number % base)

number = int(input("Enter a base 10 number: "))
base = int(input("Enter a base to convert to (2-9): "))

print("My answer:", convert(number, base))