store = [4, 5, 6, "toy", 8, 11]

# using try-except block
for item in store:
    try:
        print(item//2)
    except:
        print("item is not of the same type")

# using while-break block
n = 5
while n > 2:
    print(n)
    n -= 1
    if n == 2:
        break
print("End")
