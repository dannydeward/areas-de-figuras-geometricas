import math

a= float(input('ingrese el valor de los lados.'))
b= float(input('ingrese el valor de los lados.'))
c = float(input('ingrese el valor de los lados.'))

def area(a,b,c):    
    sp= (a+b+c)/2
    area= math.sqrt((sp-a)* (sp-b)*(sp-c))
    print('el area del triangulo es.', area)



area(a,b,c)
