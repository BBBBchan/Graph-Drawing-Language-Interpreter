import scanner_token


class ExprNode(object):
    def __init__(self, item):
        self.item = item
        # 确定双目运算符
        if self.item == scanner_token.Token_Type.PLUS or self.item == scanner_token.Token_Type.MINUS or self.item == scanner_token.Token_Type.MUL or self.item == scanner_token.Token_Type.DIV or self.item == scanner_token.Token_Type.POWER:
            self.left = None
            self.right = None
        elif self.item == scanner_token.Token_Type.FUNC:        # 函数类型
            self.Func_ptr = None
            self.middle = None
        self.value = None

    def __str__(self):
        return str(self.item)

    def GetValue(self):         # 依据不同的操作符进行运算
        if self.item == scanner_token.Token_Type.PLUS:
            self.value = self.right.value + self.left.value
        elif self.item == scanner_token.Token_Type.MINUS:
            self.value = self.left.value - self.right.value
        elif self.item == scanner_token.Token_Type.MUL:
            self.value = self.right.value * self.left.value
        elif self.item == scanner_token.Token_Type.DIV:
            self.value = self.left.value / self.right.value
        elif self.value == scanner_token.Token_Type.POWER:
            self.value = self.left.value ** self.right.value
        elif self.item == scanner_token.Token_Type.FUNC:
            self.value = self.Func_ptr(self.middle.value)
        return self.value
