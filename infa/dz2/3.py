#iris_data.csv 2 круговые диаграммы: доля разных видов (Species) ирисов в датасете,
#доли ирисов, у которых длина лепестка (PetalLengthCm) больше 1.2см, меньше 1.2см и меньше 1.5см, больше 1.5см.
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('iris_data.csv')
plt.figure(0)
s = df['Species'].value_counts ()
plt.pie(s, labels = ['setosa', 'versicolor', 'virginica'], autopct='%.2f')
plt.title('доля разных видов (Species) ирисов в датасете')
plt.figure(1)
s1 = len([i for i in df['PetalLengthCm'] if i>1.2])
s2 = len([i for i in df['PetalLengthCm'] if i<=1.2])
s3 = len([i for i in df['PetalLengthCm'] if i<1.5])
s4 = len([i for i in df['PetalLengthCm'] if i>=1.5])
x = [s1, s2, s3, s4]
plt.pie(x, labels = ['Больше 1.2см', 'Меньше 1.2см', 'Меньше 1.5см', 'Больше 1.5см'], autopct='%.2f')
plt.show()
print(x)
