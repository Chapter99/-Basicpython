# fullname=input("Enter your name:")
# age=int(input("Enter your Ege:"))
# print(fullname)
# print(age+5)

user=input("Enter username: ")
pwd=input("Enter Password: ")

set_user="admin"
set_pwd="1234"

if(user==set_user and pwd==set_pwd):
    print("Yes login success")
else:
    print("No login fail !!")
