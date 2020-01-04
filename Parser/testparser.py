import scanner.scannerprocess as scannerprocess
import Parser.parserprocess as parserprocess

file_name = '..\\graphic.txt'
scanner = scannerprocess.Scanner(file_name)
parser = parserprocess.Parser(scanner)
parser.Parser()
