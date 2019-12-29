import scannerprocess
import semantic

file_name = 'graphic.txt'
scanner = scannerprocess.Scanner(file_name)

semantic = semantic.Semantic(scanner)
semantic.init()
semantic.Parser()
