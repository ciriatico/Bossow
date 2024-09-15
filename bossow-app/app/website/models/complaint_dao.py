class Complaint:
    def __init__(self, complaint_id, user_id, game_id, complaint_type, complaint_text, solved, created_at):
        self.complaint_id = complaint_id
        self.user_id = user_id
        self.game_id = game_id
        self.complaint_type = complaint_type
        self.complaint_text = complaint_text
        self.solved = solved
        self.created_at = created_at

class ComplaintDAO:
    def __init__(self):
        pass

    def find_by_id(self, cursor, complaint_id):
        try:
            sql_command = "SELECT * FROM Complaint WHERE complaint_id = {}".format(str(complaint_id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            complaint = Complaint(*result)
            return complaint
        
        except Exception as e:
            print(e)
            return None

    def get_all(self, cursor):
        try:
            sql_command = "SELECT * FROM Complaint"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            complaints = [Complaint(*complaint) for complaint in result]
            return complaints
        
        except Exception as e:
            print(e)
            return None

    def filter_by_user_id(self, cursor, user_id):
        try:
            sql_command = "SELECT * FROM Complaint WHERE user_id = {}".format(str(user_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            complaints = [Complaint(*complaint) for complaint in result]
            return complaints
        
        except Exception as e:
            print(e)
            return None

    def add(self, cursor, complaint):
        try:
            sql_command = "INSERT INTO Complaint (user_id, game_id, complaint_type, complaint_text) VALUES ({}, {}, '{}', '{}')".format(complaint.user_id, complaint.game_id, complaint.complaint_type, complaint.complaint_text)            
            cursor.execute(sql_command)

        except Exception as e:
            print(e)

    def update(self, cursor, complaint):
        try:
            sql_command = "UPDATE Complaint SET game_id = %(game_id)s, complaint_text = %(complaint_text)s, complaint_type = %(complaint_type)s, solved = %(solved)s WHERE complaint_id = %(complaint_id)s"
            data_update = {"complaint_id": complaint.complaint_id, "game_id": complaint.game_id, "complaint_text": complaint.complaint_text, "complaint_type": complaint.complaint_type, "solved": complaint.solved}
            cursor.execute(sql_command, data_update)

        except Exception as e:
            print(e)
            return None

    def delete(self, cursor, complaint_id):
        try:
            sql_command = "DELETE FROM Complaint WHERE complaint_id = {}".format(complaint_id)
            cursor.execute(sql_command)

        except Exception as e:
            print(e)