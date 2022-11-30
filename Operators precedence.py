# Programmer Sadiq
# By@Sadiqul Islam
# Operators precedence


a = 20
b = 10
c = 15
d = 5
e = 0
e = (a+b)*c/d
print("Value of (a+b)*c/d is:",e)

e = ((a+b)*c)/d
print("Value of ((a+b)*c)/d is:",e)

e = (a+b)*(c/d)
print("Value of (a+b)*(c/d) is:",e)


e = a+(b*c)/d
print("Value of a+(b*c)/d is:",e)


result = False == False or True
print(result)

result1 = False == (False or True)
print(result1)
