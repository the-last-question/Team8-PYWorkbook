def MedianFunction(a, b, c) : 
    if a > b:
        if a < c:
           return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c
    
a = float(input("Primeiro numero: "))
b = float(input("Segundo numero: "))
c = float(input("Terceiro numero: "))

median = MedianFunction(a, b, c)
print("A mediana:", median)