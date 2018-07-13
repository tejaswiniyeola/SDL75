#SET AND SET OPERATIONS
s = set([1,2,3,4]);
print (2 in s);
print (5 in s);
print (7 in s);
print (10 in s);

print ('numbers in set' );
print(s);
print("\n ");

s1 = set([45,6,34,66,0]);

print (22 in s1);
print (21 in s1);
print (23 in s1);
print (224 in s1);

print('numbers in set1' );
print (s1);
print("\n ");

print("union ,intersection ,minus operation is::");
print(s & s1);
print(s | s1);
print(s - s1);
print("\n ")

basket = {'ab','cd','ef','gh','ij'}
print("elements in basket are as below:: ");
print(basket);
print("\n ")

a = set('vclgbfwkjvv')
b = set('yflgyfcdshkvj')

print("special elements in a are::");
print(a);
print("\n ");

print("special elements in b are::");
print(b);
print("\n ");

print('minus operation of a and b are');
print (a-b);
print("\n ");
