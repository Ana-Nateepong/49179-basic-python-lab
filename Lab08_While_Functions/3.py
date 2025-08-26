def table(n, limit):
    num = 1
    while num <= limit:
        print(f"{n} x {num} = {n * num}")
        num += 1

n = int(input("n = "))
limit = int(input("limit = "))
table(n, limit)
