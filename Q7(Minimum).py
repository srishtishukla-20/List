n= [ ]
a= [50,40,23,70,56,12,5,10,7]
i= 0
while i<len(a):
	n.append(a[i])
	i= i+1
print(min(n))
# minimum no. Of list
n= [24,5,36,57,60]
i= 0
count= 0
min= n[0]
while i<len(n):
	if n[i]>count:
		count= n[i]
	if n[i]<min:
		min= n[i]
	i= i+1
print('max',count)
print('min',min)
# Printing both max min
list=[52,62,1,2,11,98]
i=0
min=list[0]
while i<len(list):
		if list[i]<min:
			min=list[i]
		i+=1
print(min)
#minimum number