

#Строка
progr_1 = 'Программирование'

print(progr_1)
#Программирование

print(type(progr_1))
#<class 'str'>

progr_2 = 'Programování'

print(progr_2)
#Programování

#Символ Unicode можно записать не в традиционном (буквенном или цифровом представлении), а с помощью имени символа
unic_s_1= "\N{LATIN SMALL LETTER C WITH DOT ABOVE}"

print(unic_s_1)
# ċ

#Или с помощью особого формата
unic_s_2 = "\u010B"

print(unic_s_2)
# ċ

#Так же и строка может быть представлена как последовательность юникод-кодов
progr_3 = 'Программа'

progr_4 = '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'

print(progr_4)
#Программа

print(progr_3 == progr_4)
#True

print(len(progr_4))
#9

#функции ord
print(ord('ã'))
#227

#команду chr
print(chr(227))
# ã

