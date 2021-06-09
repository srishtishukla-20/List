i=1
while i<20:
	a=(4*i)-3
	if a<18:
		print(a)
	i+=1
#output 1,5,9,13,17
i=1
while i<20:
	if i%4==1:
		print(i)
	i+=1
#using modulous
list=[1,3,5,7,8]
i=0
while i<len(list):
		s=list[i]*list[i]
		print(s)
		i+=1
#squares  of elements in list
list1 = [1, 2,5,3,4, 3] 
i=1
x=0
while x<len(list1):
	i=i*list1[x]
	x=x+1
print(i)
#simple multiples in list
a=[2,5,1,4]
n=int(input('en'))
i=0
while i<len(a):
	if i%2==0:
		pass
	i=i+1
print(n-2)
#print number from user
list=[35,78,9,83]
list2=[4,98,102,39]
i=0
new=1
j=1
while i<len(list):
	new=list[i]*new
	j=list2[i]*j
	if new>j:
		a=new-j
	else:
		a=j-new
	i=i+1
print(a)

a= [1,2,3,4,5]
i= 0
j= []
while i<len(a):
	j.append(-a[i])
	i= i+1
print(j)
#output:print negative
a=[1,2,'3',6,'9',7]
i=0
sum=0
while i<len(a):
	sum=sum+int(a[i])
	i=i+1
print(sum)
#sum of list
a=["A","B"]
n=int(input('enter the num'))
i=1
b=[]
while i<=n:
	j=0
	while j<len(a):
		x=(a[j]+str(i))
		b.append(x)
		j=j+1
	i=i+1
print(b)
#o/p=A1,B1,A2,B2
list=[3,4,8,'b','q','n']
user=int(input('enter the num'))
a=len(list)
b=a-user
i=0
while i<user:
	print(list[b])
	b+=1
	i+=1
#logic
a=["q","n","r"]
b=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n= input('enter the letter')
i= 0
s= []
while i<len(a):
	j= 0
	while j<len(b[i]):
		if n==a[i]:
			lst1=b[i][j]
			s.append(lst1)
		j= j+1
	i= i+1
print(s)
#print list from user
m=[39,4,-4,55,-6]
i=0
sum=0
while i<len(m):
	if m[i]>0:
		sum=sum+m[i]
	i=i+1
print(sum)
#positive sum
a= [23,48,72,89,3,47,28,38]
user= int(input('enter no.'))
i= 0
while i<len(a)-1:
	j= i
	while j<(i+user):
		print(a[j],end=' ')
		j= j+1
	print()	
	i= i+1
# logic
a= [82,35,41,8,9,75]
user= int(input('enter no.'))
i= 0
while i<len(a)-user+1:
	j= i
	while j<(i+user):
		print(a[j],end=' ')
		j= j+1
	print()	
	i= i+1

n="PAR15"
b=[]
i=0
while i<len(n):
	b.append(n[i])
	if b[i]=="1":
		b[i]="I"
	elif b[i]=="5":
		b[i]="S"
	i=i+1
print(b)

#par15 output paris
a=["m","na","i","mama"]
b=["y","me","s","tha"]
n=[]
i=0
while i<len(a):
	m=a[i]+b[i]
	n.append(m)
	i=i+1
print(n)
#add 2 list using loop
start=int(input("enter any num for starting your loop="))
limit=int(input("enter  limit of your loop="))
i=start
empty=[]
while start<=limit:
    empty.append(start)
    start+=i
print(empty)
#starting and limit
a="12345"
i=1
b=[]
while i<len(a):
	rev=a[-i]
	b.append(rev)
	i+=1
j=0
c=[]
empty_str=""
while j<len(b):
	square=(int(b[j]))*(int(b[j]))
	c.append(square)
	k=str(c[j])+empty_str
	print(k,end="")
	j+=1
#reverse and square of string in multiple loop
a="12345"
i=1
j=0
empty_str=""
b=[]
while i<=len(a):
	b.append(a[-i])
	square=int(b[j])*int(b[j])
	k=str(square)+empty_str
	print(k,end="")
	j+=1
	i+=1
#reverse and square of string in one loop
a="Gouri"
b="Priyanka"
if len(a)<len(b):
	print(a+b+a)
elif len(b)<len(a):
	print(b+a+b)
else:
	pass
#GouriPriyanka
a="Gouri"
b="Priyanka"
i=0
while i<len(b)-1:
	if len(a)<len(b):
		print(a+b+a)
		break
	elif len(b)<len(a):
		print(b+a+b)
		break
	else:
		pass
	i+1
#GouriPriyankaGouri
s=int(input("en"))
l=int(input("en"))
e=[]
i=1
while s<=l:
	e.append(s)
	s=s+1
print(e)
#print elements from limit






