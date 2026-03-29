arr = [5, 2, 9, 1]

n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)


arr = []
n =int(input("Enter how manny number need there? :"))
for i in range(n):
    k = int(input())
    arr.append(k)
print(arr)

