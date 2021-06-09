m = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
while i<len(m):
	r1=r1+m[0][i]
	r2=r2+m[1][i]
	r3=r3+m[2][i]
	c1=c1+m[0][i]
	c2=c2+m[1][i]
	c3=c3+m[2][i]
	i=i+1
print(r1)
print(r2)
print(r3)
print(c1)
print(c2)
print(c3)
#Magic square without using sum
a=[[8,3,4],[1,5,9],[6,7,2]]
i=0
r1,r2,r3,d1,d2,c1,c2,c3=0,0,0,0,0,0,0,0
while i<len(a):
	r1=r1+a[0][i]
	r2=r2+a[1][i]
	r3=r3+a[2][i]
	c1=a[0][0]+a[1][0]+a[2][0]
	c2=a[0][1]+a[1][1]+a[2][1]
	c3=a[0][2]+a[1][2]+a[2][2]
	d1=a[0][0]+a[1][1]+a[2][2]
	d2=a[0][2]+a[1][1]+a[2][0]
	i=i+1
if r1==r2==r3==c1==c2==c3==d1==d2:
	print('magic square')
else:
	print('not magic square')	
# magic square
a=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(a):
	j=0
	r_sum=0
	c_sum=0
	while j<len(a[i]):
		c_sum=c_sum+a[i][j]
		r_sum=r_sum+a[j][i]
		j+=1
	i+=1
print(c_sum)
print(r_sum)
c=0
while c<len(a):
	d=0
	sum1=0
	while d<len(a):
		sum1=sum1+a[c][d]
		d=d+1
	c=c+1
print(sum1)
if c_sum==r_sum and c_sum==sum1:
	print("magic square")
else:
	print("not magic square")
#magic square loop using 3 loops
a=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(a):
	j=0
	r_sum=0
	c_sum=0
	while j<len(a[i]):
		c_sum=c_sum+a[i][j]
		r_sum=r_sum+a[j][i]
		j = j + 1
	i = i + 1
	print(c_sum)
	print(r_sum)
 
 
c=0 
d=0
sum1 = 0
while c<len(a):
	sum1 = sum1 + a[c][d]
	c = c + 1
	d = d + 1
print(sum1)
 
 
e=0 
f=len(a)-1
sum2 = 0
while e<len(a):
	sum2 = sum2 + a[e][f]
	e = e + 1
	f = f - 1
print(sum2)	
 
if c_sum==r_sum and c_sum==sum1 and sum1 == sum2:
	print("magic square")
else:
	print("not magic square")
#magic number
a=[[8,3,4],[1,5,9],[6,7,2]]
i= 0
r1,r2,r3,c1,c2,c3,d1,d2= 0,0,0,0,0,0,0,0
while i<len(a):
	r1=r1+a[0][i]
	r2=r2+a[1][i]
	r3=r3+a[2][i]
	c1=c1+a[i][0]
	c2=c2+a[i][1]
	c3=c3+a[i][2]
	d1=d1+a[i][i]
	d2=d2+a[i][2-i]
	i= i+1
if r1==r2==r3==c1==c2==c3==d1==d2:
	print('magic square')
else:
	print('not magic square')
# magic square
a=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(a):
	j=0
	c=0
	r_sum=0
	c_sum=0
	d1_sum=0
	while j<len(a[i]):
		c_sum=c_sum+a[i][j]
		r_sum=r_sum+a[j][i]
		d1_sum=d1_sum+a[i][c]
		j = j + 1
		c=c+1
	i = i + 1
	print(c_sum)
	print(r_sum)
	print(d1_sum)
e=0 
f=len(a)-1
d2_sum = 0
while e<len(a):
	d2_sum= d2_sum + a[e][f]
	e = e + 1
	f = f - 1
print(d2_sum)	
 
if c_sum==r_sum and c_sum==d1_sum and d1_sum == d2_sum:
	print("magic square")
else:
	print("not magic square")
#magic number
a=[[8,3,4],[1,5,9],[6,7,2]]
i=0
 
mgsum = []
while i<len(a):
	j=0
	r_sum=0
	c_sum=0
	while j<len(a[i]):
		c_sum=c_sum+a[i][j]
		r_sum=r_sum+a[j][i]
		j= j + 1
	i = i + 1
	mgsum.append(c_sum)
	mgsum.append(r_sum)
	print('sum of row is =',r_sum)
	print('sum of col is =',r_sum)
 
c=0 
d=0
f=len(a)-1
d1=0
d2=0
while c<len(a):
	d1=d1 + a[c][d]
	d2=d2+a[c][f]
	c=c+1
	d=d+1
	f=f-1
mgsum.append(d1)
mgsum.append(d2)
print("d1=",d1)
print("d2=",d2)
 
if mgsum[0]==mgsum[1] == mgsum[2]== mgsum[3] == mgsum[4] == mgsum[5] == mgsum[6] == mgsum[7]:
	print("a is magic square")
else:
	print("a is not magic square")
# magic square
a=[[8,3,4],[1,5,9],[6,7,2]]
#mgsum= []
c=0 
d=0
d1=[]
while c<len(a):
	s=a[c][d]
	d1.append(s)
	c=c+1
	d=d+1
print(d1)
a=[[8,3,4],[1,5,9],[6,7,2]]

c=0 
d2= []
f=len(a)-1
while c<len(a):
	s= a[c][f]
	d2.append(s)
	c=c+1
	f=f-1
print(d2)
# diagonal of magic square