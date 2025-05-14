def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, -n)
    elif n % 2 == 0:
        half_power = power(x, n // 2)
        return half_power * half_power
    else:
        return x * power(x, n - 1)

def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

def calculate_total(*args, discount=0):
    total = sum(args)
    if discount:
        total -= total * (discount / 100)
    return total

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def calculate_average(numbers):
    if not numbers:
        return 0
    average = sum(numbers) / len(numbers)
    return average


print(calculate_average([5, 10, 15, 20]))
print(calculate_average([]))

print(greet_user("Alice"))  # Should return "Hello, Alice!"
print(greet_user("Bob", "Hi"))  # Should return "Hi, Bob!"



##Medium
print(calculate_total(10, 20, 30))  # Should return 60
print(calculate_total(10, 20, 30, discount=10))  # Should return 54 (10% off)

double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # Should return 10
print(triple(5))  # Should return 15

##Hard
print(power(2, 10))  # Should return 1024
print(power(3, 4))   # Should return 81