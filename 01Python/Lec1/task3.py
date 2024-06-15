def counter_4(nums):
    counter=0
    for i in  nums:
     if i==4:
       counter+=1
 
    return counter     


    
print(counter_4([5,5,5,5,56]))
print(counter_4([0,2,4,6,8,4,2,10,44,4,4,4,4,4]))