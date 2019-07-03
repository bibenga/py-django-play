Запускаем:

sudo docker-compose build && sudo docker-compose up

Sensor1 и Sensor2 абсолютно идентичные модели, где-то у меня копипаст, а где-то нет.

# Приложение sensor

Генерирует 2 потока данных с некоторых абстрактных сенсоров.
Предполагается что данные обновляю``тся, а не хранятся исторические данные.

Настроен celery который генерирует данные.

Запускается с использованием uWSGI на порту 8001.
Так же он запускает целери и его бит.

Есть админка на "http://127.0.0.1:8001/api/admin/".
Логин: a
Пароль: a

# Приложение handler

Импортирует данные из sensor предварительно их обработав.
Как было указано выше предполагается что данные обновляются, хотя для исторических данных импорт был бы быстрее.
Для работы с удаленными данными используются неуправляемые модели, но можно конечно и sql заюзать.

Настроен celery который импортирует данные.
В начале возможна ситуция с ошибками если sensor еще не накатил БД.

При изменении правил удаляются данные из модели Result и запускается реимпорта данных.
Формулу обработки можно настраивать индивидуально по "кодам" датчиков.
Пустой код это формула по умолчанию.
Формулы это почти пайтон... ыВ формулах исходные данные приходят в магическом "value".

Запускается с использованием uWSGI на порту 8002.
Так же он запускает целери и его бит.

Есть админка на "http://127.0.0.1:8002/api/admin/".
Логин: a
Пароль: a

Есть API на "http://127.0.0.1:8002/api/v1/".
Логин: a
Пароль: a
В том апи что нужно было для react я отключил аутентификацию.


# Приложение react

Специальный UI на react-admin.
Запускается dev server, как диплоить продакшен реди я не настраивал...

Запускается на порту 8000.

Ходить в "http://127.0.0.1:8000/".
Аутентификацию не настраивал.

