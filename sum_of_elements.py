n=int(input("Enter the limit:")) 
arr=[]
for i in range(0,n):
    k=int(input("")) 
    arr.append(k)
sum = 0;    
   
for i in range(0, len(arr)):    
   sum = sum + arr[i];   
   
print("The Array Elements:")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
    
print()
     
print("Sum of all the elements of an array: " );  
print(sum);

