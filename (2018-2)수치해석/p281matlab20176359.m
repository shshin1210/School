%% p.281 #2 - when n=2 case
n = 2;
A = zeros(n,n);
b = ones(n,1);

for i = 1:2
    for j = 1:2
        if i<j
            A(i,j) = j;
        else
            A(i,j) = i;
        end
    end
end
[U,x] = GE(A,b);

answer = x

%% p.281 #2 - when n=5 case
n=5;
A = zeros(n,n);
b = ones(n,1);
for i = 1:n
    for j = 1:n
        if i<j
            A(i,j) = j;
        else
            A(i,j) = i;
        end
    end
end
[U,x] = GE(A,b);
answer = x
%% p.281 #2 - when n=10 case
n=10;
A = zeros(n,n);
b = ones(n,1);
for i = 1:n
    for j = 1:n
        if i<j
            A(i,j) = j;
        else
            A(i,j) = i;
        end
    end
end
[U,x] = GE(A,b);
answer = x
%% p.281 #2 - when n=20 case
n=20;
A = zeros(n,n);
b = ones(n,1);
for i = 1:n
    for j = 1:n
        if i<j
            A(i,j) = j;
        else
            A(i,j) = i;
        end
    end
end
[U,x] = GE(A,b);
answer = x
%% p.281 #3 - when n=2
n=2;
A = zeros(n,n);
b = ones(n,1);
for i = 1:n
    for j = 1:n
        if i>j
            A(i,j) = j;
        else
            A(i,j) = i;
        end
    end
end
[U,x] = GE(A,b);
answer = x
%% p.281 #3 - when n=5
n=5;
A = zeros(n,n);
b = ones(n,1);
for i = 1:n
    for j = 1:n
        if i>j
            A(i,j) = j;
        else
            A(i,j) = i;
        end
    end
end

[U,x] = GE(A,b);
answer = x
%% p.281 #3 - when n=10
n=10;
A = zeros(n,n);
b = ones(n,1);
for i = 1:n
    for j = 1:n
        if i>j
            A(i,j) = j;
        else
            A(i,j) = i;
        end
    end
end

[U,x] = GE(A,b);
answer = x
%% p.281 #3 - when n=20
n=20;
A = zeros(n,n);
b = ones(n,1);
for i = 1:n
    for j = 1:n
        if i>j
            A(i,j) = j;
        else
            A(i,j) = i;
        end
    end
end

[U,x] = GE(A,b);
answer = x
%% p.281 #5 a
A = [5,7,6,5;7,10,8,7;6,8,10,9;5,7,9,10];
b = [1;-1;-1;1];

[U,x] = GE(A,b);
answer = x 
%% p.281 #5 b
A = [1,1/2,1/3,1/4;1/2,1/3,1/4,1/5;1/3,1/4,1/5,1/6;1/4,1/5,1/6,1/7];
b = [1;-1;1;-1];


[U,x] = GE(A,b);
answer = x