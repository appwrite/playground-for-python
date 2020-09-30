
print("Playground for Python")
print("Appwrite + Python (=❤️)","\n")
result_a="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_a=result_a+"*"    
        else:      
            result_a=result_a+" "    
    result_a=result_a+"\n"    

result_p="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or ((column == 5 or column == 1) and (row == 1 or row == 2))):  
            result_p=result_p+"*"    
        else:      
            result_p=result_p+" "    
    result_p=result_p+"\n"    
    

print(result_a)
print(result_p,"\n",result_p);
print("\n", "Add 'W R I T E' alphabet.","\U0001f600")
