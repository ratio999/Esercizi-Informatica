a=input()
b=input()
c=frac(a,b)
n=["x","y","z"]
m=[3,4,5]
s=zip(n,m)
s_list=list(s)
print(s_list)
c_star, v_star=zip(*s_list) #faccio un unzip
print(c_star)
print(v_star)
  