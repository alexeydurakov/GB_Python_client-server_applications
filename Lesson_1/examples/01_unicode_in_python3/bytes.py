# Байты
# Имеют аналогичное строкам обозначение, но маркируются дополнительным указателем «b» в начале набора

bytes_s_1 = b'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'

bytes_s_2 = b"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430"
bytes_s_3 = b'''\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'''
print(type(bytes_s_1))
print(type(bytes_s_2))
print(type(bytes_s_3))
#<class 'bytes'>

bytes_s_4 = b'Program'

print(bytes_s_4)
# Out[22]: b'Program'

print(len(bytes_s_4))
# Out[23]: 7

# Если указать в байтовом типе данных символ, не относящийся к ASCII, появится сообщение об ошибке
bytes_s_5 = b'Программа'

print(bytes_s_5)
# Out[25]:
#     File "C:\Users\Администратор\Desktop\Курс Питон 2.1\01.
#     Концепции хранения информации\examples\01_unicode_in_python3\
#     bytes.py", line 15
#         bytes_s_5 = b'Программа'
#                ^
#     SyntaxError: bytes can only contain ASCII literal characters.