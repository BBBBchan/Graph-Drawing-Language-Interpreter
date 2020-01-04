import Parser.parserprocess as  parserprocess
import scanner.scanner_token as scanner_token
import numpy as np
import sys
import matplotlib.pyplot as plt


class Semantic(parserprocess.Parser):
    def init(self):
        self.fig = plt.figure()
        # plt.ylim(0, None)
        # plt.xlim(0, None)
        self.ax = self.fig.add_subplot(111)

    def calc(self, x, y):
        x *= self.x_scale
        y *= self.y_scale
        temp1 = x * np.cos(self.rot) + y * np.sin(self.rot)
        y *= np.cos(self.rot) - x * np.sin(self.rot)
        x = temp1
        x += self.x_origin
        y += self.y_origin
        return x, y

    def Draw(self):
        x, y = self.calc(self.x_ptr, self.y_ptr)
        self.ax.scatter(x, y)

    def Statement(self):
        self.enter("Statement")
        if self.token.type == scanner_token.Token_Type.ORIGIN:
            self.OriginStatement()
        elif self.token.type == scanner_token.Token_Type.SCALE:
            self.ScaleStatement()
        elif self.token.type == scanner_token.Token_Type.FOR:
            self.ForStatement()
            self.Draw()
        elif self.token.type == scanner_token.Token_Type.ROT:
            self.RotStatement()
        else:
            print(self.token.type)
            print("出错行号：", self.scanner.LineNo, " 与期望记号不符 ", self.token.lexeme)
            self.scanner.CloseScanner()
            sys.exit(1)
        self.back("Statement")

    def Parser(self):
        self.enter("Parser")
        if self.scanner.f_ptr is None:
            print("文件打开失败")
        else:
            self.FetchToken()
            self.Program()
            plt.show()
            self.scanner.CloseScanner()
            self.back("Parser")
