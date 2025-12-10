# file.close()
f = open("example.txt", "w")
f.write("Hello")
f.close()

# file.fileno()
f = open("example.txt", "r")
print(f.fileno())
f.close()

# file.flush()
f = open("example.txt", "w")
f.write("Some text")
f.flush()
f.close()

# file.isatty()
f = open("example.txt", "r")
print(f.isatty())
f.close()

# file.next() - работает только в Python 2.7, в Python 3 заменён на next(f)
f = open("example.txt", "r")
print(next(f))
f.close()

# file.read(n)
f = open("example.txt", "r")
print(f.read(5))
f.close()

# file.readline()
f = open("example.txt", "r")
print(f.readline())
f.close()

file = open("example.txt", "r")
try:
    line = file.readline()  # Читаем первую строку
    while line:            # Пока строка не пустая
        print(line.strip())
        line = file.readline()  # Читаем следующую
finally:
    file.close()

# file.readlines()
f = open("example.txt", "r")
lines = f.readlines()
print(lines)
f.close()

file = open("test.txt", "r")  # Открываем файл
try:
    lines = file.readlines()  # Читаем все строки
    print(lines)  # ['Первая строка\n', 'Вторая строка\n']
finally:
    file.close()

# file.seek(offset[, whence])
f = open("example.txt", "r")
f.seek(2)
print(f.read())
f.close()

f = open('data.txt', 'r')
try:
    f.seek(10)  # Перемещаемся на 10-й символ от начала
    print(f.read(5))  # Читаем 5 символов с этой позиции
finally:
    f.close()

# file.seekable()
f = open("example.txt", "r")
print(f.seekable())
f.close()

f = open("data.txt", "r")
try:
    print(f.seekable())  # True (обычные файлы поддерживают seek)
    f.seek(10)  # Можно перемещаться
finally:
    f.close()

# file.tell()
f = open("example.txt", "r")
f.read(3)
print(f.tell())
f.close()

f = open('data.txt', 'r')
try:
    start_pos = f.tell()  # 0 (начало файла)
    f.read(10)  # Читаем 10 символов
    print(f.tell())  # Текущая позиция (например, 10)
finally:
    f.close()

# file.truncate(n)
f = open("example.txt", "w+")
f.write("1234567890")
f.truncate()
f.seek(50)
print(f.read())
f.close()

f = open('data.txt', 'r+')  # Открываем для чтения и записи
try:
    f.truncate(100)  # Оставляем первые 100 байт
finally:
    f.close()

# file.write(str)
f = open("example.txt", "w")
f.write("New line")
f.close()

f = open('output.txt', 'w')
try:
    bytes_written = f.write('Hello, World!')
    print(f'Записано {bytes_written} байт')
finally:
    f.close()

# file.writelines(sequence)
f = open("example.txt", "w")
f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
f.close()

lines = ['First line\n', 'Second line\n']
f = open('text.txt', 'w')
try:
    f.writelines(lines)  # Запишет как есть, без добавления \n
finally:
    f.close()
