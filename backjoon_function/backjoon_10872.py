n = int(input())
def a(n):
    b = 1
    for i in range(1,n+1):
        b = b*i
    return b
dog = a(n)
print(dog)