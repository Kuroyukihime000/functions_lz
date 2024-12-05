def pl(a):
    pl=a*a*3.14
    return pl
 
def dl(a):        #Функция поиска длины
    dl=2*a*3.14
    return dl


print("Введите радиус: ") #Ввод
radius=input()
radius=int(radius)

pl=pl(radius)             #Использовние функций
dl=dl(radius)
print("Длина этой окружности:", dl)    #Вывод
print("Площадь этой окружности:", pl)
