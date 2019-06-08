"""
    Модуль для работы с хранилищем переменных
"""

from abc import ABCMeta, abstractmethod


class IStorage(metaclass=ABCMeta):
    """ Интерфейс для хранения и доступа к переменным окружения """

    @abstractmethod
    def __contains__(self, item: str) -> bool:
        """ Проверка наличия переменной в окружении """
        pass

    @abstractmethod
    def __setitem__(self, key: str, value: str) -> None:
        """ Добавить или обновить переменную окружения """
        pass

    @abstractmethod
    def __getitem__(self, key: str):
        """ Запросить значение переменной окружения """
        pass


class Storage(IStorage):
    """ Реализация интерфейса для хранения и доступа к переменным окружения """

    def __init__(self):
        self.__storage = dict()

    def __contains__(self, key: str) -> bool:
        return key in self.__storage

    def __setitem__(self, key: str, value: str) -> None:
        self.__storage[key] = value

    def __getitem__(self, key: str) -> str:
        return self.__storage[key] if key in self.__storage else ""
