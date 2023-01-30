# A "True Love Calculator" which produces a compatability rating 
# based on the number of times the words 'true' and 'love'
# appear in each person's name

print("True Love Calculator")
name1=input("Your name: ").lower()
name2=input("Your crush's name: ").lower()

true=name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")
true+=name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e")

love=name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")
love+=name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e")

true_love=str(true)+str(love)

if int(true_love)<10 or int(true_love)>90:
    print(f"Your score is {true_love}, you go together like coke and mentos")
elif int(true_love)>=40 or int(true_love)<=50:
    print(f"Your score is {true_love}, you are alright together")
else:
    print(f"Your score is {true_love}")
