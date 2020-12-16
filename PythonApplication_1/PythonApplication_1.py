print("Задание №1")
print("Hello Python from Visual Studio!")
print("Задание №2")
chislo1 = input("Введите первое число ")
chislo2 = input("Введите второе число ")
operation = input("Введите одно действие +; -; / или * ")
if operation == "+":
		result = (int(chislo1) + int(chislo2))
		print(result)
elif operation == "-":
		result = (int(chislo1) - int(chislo2))
		print(result)
elif operation == "*":
		result = (int(chislo1) * int(chislo2))
		print(result)
elif operation == "/":
		result = (int(chislo1) / int(chislo2))
		print(result)
else:
	print("Введены неправильные данные")
print("Задание №3")
year = input("Введите год ")
if (int(year)%100)==0:
    if (int(year)%400)==0:
        print("Год високосный ")
    else:
        print("Год не високосный ")
else:
    if (int(year)%4)==0:
        print("Год високосный ")
    else:
        print("Год не високосный ")
print("Задание №4")
a1 = input("Введите размер вклада ")
years = input("Введите на сколько лет вы делаете вклад ")
a2=a1
i = 0
while i < int(years):
    a2=float(a2)*1.1
    i+=1
print("через "+years+" лет(года) с вкладом "+a1+" вы получите "+str(a2))
print("Задание 5")
from tkinter import *
 
root = Tk()
root.title("Программа на Python")
root.geometry("300x250")


label1 = Label(text="Hello world")
label1.pack()

root.mainloop()