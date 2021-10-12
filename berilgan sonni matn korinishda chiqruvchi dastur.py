# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 10:32:07 2021
berilgan sonni matn korinishda chiqaruvchi dastur
@author: Acer
"""

n=int(input("1 dan 50 gacha son kiriting: "))
son=''
q=n%10
if q==0:
    q=None
elif q==1:
    q='bir'
elif q==2:
    q='ikki'
elif q==3:
    q='uch'
elif q==4:
    q='tort'
elif q==5:
    q='besh'
elif q==6:
    q='olti'
elif q==7:
    q='yetti'
elif q==8:
    q='sakkiz'
elif q==9:
    q='toqqiz'
if n>9 and n<20:
    son="o'n"+" "+q
elif n>20 and n<30:
    son="yigirma "+q
elif n>30 and n<40:
    son='ottiz '+q
elif n>40 and n<50:
    son='qirq '+q
elif n<10:
    print(q)
print(son)