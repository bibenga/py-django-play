Запускаем:

`sudo docker-compose build && sudo docker-compose up`

Sensor1 и Sensor2 абсолютно идентичные модели, где-то у меня копипаст, а где-то нет.

# Приложение sensor

Генерирует 2 потока данных с некоторых абстрактных сенсоров.
Предполагается что данные обновляются, а не хранятся исторические данные.

Настроен celery который генерирует данные.

Запускается с использованием uWSGI на порту 8001.
Так же он запускает целери и его бит.

Есть админка на `http://127.0.0.1:8001/api/admin/`.<br />
Логин: `a`<br />
Пароль: `a`<br />

# Приложение handler

Импортирует данные из sensor предварительно их обработав.
Как было указано выше предполагается что данные обновляются, хотя для исторических данных импорт был бы быстрее.
Для работы с удаленными данными используются неуправляемые модели, но можно конечно и sql заюзать.

Настроен celery который импортирует данные.
В начале возможна ситуция с ошибками если sensor еще не накатил БД.

При изменении правил удаляются данные из модели Result и запускается реимпорта данных.
Формулу обработки можно настраивать индивидуально по "кодам" датчиков.
Пустой код это формула по умолчанию.
Формулы - это почти пайтон... 
В формулах исходные данные приходят в магическом "value".

Запускается с использованием supervisor на порту 8002.
Так же он запускает nginx, daphne, celery и его бит.

В проекте используется django-channels что бы в админке 
уведомлять об измененниях сделанных другими сотрудниками.

Есть админка на `http://127.0.0.1:8002/api/admin/`.<br />
Есть API на `http://127.0.0.1:8002/api/v1/`.<br />

Логин: `a`<br />
Пароль: `a`<br />

Логин: `b`<br />
Пароль: `b`<br />

В том апи что нужно было для react я отключил аутентификацию.


# Приложение react

Специальный UI на react-admin.
Запускается nginx который так же проксирует запросы на handler.

Запускается на порту 8000.

Ходить в `http://127.0.0.1:8000/`.<br />
Аутентификацию не настраивал.

