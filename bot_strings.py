import json


class BotStrings:
    """Вспомогательный класс для работы с текстовками бота"""
    jsonObjects = []

    def __init__(self, filename):
        file = open(filename, encoding="UTF8")
        self.jsonObjects = json.load(file)

    def __getitem__(self, item):
        return str(self.get_string(item))

    def get_string(self, name):
        return str(self.jsonObjects[name])
