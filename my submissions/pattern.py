#make arrow configuration 

#introduce n variable- widest point is 5 stars 
n = 5  

#create a loop
for i in range(1, 2*n):  
    if i <= n:
        print('*' * i)  
    else:
        print('*' * (2*n - i))  