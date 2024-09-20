from pathlib import Path
import json

# Extract Route
def extract_route(request):
    if not request:
        return ''
    
    first_line = request.split('\n')[0]
    parts = first_line.split()
    
    if len(parts) < 2:
        return ''
    
    return parts[1].strip('/')


# Read File
def read_file(file):
    abrir = open(file, mode='r+b', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    return abrir.read()

def load_data(filename: str): 
    file_path = "Handout 1/data/" + filename 
    file = open(file_path, mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
    data = json.load(file)
    return data


def load_template(template_name):
    template_path = 'Handout 1/templates/' + template_name
    template = open(template_path, mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
    abre = template.read()
    return abre


def save_note(note: dict):
    file_path = 'Handout 1/data/notes.json'
    print(note)
    
    with open(file_path,'r+', encoding='utf-8') as file:
        notas = json.load(file)
        notas.append(note)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(notas, file, indent=4)
    
def build_response(body='', code=200, reason='OK', headers=''):

    if headers:
        response = f"HTTP/1.1 {code} {reason}\n{headers}\n\n{body}"
    else:
        response = f"HTTP/1.1 {code} {reason}\n\n{body}"
    if code == 303:
        print(response)
    return response.encode('utf-8') 

