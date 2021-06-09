l=[1,2,3,4,5,6,7,8,9,10]
i=int(input("enter number"))
j=0
while j<len(l):
	print(i,"*",j,"=",i*l[j])
	j=j+1
#table
List=[1,2,3,4,5,6,7,8,9,10]
i=int(input("enter number"))
j=0
while j<len(List):
	print(i*List[j])
	j=j+1
#any table
l=[0,1,2,3,4,5,6,7,8,9,10]
i=int(input("enter number"))
j=1
while j<len(l):
	print(i,"×",j,"=",i*l[j])
	j=j+1
#table
List=[1,2,3,4,5,6,7,8,9,10,11]
p=int(input("enter number"))
i=1
j=[]
while i<len(List):
    a=(i*p)
    j.append(a)
    i=i+1
print(j)
#Table of one digit in list
list=[[1,3,4,5],[5,7,8,9],[3,7,8,8],[1,3,4,7]]
i=0
while i<len(list):
	j=0
	new=1
	while j<len(list):
		new=list[j][i]*new
		j+=1
	i=i+1
	print(new)
#multiples of list
a1=[2,3,4,5,7]
a2=[1,2,3,1,2]
n=[]
i=0
while i<len(a1):
	b=a1[i]*a2[i]
	n.append(b)
	i=i+1
print(n)
#multiply both list

