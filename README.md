SkyStore - проект интернет-магазина.

Перед началом работы программы необходимо:

-установить виртуальное окружение;
-установить пакеты из файла requirements.txt;
-создать базу данных 'skystore' и внести изменения в константе DATABASE в файле settings;
-добавить в базу данных категории c помощью фикстуры - python3 manage.py loaddata data/categories.json;
-добавить в базу данных продукты с помощью команды fill - python3 manage.py fill 
-добавить в базу данных посты с помощью команды add_posts - python3 manage.py add_posts 