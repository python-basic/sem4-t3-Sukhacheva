"""
Реализовать программу-игру «Угадай число», в которой для вывода на экран информации использовать метод format. 
"""
import random


b = random.randint(1,27)

f = False
while f != True:
  s = input("Введите число: ")
  if int(s) == b:
     print("число {} - угадано верно! Игра закончена!".format(s))
     f = True
  else: 
    print("Число {} угадано неверно!".format(s))
