num1=10
num2=15
num3=20

if (num1>=num2) and (num1>=num3):
   largest=num1
elif (num2>=num1) and (num2>=num3):
   largest=num2
else:
   largest=num3

print("largest number between",num1,",",num2,",",num3,"is",largest)