Доброго времени суток, уважаемый проверяющий компании "Hammer Systems". Благодарю за возможность продемонстрировать свои навыки!

Инструкция по запуску:
1) Клонировать репозиторий: `git clone https://github.com/shoksdev/hammers-systems-test.git`
2) Перейти в папку с проектом: `cd referal_system`
3) Поднять приложение: `docker-compose up`
4) Отправить POST запрос на эндпоинт auth/request/ с параметром `phone_number` (номер телефона) для начала аутентификации;
5) Перейдите по адрес admin/user_auth/customuser/ для получения кодов аутентификации;
6) Отправить POST запрос на эндпоинт auth/verify/ с параметрами `phone_number` и `auth_code` (номер телефона и код аутентификации, полученный из админ-панели) для подтверждения номера телефона и получена JWT токена;
7) Отправить GET запрос на эндпоинт profile/ с заголовком `Authorization` и значением `Bearer <ваш_JWT_токен>` для получения профиля пользователя;
8) Отправить POST запрос на эндпоинт profile/activate_invite_code/ с заголовком `Authorization` и значением `Bearer <ваш_JWT_токен>` и параметром `invite_code` пользователя для активации;
9) Отправить GET запрос на эндпоинт profile/invited_users/ с заголовком `Authorization` и значением `Bearer <ваш_JWT_токен>` для получения номеров телефонов пользователей, которые ввели ваш инвайт-код.

Ещё раз благодарю за возможность показать себя. Всего доброго!
