import re

# Đọc nội dung file DATA.in
with open("DATA.in", "r") as file:
    content = file.read()

# Tách các phần tử trong file
elements = content.split()

# Lọc và giữ lại các từ không phải là số nguyên
words = [element for element in elements if not re.fullmatch(r'\d+', element)]

# Sắp xếp các từ theo thứ tự từ điển
words.sort()

# In kết quả, mỗi từ cách nhau một khoảng trắng
print(" ".join(words))
