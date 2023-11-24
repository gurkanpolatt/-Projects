import calendar

print("Bir yıl girin: ")
yy = input()
print("\nBir ay girin (1-12 arasında): ")
mm = input()

y = int(yy)
m = int(mm)
print("\n", calendar.month(y, m))
