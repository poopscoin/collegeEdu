taskNum = 0
taskGroup = 1
def task_sep(addGroupIndex = 0, resetTaskNum = 1):
    global taskNum, taskGroup
    taskGroup += addGroupIndex # коли треба, пишемо 1 і добовляємо к лічильнику групп завдань
    taskNum = taskNum * resetTaskNum + 1 # коли треба, пишемо 0 і taskNum множиться на нього, обнуляючись, потім на цей 0 добовляєтся 1
    print(f"\n=======================| Завдання {taskGroup}.{taskNum} |=======================\n")
task_sep()

# Робота з рядками:
#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()

num_str = 125
print(str(num_str) + " текст" + '\n' + str(type(str(num_str))))

task_sep()
#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити  
# усі букви 'y' на '0' та 'i' на '1'.

message = 'Hi, my name is Python!'
print(message)
print(message.replace('y','0').replace('i','1'))

task_sep()
#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за 
# допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join

splitTest = 'This is a split test'

print(splitTest, end="\n\n")

splitList = splitTest.split(" ")

for i, word in enumerate(splitList, start=1):
    print(f"{i} - '{word}'", end=", ")
print('\b\b \n') # прибираю ", " по завершенню циклу for

stringTestBack = ' '.join(splitList) # змінна - string_join

print(f"{stringTestBack} > {type(stringTestBack)}")

task_sep()
#  4. Визначити довжину рядку string_join за допомогою функції len()

print(len(stringTestBack)) # змінна - string_join

task_sep(1, 0)
# Робота зі списками:
#  1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5

listAppend = [1, 2, 3]
print(listAppend)
listAppend.append(4)
print(listAppend)
listAppend.append(5)
print(listAppend)

task_sep()
#  2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()

listExtend = [4, 5, 6]

print(listExtend)

listExtend.extend([7, 8, 9])

print(listExtend)

task_sep()
#  3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()

getElemListExtend = listExtend.index(6)

print(getElemListExtend, end="\n\n")
print(listExtend[getElemListExtend])

task_sep()
#  4. Визначити довжину списку list_append за допомогою функції len()

print(len(listAppend))

task_sep(1, 0)
# Робота зі словниками:
#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where

dictTest = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print("Car - " + dictTest['car'])
print("Where - " + dictTest.get('where'))


task_sep()
#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення

print("Ключі -", ', '.join(map(str, dictTest.keys())))
print("Значення -", ', '.join(map(str, dictTest.values())))

task_sep()
#  3. За допомогою функції items() вивести на екран пари ключ - значення

for key, value in dictTest.items():
    print(f'{key.capitalize()} - "{value}"')

print() # Кінцевий відступ