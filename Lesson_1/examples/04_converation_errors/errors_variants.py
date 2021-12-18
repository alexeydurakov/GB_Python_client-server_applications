# Ошибки преобразования
# Варианты ошибок

#1 Отсутствие в кодировке механизма преобразования данных из одного формата в другой.

# Например, в кодировке ASCII не предусмотрено преобразование кириллицы в байты

err_str_1 = 'Программа'

#print(err_str_1.encode('ascii'))
# Out[56]: UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-8: ordinal not in range(128)

# Строку в байтах преобразовать в строковый формат с помощью кодировки ASCII тоже будет невозможно —
# программа выдаст ошибку
err_str_2 = 'Программа'

err_str_2_bytes = err_str_2.encode('utf-8')

err_str_2_str = err_str_2_bytes.decode('ascii')

# print(err_str_2_str)
# Out[60]: UnicodeDecodeError: 'ascii' codec can't decode byte 0xd0 in position 0: ordinal not in range(128)

#2 Использование при конвертации различных кодировок.
# Речь о том случае, когда кодирование осуществляется в привязке к одной кодировке, а декодирование — к другой

err_str_3 = 'Testování'

utf_16_bytes = err_str_3.encode('utf-16')

utf_8_str = utf_16_bytes.decode('utf-8')

print(utf_8_str)
# Out[64]: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte