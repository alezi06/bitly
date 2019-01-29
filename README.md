# Обрезка ссылок с помощью Битли

Скрипт получает в качестве параметра ссылку, и проверяет является ли ссылка сокращенной.
Если ссылка обрезана, то в этом случае программа выводит количество кликов по ссылке, иначе
сокращает исходную длинную ссылку и выводит в консоль.

### Как установить

Для использования API Bitly необходимо получить Access Token.
Для этого требуется:
- зарегистрироваться на сайте [Bitly](https://bitly.com/)
- получить Access Token
- создать файл `.env`   и записать в него: `ACCESS_TOKEN=<ваш Access Token>`

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

Сокращаем ссылку:
```
$ python main.py https://github.com
http://bit.ly/2DEOYLy
```
Получаем количество кликов по ссылке:
```
$ python main.py http://bit.ly/2DEOYLy
0
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).