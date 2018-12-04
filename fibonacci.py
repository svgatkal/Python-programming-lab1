#snehal gatkal 11810225
nterms=10
n1=0
n2=1
count=0
if n terms<=0
  print("please enter positibe number ")
elif nterms==1:
  print("fibonecci sequence upto",nterns,":")
  print(n1)
else:
  print("fibonacci sequence upto",nterms,":")
  while count<nterms:
    print(n1,end=',')
    nth=n1+n2
    #update values
    n1=n2
    n2=nth
    count+=1
 
