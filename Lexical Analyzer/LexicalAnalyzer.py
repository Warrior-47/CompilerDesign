import numpy as np

class LexicalAnalyzer:
    
    """Takes a file containing C code as input and 
    makes an object that can create the symbol table"""
    
    _COMMON_KEYWORDS = ['int','long','float','double','char','if','else','do','for','while','switch',
                                'case','continue','break','default','signed','unsigned','return','void']
    
    _MATH_OPERATORS = ['++','--','+=','-=','*=','/=','%=','+','-','*','/','%','=']
    
    _LOGIC_OPERATORS = ['&&','||','<=','>=','==','!=','&','|','<','>','^','!','~']
    
    _SPECIAL_CHARACTERS = [',',';',':','"',"'",'(',')','{','}','[',']']
    
    def __init__(self, file_path):
        self.filepath = file_path
        self._keywords = set()
        self._identifiers = set()
        self._m_operator = set()
        self._l_operator = set()
        self._numeric_values = set()
        self._others = set()
    
    @property
    def keywords(self):
        return self._keywords
    
    @property
    def identifiers(self):
        return self._identifiers
    
    @property
    def math_operators(self):
        return self._m_operator
    
    @property
    def logical_operators(self):
        return self._l_operator
    
    @property
    def numeric_values(self):
        return self._numeric_values
    
    @property
    def others(self):
        return self._others
    
    def compute_symbol_table(self):
        
        """Computes the symbol table from the given file"""
        
        with open(self.filepath) as file:
            for line in file:
                line = line.strip()
                words = line.split()
                self.keyword_identifier(words)
                self.logic_ops_identifier(words)
                self.math_ops_identifier(words)
                self.special_char_identifier(words)
                self.numerics_identifier(words)
                
                self._identifiers.update(words)


    def keyword_identifier(self, words):
        
        """Takes a list of words and separates the keywords from them"""
        
        for ind,word in enumerate(words):
            for key in LexicalAnalyzer._COMMON_KEYWORDS:
                if key in word:
                    self._keywords.update([key])
                    words[ind] = ''
                    if word != key:
                        temp = word.replace(key, ' ')
                        words += temp.split()
                    break
                
        self.__remove_empty(words)
    
        
    def logic_ops_identifier(self,words):
        
        """Takes a list of words and separates the logical operators from them"""
        
        for ind, word in enumerate(words):
            for ops in LexicalAnalyzer._LOGIC_OPERATORS:
                if ops in word:
                    self._l_operator.update([ops])
                    words[ind] = ''
                    if word != ops:
                        temp = word.replace(ops, ' ')
                        words += temp.split()
                    break
                    """if word == ops:
                        del(words[ind])
                    else:
                        words[ind] = word.replace(ops, '')
                        word = word.replace(ops, '')
                        '''temp = word.replace(ops, ' ')
                        del(words[ind])
                        words += temp.split()
                        break'''
                        """
        self.__remove_empty(words)
    
    
    def math_ops_identifier(self, words):
        
        """Takes a list of words and separates the mathematical operators from them"""
        
        for ind, word in enumerate(words):
            for ops in LexicalAnalyzer._MATH_OPERATORS:
                if ops in word:
                    self._m_operator.update([ops])
                    words[ind] = ''
                    if word != ops:
                        temp = word.replace(ops, ' ')
                        words += temp.split()
                    break
                    '''if word == ops:
                        del(words[ind])
                    else:
                        words[ind] = word.replace(ops, '')
                        word = word.replace(ops, '')
                        '''
        self.__remove_empty(words)
    
    
    def special_char_identifier(self, words):
        
        """Takes a list of words and separates the Special Characters i.e. ';.,{}()[]' from them"""
        
        for ind, word in enumerate(words):
            for char in LexicalAnalyzer._SPECIAL_CHARACTERS:
                if char in word:
                    self._others.update([char])
                    words[ind] = ''
                    if word != char:
                        temp = word.replace(char, ' ')
                        words += temp.split()
                    break
                    '''if word == char:
                        del(words[ind])
                    else:
                        words[ind] = word.replace(char, '')
                        word = word.replace(char, '')
                        '''
        self.__remove_empty(words)


    def numerics_identifier(self, words):
        
        """Takes a list of words and separates the numerical values from them"""
        
        for ind, num in enumerate(words):
            if num.isnumeric() or '.' in num:
                self._numeric_values.update([num])
                words[ind] = ''
        self.__remove_empty(words)
    
    
    
    def print_symbol_table(self):
        print(self)
    
    
    def __str__(self):
        s = """Keywords: {keys}
Identifiers: {idens}
Math Operators: {math}
Logical Operators: {logic}
Numerical Values: {nums}
Others: {ot}""".format(keys=', '.join(self.keywords),idens=', '.join(self._identifiers),
                        math=', '.join(self.math_operators),logic=', '.join(self.logical_operators),
                        nums=', '.join(self.numeric_values),ot=' '.join(self.others))
        return s
    
    
    
    def __remove_empty(self,words):
        while '' in words:
            words.remove('')

a = LexicalAnalyzer('input.txt')
a.compute_symbol_table()
a.print_symbol_table()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    