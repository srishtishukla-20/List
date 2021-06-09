elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
count_even = 0
count_odd = 0
sum_even=0
sum_odd=0
i = 0 
while(i < len(elements)):
	if elements[i] % 2 ==0:
		count_even= count_even +1
		sum_even= sum_even + elements[i]
		avg_even= sum_even/4
	else: 
		count_odd = count_odd +1
		sum_odd= sum_odd + elements[i]
		avg_odd= sum_odd/7
	i= i+1
print("Even numbers in the list: ", count_even,"sum of even=",sum_even,"avrg of even:",avg_even)
print("Odd numbers in the list: ", count_odd,"sum of odd=",sum_odd,"avrg of odd:",avg_odd)
# average and sum of odd and even numbers
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
even_count = 0
odd_count = 0
i = 0 
while(i < len(elements)):
	if elements[i] % 2 ==0:
		even_count = even_count+1
	else: 
		odd_count = odd_count+1
	i= i+1
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count) 
# count of odd and even numbers in list
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
sum_even = 0
sum_odd = 0
i = 0 
while(i < len(elements)):
	if elements[i] % 2 ==0:
		sum_even= sum_even + elements[i]
	else: 
		sum_odd= sum_odd + elements[i]
	i= i+1
print(sum_even)
print(sum_odd)
# sum of odd even
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
sum_even = 0
sum_odd = 0
i = 0 
while(i < len(elements)):
	if elements[i] % 2 ==0:
		sum_even= sum_even + elements[i]
		avg_even= sum_even/4
	else: 
		sum_odd= sum_odd + elements[i]
		avg_odd= sum_odd/7
	i= i+1
print(avg_even)
print(avg_odd)
# avg of even and odd
kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
c=0
l=0
d=0
while i<len(kitna_paisa_hai):
	if kitna_paisa_hai[i]>=10000000:
	
		c=c+1
	elif (kitna_paisa_hai[i]<=1000000) and (kitna_paisa_hai[i]>10000):
	
		l=l+1
	else:
	
		d=d+1
	i=i+1
print(c,"crorepati hai")
print(l,"lakhpati hai")
print(d,"dilwale hai")
#numbers of crorepati
a=[0,5,8,7,4,6,2]
i=0
while i<len(a):
	if  a[i]%2==0:
		print("1")
	else:
		print("0")
	i=i+1
# print "1" if it is even and "0" if it is odd


