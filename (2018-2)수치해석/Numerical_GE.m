%%
A1 = [2 1 1 0; 4 3 3 1; 8 7 9 -2; 6 7 1 0]
A2 = [2 1 1 0
    4 3 3 1
    8 7 9 -2
    6 7 1 0]
%%
b1 = [2;1;-1;0]
b2 = [2 1 -1 0]
b3 = [2 1 -1 0]'

A1\b1 % Which implies to solve Ax = b

B = zeros(4,4);
B = ones(4,4);
B = ones(4,2);
B = eye(4);
%% Matrix Operation

A = rand(4,4);
B = rand(4,4);
A*B
A+B
A-B
A.*B
A.^3
sin(A)
eig(A)
inv(A)
rank(A)
det(A)
norm(A)
lu(A)