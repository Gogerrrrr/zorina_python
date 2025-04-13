#Дана строка '2020год -16 -10 -6 -4 20 32 36 32 32 15 1 -15', отражающая
#средние температуры по месяцам в году. Преобразовать информацию из строки в
#словарь, с использованием функции найти среднюю и минимальные температуры,
#результаты вывести на экран.
pogoda = {}
infa = "2020год -16 -10 -6 -4 20 32 36 32 32 15 1 -15"
infa = infa.split()
print(infa)
pogoda["январь"] = int(infa[1])
pogoda["февраль"] = int(infa[2])
pogoda["март"] = int(infa[3])
pogoda["апрель"] = int(infa[4])
pogoda["май"] = int(infa[5])
pogoda["июнь"] = int(infa[6])
pogoda["июль"] = int(infa[7])
pogoda["август"] = int(infa[8])
pogoda["сентябрь"] = int(infa[9])
pogoda["октябрь"] = int(infa[10])
pogoda["ноябрь"] = int(infa[11])
pogoda["декабрь"] = int(infa[12])
print(pogoda)
temperatures = list(pogoda.values())
min_temperature = min(temperatures)
sred_temperature = sum(temperatures) / len(temperatures)
results = {"температуры по месяцам:": pogoda, "минимальная темпераатура:": min_temperature, "средняя температура:": sred_temperature}
print(results)
