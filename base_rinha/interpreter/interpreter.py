import ujson
import llvmlite


class FileName:
    name = None
    expresion = None


class Term:
    kind = [
        'Int',
        'Str',
        'Call',
        'Binary',
        'Function',
        'Let',
        'If',
        'Print',
        'First',
        'Second',
        'Bool',
        'Tuple',
        'Var'
    ]

    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def __repr__(self):
        return f'{self.kind}: {self.value}'

    def __str__(self):
        return f'{self.kind}: {self.value}'

    def __eq__(self, other):
        if isinstance(other, Term):
            return self.kind == other.kind and self.value == other.value
        return False

    def __hash__(self):
        return hash((self.kind, self.value))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.kind < other.kind

    def __le__(self, other):
        return self.kind <= other.kind

    def __gt__(self, other):
        return self.kind > other.kind

    def __ge__(self, other):
        return self.kind >= other.kind

    def __add__(self, other):
        return self.kind + other.kind

    def __sub__(self, other):
        return self.kind - other.kind

    def __mul__(self, other):
        return self.kind * other.kind


file_name = str(input("Digite o nome do arquivo: "))
print(file_name)
comando = str(input("Digite o comando: "))
file_path = f"C:/Users/aless/PycharmProjects/rinha-de-compiler/base_rinha/interpreter/files/{file_name}.json"


def load_json_file(file_path):
    if file_name == "":
        if comando != "":
            detect_char(comando)
        else:
            print("Comando não encontrado")
    try:
        file_object = open(f"{file_path}", "r", encoding='UTF-8')
        json_content = file_object.read()
        a_list = ujson.loads(json_content)
        return a_list["name"]
    except:
        print("Arquivo não encontrado")
        return None


def detect_char(comando):
    if comando == "print":
        print("print")

    elif comando == "let":
        print("let")

    elif int(comando):
        print("int")


load_json_file(file_path)
