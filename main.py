from flask import Flask, render_template, send_from_directory, redirect
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
    {"src": "sneakers.png", "alt": "Картинка 1", "text": "Nike", "id": 1},
    {"src": "sneakers2.png", "alt": "Картинка 2", "text": "Adidas", "id": 2},
    {"src": "sneakers3.png", "alt": "Картинка 3", "text": "Convers", "id": 3},
    {"src": "sneakers4.png", "alt": "Картинка 3", "text": "Nike", "id": 4},
    {"src": "sneakers5.png", "alt": "Картинка 3", "text": "Classic-boot", "id": 5},
    {"src": "sneakers6.png", "alt": "Картинка 3", "text": "Nike", "id": 6},
    {"src": "sneakers7.png", "alt": "Картинка 3", "text": "Sneakers", "id": 7},
    {"src": "sneakers8.png", "alt": "Картинка 3", "text": "Diesel", "id": 8},
    {"src": "sneakers9.png", "alt": "Картинка 3", "text": "Sneakers", "id": 9},
]

itemss = [
    {"item_1": {"sneaker_name": "Nike",
                "sneaker_image": images[0],
                "sneaker_info": " Nike Air Force 1 - одна из самых культовых и узнаваемых моделей Nike. "
                                "Впервые выпущенные в 1982 году, Air Force 1 стали первыми баскетбольными кроссовками "
                                "с воздушной подушкой в пятке. Эта модель быстро завоевала популярность среди любителей"
                                "стритстайла и хип-хоп культуры."}},
    {"item_2": {"sneaker_name": "Adidas",
                "sneaker_image": images[1],
                "sneaker_info": "Adidas Superstar - легендарные кроссовки, выпущенные в 1969 году как "
                                "баскетбольная обувь. Superstar быстро стали культовой моделью в хип-хоп культуре "
                                "и уличной моде, особенно благодаря культовой раковине на носке. Superstar продолжают"
                                " оставаться одной из самых популярных и узнаваемых моделей Adidas."}},
    {"item_3": {"sneaker_name": "Convers",
                "sneaker_image": images[2],
                "sneaker_info": "onverse Chuck Taylor All Star - одна из самых культовых и узнаваемых моделей Converse."
                                " Впервые выпущенные в 1917 году как баскетбольные кроссовки, Чак Тейлоры быстро вышли"
                                " за рамки спорта и стали символом молодежной культуры и стиля. Их простой, лаконичный"
                                " дизайн и резиновая подошва сделали их универсальной обувью для повседневной носки."}},
    {"item_4": {"sneaker_name": "Nike Dunk",
                "sneaker_image": images[3],
                "sneaker_info": "Nike Dunk - культовая модель, изначально выпущенная в 1985 году как баскетбольные"
                                " кроссовки. Dunk быстро вышли за рамки спорта и стали одним из символов скейтбординга"
                                " и уличной моды 90-х. Различные расцветки и коллаборации сделали "
                                "эту модель настоящей иконой стиля."}},
    {"item_5": {"sneaker_name": "Classic-boot",
                "sneaker_image": images[4],
                "sneaker_info": "Timberland 6-Inch Premium - культовые ботинки, впервые представленные в 1973 году. "
                                "Timberland отличаются водонепроницаемым кожаным верхом, контрастной прошивкой и"
                                " протекторной подошвой. Эта модель стала популярна в хип-хоп "
                                "культуре и уличной моде."}},
    {"item_6": {"sneaker_name": "Nike",
                "sneaker_image": images[5],
                "sneaker_info": "Nike Cortez - классические беговые кроссовки, впервые представленные в 1972 году."
                                " Cortez отличаются простым, минималистичным дизайном и стали одной из первых моделей "
                                "Nike, получивших широкое признание. Они до сих пор остаются "
                                "популярными как повседневная обувь."}},
    {"item_7": {"sneaker_name": "Sneakers",
                "sneaker_image": images[6],
                "sneaker_info": "Nike Air Force 1: Классическая модель кроссовок, которая пользуется популярностью "
                                "уже несколько десятилетий. Они обладают удобной амортизацией "
                                "и отличной поддержкой стопы"}},
    {"item_8": {"sneaker_name": "Diesel",
                "sneaker_image": images[7],
                "sneaker_info": "Diesel S-Spaark Low - одна из самых популярных моделей кроссовок Diesel. S-Spaark Low "
                                "отличаются фирменным дизайном с контрастными вставками, массивной подошвой и логотипом"
                                " Diesel. Эта модель стала популярна благодаря своему"
                                " урбанистическому, дерзкому стилю."}},
    {"item_9": {"sneaker_name": "Sneakers",
                "sneaker_image": images[8],
                "sneaker_info": "Еще одна иконичная пара кроссовок, которая изначально была выпущена в 1960-х годах."
                                " Stan Smith отличаются минималистичным дизайном с зеленым логотипом на заднике. "
                                "Они комфортны и стильны, подходят для повседневной носки и легких тренировок."}},
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


@app.route('/items/<int:item_id>')
def info_items(item_id: int):
    if item_id <= len(itemss):
        src = itemss[item_id - 1]["item_" + str(item_id)]["sneaker_image"]["src"]
        name = itemss[item_id - 1]["item_" + str(item_id)]["sneaker_name"]
        info = itemss[item_id - 1]["item_" + str(item_id)]["sneaker_info"]

        print(id)
        return render_template('sneaker.html', items=itemss, src=src, name=name, info=info)
    else:
        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
