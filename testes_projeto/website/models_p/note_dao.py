class Note:
    def __init__(self, id, user_id, note_text, date_created):
        self.id = id
        self.user_id = user_id
        self.note_text = note_text
        self.date_created = date_created

class NoteDAO:
    def __init__(self):
        pass
    
    def filter_by_user_id(self, cursor, user_id):
        try:
            sql_command = "SELECT * FROM note WHERE user_id = {}".format(str(user_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            notes = [Note(*note) for note in result]
            return notes
        
        except Exception as e:
            print(e)
            return None