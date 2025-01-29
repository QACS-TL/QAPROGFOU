# fruit = ["APPLE", "ORANGE", "BANANA", "PEAR"]
# fruit[2]
#
# if "Pear" in fruit:
#     print('Pear is in the fruit list')
#
# if "Kiwi" not in fruit:
#     print('Kiwi is not in the fruit list')
#
# fruits = ("Apple", "Orange", "Banana", "Pear")
#
# print(fruits[1]) # Orange
#
# # fruits[1] = "Clementine"
#
# for i in range(0, len(fruits)):
#     print(fruits[i])
#
# for i, f in enumerate(fruits, 100):
#     print("Fruit is " + f + " and it's associated number is " + str(i))
#     print("Length of fruit is ", len(f))
#
# for f in fruit:
#     if "banana".upper() == f:
#         print("Banana Party!!!!")
#     print(f)
#     print(len(f))
#
# i = None
# if i:
#     print("i is one")

name = "Pete"
pin = "1234"
password = "secret"

i = 0
while True:
    username = input("Please enter your name: ")
    userpin = input("Please enter your PIN: ")
    userpassword = input("Please enter your password: ")

    if username == name and userpin == pin and userpassword == password:
        print("You have full access!")
        break
    if i >= 2:
        print("Goodbye")
        exit()
    else:
        print("Wrong credential, try again!")
        i += 1



print("All Done!")
