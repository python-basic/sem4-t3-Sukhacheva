"""
Разработка сценария с реализацией операции поиска подстроки в тексте. 
"""

text = """Разработка сценария с реализацией операции поиска подстроки в тексте."""
print(text)

s = input()

print("данной строки нет в тексте") if text.find(s) == -1 else print("да, символ: {}".format(text.find(s)))
