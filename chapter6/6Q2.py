m1=int(input("enter the marks of the first subject: "))
m2=int(input("enter the marks of the second subject: "))
m3=int(input("enter the marks of the third subject: "))


if((m1+m2+m3)/3>40 and m1>=33 and m2>=33 and m3>=33):
    print("The student has passed the exam.")
else:
    print("The student has failed the exam.")
 
