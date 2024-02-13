import math

archivo = open("cos100.csv", "w", encoding="utf-8")
for i in range(361):
    a=i*math.pi/180
    b=math.cos(a)
    c=((b*50)+50)
    d=repr(c)
    e=repr(i)
    print(c)
    archivo.write(e + ',' + d + '\n')
archivo.close

