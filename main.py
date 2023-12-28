import requests
from bs4 import BeautifulSoup as bs
import sqlite3



connection = sqlite3.connect('weather_data.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS weather(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  date_time DATE DATETIME DEFAULT CURRENT_TIMESTAMP,
                  temperature REAL
                  );''')
url = 'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2'
r = requests.get(url)


html = bs(r.text, 'html.parser')

temperature_element = html.find_all('td', class_='p5 cur')
day = html.find_all('p', class_='day-link')
days = []
for i in temperature_element:
    print(i.text)

for a in day:
    print(a.text)



cursor.execute(f"""INSERT INTO weather (date_time,temperature) VALUES ('2023-12-28, 14:00','5 C');""")
cursor.execute("""SELECT * FROM weather;""")
data = cursor.fetchall()
connection.commit()
connection.close()
print(data)
