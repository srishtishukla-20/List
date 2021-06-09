a=[-78,-89,-54,-4,-3]
i=0
count=a[i]
while i<len(a):
	if a[i]>count:
		count=a[i]
	i=i+1
print(count)
#maximum number in minus
n=[50,40,24,70,56,12,5,10,7]
i=0
count=0
while i<len(n):
	if n[i]>count:
		count=n[i]
	i=i+1
print(count)
#maximum number without using max function
list=[52,62,1,2,11,98]
i=0
while i<len(list):
	c=0
	while c<len(list):
		if list[i]>list[c]:
			min=list[i]
		c+=1
	i+=1
print(min)
#maximum number
list1 = [10, 20, 4,45, 99]
a=max(list1[0],list1[1]) 
b=min(list1[0],list1[1]) 
i=0
while i<len(list1):
	if list1[i]>a:
		b=a
		a=list1[i] 
	elif list1[i]>b and a != list1[i]:
		b=list1[i]
	i+=1
print("second largest number:",str(b))
#second largest
list=[50,40,23,79,70,56]
i=0
largest1=0
largest2=0
while i<len(list):
	if list[i]>largest1:
		largest1=list[i]
	j=0
	while j<len((list)):
		if (largest1>list[j] and largest2<list[j]):
			largest2=list[j]
		j+=1
	i+=1
print(largest2)
#second largest in diff way
