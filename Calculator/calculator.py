from mathparser import parse_to_postfix_annotation, parse_postfix_to_float
from typing import Self


class Calculator:
    def __init__(self, math_expression: str = ""):
        self.__ast = None
        self.__expression = math_expression
        self.__parsed_expression = ""
        self.__result = 0
        self.__flag = False

    def calc(self) -> float:
        if self.__flag:
            return self.__result
        self.__parsed_expression = parse_to_postfix_annotation(self.__expression)
        if self.__parsed_expression == "":
            self.__result = 0
            self.__flag = True
        else:
            self.__result = parse_postfix_to_float(self.__parsed_expression)
            self.__flag = True
        return float(self.__result)

    def load_new_expression(self, math_expression: str) -> Self:
        self.__expression = math_expression
        self.__flag = False
        return self



