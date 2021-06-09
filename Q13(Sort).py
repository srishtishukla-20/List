n=[30,10,12,14,15]
i=0
c=0
while i<len(n):
	j=0
	while j<len(n):
		if n[i]<n[j]:
			c=n[j]
			n[j]=n[i]
			n[i]=c
		j=j+1
	i=i+1
print(n)
#bubble sort
new=[12,54,67,3,4,58,34]
i=0
while i<len(new):
     r=new[i]
     s=i
     while s>0 and new[s-1]>r:
         new[s]=new[s-1]
         s=s-1
     new[s]=r
     i+=1
print(new)
#insertion sort
A = [4,34,67,12,32,10,5,2,78,20,19]
i=0
while i<len(A):
	j=0
	min_=i
	while j<len(A):
	        if A[min_]<A[j]:
	        	min_ = j
	        j=j+1
	        A[i], A[min_] = A[min_], A[i]
	i=i+1
print(A)
#selection sort
A= ['c','a','b','q','r','i','j']
i= 0
while i<len(A):
	j=0
	min_= i
	while j<len(A):
		if A[min_]<A[j]:
			min_= j
		j= j+1
		A[i], A[min_] = A[min_], A[i]
	i= i+1
print(A)
# sort alphabet
list1=[2,4,5,6]
list2=[1,2,8,9,6]
list3=list1+list2
i=0
list4=[]
while i<len(list3):
        j=i+1
        while j<len(list3):
            if list3[j]==list3[i]:  
                list4.append(list3[i])
            j+=1
            e=0
            while e<len(list4):
                	if (list4[e])  in (list3):
                		list3.remove(list4[e])
                		temp=list3+list4
                		temp.sort()
                	e=e+1
        i+=1
print(temp)
#sort from both list
list1=[2,3,4,5,6]
list2=[1,2,8,9,3,6]
i=0
list3=[]
while i<len(list1):
	list3.append(list1[i])
	i+=1
j=0
while j<len(list2):
	list3.append(list2[j])
	j+=1
print("adding two lists=",list3)
m=0
a=[]
while m<len(list3):
        k=m+1
        while k<len(list3):
            if list3[m]==list3[k]:  
                a.append(list3[m])
            k=k+1
        m+=1
e=0
b=[]
while e<len(a):
		if (a[e])  in list3:
			list3.remove(a[e])
		e=e+1
f=0
list4=[]
while f<len(list3):
	list4.append(list3[f])
	list4.sort()
	f=f+1
print("duplicates=",a)
print("new list=",list3)
print("sorted list=",list4)
#sort both list long method
list=[34,-1,9,-6,-1,1,8]
i=0
while i<len(list):
	if list[i]<0:
		list[i]=0
	i+=1
j=0
while j<len(list):
	s=j
	while s<len(list):
		if list[s]>0:
			if list[j]>list[s]:
				attemp=list[j]
				list[j]=list[s]
				list[s]=attemp
		s+=1
	j+=1
print(list)
#in - position 0 and ascending order
a=[8,3,5,-3,4,-2,9]
i=0
b=[]
while i<len(a):
	if a[i]<0:
		a[i]=0
	i+=1
j=0
while j<len(a):
		z=j
		while z<len(a):
			if a[z]>0:
				if a[j]>a[z]:
					attemp=a[j]
					a[j]=a[z]
					a[z]=attemp
			z+=1
		j=j+1
print(a)
#print 0 in place of negative and sort




