users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dict = {"Общее количество": 0, "Уникальные посещения":0}
dict.update({"Общее количество": len(users)})
dict.update({"Уникальные посещения": len(set(users))})
print(dict)