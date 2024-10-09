friends = ['an', 'linh', 'thanh', 'thao']
print(friends, type(friends))
friends[1] = 'trang'
print(friends)
friends.append('xuan')
print(friends)
friends.insert(-1, 'hong')
print(friends)
del friends[2]
print(friends)
name = friends.pop()
print(name, friends)
friends.remove('thao')
print(friends)
print(len(friends))
list1 = sorted(friends)
print(list1)
for item in list1:
    print(f"toi chi yeu {item}")
list_slice = list1[1:3]
print(list_slice)
number = [value ** 5 for value in range(1, 101)]
print(number)