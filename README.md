# Загрузка и расылка фото NASA и SpaceX

Данный скрипт позволяет загружать фотографии с сервисов [NASA EPIC](https://api.nasa.gov/#epic) и [NASA APOD](https://api.nasa.gov/#apod) и фотографии [последнего запуска SpaceX](https://github.com/r-spacex/SpaceX-API), а затем постить их в свой телеграмм канал.

### Как установить

Для начала работы необходимо:
- Зарегистрироваться на сайте NASA и сгенерировать токен;
- Затем создать бота в TG [(Как создать канал, бота и получить токен)](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html);
- Создать канал в TG и добавить бота в него;

Далее,  в папке со скриптом необходимо создать файл ```.env``` и записать в него настройки ввиде:

```
NASA_APIKEY=Ваш токен NASA
SPACEX_LAUNCH_ID=id запуска SpaceX
TG_TOKEN=токен Вашего бота в телеграмм
TG_CHAT_ID=@название Вашего канала
```

[Python3](https://www.python.org/) должен быть уже установлен. Затем используйте ```pip``` (или ```pip3```, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

### Как использовать
- Для загрузки изображений NASA epic, используйте команду:
 ```
 python fetch_nasa_epic.py
 ```
- Для загрузки изображений NASA apod, используйте команду: 
```
python fetch_nasa_apod.py
```
- Для загрузки изображений SpaceX, используйте команду: 
```
python fetch_spacex_images.py
```
- Для постинга изображений в телеграмм запустите скрипт:
```
python main.py
```

### Цель проекта
Код написан учеником в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/)
