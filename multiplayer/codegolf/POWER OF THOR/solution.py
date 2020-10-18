X,Y,x,y=map(int,input().split())
while 1:a,b=(X>x)-(X<x),(Y>y)-(Y<y);print((' SN'[b]+' EW'[a]).strip());x+=a;y+=b
