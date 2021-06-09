n=input("enter the br")
b=0
b1=0
b2=0
b3=0
b4=0
b5=0
i=0
while i<len(n):
	if n[i]=='(':
		b=b+1
	elif n[i]==')':
		b1=b1+1
	elif n[i]==']':
		b2=b2+1
	elif n[i]=='[':
		b3=b3+1
	elif n[i]=='{':
		b4=b4+1
	elif n[i]=='}':
		b5=b5+1
	else:
		print('not')
	if b==b1 and b2==b3 and b4==b5 :
		print("correct")
	else:
		print('not correct')