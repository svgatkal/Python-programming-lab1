#snehal gatkal 11810225
name=input("enter your name-")
rollno=input("enter your roll no-")
grno=input("enter your gr no-")
english=input("enter your english marks-")
maths=input("enter your maths marks-")
science=input("enter your sci marks-")
x=["name","roll no","gr no","english","maths","sci"]
y=[name,rollno,grno,english,maths,science]
t=dict(zip(x,y))
print(t)
