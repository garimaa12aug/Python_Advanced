#to know running time of algo

import time

initial =  time.time()
i=0
while (i<10):
	print("first loop")
	i +=1
print("time for loop is", time.time()-initial);
i=0
initial3 = time.time()
while (i<10):
	print("first loop sleep mode")
	time.sleep(2)
	i +=1
print("time for loop is", time.time()-initial3);

initial2 = time.time()
k=0
for k in range(45):
	print("second loop")
print("time for second loop is" , time.time()-initial2)

#to tell the local time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
