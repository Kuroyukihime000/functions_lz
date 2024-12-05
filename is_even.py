print("Введите число для проверки на четность: ")
chisl=input()
chisl=int(chisl)
def even(a):  #Функция проверки на четность
    if a%2==0 : return 1
    elif a%2==1 : return 2

check=even(chisl) #Использование функции
if check==1 : print("Число четно")
elif check==2 : print("Число нечетно")