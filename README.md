Прогноз погоды
========================
Выводит прогноз погоды для Лондона, Аэропорта Шереметьево, Череповца.

Как установить
-------------------------

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```Python
pip install -r requirements.txt
```
***

В программе используются ключи словаря *params* для настройки запроса к сайту.
```Python
params = {"lang": "ru",
              "M": "",
              "n": "",
              "q": "",
              "T": "",
              }
```
Словарь *params* можно дополнить используя ключи из [документации к сайту](https://ru.wttr.in/:help). Значение оставляйте пустым.


Чтобы поменять язык, измените **значение** ключа *lang*. [Список поддерживаемых языков](https://ru.wttr.in/:translation)
![Допустимые значения](https://sun9-31.userapi.com/impg/hHAX5Xhx9x44tbGeDhbqy9KZ-AhmZNhSXlvj6w/LfNYESE4XRY.jpg?size=986x51&quality=95&sign=e842a6abfcbf4ea88a8374cea50e319a&type=album)

Цель проекта
-------------------------
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

