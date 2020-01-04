import scanner.scanner_token as scanner_token
import scanner.scannerprocess as scannerprocess

f_name = 'graphic.txt'
scanner = scannerprocess.Scanner(f_name)

if scanner.f_ptr is not None:
    print("token_type           lexeme          value       ptr")
    print("------------------------------------------------------")
    while True:
        token = scanner.GetToken()
        if token.type != scanner_token.Token_Type.NONTOKEN:
            print("{:20s}|{:12s}|{:12f}|{}".format(token.type, token.lexeme, token.value, token.funcptr))
        else:
            break
    print("文本程序共", scanner.LineNo, "行")
else:
    print("打开文件失败")