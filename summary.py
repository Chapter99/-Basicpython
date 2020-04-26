print("-----------------------------")
print("# Summation Programe")
print("# Type 'exit' to end the programe")
print("-----------------------------")

# ตัวแปลไว้เก็บผลรวม
sumdata=0
count=1

while True:
    data=input(f"ใส่หมายเลข {count}:")
    # ตรวจสอบว่าผู้ใช้ป้อน 'exit'
    if data=="exit":
        break
    # การหาผลรวม
    sumdata += int(data)
    count=count+1
# แสดงผลรวมของค่าที่ป้อนหลังจากป้อน exit
print(f"Sum value is {sumdata}")

