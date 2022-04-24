class Complaint:
    def __init__(self, id, user_id, game_id, complaint_type, complaint_text, solved, date_created):
        self.id = id
        self.user_id = user_id
        self.game_id = game_id
        self.type = complaint_type
        self.complaint_text = complaint_text
        self.solved = solved
        self.date_created = date_created

class ComplaintDAO:
    def __init__(self):
        pass

    def get_all(self, cursor):
        try:
            sql_command = "SELECT * FROM complaint"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            complaints = [Complaint(*complaint) for complaint in result]
            return complaints
        
        except Exception as e:
            print(e)
            return None

    def filter_by_user_id(self, cursor, user_id):
        try:
            sql_command = "SELECT * FROM complaint WHERE user_id = {}".format(str(user_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            complaints = [Complaint(*complaint) for complaint in result]
            return complaints
        
        except Exception as e:
            print(e)
            return None