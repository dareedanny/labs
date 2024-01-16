# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, a = ","):
    first = participants_first_group.split(a)
    second = participants_second_group.split(a)
    common_participants = list(set(first) & set(second))
    return sorted(common_participants)

group1 = "Alice,Bob,Charlie,David"
group2 = "Bob,David,Eve"
common_participants = find_common_participants(group1, group2)
print(common_participants)  # Вывод: ['Bob', 'David']

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
