import pandas as pd
from sklearn.datasets import load_digits, make_regression, make_classification, make_blobs
import matplotlib.pyplot as plt
import sqlite3

# 1. Загрузка набора значений рукописных цифр (.load_digits())
digits = load_digits()
X_digits = pd.DataFrame(digits.data)
y_digits = pd.Series(digits.target)

# 2. Создание симулированных данных для задач регрессии, классификации и кластеризации
X_regression, y_regression, coef_regression = make_regression(n_samples=100, n_features=1, n_informative=1, noise=0.1, coef=True)
X_classification, y_classification = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=42)
X_clusters, y_clusters = make_blobs(n_samples=300, centers=3, cluster_std=0.5, random_state=42)

# 3. Создание фрейма данных из симулированных данных
df_simulated = pd.DataFrame({'Feature1': X_regression.flatten(), 'Target': y_regression})

# Загрузка данных из файла *.csv
df_csv = pd.read_csv('file.csv')
print("Первые 4 строки из файла *.csv:")
print(df_csv.head(4))

# Загрузка данных из файла *.xlsx
df_xlsx = pd.read_excel('file.xlsx')
print("\nПервые 4 строки из файла *.xlsx:")
print(df_xlsx.head(4))

# Загрузка данных из файла *.json
df_json = pd.read_json('file.json')
print("\nПервые 4 строки из файла *.json:")
print(df_json.head(4))

# Загрузка данных из БД SQLite с помощью языка SQL

conn = sqlite3.connect('database.db')
# cur = conn.cursor()
# cur.execute("create table file (Имя, Возраст, Зарплата)")

df_sql = pd.read_sql_query("SELECT * FROM file LIMIT 4", conn)
print("\nПервые 4 строки из БД SQLite:")
print(df_sql)
