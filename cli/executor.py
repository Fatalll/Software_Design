"""
    Модуль исполняющий команды интерпретатора
"""

from abc import ABCMeta, abstractmethod
from interpreter import ICommandInterpreter
from pparser import IParser
from evaluator import IEvaluator


class IExecutor(metaclass=ABCMeta):
    """ Интерфейс исполнителя выражений """

    def __init__(self, command_interpreter: ICommandInterpreter,
                 parser: IParser, evaluator: IEvaluator):
        self._command_interpreter = command_interpreter
        self._parser = parser
        self._evaluator = evaluator

    @abstractmethod
    def execute_expression(self, expr: str) -> str:
        """ Исполнить выражение и вернуть результат """
        pass


class Executor(IExecutor):
    """ Реализация исполнителя выражений """

    def execute_expression(self, expr: str) -> str:
        tokens = self._parser.tokenize(expr)
        commands = self._command_interpreter.retrieve_commands(iter(tokens))

        result = ""
        for command in commands:
            result = command.execute(result, self._evaluator.get_storage())

        return result
