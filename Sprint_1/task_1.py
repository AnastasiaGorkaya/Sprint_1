times = '1h 45m,360s,25m,30m 120s,2h 60s'
times = times.replace(' ',',')  #Заменяем пробелы на запятые
new_times = times.split(',') #Сплитуем по запятой получаем ['1h', '45m', '360s', '25m', '30m', '120s', '2h', '60s']
minutes = 0 #Задаю переменную куда буду складывать вычисленные минуты 
for i in new_times:
    if i[-1] == 'h':
        x = int(i[:-1]) * 60
        minutes = minutes + x
    elif i[-1] == 's':
         x = (int(i[:-1])//60)
         minutes = minutes + x
    else: minutes = minutes + int(i[:-1])
    
print('Общее количество минут=', minutes)
