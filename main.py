while(True):
    a = input("Напишите пример, разделенный пробелом: \n").split()
    x = int(a[0])
    z = a[1]
    y = int(a[2])
    if z == "+":
        print(x+y)
    elif z == "-":
        print(x-y)
    elif z == "*":
        print(x*y)
    elif z == "/":
        print("Результат: ",x/y,"\n")
