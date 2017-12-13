
a=int(input("enter the number:"))
sum=0
for i in range(a):
    if(i>0):
        if(a%i==0):
            sum=sum+i

            i=i+1   
print(sum)            
    
   
 
