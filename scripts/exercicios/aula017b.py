num = [2, 5, 9, 1]
num[0] = 5
print(num)
num.append(7)
print(num.count(5))
print(num.index(5))
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista te {len(num)} elementos')
num.insert(1, 10)
print(num)
num.remove(10)
print(num)
num.pop(2)
print(num)
del(num)
print(num)