class FullComplaint:
    def __init__(self, complaint_id, user_id, full_name, profile_picture, game_id, complaint_type, complaint_text, solved, date_created, title, cover_picture):
        self.complaint_id = complaint_id
        self.user_id = user_id
        self.full_name = full_name
        self.profile_picture = profile_picture
        self.game_id = game_id
        self.complaint_type = complaint_type
        self.complaint_text = complaint_text
        self.solved = solved
        self.date_created = date_created
        self.title = title
        self.cover_picture = cover_picture

class FullComplaintDAO:
    def __init__(self):
        pass
    
    def get_all(self, cursor):
        try:
            sql_command = "SELECT complaint_id, user_id, full_name, profile_picture, game_id, type, complaint_text, solved, date_created, title, cover_picture FROM (SELECT complaint.id as complaint_id, user_id, game_id, type, complaint_text, solved, date_created, title, cover_picture FROM complaint INNER JOIN game ON complaint.game_id = game.id) as complaint_game INNER JOIN user ON complaint_game.user_id = user.id ORDER BY date_created"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            complaints = [FullComplaint(*complaint) for complaint in result]
            return complaints
        
        except Exception as e:
            print(e)
            return None
    
    def filter_by_user_id(self, cursor, user_id):
        try:
            sql_command = "SELECT complaint_id, user_id, full_name, profile_picture, game_id, type, complaint_text, solved, date_created, title, cover_picture FROM (SELECT complaint.id as complaint_id, user_id, game_id, type, complaint_text, solved, date_created, title, cover_picture FROM complaint INNER JOIN game ON complaint.game_id = game.id WHERE user_id = {}) as complaint_game INNER JOIN user ON complaint_game.user_id = user.id ORDER BY date_created".format(user_id)
            cursor.execute(sql_command)
            result = cursor.fetchall()
            complaints = [FullComplaint(*complaint) for complaint in result]
            return complaints

        except Exception as e:
            print(e)
            return None