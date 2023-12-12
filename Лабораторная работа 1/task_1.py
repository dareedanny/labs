numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_ = 0
count = 0

for num in numbers:
    if num is not None:
        sum_ += num
        count += 1

average = sum_ / count
average = round(round(average, 2) + 0.82, 2)
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average

print("Измененный список:", numbers)
