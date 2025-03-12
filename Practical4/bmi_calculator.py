weight=input('your weight is:') #gain the weight
height=input('your height is:') #gain the height
weight=int(weight) #trun the string to number
height=int(height) #trun the string to number
bmi=weight/(height*height) #calculate the bmi
if bmi>30: #tell the type
    print('obese')
elif bmi<18.5:
    print('underweight')
else:
    print('normal')

print('your BMI is:',str(bmi)) #output the bmi
