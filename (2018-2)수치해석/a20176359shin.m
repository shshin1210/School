%% p384 1.(b) h=0.2
a=0 ; b=10 ;
h = 0.2;
n = (b-a)/h;
t = a:h:b;
y(1) = 1;
f = @(t,y)((1/(1+t^2))-2*y^2);

for i = 1:n        
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = t(i)/(1+(t(i))^2);
end

err = abs(e_y-y);
ans=err
%% p384 1.(b) h=0.1
a=0 ; b=10 ;
h = 0.1;
n = (b-a)/h;
t = a:h:b;
y(1) = 1;
f = @(t,y)((1/(1+t^2))-2*y^2);

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = t(i)/(1+(t(i))^2);
end

err = abs(e_y-y);
ans=err
%% p384 1.(b) h=0.05
a=0 ; b=10 ;
h = 0.05;
n = (b-a)/h;
t = a:h:b;
y(1) = 1;
f = @(t,y)((1/(1+t^2))-2*y^2);

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = t(i)/(1+(t(i))^2);
end

err = abs(e_y-y);
ans=err
%% p384 1.(c) h=0.2
a=0 ; b=20 ;
h = 0.2;
n = (b-a)/h;
t = a:h:b;
y(1) = 20/(1+19*exp(-1/4));
f = @(t,y)(y/4*(1-y/20));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = 20/(1+19*exp(-t(i)/4));
end

err = abs(e_y-y);
ans=err
%% p384 1.(c) h=0.1
a=0 ; b=20 ;
h = 0.1;
n = (b-a)/h;
t = a:h:b;
y(1) = 20/(1+19*exp(-1/4));
f = @(t,y)(y/4*(1-y/20));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = 20/(1+19*exp(-t(i)/4));
end

err = abs(e_y-y);
ans=err
%% p384 1.(c) h=0.05
a=0 ; b=20 ;
h = 0.05;
n = (b-a)/h;
t = a:h:b;
y(1) = 20/(1+19*exp(-1/4));
f = @(t,y)(y/4*(1-y/20));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = 20/(1+19*exp(-t(i)/4));
end

err = abs(e_y-y);
ans=err
%% p384 1.(e) h=0.2
a=0 ; b=10 ;
h = 0.2;
n = (b-a)/h;
t = a:h:b;
y(1) = 3/2*exp(-1);
f = @(t,y)(t*exp(-t)-y);

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = (1+(t(i)^2)/2)*exp(-t(i));
end

err = abs(e_y-y);
ans=err
%% p384 1.(e) h=0.1
a=0 ; b=10 ;
h = 0.1;
n = (b-a)/h;
t = a:h:b;
y(1) = 3/2*exp(-1);
f = @(t,y)(t*exp(-t)-y);

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = (1+(t(i)^2)/2)*exp(-t(i));
end

err = abs(e_y-y);
ans=err
%% p384 1.(e) h=0.05
a=0 ; b=10 ;
h = 0.05;
n = (b-a)/h;
t = a:h:b;
y(1) = 3/2*exp(-1);
f = @(t,y)(t*exp(-t)-y);

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = (1+(t(i)^2)/2)*exp(-t(i));
end

err = abs(e_y-y);
ans=err
%% p384 1.(f) h=0.2
a=0 ; b=10 ;
h = 0.2;
n = (b-a)/h;
t = a:h:b;
y(1) = sqrt(3/2);
f = @(t,y)((t^3)/y);

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sqrt((t(i))^4+1);
end

err = abs(e_y-y);
ans=err
%% p384 1.(f) h=0.1
a=0 ; b=10 ;
h = 0.1;
n = (b-a)/h;
t = a:h:b;
y(1) = sqrt(3/2);
f = @(t,y)((t^3)/y);

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sqrt((t(i))^4+1);
end

err = abs(e_y-y);
ans=err
%% p384 1.(f) h=0.05
a=0 ; b=10 ;
h = 0.05;
n = (b-a)/h;
t = a:h:b;
y(1) = sqrt(3/2);
f = @(t,y)((t^3)/y);

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sqrt((t(i))^4+1);
end

err = abs(e_y-y);
ans=err
%% p385 2.(a) h=0.5
a=0 ; b=10 ;
h = 0.5;
n = (b-a)/h;
t = a:h:b;
y(pi/4) = sqrt(2);
f = @(t,y)(-y+2*cos(t));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sin(t(i))+cos(t(i));
end

err = abs(e_y-y);
ans=err
%% p385 2.(a) h=0.25
a=0 ; b=10 ;
h = 0.25;
n = (b-a)/h;
t = a:h:b;
y(pi/4) = sqrt(2);
f = @(t,y)(-y+2*cos(t));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sin(t(i))+cos(t(i));
end

err = abs(e_y-y);
ans=err
%% p385 2.(a) h=0.125
a=0 ; b=10 ;
h = 0.125;
n = (b-a)/h;
t = a:h:b;
y(pi/4) = sqrt(2);
f = @(t,y)(-y+2*cos(t));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sin(t(i))+cos(t(i));
end

err = abs(e_y-y);
ans=err
%% p385 2.(b) h=0.5
a=0 ; b=10 ;
h = 0.5;
n = (b-a)/h;
t = a:h:b;
y(pi/4) = sqrt(2);
f = @(t,y)(y+-2*sin(t));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sin(t(i))+cos(t(i));
end

err = abs(e_y-y);
ans=err
%% p385 2.(b) h=0.25
a=0 ; b=10 ;
h = 0.25;
n = (b-a)/h;
t = a:h:b;
y(pi/4) = sqrt(2);
f = @(t,y)(y+-2*sin(t));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sin(t(i))+cos(t(i));
end

err = abs(e_y-y);
ans=err
%% p385 2.(b) h=0.125
a=0 ; b=10 ;
h = 0.125;
n = (b-a)/h;
t = a:h:b;
y(pi/4) = sqrt(2);
f = @(t,y)(y+-2*sin(t));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sin(t(i))+cos(t(i));
end

err = abs(e_y-y);
ans=err
%% p385 2.(c) h=0.5
a=0 ; b=10 ;
h = 0.5;
n = (b-a)/h;
t = a:h:b;
y(pi/4) = sqrt(2);
f = @(t,y)(-5*y+6*cos(t)+4*sin(t));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sin(t(i))+cos(t(i));
end

err = abs(e_y-y);
ans=err
%% p385 2.(c) h=0.25
a=0 ; b=10 ;
h = 0.25;
n = (b-a)/h;
t = a:h:b;
y(pi/4) = sqrt(2);
f = @(t,y)(-5*y+6*cos(t)+4*sin(t));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sin(t(i))+cos(t(i));
end

err = abs(e_y-y);
ans=err
%% p385 2.(c) h=0.125
a=0 ; b=10 ;
h = 0.125;
n = (b-a)/h;
t = a:h:b;
y(pi/4) = sqrt(2);
f = @(t,y)(-5*y+6*cos(t)+4*sin(t));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sin(t(i))+cos(t(i));
end

err = abs(e_y-y);
ans=err
%% p385 2.(c) h=0.0625
a=0 ; b=10 ;
h = 0.0625;
n = (b-a)/h;
t = a:h:b;
y(pi/4) = sqrt(2);
f = @(t,y)(-5*y+6*cos(t)+4*sin(t));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sin(t(i))+cos(t(i));
end

err = abs(e_y-y);
ans=err
%% p385 2.(d) h=0.0625
a=0 ; b=10 ;
h = 0.0625;
n = (b-a)/h;
t = a:h:b;
y(pi/4) = sqrt(2);
f = @(t,y)(5*y-4*cos(t)-6*sin(t));

for i = 1:n
    y(1) = 1;
    y(i+1) = y(i) + h*f(t(i), y(i));
end

e_y = zeros(1,length(y));
for i = 1:n+1
    e_y(i) = sin(t(i))+cos(t(i));
end

err = abs(e_y-y);
ans=err
%% p.364 #2 (b)
 x_init=[1.7,0.4];err_tol=10^(-15);max_iterates=1000000000;
 solution = newton_sys(x_init,err_tol,max_iterates)
 
 x_init=[-1.4,0.6];err_tol=10^(-15);max_iterates=1000000000;
 solution = newton_sys(x_init,err_tol,max_iterates)
 
 x_init=[-0.8,-0.9];err_tol=10^(-15);max_iterates=1000000000;
 solution = newton_sys(x_init,err_tol,max_iterates)
 
  x_init=[1.3,-0.7];err_tol=10^(-15);max_iterates=1000000000;
 solution = newton_sys(x_init,err_tol,max_iterates)
%% p.364 #2 (d)

 x_init=[0.2,-0.3];err_tol=10^(-15);max_iterates=1000000000;
 solution = newton_sys2(x_init,err_tol,max_iterates)
 
 x_init=[0.3,-1.7];err_tol=10^(-15);max_iterates=1000000000;
 solution = newton_sys2(x_init,err_tol,max_iterates)
 
%% p.364 #3

x_init=[1.2,2.5];err_tol=10^(-15);max_iterates=100000000;
solution = newton_sys3(x_init,err_tol,max_iterates)

x_init=[-2,2.5];err_tol=10^(-15);max_iterates=100000000;
solution = newton_sys3(x_init,err_tol,max_iterates)

x_init=[-1.2,-2.5];err_tol=10^(-15);max_iterates=100000000;
solution = newton_sys3(x_init,err_tol,max_iterates)

x_init=[2,-2.5];err_tol=10^(-15);max_iterates=100000000;
solution = newton_sys3(x_init,err_tol,max_iterates)

%% #8

x_init=[0.6,-1.3];err_tol=10^(-15);max_iterates=100000000;
solution = newton_sys8(x_init,err_tol,max_iterates)

x_init=[0.7,-1.3];err_tol=10^(-15);max_iterates=100000000;
solution = newton_sys(x_init,err_tol,max_iterates)


%% p.364 2.(b)
function solution = newton_sys1(x_init,err_tol,max_iterates)
x0 = zeros(2,1);
for i=1:2
     x0(i) = x_init(i);
end
error = inf;
it_count = 0;


% begin the main loop
while error > err_tol && it_count < max_iterates
    it_count = it_count + 1;
    rhs = fsys(x0);
    A = deriv_fsys(x0);
    delta = A\rhs;
    x1 = x0 - delta;
    error = norm(delta,inf);
    [it_count x1' error]
    pause
    x0 = x1;
end

%return with the solution
solution = x1;
if it_count == max_iterates
    disp(' ')
    disp('*** Your answer may possibly not ... satisfy your error tolerance.')
end


%%%%%%%% Definition of function %%%%%%
function f_val = fsys(x)

f_val = [x(1)^2+4*x(2)^2-4,x(1)^2-0.4*x(1)-x(2)-1.96]';

function df_val = deriv_fsys(x)
df_val = [2*x(1),8*x(2); 2*x(1)-0.4,-1];

 

