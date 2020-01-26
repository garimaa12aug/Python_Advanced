# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4

var1 = input()
var2 = int(input())
var3 = int(input())

if var1 == '*':
	if var2 == 45 and var3 == 3:
		print("555")
	else:
		print(var2 * var3)
elif var1 == '+':
	if var2 == 56 and var3 == 9:
		print("77")
	else:
		print(var2+var3)
elif var1 == '/':
	if var2 == 56 and var3 == 6:
		print("4")
	else:
		print(var2/var3)
else:
	print(var2-var3)


