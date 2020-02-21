'''
lambda functions or anonymous function 

def minus(a,b):
	return a-b;

minus = lambda a,b : a-b 

both these mean same
'''

minus = lambda a,b :a-b

print(minus(9,2))

#sort according to first element in list
def a_first(a):
	return a[1]

a = [[1,4], [7,2], [6,22]]

a.sort(key = a_first)
print(a)

#using lambda function

b = [[4,2], [77,33], [3,66]]

a.sort(key = lambda b:b[1])
print(a)
