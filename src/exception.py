def frac(x,y):
 try:
   result=float(x)/float(y)
   print(result)
 except ZeroDivisionError:
   print("Mai dividere per 0!")
 except:
   print("Qui c'è qualcosa che non va...") #prova a scrivere "cane" in input
 finally:
   print("Buona giornata!")
 
a=input()
b=input()
c=frac(a,b)
n=["x","y","z"]
m=[3,4,5]
s=zip(n,m)
s_list=list(s)
print(s_list)
c_star, v_star=zip(*s_list)
print(c_star)
print(v_star)
sum=lambda[arg1,arg2]: arg1+arg2
d=sum[a,b]  