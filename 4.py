n = int(input("Введите, пожалуйста, целое положительное число"))
m=n%10
n=n//10
while n>0:
    if n%10>m:
        m=n%10
    n=n//10
print(m)