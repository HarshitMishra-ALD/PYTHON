p1 ="Make a lot of money"
p2 ="buy now"
p3 ="subscribe this"
p4 ="Click here"

massage = input("Enter your massage: ")

if((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("This is a spam massage")

else:
    print("This is not a spam massage")    