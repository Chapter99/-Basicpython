#การสร้างฟังก์ชั่นโดยไม่มีการรีเทอนค่า 
def hello(name):
    print(f"Hello {name}")


#สร้างฟังก์ชั่นแบบมีการ Return Value
def area(width, heigth):
    total=width*heigth
    return total


#เรียกใช้งานฟังก์ชั่น hello


#การเรียกใช้งานฟังก์ชั่น area() โดยใส่ค่าในตัวแปล
print(area(5, 8))
print(area(15, 7.5))

#ฟังก์ชั่นแบบมีค่าเริ่มต้น
def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name:{name}")
    print(f"Salary:{salary}")
    print(f"Language:{lang}")


#เรียกใช้งานฟังก์ชั่น
show_info()
print()
show_info('Anucha', 12000, 'PHP')







