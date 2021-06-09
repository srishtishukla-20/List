row=int(input("en"))
c=int(input("en"))
i=1
a=1
list1=[]
while i<=row:
	b=a
	j=1
	list2=[]
	while j<=c:
		list2.append(b)
		j=j+1
		b=b+1
	list1.append(list2)
	i=i+1
	a=a+c
print(list1)
#creating nested list using user input
list1=[7,9,8,5,3,4,2,1]
a=int(input('enter the number'))
i=0
b=[]
while i<len(list1):
	j=0
	c=[]
	while j<len(list1):
		if list1[j]==a:
			c.append(list1[i])
			c.append(list1[j])
			b.append(c)
		j+=1
	i+=1
print(b)
#creating nested list from user
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
n=3
lst2= []
i=0
while i<n:
    	j=i
    	lst3=[]
    	while j<len(lst):
    		lst3.append(lst[j])
    		j=j+3
    	lst2.append(lst3)
    	i+=1
print(lst2)
#o/p:[a,d,g,j,m],[b,e,h,k],[c,f,i,l]


