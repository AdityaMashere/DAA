def karatsuba(x, y):
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y
    
    # Calculate the size of the numbers
    m = min(len(str(x)), len(str(y)))
    m2 = m // 2
    
    # Split the digit sequences in the middle
    high1, low1 = divmod(x, 10**m2)
    high2, low2 = divmod(y, 10**m2)
    
    # 3 recursive calls
    z0 = karatsuba(low1, low2)  # (low1 * low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))  # (low1 + high1) * (low2 + high2)
    z2 = karatsuba(high1, high2)  # (high1 * high2)
    
    return z2 * 10**(2 * m2) + (z1 - z2 - z0) * 10**m2 + z0

def square_large_number(number):
    return karatsuba(number, number)

if __name__ == "__main__":
    large_number = int(input("Enter the Number: "))
    result = square_large_number(large_number)
    print(f"The square of {large_number} is {result}")
