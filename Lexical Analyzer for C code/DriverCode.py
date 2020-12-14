from LexicalAnalyzer import LexicalAnalyzer as la

a = la('input.txt')

a.compute_symbol_table()

a.print_symbol_table()