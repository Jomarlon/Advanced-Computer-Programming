name = input("Father's Name: ")
birthplace = input("Birthplace: ")
bmonth = input("Birthmonth: ")
bday = int(input("Day: "))
byear = int(input("Year: "))
age = 2023 - byear

print(" ")
print("Father's Name: " + name)
print("Birthplace: " + birthplace)
print("Birthday: " + bmonth + " " + str(bday) + ", " + str(byear))
print("Age: " + str(age))
