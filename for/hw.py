# numbers = [12, 35, 42, 15, 237, 64, 70]

# for num in numbers:
#     if num == 237:
#         break
#     if num % 2 == 0:
#         print(num)



# roster = [3, 423, 654, 7, 2, 34, 54, 37, 87, 65]
# removed_num = []
# i = 0
# while i < len(roster):
#     if 35 < roster[i] < 65:
#         removed_num.append(roster.pop(i))
#     else:
#         i += 1
# print("итоговый список: ", roster)
# print("удаленные числа: ", removed_num)



# while True:
#     print("бесконечный калькулятор")
#     print("1. сложение")
#     print("2. вычитание")
#     print("3. умножение")
#     print("4. деление")
#     print("5. выход")
#
#     choice = input("выберите операцию (1/2/3/4/5): ")
#
#     if choice == '5':
#         print("выход из калькулятора.")
#         break
#
#     if choice not in ('1', '2', '3', '4'):
#         print("неверный ввод, пожалуйста, выберите операцию от 1 до 5.")
#         continue
#
#     num1 = float(input("введите первое число: "))
#     num2 = float(input("введите второе число: "))
#
#     if choice == '1':
#         print(f"результат: {num1} + {num2} = {num1 + num2}")
#     elif choice == '2':
#         print(f"результат: {num1} - {num2} = {num1 - num2}")
#     elif choice == '3':
#         print(f"результат: {num1} * {num2} = {num1 * num2}")
#     elif choice == '4':
#         if num2 != 0:
#             print(f"результат: {num1} / {num2} = {num1 / num2}")
#         else:
#             print("ошибка: деление на ноль!")