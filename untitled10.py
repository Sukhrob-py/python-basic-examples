# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:37:59 2021

@author: Acer
"""

word=input("soo'z kiriting>>>")
n=0
javob=[]
result=[]
for i in word:
    result.append(i)
for i in result:
    for j in result:
        if i==j:
            n+=1
            
    if i in javob:
        continue
    else:
        javob.append(i)
    
        
    print(f"sizning so'zingizda {n} ta {i} bor")
    n=0
    
print(javob)