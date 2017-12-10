n=int(input())
a=int(input())
sum=0
for i in range(n):
    if(i>0):
        if(a%i==0):
            sum=sum+i

            i=i+1   
print(sum)            
    
   
 