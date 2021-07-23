%% p.136 #26 (a)
clear
x=0:0.2:1;
y=exp(x);
m=length(x);

D=zeros(m,m);
D(:,1)=y';

for j=2:m
    for i=j:m
    D(i,j)=(D(i,j-1)-D(i-1,j-1))/(x(i)-x(i-j+1));
    end
end

D=D

%% p.136 #26 (b)
x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P0=[a(m-5),a(m-5),a(m-5)]

x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P1=a(m-4);

for i=m-5:-1:1
    P1=a(i)+(x0-x(i)).*P1;
end

P1=P1

x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P2=a(m-3);

for i=m-4:-1:1
    P2=a(i)+(x0-x(i)).*P2;
end

P2=P2

x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P3=a(m-2);

for i=m-3:-1:1
    P3=a(i)+(x0-x(i)).*P3;
end

P3=P3

x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P4=a(m-1);

for i=m-2:-1:1
    P4=a(i)+(x0-x(i)).*P4;
end

P4=P4

x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P5=a(m);

for i=m-1:-1:1
    P5=a(i)+(x0-x(i)).*P5;
end

P5=P5

function_value=[exp(0.1),exp(0.3),exp(0.5)]

%% p.136 #27(a)
clear
x=0:0.2:1;
y=atan(x);
m=length(x);

D=zeros(m,m);
D(:,1)=y';

for j=2:m
    for i=j:m
    D(i,j)=(D(i,j-1)-D(i-1,j-1))/(x(i)-x(i-j+1));
    end
end

D=D

%% p.136 #27(b)
x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P0=[a(m-5),a(m-5),a(m-5)]

x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P1=a(m-4);

for i=m-5:-1:1
    P1=a(i)+(x0-x(i)).*P1;
end

P1=P1

x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P2=a(m-3);

for i=m-4:-1:1
    P2=a(i)+(x0-x(i)).*P2;
end

P2=P2

x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P3=a(m-2);

for i=m-3:-1:1
    P3=a(i)+(x0-x(i)).*P3;
end

P3=P3

x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P4=a(m-1);

for i=m-2:-1:1
    P4=a(i)+(x0-x(i)).*P4;
end

P4=P4

x0=0.1:0.2:0.5;
for i=1:m
    a(i)=D(i,i);
end

P5=a(m);

for i=m-1:-1:1
    P5=a(i)+(x0-x(i)).*P5;
end

P5=P5

function_value=[exp(0.1),exp(0.3),exp(0.5)]

%% p.143 #4.2.5
clear
figure (1)
n=5
h1=10/n

x=[-5:h1:5];
y=1./(1+x.^2);
x0=linspace(-5,5,10000);
y0=newtonpoly(x,y,x0);

plot(x,y,'*'); hold on; plot(x0,y0)

figure (2)
n=10
h1=10/n

x=[-5:h1:5];
y=1./(1+x.^2);
x0=linspace(-5,5,10000);
y0=newtonpoly(x,y,x0);

plot(x,y,'*'); hold on; plot(x0,y0)

figure (3)
n=15
h1=10/n

x=[-5:h1:5];
y=1./(1+x.^2);
x0=linspace(-5,5,10000);
y0=newtonpoly(x,y,x0);

plot(x,y,'*'); hold on; plot(x0,y0)

figure (4)
n=20
h1=10/n

x=[-5:h1:5];
y=1./(1+x.^2);
x0=linspace(-5,5,10000);
y0=newtonpoly(x,y,x0);

plot(x,y,'*'); hold on; plot(x0,y0)

figure (5)
n=25
h1=10/n

x=[-5:h1:5];
y=1./(1+x.^2);
x0=linspace(-5,5,10000);
y0=newtonpoly(x,y,x0);

plot(x,y,'*'); hold on; plot(x0,y0)