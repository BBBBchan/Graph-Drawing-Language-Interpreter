from enum import Enum
import numpy as np

Token_Type = Enum('Token_Type', ('ORIGIN', 'SCALE', 'ROT', 'IS', 'TO', 'STEP', 'DRAW', 'FOR', 'FROM',  # 保留字
                                 'T',  # 参数
                                 'SEMICO', 'L_BRACKET', 'R_BRACKET', 'COMMA',  # 分隔符
                                 'PLUS', 'MINUS', 'MUL', 'DIV', 'POWER',  # 运算符
                                 'FUNC',  # 函数符
                                 'CONST_ID',  # 常数
                                 'NONTOKEN',  # 空记号
                                 'ERRTOKEN'))  # 出错记号


class Tokens:
    def __init__(self, type, lexeme, value, funcptr):
        self.lexeme = lexeme
        self.value = value
        self.funcptr = funcptr
        if type in Token_Type:
            self.type = type
        else:
            print("非法类型")


TokenTab = dict([
    ('PI', Tokens(Token_Type.CONST_ID, "PI", 3.1415926, None)),  # 符号表
    ('E', Tokens(Token_Type.CONST_ID, "E", 2.71828, None)),  # 左key右value
    ('T', Tokens(Token_Type.T, 'T', 0.0, None)),
    ('SIN', Tokens(Token_Type.FUNC, 'SIN', 0.0, np.sin)),  # 不能用math库，无法进行矩阵运算
    ('COS', Tokens(Token_Type.FUNC, 'COS', 0.0, np.cos)),
    ('TAN', Tokens(Token_Type.FUNC, 'TAN', 0.0, np.tan)),
    ('LN', Tokens(Token_Type.FUNC, 'LN', 0.0, np.log)),
    ('EXP', Tokens(Token_Type.FUNC, 'EXP', 0.0, np.exp)),
    ('SQRT', Tokens(Token_Type.FUNC, 'SQRT', 0.0, np.sqrt)),
    ('ORIGIN', Tokens(Token_Type.ORIGIN, 'ORIGIN', 0.0, None)),
    ('SCALE', Tokens(Token_Type.SCALE, 'SCALE', 0.0, None)),
    ('ROT', Tokens(Token_Type.ROT, 'ROT', 0.0, None)),
    ('IS', Tokens(Token_Type.IS, 'IS', 0.0, None)),
    ('FOR', Tokens(Token_Type.FOR, 'FOR', 0.0, None)),
    ('FROM', Tokens(Token_Type.FROM, 'FROM', 0.0, None)),
    ('TO', Tokens(Token_Type.TO, 'TO', 0.0, None)),
    ('STEP', Tokens(Token_Type.STEP, 'STEP', 0.0, None)),
    ('DRAW', Tokens(Token_Type.DRAW, 'DRAW', 0.0, None))
])
