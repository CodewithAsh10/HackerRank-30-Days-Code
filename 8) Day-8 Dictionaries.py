# Inserting Keys and Value and printng output through queries
n=int(input())
phone_book = dict(input().split() for i in range(n))

while True:
    try:
        name = input()
    except EOFError as e:
        break
    if name not in phone_book.keys():
        print("Not found")
    else:
        print(f"{name}={phone_book[name]}") 
