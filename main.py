from flask import Flask, render_template, send_from_directory
import os
import requests
import sys

app = Flask(__name__)
STATIC_DIR = os.path.abspath(os.path.dirname(__file__)) + "/static"


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


menu = ["Наши товары", "Где мы находимся?", "Контакты"]


# Функция для получения изображения карты
def getImage():
    map_request = "http://static-maps.yandex.ru/1.x/?ll=37.6354,55.807602&spn=0.002,0.002&l=map"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    # Записываем полученное изображение в файл.
    map_file = "map.png"
    with open(os.path.join(STATIC_DIR, map_file), "wb") as file:
        file.write(response.content)
    return map_file


images = [  # картинки для Наших товаров
    {"src": "sneakers.png", "alt": "Картинка 1", "text": "Nike"},
    {"src": "sneakers2.png", "alt": "Картинка 2", "text": "Adidas"},
    {"src": "sneakers3.png", "alt": "Картинка 3", "text": "Convers"},
    {"src": "sneakers4.png", "alt": "Картинка 3", "text": "Nike"},
    {"src": "sneakers5.png", "alt": "Картинка 3", "text": "Classic-boot"},
    {"src": "sneakers6.png", "alt": "Картинка 3", "text": "Nike"},
    {"src": "sneakers7.png", "alt": "Картинка 3", "text": "Текст для картинки 3"},
    {"src": "sneakers8.png", "alt": "Картинка 3", "text": "Diesel"},
    {"src": "sneakers9.png", "alt": "Картинка 3", "text": "Текст для картинки 3"},
]


@app.route('/')
def index():
    # Отображение главной страницы с меню
    return render_template('index.html', menu=menu)


@app.route('/items')
def items():
    # Отображение страницы "Наши товары" с изображениями
    return render_template('items.html', images=images, menu=menu)


@app.route('/about')
def about():
    # Отображение страницы "Контакты"
    return render_template('about.html')


@app.route('/map')
def map():
    # Отображение страницы с картой
    map_file = getImage()
    return render_template('map.html', images=images, menu=menu, map_file=map_file)


if __name__ == '__main__':
    app.run(debug=True)
