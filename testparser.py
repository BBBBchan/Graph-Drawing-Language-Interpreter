import scannerprocess
import parserprocess

file_name = 'graphic.txt'
scanner = scannerprocess.Scanner(file_name)
parser = parserprocess.Parser(scanner)
parser.Parser()
