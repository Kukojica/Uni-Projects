import pandas as pd
pd.set_option('display.max_columns', None)
#Группировка и агрегирование
email = pd.read_csv('email.csv')
username = pd.read_csv('username.csv')
print(email.head())
print(username.head())
email_gr = email.groupby('Passport copy', as_index=False).agg({'Trip count': 'mean'})
username_gr = username.groupby('First name', as_index=False).agg({'Trip count': 'mean'})
print(email_gr.head())
print(username_gr.head())

#Обработка пропущенных значений
email = email.fillna(0)
username = username.interpolate(method='pad')
print(username.isna().sum())
print(email.isna().sum())

#Слияние данных
email_flt = email[['Identifier', 'Login email']]
df = username.merge(email_flt, on='Identifier', how='left')
print(df.head())

#Сводная таблица
sales = pd.read_csv('sales.csv')
print(sales.head())
sales_t = pd.pivot_table(sales, index=['Rep', 'Manager', 'Product'], values=['Price', 'Quantity'], aggfunc='sum')
print(sales_t)

#Сводная таблица
data = pd.read_csv('data.csv')
data_table = pd.pivot_table(data, index='Date', columns='Product', values='Sales', aggfunc='sum')
print(data_table.fillna(0))

#Простой линейный график
import matplotlib.pyplot as plt
x=username['Username']
y=username['Trip count']
plt.plot(x,y)
plt.show()

# График распределения набора данных
import numpy as np
data = np.random.normal(50, 10, 100)
plt.hist(data, bins=20)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data')
plt.show()

#Сравнение наоборов данных на графике
data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 15, 100)
fig, ax = plt.subplots()
ax.plot(data1, label='Dataset 1')
ax.plot(data2, label='Dataset 2')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
ax.set_title('Comparison of Two Datasets')
ax.legend()
plt.show()

#Построение мат. функции
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
y_cos = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, y_cos)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Plot of the Sine Function')
plt.show()

#Моделирование анимации графиков
from matplotlib.animation import FuncAnimation
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
l, = ax.plot(x, y)
k, = ax.plot(x, y_cos)
def animate(i):
    l.set_ydata(np.sin(x + i / 10))
    k.set_ydata(np.cos(x + i / 15))
    return l, k,
ani = FuncAnimation(fig, animate, frames=100, blit=True)
plt.show()

#Отображение определенных строк в порядке увеличения
sales_f = sales.query('Status == "presented"').sort_values(by='Price')
print(sales_f)
#
climate = pd.read_csv('climate.csv')
print(climate)
climate_f = climate[(climate['cri_score'] > 100) & (climate['fatalities_total'] < 10)][['country', 'rw_country_code']]
print(climate_f.head())
#
cars = pd.read_csv('cars.csv')
print(cars.head())
cars_f = cars[(cars['MPG'] >= 25) & (cars['Displacement'] <= 97.0) & (cars['Cylinders'] <= 40)]['Car']
cars_f = cars_f[:50].sort_values(ascending=True)
print(cars_f)
#Вычисление среднего, стандартного отклонения и макс. значения массива
d = np.genfromtxt('data.csv', delimiter=',', usecols=(1, 2), filling_values=0)
print(d)
mean = np.mean(d)
std = np.std(d)
max_value = np.max(d)
print("Mean:", mean)
print("Standard deviation:", std)
print("Max value:", max_value)

#Создание матриц и операции с ними
matrix1 = np.array([[1,2,3],[4,5,6]])
matrix2 = np.array([[7,8,9],[10,11,12]])

add_matrix = matrix1 + matrix2
print("Addition of matrices:", add_matrix)

sub_matrix = matrix1 - matrix2
print("Subtraction of matrices:", sub_matrix)

mul_matrix = matrix1 * matrix2
print("Multiplication of matrices:", mul_matrix)

tr = matrix1.transpose()
print(tr)