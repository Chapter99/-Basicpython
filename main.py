#import ทั้งหมดทุกฟังก์ชั่นใน Module
#import numbers

#import มาแค่บางฟังก์ชั่น
#from numbers import factorial, fibonacci

#import ทุกฟังก์ชั่น
#from numbers import*

#import และทำการเปลี่ยนชื่อฟังก์ชั่น เป็นนามแฟง โดยใช้ as ตามด้วยชื่อ
from numbers import factorial as fa, fibonacci as fi


#เรียกใช้งาน
#print(numbers.factorial(5))
#print(numbers.fibonacci(100))

print(fa(5))
print(fi(100))