x=1
y=101


print(list(range(x, y)))
low = x - 1
high = y - 1
mid = (low + high) //2
print(mid)

item = mid
guess = list[mid]

if guess > item:
    low = mid + 1
    if low == high:
         guess = item
elif guess < item:
    high = mid - 1
else:  guess = item
    



