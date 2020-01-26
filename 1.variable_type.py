var1 = "hello"
var2 = 4
var3 = 35.6
print(type(var1)) #gives the type of variable
var4 = "world"
print(var1+var4)
var4 = "34"
var5 = "44"
print(int(var4)+int(var5))  # this is doing typecasting..creating integer out of string
print(10 * "hello")
print(10 *str(int(var4)+int(var5) ))  # doing typecasting of interget obtained as a result of addition back to string

#take variable input from user
print("\nenter number")
num= input()
print(num)
#num will be a string so typecast to convert to integer
print(str(num)*10)
print(int(num)*10)