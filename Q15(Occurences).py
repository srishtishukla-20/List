l= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
i=0
s=[]
a_c,n_c,t_c,x_c,u_c,g_c=0,0,0,0,0,0
while i<len(l):
	if l[i]=='a':
		a_c=a_c+1
	elif l[i]=='n':
		n_c=n_c+1
	elif l[i]=='t':
		n_c=t_c+1
	elif l[i]=='x':
		x_c=x_c+1
	elif l[i]=='u':
		u_c=u_c+1
	elif l[i]=='g':
		g_c=g_c+1
	else:
		print("no")
	i=i+1
print("a",a_c)
print("n",n_c)
print("t",t_c)
print("x",x_c)
print("u",u_c)
print("g",g_c)
#count occurences