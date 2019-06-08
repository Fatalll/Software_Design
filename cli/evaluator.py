"""
    Модуль для работы с переменными окружения
"""

import re
from abc import ABCMeta, abstractmethod
from storage import IStorage


class IEvaluator(metaclass=ABCMeta):
    """ Интерфейс для работы с переменными окружения """

    @abstractmethod
    def __init__(self, storage: IStorage, regexp: str):
        """ regexp - регулярное выражение для поиска переменных окружения """
        """ storage - хранилище переменных окружения """
        pass

    @abstractmethod
    def get_storage(self) -> IStorage:
        """ вернуть хранилище переменных окружения """
        pass

    @abstractmethod
    def evaluate_variables(self, expression: str) -> str:
        """ Заменить переменные окружения на их значения из хранилища
            возвращает новую строку с проведенной заменой """
        pass


class Evaluator(IEvaluator):
    """ Реализация интерфейса для работы с переменными окружения """

    def __init__(self, storage: IStorage, regexp: str):
        self.__storage = storage
        self.__regexp = regexp

    def get_storage(self) -> IStorage:
        return self.__storage

    def evaluate_variables(self, expression: str) -> str:
        return re.sub(self.__regexp,
                      lambda var: self.__storage[var.group()[1:]],
                      expression)
