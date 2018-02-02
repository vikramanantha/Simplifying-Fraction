#SIMPLIFY FRACTIONS.py by Vikram Anantha

factors = []
print("Hi! This is a Simplify fractions Calcultor.")
num = input("Numerator: ")
den = input("Denominator: ")
num = int(num)
den = int(den)
num1 = num+1
den1=den+1
for i in range(1, num1):
	if num % i == 0 and den % i == 0:
		factors.append(i)

cn = max(factors)
upDen = den/cn
upDen = int(upDen)
upNum = num/cn
upNum = int(upNum)
print("Your number is", upNum, "/", upDen)
input()
