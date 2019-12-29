import scanner_token
import os


class Scanner:
    def __init__(self, f_name):
        self.LineNo = 0
        self.TokenBuffer = ''
        self.f_name = f_name
        if os.path.exists(self.f_name):
            self.f_ptr = open(self.f_name, "r")
        else:
            self.f_ptr = None

    def CloseScanner(self):
        if self.f_ptr is None:
            self.f_ptr.close()

    def GetChar(self):
        Char = self.f_ptr.read(1)  # 读取一个字符
        return Char.upper()

    def BackChar(self, Char):
        if Char != '':
            self.f_ptr.seek(self.f_ptr.tell() - 1)

    def AddCharTokenString(self, Char):
        self.TokenBuffer += Char

    def EmptyTokenString(self):
        self.TokenBuffer = ''

    def JudgeKeyToken(self):  # 获取Token
        Token = scanner_token.TokenTab.get(self.TokenBuffer,
                                           scanner_token.Tokens(scanner_token.Token_Type.ERRTOKEN, self.TokenBuffer,
                                                                0.0, None))
        # Token = scanner_token.Tokens(scanner_token.TokenTab.get(self.TokenBuffer), self.TokenBuffer, 0.0, None)
        return Token

    def GetToken(self):
        Char = ''
        token = ''
        self.EmptyTokenString()
        while True:
            Char = self.GetChar()
            if Char == '':
                token = scanner_token.Tokens(scanner_token.Token_Type.NONTOKEN, Char, 0.0, None)

                return token
            if Char == '\n':
                self.LineNo += 1
            if ~Char.isspace():
                break
        self.AddCharTokenString(Char)

        if Char.isalpha():
            while True:
                Char = self.GetChar()
                if Char.isalnum():
                    self.AddCharTokenString(Char)
                else:
                    break
            self.BackChar(Char)
            token = self.JudgeKeyToken()
            token.lexme = self.TokenBuffer

            return token
        elif Char.isdigit():
            while True:

                Char = self.GetChar()
                if Char.isdigit():
                    self.AddCharTokenString(Char)
                else:
                    break
            if Char == '.':
                self.AddCharTokenString(Char)
                while True:
                    Char = self.GetChar()
                    if Char.isdigit():
                        self.AddCharTokenString(Char)
                    else:
                        break
            self.BackChar(Char)
            token = scanner_token.Tokens(
                scanner_token.Token_Type.CONST_ID, self.TokenBuffer, float(self.TokenBuffer), None)

            return token
        else:
            if Char == ';':
                token = scanner_token.Tokens(scanner_token.Token_Type.SEMICO, Char, 0.0, None)
            elif Char == '(':
                token = scanner_token.Tokens(scanner_token.Token_Type.L_BRACKET, Char, 0.0, None)
            elif Char == ')':
                token = scanner_token.Tokens(scanner_token.Token_Type.R_BRACKET, Char, 0.0, None)
            elif Char == ',':
                token = scanner_token.Tokens(scanner_token.Token_Type.COMMA, Char, 0.0, None)
            elif Char == '+':
                token = scanner_token.Tokens(scanner_token.Token_Type.PLUS, Char, 0.0, None)
            elif Char == '-':
                Char = self.GetChar()
                if '-' == Char:
                    while Char != '\n' and Char != '':
                        Char = self.GetChar()
                    self.BackChar(Char)
                    return self.GetToken()
                else:
                    self.BackChar(Char)
                    token = scanner_token.Tokens(scanner_token.Token_Type.MINUS, '-', 0.0, None)
            elif Char == '/':
                Char = self.GetChar()
                if Char == '/':
                    while Char != '\n' and Char != '':
                        Char = self.GetChar()
                    self.BackChar(Char)
                    return self.GetToken()
                else:
                    self.BackChar(Char)
                    token = scanner_token.Tokens(scanner_token.Token_Type.DIV, '/', 0.0, None)
            elif Char == '*':
                Char = self.GetChar()
                if Char == '*':
                    token = scanner_token.Tokens(scanner_token.Token_Type.POWER, '**', 0.0, None)
                else:
                    self.BackChar(Char)
                    token = scanner_token.Tokens(scanner_token.Token_Type.MUL, '*', 0.0, None)
            else:
                if Char == ' ' or Char == '\n':
                    return self.GetToken()
                else:
                    token = scanner_token.Tokens(scanner_token.Token_Type.ERRTOKEN, Char, 0.0, None)
        return token
