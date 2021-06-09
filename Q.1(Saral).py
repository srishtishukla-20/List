students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
print(len(students))
length = (len(marks)) 
counter = 0
while (counter < length):
    print (students[counter] + str(marks[counter]))
    counter=counter+1
#saral example
num=[50,40,23,70,56,12,5,10,7]
print(len(num))
length=(len(num))
counter=0
while (counter<length):
	if (counter>20) or (counter<40):
		print(num[counter])
		counter=counter+1
#print numbers from list
list= [7,9,10,5,4,3,1,2]
a= 0
while a<len(list):
	print(list[a])
	a= a+1
# list print
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
i= 0
sum= 0
while i< len(marks[0]):
	sum= sum+marks[0][i]+marks[1][i]+marks[2][i]
	i= i+1
print(sum)
# report card   
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
i= 0
sum= 0
while i<len(marks):
	j= 0
	while j< len(marks[i]):
		sum= sum+ marks[i][j]
		j= j+1
	i= i+1
print(sum)
# report card using nested loop
a=[1,2,3,4]
i=1
while a[i:]:
	i+=1
print(i)
#without using length function
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
] 
i= 0
sum= 0
while i<len(marks):
	j= 0
	while j< len(marks[i]):
		sum= sum+ marks[i][j]
		j= j+1
	i= i+1
print(sum)
#report card second question
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
] 
i= 0
sum= 0
while i<len(marks):
	j= 0
	while j< len(marks[i]):
		sum= sum+ marks[i][j]
		j= j+1
	i= i+1
print(sum)
# report card third no.
list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
a=[]
i=0
while i<(len(list1)):
	if (list1[i]) not in (list2):
		a.append(list1[i])
	i=i+1
print(a)	
# array
number_list=[1,2,3,4,5,6,7,8,9,10]
i=0
sum=0
while i<len(number_list):
	sum=sum+number_list[i]
	i=i+1
print(sum)
#print the sum of 1 to 10
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
i = 0
while i < len(n):
	j = i 
	while j < len(n):
		if n[i] + n[j] == number:
			print(n[i], n[j], end='\n')
		j = j + 1
	i = i + 1
# Total of sum

a=[2,3,6]
b=[5,6,7]
i=0
sum=0
while i<len(a):
	sum=a[i]+b[i]
	i=i+1
	print(sum,end=" ")
#sum of list
num=30
n=[10,11,12,13,14,17,18,19]

i=0
b=[]
while i<len(n):
	j=i
	a=[]
	while j<len(n):
		if n[i] + n[j] ==num:
			a.append(n[i])
			a.append(n[j])
			b.append(a)
		j=j+1
	i=i+1
print(b)
#output is [[11,19],[12,18],[13,17]]
num=[50,40,23,70,56,12,5,10,7]
counter=0
while counter<len(num):
	if num[counter]>=20 and num[counter]<=40:
		print(num[counter])
	counter=counter+1
#greater than 20 less than 40
num=[63,2,3]
total=sum(num)
print(total)
#sum of numbers using sum function
n=int(input("enter value"))
list=[12,34,56,78,13,56,8,9]
j=1
i=0
while i<len(list):
	if n==j:
		print(list[0:j])
	i=i+1
	j=j+1
#user input questions
list1=[5,7,8,9]
list2=[5,7,3,2]
i=0
while i<len(list2):
	if list1[i] not in list2:
		print(list1[i])
	i=i+1
#print numbers which is not in list2
a=[2,3,6,9,10]
i=-1
while i>=(-len(a)):
	print(a[i])
	i=i-1
#reverse list
a=[[1,2,3],[5,6,8],[9,8]]
i=0
b=[]
while i<len(a):
	j=0
	sum=0
	while j<len(a[i]):
		sum=sum+a[i][j]
		j=j+1
	b.append(sum)
	i=i+1
print(b)
#sum of list
a1=[2,3,4,5,7]
a2=[1,2,3,1,2]
n=[]
i=0
while i<len(a1):
	b=a1[i]**a2[i]
	n.append(b)
	i=i+1
print(n)
#multiplication of list from from another elements from power
a=[4,5,7]
i=0
while i<len(a):
	if a[i]==5:
		print(a[i])
	i+=1
#print middle one



