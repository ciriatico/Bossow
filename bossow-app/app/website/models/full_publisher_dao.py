class FullPublisher:
    def __init__(self, publisher_id, game_id, publisher_name, logo_picture):
        self.publisher_id = publisher_id
        self.game_id = game_id
        self.publisher_name = publisher_name
        self.logo_picture = logo_picture

class FullPublisherDAO:
    def __init__(self):
        pass
    
    def find_by_game_id(self, cursor, game_id):
        try:
            sql_command = "SELECT Publisher.publisher_id, game_id, publisher_name, logo_picture FROM Publisher INNER JOIN Game ON Publisher.publisher_id = Game.publisher_id WHERE game_id = {}".format(str(game_id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            full_publisher = FullPublisher(*result)
            return full_publisher
        
        except Exception as e:
            print(e)
            return None