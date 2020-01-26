dy = {}
print(type(dy))
#dictionary is a key vaue pair

dy = {"garima":"23","ayshi":"28"}
print(dy)
print(dy["ayshi"])
dy["ayushi"] = "44"
print(dy)
del dy["garima"]
print(dy)

#create dictionary and take input from user and tell its meaning from dictionary

dic = {"mutable":"that can change", "immutable":"that can change","playground":"an open area to play","office":"work area for employess", "school":"a place to learn"}
print("enter word")
word = input()
print(dic[word])
