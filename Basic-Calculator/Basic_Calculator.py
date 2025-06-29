def add(l):
    return sum(l)

def sub(l):
    result = l[0]
    for i in l[1:]:
        result -= i
    return result

def mul(l):
    result = 1
    for i in l:
        result *= i
    return result

def div(l):
    result = l[0]
    for i in l[1:]:
        if i == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result /= i
    return result

try:
    length = int(input("Enter the count of numbers: "))
    l = []
    for i in range(length):
        e = float(input(f"Enter number {i + 1}: "))
        l.append(e)

    choice = input("Choose operation - a (add), s (subtract), m (multiply), d (divide): ").lower()

    if choice == 'a':
        print("Result:", add(l))
    elif choice == 's':
        print("Result:", sub(l))
    elif choice == 'm':
        print("Result:", mul(l))
    elif choice == 'd':
        print("Result:", div(l))
    else:
        print("Invalid operation choice.")

except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError as zde:
    print("Error:", zde)
