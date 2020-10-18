X,Y,x,y=map(int,input().split())
while 1:a,b=(X>x)-(X<x),(Y>y)-(Y<y);print(('S N'[1-b]+'E W'[1-a]).strip());x+=a;y+=b
