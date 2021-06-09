question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal= ", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1] 
print("Co-Powered by Dabur Amla presents,Kaun Banega Crorepati mein apka swagat hai!!")
print("Sadab,Aadab aur Shastriyakal.")
print("Pehla Question yeh rha apke screen ke upar:")
i= 0
while i<len(question_list):
	#print('your question is')
	print(i+1,question_list[i])
	
	a= 0
	while a<=len(options_list):
		#print('your options')
		print(a+1,options_list[i][a])
		a= a+1
	j= int(input('enter solution'))
	if j==solution_list[i]:
			print('congrats')
	else:
			print('quit')
			break
	i=i+1
# kon banega crorepati without lifeline
list = [".How many continents are there?",".What is the capital of India?",       ".in Ng what we learning"]
opt= [["Four", "Nine", "Seven", " Eight"],[" Chandigarh", "Bhopal", " Chennai", "Delhi"],["Software Engineering", " Counseling", "Tourism", "Agriculture"]]
fiftyfifty=[['four','seven'],['Delhi','Bhopal'],['Tourism','software engineering']]
solution1=[2,1,2]
solution=[3,4,1]
i=0
c=0
while i<len(list):
        print('your question is')
        print(i+1,list[i])
        j=0
        print('your options are')
        while j<=len(opt):
            print(j+1,opt[i][j])
            j +=1
        n=int(input('enter sol'))
        if n==solution[i]:
            print('congrates')      
        elif n==5050:
            if c==0:
                m=0
                while m<len(fiftyfifty[i]):
                    print(m+1,fiftyfifty[i][m])
                    m=m+1
                c=c+1
                num=int(input('enter sol'))
                if num==solution1[i]:
                    print('correct')
                else:
                    print("your option is wrong")
                    print('quit')
                    break
            else:
                print('you used 5050 lifeline')
                num1=int(input("enter your option"))
                if num1==solution[i]:
                    print("congrates")
                else:
                    print("your option is wrong")
                    break
        else:
            print('your answer is wrong')
            print('quit')
            break    
        i +=1
#KBC using 5050 
question_list = ["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai"]
options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
solution_list = [3, 4, 1] 
fifty_fifty = [
['1.Four','3.seven'],['2.Bhopal','4.Delhi'],['1.Software Engineering','2.Counseling']]
i = 0
c=0
print("you have 5050 lifeline , if you want you  can  use it by entering '5050' ")
while i < len(question_list):
    print(question_list[i])
    j = 0
    while j < len(options_list[i]):
        print(options_list[i][j])
        j +=1
    user=int(input("enter your number option: "))
    if user == solution_list[i]:
        print('congress')
    elif user == 5050:
        if c == 0:
            print(fifty_fifty[i])
            c+=1
            user1  = int(input("enter your option now : "))
            if user1 == solution_list[i]:
                print("congrates! , you choice correct option" )
            else:
                print("sadly!, your choice wrong option")
        else:
            print("you used fifty fifty ,so please enter your own answer") 
    else:
        print("oops! your answer is wrong ")
        print('quite')
        break
    i+=1
    #kbc using 50-50
    
