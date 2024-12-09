# Reversing a Array
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    rev_arr = arr[::-1]
    for i in rev_arr:
        print(i,end=" ")
