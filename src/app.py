import ply.lex as lex
import gradio as gr

# Lista de nomes de tokens
tokens = (
    'ID',
    'INT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
)

# Regras de expressão regular para cada token
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Expressão regular para identificadores (nomes de variáveis)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Expressão regular para números inteiros
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Tratamento de quebra de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manipulação de erros
def t_error(t):
    print(f"Caractere ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

# Criar uma string de saída
def output_tokens(lexer:lex):
    str_output = ''
    for token in lexer:
        str_output += str(token) + '\n'
    return str_output

# API GRADIO
def display(text):
    lexer.input(text)
    return output_tokens(lexer)

# Cria um Texto para as informações adicionais
def text_markdown():
    text_output = """
    # Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus de Tianguá
    ## Curso
    - Bacharelado em Ciência da Computação
      - Compiladores 2023.2
    ## Professor
    - M.e Adonias Caetano de Oliveira
    ## Equipe 02
    - Esrael Saraiva de Sousa 
    - Francinilson Rodrigues Lima
    - Jordan Ferreira de Sousa
    - Ricardo Martins Cordeiro
    """
    return text_output

# Programa Principal
if __name__=='__main__':
    # Criar o analisador léxico
    lexer = lex.lex()

    # Utiliza a API Gradio
    with gr.Blocks() as interface: # Cria blocos
        gr.Markdown('Atividade de Compiladore - Analisador Léxico')
        with gr.Tab("Ply"):
            input_user = gr.Textbox(lines=1, placeholder="ax+b=0")
            output = gr.TextArea(lines=10)
            text_button = gr.Button("Analisar Lexicamente")
        with gr.Accordion('Informações Adicionais!'):
            gr.Markdown(text_markdown())
        text_button.click(fn=display, inputs=input_user, outputs=output)
    interface.launch()
    