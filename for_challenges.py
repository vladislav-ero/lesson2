# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name)

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(f"{name}: {len(name)} chars")
# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика
is_male = {
'Оля': False,  # если True, то пол мужской
'Петя': True,
'Вася': True,
'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    sex = None
    if is_male[name]:
        sex = "male"
    else:
        sex = "female"
    print(f"{name} is {sex}.")
        
# ???
# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.
groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print(f"There are {len(groups)} groups total:")
for i in range(len(groups)):
    print(f"group {i+1} has {len(groups[i])} students")

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша
groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
for i in range(len(groups)):
    string_to_print = f"Group {i + 1}: "
    ammount_of_students = len(groups[i])
    for k in range(ammount_of_students):
        if k < ammount_of_students - 1:
            string_to_print += f"{groups[i][k]}, "
        else:
            string_to_print += f"{groups[i][k]}"
    print(string_to_print)

# ???