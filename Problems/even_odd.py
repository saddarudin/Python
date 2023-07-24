def even_odd(n):
    if 0 != n % 2:
        print(f"{n} is odd")
    else:
        print(f"{n} is even")


n = int(input("Enter a positive integer number: "))
even_odd(n)