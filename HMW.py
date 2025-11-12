number = int(input("ENter a number :"))

rev_num = ""

while number != 0:
    num = (number & 1)
    rev_num += str(num)
    number = number >> 1

print("Your number reversed is " + rev_num )
