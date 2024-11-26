import numpy as np
import sys
import Parser.parser_node as parser_node
import scanner.scanner_token as scanner_token


class Parser(object):
    def __init__(self, scanner):
        self.scanner = scanner
        self.token = None
        self.Parameter = 0
        self.x_origin = 0
        self.y_origin = 0
        self.x_scale = 1
        self.y_scale = 1
        self.rot = 0
        self.x_ptr = None
        self.y_ptr = None
        self.Tvalue = 0

    def enter(self, x):
        print("进入", str(x))

    def back(self, x):
        print("离开", str(x))

    def call_match(self, x):
        print('匹配token', str(x))

    def Tree_trace(self, x):
        self.PrintSyntaxTree(x, 1)

    def FetchToken(self):
        self.token = self.scanner.GetToken()
        while self.token.type == scanner_token.Token_Type.NONTOKEN:
            self.token = self.scanner.GetToken()
        if self.token == scanner_token.Token_Type.ERRTOKEN:
            print(self.token.type)
            print("出错行号：", self.scanner.LineNo, " 记号错误 ", self.token.lexeme)
            self.scanner.CloseScanner()
            sys.exit(1)

    def MatchToken(self, token_type):
        if self.token.type != token_type:
            print(self.token.type)
            print("出错行号：", self.scanner.LineNo, " 与期望记号不符 ", self.token.lexeme)
            self.scanner.CloseScanner()
            sys.exit(1)
        if token_type == scanner_token.Token_Type.SEMICO:
            self.scanner.f_ptr.readline()
            last = self.scanner.f_ptr.tell()
            next_line = self.scanner.f_ptr.readline()
            if len(next_line) == 0:
                return
            else:
                self.scanner.f_ptr.seek(last)
        self.FetchToken()

    def PrintSyntaxTree(self, root, indent):
        for i in range(indent):
            print('\t', end=' ')
        if root.item == scanner_token.Token_Type.PLUS:
            print('+ ')
        elif root.item == scanner_token.Token_Type.MINUS:
            print('- ')
        elif root.item == scanner_token.Token_Type.MUL:
            print('* ')
        elif root.item == scanner_token.Token_Type.DIV:
            print("/ ")
        elif root.item == scanner_token.Token_Type.POWER:
            print("** ")
        elif root.item == scanner_token.Token_Type.FUNC:
            print("{} ".format(root.Func_ptr))
        elif root.item == scanner_token.Token_Type.CONST_ID:
            print('{:5f} '.format(root.value))
        elif root.item == scanner_token.Token_Type.T:
            print('{} '.format(root.value))
        else:
            print("节点类型错误")
            sys.exit(0)
        if root.item == scanner_token.Token_Type.CONST_ID or root.item == scanner_token.Token_Type.T:
            return
        elif root.item == scanner_token.Token_Type.FUNC:
            self.PrintSyntaxTree(root.middle, indent + 1)
        else:
            self.PrintSyntaxTree(root.left, indent + 1)
            self.PrintSyntaxTree(root.right, indent + 1)

    def Parser(self):
        self.enter("Parser")
        if self.scanner.f_ptr is None:
            print("文件打开错误")
        else:
            self.FetchToken()
            self.Program()
            self.scanner.CloseScanner()
            self.back("Parser")

    def Program(self):
        self.enter("Program")
        while self.token.type != scanner_token.Token_Type.SEMICO:
            self.Statement()
            self.MatchToken(scanner_token.Token_Type.SEMICO)
            self.call_match("; ")
        self.back("Program")

    def Statement(self):
        self.enter("Statement")
        if self.token.type == scanner_token.Token_Type.ORIGIN:
            self.OriginStatement()
        elif self.token.type == scanner_token.Token_Type.SCALE:
            self.ScaleStatement()
        elif self.token.type == scanner_token.Token_Type.FOR:
            self.ForStatement()
        elif self.token.type == scanner_token.Token_Type.ROT:
            self.RotStatement()
        elif self.token.type == scanner_token.Token_Type.CONST_ID or self.token.type == scanner_token.Token_Type.L_BRACKET or self.token.type == scanner_token.Token_Type.MINUS:
            self.Expression()
        else:
            print(self.token.type)
            print("出错行号：", self.scanner.LineNo, " 与期望记号不符 ", self.token.lexeme)
            self.scanner.CloseScanner()
            sys.exit(1)
        self.back("Statement")

    def OriginStatement(self):
        self.enter("OriginStatement")
        self.MatchToken(scanner_token.Token_Type.ORIGIN)
        self.call_match("ORIGIN")
        self.MatchToken(scanner_token.Token_Type.IS)
        self.call_match("IS")
        self.MatchToken(scanner_token.Token_Type.L_BRACKET)
        self.call_match("(")
        temp = self.Expression()
        self.x_origin = temp.GetValue()
        self.MatchToken(scanner_token.Token_Type.COMMA)
        self.call_match(",")
        temp = self.Expression()
        self.y_origin = temp.GetValue()
        self.MatchToken(scanner_token.Token_Type.R_BRACKET)
        self.call_match(")")
        self.back("OriginStatement")

    def ScaleStatement(self):
        self.enter("ScaleStatement")
        self.MatchToken(scanner_token.Token_Type.SCALE)
        self.call_match("SCALE")
        self.MatchToken(scanner_token.Token_Type.IS)
        self.call_match("IS")
        self.MatchToken(scanner_token.Token_Type.L_BRACKET)
        self.call_match("(")
        temp = self.Expression()
        self.x_scale = temp.GetValue()
        self.MatchToken(scanner_token.Token_Type.COMMA)
        self.call_match(",")
        temp = self.Expression()
        self.y_scale = temp.GetValue()
        self.MatchToken(scanner_token.Token_Type.R_BRACKET)
        self.call_match(")")
        self.back("ScaleStatement")

    def ForStatement(self):
        self.enter("ForStatement")
        start = 0.0
        end = 0.0
        step = 0.0
        self.MatchToken(scanner_token.Token_Type.FOR)
        self.call_match("FOR")
        self.MatchToken(scanner_token.Token_Type.T)
        self.call_match("T")
        self.MatchToken(scanner_token.Token_Type.FROM)
        self.call_match("FROM")
        start_ptr = self.Expression()
        start = start_ptr.GetValue()
        self.MatchToken(scanner_token.Token_Type.TO)
        self.call_match("TO")
        end_ptr = self.Expression()
        end = end_ptr.GetValue()
        self.MatchToken(scanner_token.Token_Type.STEP)
        self.call_match("STEP")
        step_ptr = self.Expression()
        step = step_ptr.GetValue()
        self.Tvalue = np.arange(start, end, step)
        self.MatchToken(scanner_token.Token_Type.DRAW)
        self.call_match("DRAW")
        self.MatchToken(scanner_token.Token_Type.L_BRACKET)
        self.call_match("(")
        self.x_ptr = self.Expression()
        self.x_ptr = self.x_ptr.value
        self.MatchToken(scanner_token.Token_Type.COMMA)
        self.call_match(",")
        self.y_ptr = self.Expression()
        self.y_ptr = self.y_ptr.value
        self.MatchToken(scanner_token.Token_Type.R_BRACKET)
        self.call_match(")")
        self.back("ForStatement")

    def RotStatement(self):
        self.enter("RotStatement")
        self.MatchToken(scanner_token.Token_Type.ROT)
        self.call_match("ROT")
        self.MatchToken(scanner_token.Token_Type.IS)
        self.call_match("IS")
        temp = self.Expression()
        self.rot = temp.GetValue()
        self.back("RotStatement")

    def Expression(self):
        self.enter("Expression")
        left = self.Term()
        while self.token.type == scanner_token.Token_Type.PLUS or self.token.type == scanner_token.Token_Type.MINUS:
            temp = self.token.type
            self.MatchToken(temp)
            right = self.Term()
            left = self.MakeExprNode(temp, left, right)
        self.Tree_trace(left)
        self.back("Expression")
        return left

    def Term(self):
        left = self.Factor()
        while self.token.type == scanner_token.Token_Type.MUL or self.token.type == scanner_token.Token_Type.DIV:
            temp = self.token.type
            self.MatchToken(temp)
            right = self.Factor()
            left = self.MakeExprNode(temp, left, right)
        return left

    def Factor(self):
        if self.token.type == scanner_token.Token_Type.PLUS:
            self.MatchToken(scanner_token.Token_Type.PLUS)
            right = self.Factor()
            left = None
            right = self.MakeExprNode(scanner_token.Token_Type.PLUS, left, right)
        elif self.token.type == scanner_token.Token_Type.MINUS:
            self.MatchToken(scanner_token.Token_Type.MINUS)
            right = self.Factor()
            left = parser_node.ExprNode(scanner_token.Token_Type.CONST_ID)
            left.value = 0.0
            right = self.MakeExprNode(scanner_token.Token_Type.MINUS, left, right)
        else:
            right = self.Component()
        return right

    def Component(self):
        left = self.Atom()
        if self.token.type == scanner_token.Token_Type.POWER:
            self.MatchToken(scanner_token.Token_Type.POWER)
            right = self.Component()
            left = self.MakeExprNode(scanner_token.Token_Type.POWER, left, right)
        return left

    def Atom(self):
        if self.token.type == scanner_token.Token_Type.CONST_ID:
            temp = self.token.value
            self.MatchToken(scanner_token.Token_Type.CONST_ID)
            address = self.MakeExprNode_CONST(scanner_token.Token_Type.CONST_ID, temp)
        elif self.token.type == scanner_token.Token_Type.T:
            self.MatchToken(scanner_token.Token_Type.T)
            if len(self.Tvalue) == 1:
                address = self.MakeExprNode_CONST(scanner_token.Token_Type.T, 0.0)
            else:
                address = self.MakeExprNode_CONST(scanner_token.Token_Type.T, self.Tvalue)
        elif self.token.type == scanner_token.Token_Type.FUNC:
            temp_ptr = self.token.funcptr
            self.MatchToken(scanner_token.Token_Type.FUNC)
            self.MatchToken(scanner_token.Token_Type.L_BRACKET)
            self.call_match("(")
            temp = self.Expression()
            address = self.MakeExprNode(scanner_token.Token_Type.FUNC, temp_ptr, temp)
            self.MatchToken(scanner_token.Token_Type.R_BRACKET)
            self.call_match(")")
        elif self.token.type == scanner_token.Token_Type.L_BRACKET:
            self.MatchToken(scanner_token.Token_Type.L_BRACKET)
            self.call_match("(")
            address = self.Expression()
            self.MatchToken(scanner_token.Token_Type.R_BRACKET)
            self.call_match(")")
        else:
            print(self.token.type)
            print("出错行号：", self.scanner.LineNo, " 与期望记号不符 ", self.token.lexeme)
            self.scanner.CloseScanner()
            sys.exit(1)
        return address

    def MakeExprNode(self, item, left, right):
        ExprPtr = parser_node.ExprNode(item)
        if item == scanner_token.Token_Type.FUNC:
            ExprPtr.Func_ptr = left
            ExprPtr.middle = right
        else:
            ExprPtr.left = left
            ExprPtr.right = right
        ExprPtr.GetValue()
        return ExprPtr

    def MakeExprNode_CONST(self, item, value):
        ExprPtr = parser_node.ExprNode(item)
        ExprPtr.value = value
        return ExprPtr
