from utils import load_data, load_template, save_note, build_response
from urllib.parse import unquote_plus

def index(request):
    # Carrega os post-its existentes
    if request.startswith('POST'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        print('corpo:', corpo)

        for chave_valor in corpo.split('&'):
            print(chave_valor.split('='))
            chave_valor = chave_valor.split('=')
            if len(chave_valor) >= 2:
                params[chave_valor[0]] = unquote_plus(chave_valor[1])
        
        save_note(params)
        return build_response(code=303, reason='See Other', headers='Location: /')
    
    notes = load_data('notes.json')
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=note['titulo'], details=note['detalhes'])
        for note in notes
    ]
    notes_html = '\n'.join(notes_li)

    # Carrega o template principal e insere os post-its
    body = load_template('index.html').format(notes=notes_html)
    # print(body)

    return build_response(body=body)