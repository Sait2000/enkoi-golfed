I=lambda:map(int,input().split());t,n,*_=*I(),0;d=[];m=0
for M in[max]*t:T,S,P,*_=*I(),0,1;d+=T,;m+=M(T-S,0)*P
s=m
for i in range(n-t):s-=d[i%t];v,=I();s+=v;d[i%t]=v;m=M(m,s)
print(m)