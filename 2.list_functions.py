number = [3,5,1,6,2,8,7]
number.sort()
print(number)
number.reverse()
print(number)
print(number[1:5:2])  #start from 1st index end with 5th index and print every 2nd element tha is skip one element and print
print(max(number))
number.append(1) #keep 1 at the end of the list , append will go to last and keep it
print(number)

number.insert(2,45) # 2 is the index at which we want to inset and 45 is the number we insert
print(number)

number.remove(5)
print(number)
number.pop()
print(number)

#TUPLE 
#mutable : can change, list is mutable 
#immutable :  cannt change , tuple is immutable

tp = (2,3,4)
print(tp)
