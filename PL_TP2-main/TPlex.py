
import ply.lex as lex

tokens = ('START',
          'END',  

          'MAIN',
          'READ',
          'WRITE', 

          #'FSS', #inicio de uma string

          'VOID',
          'INT',

          'REPEATE',
          'UNTIL',
          'IF',
          'ELSE',
          
          'ID', #variavel
          'STR', #string
          #'FSTR',

          'NUM',

          'AND',
          'OR',
          'NOT',

          'EQ',
          'NEQ',
          'GE',
          'LE',
          )


literals = [ '=', '+', '-', '/', '*', '(', ')', ',', ';','>','<','{','}','%']

t_START=r'\:\:'
t_END=r'\:\;'

t_MAIN=r'-MAIN'
t_READ=r'-READ'
t_WRITE=r'-WRITE'
#t_FSS=r'\"'

t_VOID=r'-VOID'

t_INT=r'-INT'

t_IF = r'-IF'
t_ELSE = r'-ELSE'

def t_AND(t):
    r'AND'
    return t
    
def t_OR(t):
    r'OR'
    return t
def t_NOT(t):
    r'NOT'
    return t
    
t_REPEATE=r'-REPEATE'
t_UNTIL=r'-UNTIL'

t_EQ=r'\=\='
t_NEQ=r'\!\='

def t_GE(t):
    r'\>\='
    return t 


t_LE=r'\<\='


def t_ID(t):
    r'[A-Za-z]+'
    return t
    
def t_NUM(t):
    r'\d+'
    return t
    
def t_STR(t):
    r'\".*?\"'
    return t
    
t_ANY_ignore = ' \n\t'

def t_ANY_error(t):
    print('Illegal character: ', t.value[0])

lexer = lex.lex()
#lexer.input('-INT x; -INT zzz;-MAIN -IF ((x>=3)OR(var<=y)AND NOT(2==zzz)) :: -WRITE("Ola mundo! ca vou eu para o sucesso"):;')
#for tok in lexer:
#    print(tok)

