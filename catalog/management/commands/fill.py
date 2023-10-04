from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {
                "title": "Удобный сервис рассылок",
                "description": "Неограниченная лицензия, поддержка, установка на сервер, получение обновлений",
                "image": "products/rassylka.png",
                "category": "Рассылки",
                "price": 200,
                "date_of_creation": "2023-10-02T10:59:49.537Z",
                "date_of_change": "2023-10-02T10:59:49.537Z"

            },
            {

                "title": "Чат-бот",
                "description": "Генерирует простейшие диалоги на определенную тему, которую задает пользователь.",
                "image": "products/chat-bot.jpeg",
                "category": "Телеграм боты",
                "price": 300,
                "date_of_creation": "2023-10-03T12:26:30.632Z",
                "date_of_change": "2023-10-03T12:26:30.632Z"
            },
            {

                "title": "Телеграм-бот",
                "description": "Telegram-бот умеет делать всё, что мог бы делать человек в чате: отвечать на вопросы, "
                               "присылать ссылки на сайты или создавать мемы.",
                "image": "products/telegram_bot.jpeg",
                "category": "Телеграм боты",
                "price": 350,
                "date_of_creation": "2023-10-04T12:26:30.632Z",
                "date_of_change": "2023-10-04T12:26:30.632Z"
            },
            {
                "title": "Система управления контентом",
                "description": "Информационная система или компьютерная программа, используемая для обеспечения и "
                               "организации совместного процесса создания, редактирования и управления содержимым, "
                               "иначе — контентом",
                "image": "products/systema_upravleniya.jpeg",
                "category": "Веб-приложения",
                "price": 400,
                "date_of_creation": "2023-10-04T12:26:30.632Z",
                "date_of_change": "2023-10-04T12:26:30.632Z"
            }
        ]

        products_objects = []
        for item in products_list:
            products_objects.append(Product(**item))

        Product.objects.bulk_create(products_objects)
