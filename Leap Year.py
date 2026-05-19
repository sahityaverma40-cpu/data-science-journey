# x = int(input("Enter an year:"))
# if x % 4 == 0:
#     print(x, "is a leap year")
# else:
#     print(x, "is not a leap year")

x = int(input("Enter an year:"))
result = "leap year" if x % 400 == 0 else "Leap year" if x % 4 ==0 and x % 100!= 0 else "Non leap year"
print(result)