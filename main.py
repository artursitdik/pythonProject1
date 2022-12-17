# print("результат=" , 5//5)
# print("результат=" , max(5, 6, 7, 9))
# print("Результат=", 5, 9, sep=" ", end="\n")
# print("Second \"line")
# input("введите число")

# number = 5
# print("",number)
# del number
# digit=4.5555
# print(digit,number)
# word="Результат"
# boolean=True
# print(word + str(number+int(digit)))

# num1 = int(input("введите первое число ="))
# num2 = int(input("введите второе число ="))
# num1 += 1
# print("result:", num1+num2)
# print("result:", num1-num2)
# print("result:", num1/num2)
# print("result:", num1*num2)
# print("result:", num1**num2)
# print("result:", num1//num2)
# word = "hi"
# print(word * 2)
# word = 5
# print(word)
# user_data = int(input("введите число: "))
# isHappy = False
# if isHappy and user_data == 6: # or
# # if not isHappy:
#     print("user is happy")
# elif user_data == 5:
#     print("number is 5")
# else:
#     print("user is unhappy")

# if user_data != 5:
#     print("мы на месте")
#     if user_data > 6:
#         print("number is bigger than 6")
# data = input()
# number = 5 if data == "five" else 0
# if data == "five":
#     nuber = 5
# else:
#     nuber = 0

# print(nuber)
# for i in range(1,6,2):
#     print(i)
# count = 0
# word = "hello world"
# for i in word:
#     if i == "l":
#         count += 1
# print(count)
# i = 5
# while i < 15:
#     print(i)
#     i += 2
# isHasCar = True
# while isHasCar:
#     if input("enter data: ") == "stop":
#         isHasCar = False
# for i in range(1, 11):
#     if i > 5:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)
# found = None
# for i in "hello":
#     if i == "l":
#         found = True
#         break
# else:
#     found = False
# print(found)
# a = 2
# b = 5
# tmp = a
# a = b
# b = tmp
#
# a = 2
# b = 5
# tmp1 = b
# tmp2 = a
# a = tmp1
# b = tmp2
#
# a, b = b, a
#
# a = -12
# b = 5
#
# print(a//b)
###7 Списки List
# nums = [5, 6, 7, 8, 9, "hello,", True, [9, 8]]
# nums[0]=50
# nums[6]=False
# nums[2]=1.55
# print(nums)
# print(nums[5])
# print(nums[-1][1])
# nubers = [5, 2, 7, '50', False]
# nubers.append(100) # добавить в конец
# nubers.insert(1, True) # вставить в нужное место
# nubers.extend([5, 6, 8])
# nubers.sort()
# nubers.reverse()
# nubers.pop(-1)
# nubers.remove(5)
# # nubers.clear()
# nums = [5, 2, 7, '50', False]
# for i in nums:
#     i *= 2
#     print(i)
# mass = []
# l = int(input('enter length: '))
# i = 0
# # for i in range(0, l):
# #     string = 'enter element' + str(i) + ':'
# #     mass.append(input(string))
# while i < l:
#     string = 'enter element' + str(i) + ':'
#     mass.append(input(string))
#     i += 1
# print(mass)
# word = 'строка, абзац, пораграф'
# print(word[1])
# print(len(word))
# print(word.count('к'))
# print(word.upper())
# print(word.isupper())
# print(word.islower())
# print(word.lower())
# print(word.capitalize())
# print(word.find('с'))
# print(word.split(', '))
# new_str = word.split(', ')
# print(new_str[1])
# print(word)
# word = word.split(', ')
# for i in range(len(word)):
#     word[i] = word[i].capitalize()
# print(word)
# result = ', '.join(word)
# print(result)
# word = 'Football'
# print(word[0:4])
# print(word[4:])
# print(word[0:8:2])
# lis = [6, 4, 'Stoka', True, 6.66]
# print(lis[2:5:2])
# print(lis[::-1])
# korteg_tuple = (4, 5, 6, 7, True, 6.66, "slova")
# print(korteg_tuple[1])
# print(korteg_tuple[0:2])
# print(korteg_tuple.count(True))
# print(len(korteg_tuple))
# data = 5, 6, 7
# print(data)
# data = 5,
# print(data)
# nums = [1, 2, 3]
# for elemets in korteg_tuple:
#     print(elemets)
# print(nums)
# new_data = tuple(nums)
# print(new_data)
# word = tuple("Hello world")
# print(word)
# country = {4: 3}
# country = {(5, 6): 3}
# print(country[(5, 6)])
country = {"code": "RU", "name": "Russia", "Population": 200 }
# country = dict(code='RU', name='Russia', Population=200)
# print(country['name'])
# print(country)
# print(country.items())
# for key, value in country.items():
#     print(key, '-', value)
# print(country.get('name'))
# country.clear()
# print(country)
# country.pop('name')
# country.popitem()
# print(country.keys())
# print(country.items())
# print(country.values())
# country['code'] = 'None'
# print(country.items())
persona = {
#     'user_1': {
#         'first_name': 'John',
#         'last_name': 'Marlin',
#         'male': 'None',
#         'address': ('Moscow', 'Brothers str'),
#         'grades': {'math': 3, 'fhysics': 3},
#     }
# }
# print(persona['user_1']['address'][0])












