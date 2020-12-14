import re

class LexicalAnalyzer:
    """
    Takes a file containing Java code as input and
    makes an object that can create the symbol table for methods.

    The __init__ method takes the filepath of the file that contains the Java code as argument
    and initilizes all the attributes.

    Args:
        file_path (str): The path of the file that contains the Java code.

    Attributes:
        filepath (str): The path of the file that contains the Java code.

    """

    _DATATYPES = ['void', 'boolean', 'char', 'byte', 'short', 'int', 'long', 'float', 'double']

    def __init__(self, filepath):
        self.filepath = filepath
        self._method_name = []

    @property
    def method_names(self):
        """
        :obj:`list` of :obj:`tuples`: Holds all the methods and
        their return types found in the Java code.

        """
        return self._method_name

    def method_identifier(self):
        """
        Computes the symbol table for methods from the given file.

        Uses regular expression to look for methods and
        extracts the method name, parameter(s) and return type.

        """
        regex = '(public|private|protected)(( )+static)?( )+'+'('+'|'.join(
            self._DATATYPES)+')'+'( )+(_|$)?[a-zA-Z]+(?<!main)( )*\('

        with open(self.filepath, 'r') as f:
            for line in f:
                line = line.strip()
                match = re.search(regex, line)
                if match is not None:
                    words = match.group()[:-1].split()
                    return_type = words[-2]

                    name = line[line.find(words[-1]):][:len(words[-1])] + line[line.find('('):]
                    name = ' '.join(name.split())
                    self._method_name.append((name, return_type))


    def show(self):
        """
        Prints the symbol table for methods.

        """
        print('Methods:')
        for met, ret in self._method_name:
            print(met+',', 'return type:', ret)



a = LexicalAnalyzer('input.txt')
a.method_identifier()
a.show()
