def ListOfDictsToDict(initial_list, key_value):
    primary_dict = {}
    for secondary_dict in initial_list:
        key = secondary_dict.get(key_value, "")
        if key not in primary_dict.keys():
            primary_dict[key] = 1
        else:
            primary_dict[key] += 1
    # print(first_names)
    primary_dict = dict(sorted(primary_dict.items()))
    return primary_dict

def KeyWithMostValue(checked_dictionary):
    counter = 0
    key_with_most_value = ""
    for k,v in checked_dictionary.items():
        if v > counter:
            counter = v
            key_with_most_value = k
    return key_with_most_value

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

first_names = ListOfDictsToDict(students,"first_name")
for k, v in first_names.items():
    print(f"{k}: {v}")

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
first_names = ListOfDictsToDict(students,"first_name")
most_popular_name = KeyWithMostValue(first_names)
print(f"Most popular name is {most_popular_name}")

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

for school_class in range(len(school_students)):
    first_names = ListOfDictsToDict(school_students[school_class],"first_name")
    most_popular_name = KeyWithMostValue(first_names)
    print(f"Most popular name in class {school_class + 1} is {most_popular_name}")

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for school_class in school:
    ammount_of_girls = 0
    ammount_of_boys = 0
    first_names = ListOfDictsToDict(school_class["students"],"first_name")
    for name,ammount in first_names.items():
        if is_male[name]:
            ammount_of_boys += ammount
        else:
            ammount_of_girls += ammount
    print(f"There are {ammount_of_girls} girls and {ammount_of_boys} boys in class {school_class['class']}")


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

most_boys = 0
class_with_most_boys = ""
most_girls = 0
class_with_most_girls = ""

for school_class in school:
    ammount_of_girls = 0
    ammount_of_boys = 0
    first_names = ListOfDictsToDict(school_class["students"],"first_name")
    for name,ammount in first_names.items():
        if is_male[name]:
            ammount_of_boys += ammount
        else:
            ammount_of_girls += ammount
    if ammount_of_girls > most_girls:
        most_girls = ammount_of_girls
        class_with_most_girls = school_class['class']
    if ammount_of_boys > most_boys:
        most_boys = ammount_of_boys
        class_with_most_boys = school_class['class']

print(f"Class with most boys is {class_with_most_boys}")
print(f"Class with most girls is {class_with_most_girls}")
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a