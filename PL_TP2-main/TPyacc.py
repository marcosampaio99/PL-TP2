
from os import system
import ply.yacc as yacc
from TPlex import tokens



#def p_grammar(p):

#    """
#    L : START funcs main END (nao implementado)
#      |  main END      
#
#    endline : ';'
#    
#    main : MAIN instrs    
#     
#    instrs : instrs instr     
#       | instr 
#       |          
#       
#    instr : atr endline   
#      | write endline   
#      | read endline
#      | cond      
#      | cycle endline    
#      | endline  
#                
#    cycle : REPEATE START '(' instrs ')' UNTIL instrs END
#  
#    cond : IF '(' lexpr ')' START instrs START ELSE START instrs END 

#    write : WRITE '(' STR ')'  
#      
#    read : READ ID                  
#        
#     atr : ID '=' expr                 
#                                                              
#     
#    lexpr : expr EQ expr    
#      | expr NEQ expr    
#      | expr GE expr      
#      | expr LE expr     
#      | expr '>' expr    
#      | expr '<' expr    
#      | expr              
#      
#    expr : expr '+' expr   
#       | expr '-' expr   
#       | expr OR lexpr   
#       | term               
#       
#    term : term '*' par   
#     | term '/' par    
#     | term '%' par  
#     | term AND par   
#     | par            
#     
#    par : '(' expr ')'        
#        |  NUM                   
#        | ID   
#        |  NOT lexpr     (n implementado)                                
#    """
#
#
#










def p_MAIN(p):    
     "main : MAIN instrs END"
     vars=p.parser.registers.get("countVARS")
     while(vars>0):
              f.write("PUSHI 0 \n")
              vars=vars-1
     f.write("START\n")
     f.write(p[2])

      
def p_Instrs(p):
      "instrs : instrs instr"
      p[0] = p[1] + p[2]
      pass

def p_InstrSING(p):
      "instrs : instr"
      p[0]=p[1]
      pass


def p_Instr(p):
      """
       instr : atr endline   
              | write endline   
              | read endline
              | endline
              | cond
              | cycle
              | lexpr
              |       

      """
      p[0]=p[1]

def p_end(p):
      """
      endline : ';'
      """

def p_cond(p):                   
       "cond : IF '(' lexpr ')' START instrs START ELSE START instrs END"
       p[0] = p[3] + ("JZ ELSE") + str(p.parser.registers.get("countIF")) + "\n" + p[6] + ("JUMP EndIf") + str(p.parser.registers.get("countIF")) + "\n"  + ("ELSE") + str(p.parser.registers.get("countIF")) +(":\n") + p[10] + ("EndIf") + str(p.parser.registers.get("countIF")) +(":\n")
       p.parser.registers.update({"countIF":(p.parser.registers.get("countIF")+1)})
       


def p_repeat(p):
      "cycle : REPEATE START '{' instrs '}' UNTIL '(' instrs ')' END"
      p[0] = "ciclo" + str(p.parser.registers.get("countCYCLE")) +":\n" + p[4] + p[8] + "jz ciclo" + str(p.parser.registers.get("countCYCLE")) + "\n"
      p.parser.registers.update({"countCYCLE":(p.parser.registers.get("countCYCLE")+1)})
      

  
      
def p_WRITE(p):
      "write : WRITE ID "
      p[0] = "PUSHG " + str(p.parser.registers.get(p[2])) + "\n" + ("WRITEI\n") 



def p_WRITESTR(p):
      "write : WRITE STR"
      p[0] =  "PUSHS " + p[2] + "\n" + "WRITES\n" 


def p_atr(p):
      "atr : ID '=' expr"
      if p[1] in p.parser.registers:
            p[0] = p[3] + ("STOREG " + str(p.parser.registers.get(p[1]))+ "\n")

      else:
            p.parser.registers.update({p[1]:p.parser.registers.get("countVARS")})
            p[0] = p[3] + ("STOREG " + str(p.parser.registers.get(p[1]))+ "\n")
            p.parser.registers.update({"countVARS":(p.parser.registers.get("countVARS")+1)})



def p_READ(p):
      "read : READ ID"
      if p[2] in p.parser.registers:
            p[0] = ("READ\nATOI\n") + ("STOREG " + str(p.parser.registers.get(p[2]))+ "\n")
      
      else:
       p.parser.registers.update({p[2]:p.parser.registers.get("countVARS")})
       p[0] = ("READ\nATOI\n") + ("STOREG " + str(p.parser.registers.get(p[2]))+ "\n")
       p.parser.registers.update({"countVARS":(p.parser.registers.get("countVARS")+1)})




def p_Cond(p):
      "lexpr : lexpr AND lexpr"
      p[0] = p[1] + p[3] + "MUL\n"


def p_LEXPR_EQ(p):
      "lexpr : expr EQ expr"
      p[0] = p[1] + p[3] + "EQUAL\n"




def p_LEXPR_LE(p):
      "lexpr : expr LE expr"
      p[0] = p[1] + p[3] + "INFEQ\n"


def p_LEXPR_GE(p):
      "lexpr : expr GE expr"
      p[0] = p[1] + p[3] + "SUPEQ\n"

def p_LEXPR_MAIOR(p):
      "lexpr : expr '>' expr"
      p[0] = p[1] + p[3] + "SUP\n"

def p_LEXPR_MENOR(p):
      "lexpr : expr '<' expr"
      p[0] = p[1] + p[3] + "INF\n"

def p_LEXPR_EXPR(p):
      "lexpr : expr"
      p[0] = p[1]


def p_LEXPR(p):
      "lexpr : '(' lexpr ')' "
      p[0] = p[2]

def p_LEXPR_NOT(p):
      "lexpr : NOT lexpr"
      p[0] = p[2] + "pushi 0\n" + "EQUAL\n"


def p_EXPR_PLUS(p):
      "expr : expr '+' expr"
      p[0] = p[1] + p[3] + "ADD\n"
      
def p_EXPR_MINUS(p):
      "expr : expr '-' expr"
      p[0] = p[1] + p[3] + "SUB\n"
#
#def p_EXPR_OR(p):
#      "expr : expr OR expr"
#      p[0] = p[1]  p[3] 
#
def p_EXPR_TERM(p):
      "expr : term"
      p[0] = p[1] 




def p_TERM_MUL(p):
      "term : term '*' par" 
      p[0] = p[1] + p[3] + "MUL \n"

def p_TERM_DIV(p):
      "term : term '/' par"
      p[0] = p[1] + p[3] + "DIV \n"

def p_TERM_MOD(p):
      "term : term '%' par"
      p[0] = p[1] + p[3] + "MOD \n" 

def p_TERM_AND(p):
      "term : term AND par"
      p[0] = p[1] + p[3] 

def p_TERM_par(p):
      "term : par"
      p[0] = p[1] 
      



def p_PAR_EXPR(p):
      "par : '(' expr ')'"
      p[0] = p[2]  

def p_PAR_NUM(p):
      "par : NUM"
      p[0] = "PUSHI " + str(int(p[1])) + "\n"

def p_PAR_ID(p):
      "par : ID"
      p[0] = "PUSHG " + str(p.parser.registers.get(p[1])) + "\n"





def p_error(p):
    print('Erro sintático: ', p )
    parser.success = False


# build the parser
parser = yacc.yacc()

# my state
parser.registers = {}
parser.registers.update({"countVARS":0})
parser.registers.update({"countIF":0})
parser.registers.update({"countCYCLE":0})



with open(r"Menor.ex.txt", 'r') as file:
    data = file.read()

f = open("ex.vm", "w")

parser.success = True
parser.parse(data)


if parser.success:
    f.write("STOP\n")
    f.close()
    print("Sintaxe reconhecida: ", data)

else:
    print("Erro de sintaxe")


