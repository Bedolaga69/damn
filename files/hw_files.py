import random


number = random.randint(1, 10)
print(number)

# генерация списка из 1000 случайных чисел от 1 до 100
random_numbers = [random.randint(1, 100) for i in range(1000)]
print(random_numbers)

# запись чисел в файл
file_mode = 'w'
try:
    file = open("numbers.txt", file_mode)
    try:
        for number in random_numbers:
            file.write(str(number)+ "\n")
        print("числа записаны в файл")
    finally:
        file.close()
except Exception as ex:
    print(ex)

# запись чисел с условием

filtered_numbers = []
file = open("numbers.txt", 'r')
for i in file:
    number = int(i.strip())
    if number % 5!= 0:
        filtered_numbers.append(number)
file.close()