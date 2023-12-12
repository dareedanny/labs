list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
total_players = len(list_players)
half_players = total_players // 2

team1 = list_players[:half_players]
team2 = list_players[half_players:]

print(team1)
print(team2)