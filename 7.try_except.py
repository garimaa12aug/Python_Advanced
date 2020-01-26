print("enter num 1")
num1 = input()
print("enter num 2")
num2 = input()
try:
	print("the sum is",int(num1)+int(num2))
except Exception as e:
	print(e)

print("this line is very imortant")

#if we enter num2 as a string the prog will stop nd our last line will not be executed , but we want to print it so use try except
#except exception as e means whateer error will be there it will store it in e and print e nd then continue to execute further program
