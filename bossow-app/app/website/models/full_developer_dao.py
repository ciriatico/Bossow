class FullDeveloper:
    def __init__(self, developer_id, game_id, developer_name, logo_picture):
        self.developer_id = developer_id
        self.game_id = game_id
        self.developer_name = developer_name
        self.logo_picture = logo_picture

class FullDeveloperDAO:
    def __init__(self):
        pass
    
    def find_by_game_id(self, cursor, game_id):
        try:
            sql_command = "SELECT Developer.developer_id, game_id, developer_name, logo_picture FROM Developer INNER JOIN Game ON Developer.developer_id = Game.developer_id WHERE game_id = {}".format(str(game_id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            full_developer = FullDeveloper(*result)
            return full_developer
        
        except Exception as e:
            print(e)
            return None