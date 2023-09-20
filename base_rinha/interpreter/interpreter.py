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


file_name = "hello"
file_path = f"C:/Users/aless/PycharmProjects/rinha-de-compiler/base_rinha/interpreter/files/{file_name}.json"


def load_json_file(file_path):
    file_object = open(f"{file_path}", "r", encoding='UTF-8')
    json_content = file_object.read()
    a_list = ujson.loads(json_content)
    return a_list["name"]


print(load_json_file(file_path))
