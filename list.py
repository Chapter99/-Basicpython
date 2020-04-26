number=[5, 8, 13, 24, 7, 16]
name=['Jorn', 'Jane', 'Jany', 'Anucha']
mixed=[10, 25.75, True, 'Anucha']

# การแสดงค่าถึงสมาชิกใน list
print(number[1])
print(number)
print(name[3])
print(mixed[2])

# นับจำนวนสมาชิกใน list
print(len(number))
print(len(name))
print(len(mixed))

# การสร้าง list แบบว่าง(empty list)
data=[]

# การเพิ่มข้อมูลเข้าไปใน list ว่าง
data.append(10)
data.append(15)
data.append(20)

print(data)

# การอับเดสสมาชิก
data[1]=12

print(data)

# ฟังก์ชั่นวนลูปอ่านสมาชิกทั้งหมด
for n in number:
    print(n)

#loop แล้วหาผลรวม
sum = 0
for num in number:
    sum += num

print(sum)



