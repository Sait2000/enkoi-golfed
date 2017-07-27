I=lambda:map(int,input().split());t,n,*_=*I(),0;d=[];m=0
for i in range(t):T,S,P,*_=*I(),0,1;d+=T,;m+=max(T-S,0)*P
s=m
for i in range(n-t):s-=d[i%t];v,=I();s+=v;d[i%t]=v;m=max(m,s)
print(m)