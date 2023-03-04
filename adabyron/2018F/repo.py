import math




n = int(input())
def list_in(a, b):
    for i in range(len(b) - len(a)):
        if(a[0] == b[i] and a == b[i:i+len(a)]):
            print("a")
            return True
    return False
for i in range(n):
    arr = list(map(int, input().split()))
    print(arr)
    diff = []
    patron = []
    for i in range(n -1):
        diff.append(arr[i +1] - arr[i])
    for i in reversed(range(math.floor(n/2))):
        bus = arr[0:i+1]
        print(bus)
        print(arr[i+1:n])
        if (list_in(bus,arr[i+1:n])):
            print("a")
            patron = bus
            break
    print(patron)
