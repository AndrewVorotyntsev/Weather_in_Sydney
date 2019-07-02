# Загружаем библиотеки
import pandas as pd
import matplotlib.pyplot as plt

# Читаем .csv файл с данными
df = pd.read_csv('weatherAUS.csv')

# Напечатать первые пять строк из файла
print( df.head() )

# Преобразуем колонку Date в формат даты
df['Date'] = pd.to_datetime( df['Date'] )

# Вывести все уникальные местоположения (Location) и их количество
print( df['Location'].unique())
print( df['Location'].nunique())

# Выбираем Location c индексом 10
# это 'Sydney'
location_name = df['Location'].unique()[10]

# Создаем новый датафрейм только с данными для этого Location
df_new = df[df['Location'] == location_name]

print( df_new.loc[:,['Date','Rainfall']] )
print(f'Location: {location_name}')

# Датафрейм содержащий только данные об уровне осадков.
d_rainfall = df_new.loc[:,['Date','Rainfall']]
d_rainfall['Year'] = d_rainfall['Date'].dt.year

d_temp9am = df_new.loc[:, 'Temp9am']

fig, axes = plt.subplots(1, 2, figsize=(10,4))

# Построить график
d_rainfall.plot(x='Date', y='Rainfall', legend=False, ax=axes[0], title=f'Количество осадков в {location_name}')
axes[0].set_xlabel("Дата")
axes[0].set_ylabel("мм")

# density=True чтобы площадь под гистограммой была равна 1
# в данном случае не обязательно
d_temp9am.hist(density=True, bins=120, ax=axes[1])
axes[1].set_title(f'Гистограмма температуры в {location_name}')
axes[1].set_xlabel("°С")

# Сохранить в файл
plt.savefig('output.png')

# Отобразить графики
plt.show()