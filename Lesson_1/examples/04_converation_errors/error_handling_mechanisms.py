# Механизмы обработки ошибок
#
# Обработка ошибок метода encode

# При использовании метода encode при возникновении ошибок генерируется исключение UnicodeError.
# Чтобы решить подобную проблему и запретить генерацию исключения UnicodeError, можно использовать режим replace
# для замены недостающих символов знаком вопроса
handl_err = 'Testování'

handl_err_bytes = handl_err.encode('ascii', 'replace')

print(handl_err_bytes)
# Out[67]:  b'Testov?n?'

# Можно применить метод namereplace для замены символа именем.
handl_err_bytes_2 = handl_err.encode('ascii', 'namereplace')

print(handl_err_bytes_2)
# Out[69]:  b'Testov\\N{Latin Small Letter a with Acute}n\\N{ Latin Small Letter i with Acute }'

# Еще вариант — просто проигнорировать символы, у которых есть проблемы с кодированием.
# Для этого применяется режим ignore

handl_unicode = 'Testování'

handl_bytes = handl_unicode.encode('ascii', 'ignore')

print(handl_bytes)
# Out[72]:  b'Testovn'

# Обработка ошибок метода decode
# При некорректном декодировании генерируется исключение UnicodeDecodeError,
# которое может быть заблокировано механизмами ignore и replace.
handl_str = 'Testování'

handl_str_utf8 = handl_str.encode('utf-8')

print(handl_str_utf8)
# Out[75]:  b'Testov\xc3\xa1n\xc3\xad'

handl_str_utf8_str = handl_str_utf8.decode('ascii', 'ignore')

print(handl_str_utf8_str)
# Out[77]:  Testovn

handl_str = 'Testování'

handl_str_utf8 = handl_str.encode('utf-8')

handl_str_utf8_str = handl_str_utf8.decode('ascii', 'replace')

print(handl_str_utf8_str)
# Out[81]:  Testov''n'' 