import sqlite3
from dataclasses import dataclass

class Database:
        def __init__(self,db_arquivo):

        
        
                db_file = f"{db_arquivo}.db"

                self.conn = sqlite3.connect(db_file)
                print(f"Conectado ao banco de dados {db_file}")
        
                self.conn.execute('CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,title STRING,content STRING NOT NULL);')

        def add(self,note):
                query = "INSERT INTO note (title, content) VALUES (?, ?);"
                self.conn.execute(query, (note.title, note.content))
                self.conn.commit()

        def get_all(self):
                notes = []
                cursor = self.conn.execute("SELECT id, title, content  FROM note")
                for linha in cursor:
                        id = linha[0]
                        title = linha[1]
                        content = linha[2]
                        notes.append(Note(id,title,content))
                return notes

        def update(self,entry):
                query = "UPDATE note SET title = ?, content = ? WHERE id = ?"
                self.conn.execute(query, (entry.title, entry.content, entry.id))
                self.conn.commit()

        def delete(self,note_id):
                query = "DELETE FROM note WHERE id = ?;"
                self.conn.execute(query,(note_id,))
                self.conn.commit()


class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content