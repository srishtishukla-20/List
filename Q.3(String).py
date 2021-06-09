s=['window','os','linax']
print('original list:',s)
s.reverse()
print('update list:',s)
#Using reverse function
p=["delhi","gujrat","rajasthan","punjab","kerala"]
i=-1
b=[]
while i>=(-len(p)):
	b.append(p[i])
	i-=1
print(b)
#reverse
list= input('enter the name')
str= ' '
i= len(list)-1
while i>=0:
	str= str+list[i]
	i= i-1
print('revers string',str)
# without function and without colen using reverse
text= "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
print(text.replace("over","on"))
#with using replace
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 
i=1
while i<=len(places):
	print(places[-i],end=' ')
	i=i+1
#reverse string without using function and slicing
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 

i=1
j=[]
while i<=len(places):
	j.append(places[-i])
	i=i+1
print(j)
#list inside list
list1 = 'wather'
list2 ='theeraphw' 
a=[]
i=0
while i<(len(list1)):
	if (list1[i]) in (list2):
		a.append(list1[i])
	i=i+1
print(a)	
#append duplicates
#Q 2.Sort the letters in the string s by the order the occur in the string t.
# Example
# For s = "weather" and t = "therapyw", the output should be
# sortByString(s, t) = "theeraw";
#Solution:
a='weather'
b='therapyw'
i=0
c=" "
while i<len(b):
    j=0
    while j<len(a):
        if b[i]==a[j]:
            print(a[j],end="")
        j=j+1
    i=i+1

mainstr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
newstr=mainstr.split(' ')
i=0
a=' '
while i < len(newstr):
	if newstr[i]=="over":
		a=a+'on'+' '
	else:
		a=a+newstr[i]+' '
	i=i+1
print(a)
		#add=mainStr[i]
		#new_str.append(add)
	#i=i+1
#print(new_str)
a= ['gouri','srishti','puja','prinyanka','gita','suman']
i= 0
m= []
j= input('enter the name')
while i<len(a):
	if a[i][0]==j:
		m.append(a[i])
	i= i+1
print(m)
#name list with user input
a=["Priyanka"]
i=0
while i<len(a[0]):
	print(a[0][i])
	i+=1
#names printing
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
lst2= []
n = 3
i=0
while i<n:
    lst2.append(lst[i::n])
    i+=1
    print(lst2)
#using slicing
list= input('enter the name')
str= ' '
i= len(list)-1
while i>=0:
	str= str+list[i]
	i= i-1
print('revers string',str)
#reverse name


