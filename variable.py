a = 3
b = 4.92
c = "Anucha"
print(a)
print(b)
print(c)

# การสร้างตัวแปรหลายหัวในบรรทัดเดียวกัน
x = y = z = 10
j,k=5,15
print(x)
print(y)
print(z)
print(j)
print(k)

# Boolean
status=True
msg=False

print(status,msg)

# ตัวแปรแสดงผลร่วมกันข้อความ
# วิธีที่ 1 ใช้คอมมาร์ขั้น เรียกว่า concat string
print("ราคาขายต่อชิ้น",b,"บาท มีจำนวน",a,"ชิ้น")

# วิธีที่ 2 %f เป็นค่าของตัวแปลที่เป็นทุศนิยม 2f ทศนิยม 2 ตำแหน่ง เรียกว่า string interpolation
print("ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น" % (b,a))

# วิธีที่ 3 fomat string
print(f"ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น")


