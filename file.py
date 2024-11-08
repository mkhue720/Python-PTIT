import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
print(dname)
os.chdir(dname)
# doc file
file_name = 'file.txt'
# with open(file_name) as file_object:
#     # contents = file_object.read()
#   lines = file_object.readlines()
# # print(contents)
# print(lines)
# for line in lines:
#     print(line.rstrip())
# # ghi file
# with open(file_name, 'a') as file_object:
#     file_object.write("\nI love programming.\n")


class Person:
    def __init__(self, id, name, avg):
        self.id = id
        self.name = name
        self.avg = avg

    def ouput(self):
        print(f"{self.id} {self.name} {self.avg}")

list=[]
with open(file_name) as file_object:
    lines = file_object.readlines()
# print(lines)
for line in lines:
    s = line.strip().split()
    id = s[0]
    name = s[1]
    work_day = len(s) - 2
    total = 0
    for i in range(2, len(s)):
        total += float(s[i])
    avg = total / work_day
    person = Person(id, name, avg)
    list.append(person)
for person in list:
    person.ouput()