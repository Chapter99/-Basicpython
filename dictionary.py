scores={
    'Jorn':2000, 
    'bobby':2000, 
    'janny':3000
}

print(scores)
print(scores['bobby'])

#เพิ่มสมาชิกใหม่เข้า dictionary
scores['roger']=3200

print(scores)

#การสร้าง dictionary ว่างโดยใส่เครื่องหมาย {}
points={}

#เพิ่มค่าเข้า dictionary ว่าง
points['mr_a']=10.2
points['mr_a']=15.5
points['mr_a']=22.8

print(points)

#การ loop อ่านสมาชิกของ dictionary
for k, v in scores.items():
    print(k, v)

