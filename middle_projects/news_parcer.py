import requests
from bs4 import BeautifulSoup

url = "https://24.kg"
response = requests.get(url)

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все блоки с новостями в ленте
# На основе вашего лога, новости лежат в <div class="one"> внутри списка новостей
news_items = soup.find_all('div', class_='one')

print(f"{'Время':<7} | {'Заголовок'}")
print("-" * 50)

for item in news_items:
    # Ищем время (оно в <div class="time">)
    time_tag = item.find('div', class_='time')
    # Ищем заголовок (он внутри тега <a> в <div class="title">)
    title_tag = item.find('div', class_='title')

    if time_tag and title_tag:
        time = time_tag.get_text(strip=True)
        title = title_tag.get_text(strip=True)
        print(f"{time:<7} | {title}")