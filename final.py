import scanner.scannerprocess as sp
import semantic.semantic as se

file_name = 'graphic.txt'
scanner = sp.Scanner(file_name)

semantic = se.Semantic(scanner)
semantic.init()
semantic.Parser()
