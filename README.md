## 🤖 Telebot + DRF API (AdminPanel)
Telegram bot youtube blogger [Приятный Ильдар](https://www.youtube.com/@pleasantildar)

## 📲 Usage
Bot for blogger’s personal telegram channel

The bot has commands:
- `/vote_emotion` - poll vote: what emotion is associated with the video?
- `/vote_food` - poll vote: what food is associated with the video?
- `/select_video` - choose a video based on emotion and a snack for the video

👉 [Presentation video](https://drive.google.com/file/d/16fTpsrhUQ0DJNTDCab_toDnviKzuT6yb/view?usp=drive_link)

👉 [Telegram Bot](https://t.me/TestTestIldarBotBot)

👉 [Swagger](http://31.129.98.245/api/v1/schema/swagger-ui/)

## 📈 DRF API Tests
```
Name                                Stmts   Miss  Cover
-------------------------------------------------------
botapp/__init__.py                      0      0   100%
botapp/admin.py                        40      0   100%
botapp/apps.py                          4      0   100%
botapp/docs.py                         10      0   100%
botapp/migrations/0001_initial.py       6      0   100%
botapp/migrations/__init__.py           0      0   100%
botapp/models.py                       53      0   100%
botapp/serializers.py                  97      0   100%
botapp/tests.py                       115      0   100%
botapp/urls.py                         11      0   100%
botapp/views.py                        46      0   100%
core/__init__.py                        0      0   100%
core/settings.py                       22      0   100%
core/urls.py                            6      0   100%
manage.py                              12      2    83%
-------------------------------------------------------
TOTAL                                 422      2    99%
```
