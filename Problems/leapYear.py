def is_leap_year(n):
    if n % 100 == 0:
        return n % 400 == 0
    return n % 4 == 0


n = int(input("Enter any year: "))
print(is_leap_year(n))

