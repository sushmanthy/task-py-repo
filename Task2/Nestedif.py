#Job Eligibility
name=input("enter your name:-")
age=int(input("enter your age:-"))
height=int(input("enter your height using cm:-"))
weight=int(input("enter your weightusing kg:-"))

if(age>=18):
    if(height>=160):
        if(weight>=60):
            print(name,"congradulation your selected")
        else:
            print(name,"your weight is not eligible")
    else:
        print(name,"your height is not eligible")
else:
    print(name,"your age is not eligible")          


#College Admission

name=input("enter your name:-")
age=int(input("enter your age:-"))
marks=int(input("enter your marks:-"))

if(age>=17):
    if(marks>=60):
            print(name,"congradulation your selected")
    else:
        print(name,"your marks is not eligible")
else:
    print(name,"your age is not eligible") 


#sports selection

name=input("enter your name:-")
age=int(input("enter your age:-"))
height=int(input("enter your height using cm:-"))
weight=int(input("enter your weightusing kg:-"))

if(age>=16):
    if(height>=150):
        if(weight>=50):
            print(name,"congradulation your selected")
        else:
            print(name,"your weight is not eligible")
    else:
        print(name,"your height is not eligible")
else:
    print(name,"your age is not eligible")          

