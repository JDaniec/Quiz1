
#input
n = int(input("escriba un numero de tres digitos: "))

#process 
x = n % 10 
Y = n // 10 
z = Y % 10
a = Y // 10

b = x * 100
c = z * 10 

D = b + c + a

print("El inverso del numero es: " + str(D))

