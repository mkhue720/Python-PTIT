student={"name":"Trần Văn A",'age':22}
print(student, type(student))
#update value of a key
student["name"]="Trần Văn B"
print(student)
student['sex']=False
print(student, len(student))
student['languages']=["English","Vietnamese","Thailand"]
print(student)
if student["age"]<23:
    print(student["name"], "chưa đủ tuổi lái xe PKL")
for key, value in student.items():
    if key!="languages":
        print(f"{key} có giá trị là {value}")
    else:
        print("Ngoại ngữ: ")
        for language in value:
            print(f"\t{language}")

for key in sorted(student.keys()):
    print(key)