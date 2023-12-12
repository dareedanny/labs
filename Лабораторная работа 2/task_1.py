salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
months = 0
while months < 10:
    money_capital += spend - salary
    spend = spend * (1 + increase)
    months += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital,2))
