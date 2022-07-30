x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

# i) 4 – 4/3 + 4/5 – 4/7+…………….. nth term .
sign = '-'
total = 0
temp = 1
for i in range(n):
    if sign == '+':
        total -= 4/temp
        sign = '-'
    else:
        total += 4/temp
        sign = '+'

    temp += 2
print(total) 
    
# ii) 1 + x/1! + x2 /2! + x3 /3! +…………….. + xn /n! 

def fact(m):
    if m == 1:
        return 1
    return m*fact(m-1)

total = 1
for i in range(1,n+1):
    total += x**i/fact(i)
    
print(total)