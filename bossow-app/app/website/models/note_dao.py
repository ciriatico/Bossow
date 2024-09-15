class Note:
    def __init__(self, note_id, user_id, note_text, created_at):
        self.note_id = note_id
        self.user_id = user_id
        self.note_text = note_text
        self.created_at = created_at

class NoteDAO:
    def __init__(self):
        pass
    
    def filter_by_user_id(self, cursor, user_id):
        try:
            sql_command = "SELECT * FROM Note WHERE user_id = {}".format(str(user_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            notes = [Note(*note) for note in result]
            return notes
        
        except Exception as e:
            print(e)
            return None

    def find_by_id(self, cursor, note_id):
        try:
            sql_command = "SELECT * FROM Note WHERE note_id = {}".format(str(note_id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            note = Note(*result)
            return note
        
        except Exception as e:
            print(e)
            return None

    def delete(self, cursor, note_id):
        try:
            sql_command = "DELETE FROM Note WHERE note_id = {}".format(str(note_id))
            cursor.execute(sql_command)

        except Exception as e:
            print(e)

    def add(self, cursor, note):
        try:
            sql_command = "INSERT INTO Note (user_id, note_text) VALUES ({}, '{}')".format(note.user_id, note.note_text)            
            cursor.execute(sql_command)

        except Exception as e:
            print(e)